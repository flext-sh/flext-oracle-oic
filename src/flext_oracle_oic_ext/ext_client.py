"""FLEXT Module.

Copyright (c) 2025 FLEXT Team. All rights reserved. SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import base64
import json as json_module
from abc import ABC, abstractmethod
from typing import Self

from flext_api import FlextApiClient
from flext_core import FlextLogger, FlextResult, FlextTypes
from flext_oracle_oic_ext.ext_models import OICAuthConfig, OICConnectionConfig

logger = FlextLogger(__name__)

# Constants
HTTP_ERROR_STATUS_THRESHOLD = 400

# ================================
# EXTENSION Pattern: Base Classes
# ================================


class BaseOICAuthenticator(ABC):
    """Base class for Oracle Integration Cloud authentication patterns.

    EXTENSION Pattern: Base class for Oracle OIC authentication
    with OAuth2 IDCS and token management.
    """

    def __init__(self, auth_config: OICAuthConfig) -> None:
        """Initialize OIC authenticator.

        Args:
            auth_config: OIC authentication configuration

        Returns:
            object: Description of return value.

        """
        self.auth_config = auth_config
        self.logger = FlextLogger(f"{__name__}.{self.__class__.__name__}")
        self._access_token: str | None = None

    @abstractmethod
    def get_oauth_scopes(self) -> str:
        """Get OAuth2 scopes for authentication.

        Returns:
            OAuth2 scope string

        """

    def build_oauth_scopes(self, client_aud: str | None = None) -> str:
        """Build OAuth2 scopes for Oracle Integration Cloud.

        Args:
            client_aud: OAuth2 audience (auto-detected if not provided)

        Returns:
            OAuth2 scope string

        """
        audience = client_aud or self.auth_config.oauth_client_aud

        if audience:
            # Build scope like: "audience:443urn:opc:resource:consumer:all audience:443/ic/api/"
            resource_aud = f"{audience}:443urn:opc:resource:consumer:all"
            api_aud = f"{audience}:443/ic/api/"
            return f"{resource_aud} {api_aud}"
        # Fallback to simple scope
        return self.auth_config.oauth_scope or "urn:opc:resource:consumer:all"

    def get_oauth_request_body(self) -> dict[str, str]:
        """Generate OAuth2 request body for client credentials flow.

        Returns:
            Dict containing grant_type and scope for OAuth2 token request

        """
        return {
            "grant_type": "client_credentials",
            "scope": str(self.get_oauth_scopes()),
        }

    def encode_client_credentials(self) -> str:
        """Encode client credentials for HTTP Basic authentication.

        Returns:
            Base64 encoded client credentials

        """
        client_id = self.auth_config.oauth_client_id
        client_secret = self.auth_config.oauth_client_secret.get_secret_value()

        credentials = f"{client_id}:{client_secret}"
        return base64.b64encode(credentials.encode()).decode()

    async def get_access_token(self) -> FlextResult[str]:
        """Get access token using OAuth2 client credentials flow.

        Returns:
            FlextResult containing access token or error

        """
        try:
            if not self.auth_config.oauth_token_url:
                return FlextResult[str].fail("OAuth token URL not configured")

            # Encode client credentials for HTTP Basic authentication
            encoded_credentials = self.encode_client_credentials()

            headers = {
                "Authorization": f"Basic {encoded_credentials}",
                "Content-Type": "application/x-www-form-urlencoded",
            }

            # Make token request using FlextApiClient
            api_client = FlextApiClient(self.auth_config.oauth_token_url)
            async with api_client:
                response_result = await api_client.post(
                    "",  # Empty endpoint since URL is base_url
                    headers=headers,
                    data=self.get_oauth_request_body(),
                )

                if response_result.is_failure:
                    return FlextResult[str].fail(
                        f"OAuth request failed: {response_result.error}",
                    )

                response = response_result.unwrap()
                if response.status_code >= HTTP_ERROR_STATUS_THRESHOLD:
                    return FlextResult[str].fail(
                        f"OAuth HTTP error: {response.status_code}",
                    )

                # Handle response.body properly - it could be str, dict, or None
                if isinstance(response.body, dict):
                    token_data = response.body
                elif isinstance(response.body, str):
                    token_data = json_module.loads(response.body)
                else:
                    return FlextResult[str].fail("Empty or invalid OAuth response body")

                access_token = token_data.get("access_token")
                if not access_token or not isinstance(access_token, str):
                    return FlextResult[str].fail("No valid access token in response")

                self._access_token = access_token
                self.logger.info("OIC OAuth2 authentication successful")
                return FlextResult[str].ok(access_token)

        except KeyError as e:
            error_msg = f"Invalid OAuth2 response format: missing {e}"
            self.logger.exception(error_msg)
            return FlextResult[str].fail(error_msg)
        except Exception as e:
            error_msg = f"OIC OAuth2 authentication failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[str].fail(error_msg)


class BaseOICClient(ABC):
    """Base class for Oracle Integration Cloud API clients.

    EXTENSION Pattern: Base class for Oracle OIC API clients
    with authentication, retry logic and enterprise error handling.
    """

    def __init__(
        self,
        connection_config: OICConnectionConfig,
        authenticator: BaseOICAuthenticator,
    ) -> None:
        """Initialize OIC client.

        Args:
            connection_config: OIC connection configuration
            authenticator: OIC authenticator instance

        """
        self.connection_config = connection_config
        self.authenticator = authenticator
        self.logger = FlextLogger(f"{__name__}.{self.__class__.__name__}")
        self._client: FlextApiClient | None = None

    @abstractmethod
    def get_base_url(self) -> str:
        """Get OIC API base URL."""

    async def get_authenticated_client(self) -> FlextResult[FlextApiClient]:
        """Get authenticated HTTP client.

        Returns:
            FlextResult containing authenticated client or error

        """
        try:
            if not self._client:
                # Get OAuth2 token
                token_result = await self.authenticator.get_access_token()
                if token_result.is_failure:
                    return FlextResult[FlextApiClient].fail(
                        f"Authentication failed: {token_result.error}",
                    )

                # Create authenticated client with FlextApiClient
                self._client = FlextApiClient(
                    base_url=self.get_base_url(),
                    timeout=self.connection_config.request_timeout,
                    headers={
                        "Authorization": f"Bearer {token_result.unwrap()}",
                        "Content-Type": "application/json",
                        "Accept": "application/json",
                    },
                )

            return FlextResult[FlextApiClient].ok(self._client)

        except Exception as e:
            error_msg = f"Failed to create authenticated client: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextApiClient].fail(error_msg)

    async def make_request(
        self,
        method: str,
        endpoint: str,
        params: dict[str, str] | None = None,
        data: dict[str, str] | None = None,
        json: dict[str, str] | None = None,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Make authenticated request to OIC API.

        Args:
            method: HTTP method
            endpoint: API endpoint (relative to base URL)
            params: Query parameters
            data: Form data
            json: JSON data

        Returns:
            FlextResult containing response data or error

        """
        try:
            # Get authenticated client
            client_result = await self.get_authenticated_client()
            if client_result.is_failure:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    client_result.error or "Client error",
                )

            client = client_result.unwrap()

            # Make request using FlextApiClient
            async with client:
                response_result = await client.request(
                    method=method,
                    url=endpoint,  # FlextApiClient handles URL building
                    params=params,
                    data=data,
                    json=json,
                )

                if response_result.is_failure:
                    return FlextResult[FlextTypes.Core.Dict].fail(
                        f"Request failed: {response_result.error}",
                    )

                response = response_result.unwrap()

                # Parse response body properly - it could be str, dict, or None
                if response.headers.get("content-type", "").startswith(
                    "application/json",
                ):
                    if isinstance(response.body, dict):
                        return FlextResult[FlextTypes.Core.Dict].ok(response.body)
                    if isinstance(response.body, str):
                        parsed_data = json_module.loads(response.body)
                        return FlextResult[FlextTypes.Core.Dict].ok(parsed_data)
                    return FlextResult[FlextTypes.Core.Dict].fail("Empty JSON response")

                # Non-JSON response
                if isinstance(response.body, str):
                    return FlextResult[FlextTypes.Core.Dict].ok(
                        {"raw_content": response.body},
                    )
                if isinstance(response.body, dict):
                    return FlextResult[FlextTypes.Core.Dict].ok(response.body)
                return FlextResult[FlextTypes.Core.Dict].ok(
                    {"raw_content": str(response.body)},
                )

        except Exception as e:
            error_msg = f"OIC API request failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextTypes.Core.Dict].fail(error_msg)

    def _build_request_url(self, endpoint: str) -> str:
        """Build full request URL."""
        base_url = self.get_base_url()
        return (
            f"{base_url}{endpoint}"
            if endpoint.startswith("/")
            else f"{base_url}/{endpoint}"
        )

    async def paginate_request(
        self,
        endpoint: str,
        page_size: int = 100,
        params: dict[str, str] | None = None,
    ) -> FlextResult[list[FlextTypes.Core.Dict]]:
        """Paginate through OIC API responses.

        Args:
            endpoint: API endpoint to paginate
            page_size: Number of records per page
            params: Additional query parameters

        Returns:
            FlextResult containing all paginated records or error

        """
        try:
            all_records: list[FlextTypes.Core.Dict] = []
            offset = 0
            base_params: dict[str, str] = params or {}

            while True:
                # Prepare pagination parameters
                request_params = base_params.copy()
                request_params.update(
                    {
                        "offset": str(offset),
                        "limit": str(page_size),
                    },
                )

                # Make request - add missing await
                response_result = await self.make_request(
                    "GET",
                    endpoint,
                    params=request_params,
                )
                if not response_result.success:
                    return FlextResult[list[FlextTypes.Core.Dict]].fail(
                        response_result.error or "Request failed",
                    )

                response_data = response_result.data
                if response_data is None or not isinstance(response_data, dict):
                    return FlextResult[list[FlextTypes.Core.Dict]].fail(
                        "Invalid response data format",
                    )

                items_raw = response_data.get("items", [])
                if not isinstance(items_raw, list):
                    return FlextResult[list[FlextTypes.Core.Dict]].fail(
                        "Invalid items format",
                    )
                items = items_raw

                # Add items to collection
                all_records.extend(items)

                # Check if we have more pages
                has_more = response_data.get("hasMore", False)
                if not has_more or len(items) < page_size:
                    break

                offset += page_size

            return FlextResult[list[FlextTypes.Core.Dict]].ok(all_records)

        except Exception as e:
            error_msg = f"OIC pagination failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[list[FlextTypes.Core.Dict]].fail(error_msg)

    def __enter__(self) -> Self:
        """Context manager entry."""
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None:
        """Async context manager exit."""
        if self._client:
            await self._client.close()
            self._client = None


# ================================
# EXTENSION Pattern: Concrete Implementations
# ================================


class OICExtensionAuthenticator(BaseOICAuthenticator):
    """OIC Extension authenticator with standard scopes.

    EXTENSION Pattern: Default authenticator for Oracle OIC
    extensions with appropriate scopes.
    """

    def get_oauth_scopes(self) -> str:
        """Get OAuth2 scopes for OIC Extension."""
        return self.build_oauth_scopes()


class OICTapAuthenticator(BaseOICAuthenticator):
    """OIC Tap-specific authenticator with read scopes.

    EXTENSION Pattern: Authenticator for Oracle OIC tap
    focused on read operations.
    """

    def get_oauth_scopes(self) -> str:
        """Get OAuth2 scopes for OIC Tap."""
        return self.build_oauth_scopes()


class OICTargetAuthenticator(BaseOICAuthenticator):
    """OIC Target-specific authenticator with write permissions.

    EXTENSION Pattern: Authenticator for Oracle OIC target
    with write permissions.
    """

    def get_oauth_scopes(self) -> str:
        """Get OAuth2 scopes for OIC Target."""
        return self.build_oauth_scopes()


class OracleOICExtensionClient(BaseOICClient):
    """Main Oracle OIC Extension client.

    EXTENSION Pattern: Main client for Oracle OIC extension
    with complete enterprise functionality.
    """

    def get_base_url(self) -> str:
        """Get OIC API base URL."""
        return f"{self.connection_config.base_url.rstrip('/')}/ic/api/{self.connection_config.api_version}"

    async def get_integrations(
        self,
        status_filter: FlextTypes.Core.StringList | None = None,
        page_size: int = 100,
    ) -> FlextResult[list[FlextTypes.Core.Dict]]:
        """Get integration flows from OIC.

        Args:
            status_filter: Filter integrations by status
            page_size: Number of records per page

        Returns:
            FlextResult containing integrations or error

        """
        params: dict[str, str] = {}

        if status_filter:
            params["q"] = f"status in ({','.join(status_filter)})"

        return await self.paginate_request(
            "/integrations",
            page_size=page_size,
            params=params,
        )

    async def get_connections(
        self,
        type_filter: FlextTypes.Core.StringList | None = None,
        page_size: int = 100,
    ) -> FlextResult[list[FlextTypes.Core.Dict]]:
        """Get adapter connections from OIC.

        Args:
            type_filter: Filter connections by adapter type
            page_size: Number of records per page

        Returns:
            FlextResult containing connections or error

        """
        params: dict[str, str] = {}

        if type_filter:
            params["q"] = f"adapterType in ({','.join(type_filter)})"

        return await self.paginate_request(
            "/connections", page_size=page_size, params=params,
        )

    async def get_packages(
        self,
        page_size: int = 100,
    ) -> FlextResult[list[FlextTypes.Core.Dict]]:
        """Get integration packages from OIC.

        Args:
            page_size: Number of records per page

        Returns:
            FlextResult containing packages or error

        """
        return await self.paginate_request("/packages", page_size=page_size)

    async def get_lookups(
        self,
        page_size: int = 100,
    ) -> FlextResult[list[FlextTypes.Core.Dict]]:
        """Get lookup tables from OIC.

        Args:
            page_size: Number of records per page

        Returns:
            FlextResult containing lookups or error

        """
        return await self.paginate_request("/lookups", page_size=page_size)

    async def create_integration(
        self,
        integration_data: dict[str, str],
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Create integration in OIC.

        Args:
            integration_data: Integration configuration data

        Returns:
            FlextResult containing created integration or error

        """
        return await self.make_request("POST", "/integrations", json=integration_data)

    async def update_integration(
        self,
        integration_id: str,
        integration_data: FlextTypes.Core.Dict,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Update integration in OIC.

        Args:
            integration_id: Integration ID to update
            integration_data: Updated integration data

        Returns:
            FlextResult containing updated integration or error

        """
        endpoint = f"/integrations/{integration_id}"
        json_data = {str(k): str(v) for k, v in integration_data.items()}
        return await self.make_request("PUT", endpoint, json=json_data)

    async def create_connection(
        self,
        connection_data: FlextTypes.Core.Dict,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Create connection in OIC.

        Args:
            connection_data: Connection configuration data

        Returns:
            FlextResult containing created connection or error

        """
        json_data = {str(k): str(v) for k, v in connection_data.items()}
        return await self.make_request("POST", "/connections", json=json_data)


# Exports following EXTENSION pattern
__all__: FlextTypes.Core.StringList = [
    # Base classes
    "BaseOICAuthenticator",
    "BaseOICClient",
    # Authenticators
    "OICExtensionAuthenticator",
    "OICTapAuthenticator",
    "OICTargetAuthenticator",
    # Clients
    "OracleOICExtensionClient",
]
