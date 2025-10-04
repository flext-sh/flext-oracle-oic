"""FLEXT Module.

Copyright (c) 2025 FLEXT Team. All rights reserved. SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import base64
import json as json_module
from abc import ABC, abstractmethod
from typing import Self, cast, override

from flext_api import FlextApiClient
from flext_core import FlextLogger, FlextResult, FlextTypes

from flext_oracle_oic.models import FlextOracleOicExtModels

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

    @override
    def __init__(self, auth_config: FlextOracleOicExtModels.OICAuthConfig) -> None:
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
    def get_oauth_scopes(self: Self) -> str:
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
            # Build scope like: audience:443urn:opc:resource:consumer:all audience:443/ic/api/
            resource_aud = f"{audience}:443urn:opc:resource:consumer:all"
            api_aud = f"{audience}:443/ic/api/"
            return f"{resource_aud} {api_aud}"
        # Fallback to simple scope
        return self.auth_config.oauth_scope or "urn:opc:resource:consumer:all"

    def get_oauth_request_body(self) -> FlextTypes.StringDict:
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

    def get_access_token(self) -> FlextResult[str]:
        """Get access token using OAuth2 client credentials flow.

        Returns:
            FlextResult containing access token or error

        """
        # Railway-oriented OAuth2 token retrieval
        return (
            FlextResult[object]
            .ok(None)
            .flat_map(lambda _: self._validate_token_url())
            .flat_map(lambda _: self._prepare_oauth_request())
            .flat_map(self._execute_token_request)
            .flat_map(self._parse_token_response)
            .map(self._store_and_return_token)
        )

    def _validate_token_url(self) -> FlextResult[None]:
        """Validate that OAuth token URL is configured."""
        if not self.auth_config.oauth_token_url:
            return FlextResult[None].fail("OAuth token URL not configured")
        return FlextResult[None].ok(None)

    def _prepare_oauth_request(self) -> FlextResult[tuple[dict, dict]]:
        """Prepare OAuth request headers and data."""
        try:
            encoded_credentials = self.encode_client_credentials()
            headers = {
                "Authorization": f"Basic {encoded_credentials}",
                "Content-Type": "application/x-www-form-urlencoded",
            }
            data = self.get_oauth_request_body()
            return FlextResult[tuple[dict, dict]].ok((headers, data))
        except Exception as e:
            error_msg = f"Failed to prepare OAuth request: {e}"
            self.logger.exception(error_msg)
            return FlextResult[tuple[dict, dict]].fail(error_msg)

    def _execute_token_request(
        self, request_data: tuple[dict, dict]
    ) -> FlextResult[object]:
        """Execute OAuth token request."""
        headers, data = request_data
        try:
            api_client = FlextApiClient(self.auth_config.oauth_token_url)
            with api_client:
                response_result = api_client.post("", headers=headers, data=data)
                if response_result.is_failure:
                    return FlextResult[object].fail(
                        f"OAuth request failed: {response_result.error}"
                    )

                response = response_result.unwrap()
                if response.status_code >= HTTP_ERROR_STATUS_THRESHOLD:
                    return FlextResult[object].fail(
                        f"OAuth HTTP error: {response.status_code}"
                    )

                return FlextResult[object].ok(response)
        except Exception as e:
            error_msg = f"OAuth token request failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[object].fail(error_msg)

    def _parse_token_response(self, response: object) -> FlextResult[str]:
        """Parse access token from OAuth response."""
        try:
            # Handle response.body properly - it could be str, dict, or None
            if hasattr(response, "body"):
                body = response.body
            else:
                return FlextResult[str].fail("Invalid response format")

            if isinstance(body, dict):
                token_data = body
            elif isinstance(body, str):
                token_data = json_module.loads(body)
            else:
                return FlextResult[str].fail("Empty or invalid OAuth response body")

            access_token = token_data.get("access_token")
            if not access_token or not isinstance(access_token, str):
                return FlextResult[str].fail("No valid access token in response")

            return FlextResult[str].ok(access_token)
        except Exception as e:
            error_msg = f"Failed to parse OAuth response: {e}"
            self.logger.exception(error_msg)
            return FlextResult[str].fail(error_msg)

    def _store_and_return_token(self, token: str) -> str:
        """Store token and return it."""
        self._access_token = token
        self.logger.info("OIC OAuth2 authentication successful")
        return token


class BaseOICClient(ABC):
    """Base class for Oracle Integration Cloud API clients.

    EXTENSION Pattern: Base class for Oracle OIC API clients
    with authentication, retry logic and enterprise error handling.
    """

    @override
    def __init__(
        self,
        connection_config: FlextOracleOicExtModels.OICConnectionConfig,
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

    def get_authenticated_client(self) -> FlextResult[FlextApiClient]:
        """Get authenticated HTTP client.

        Returns:
            FlextResult containing authenticated client or error

        """
        # Railway-oriented authenticated client creation
        return (
            FlextResult[FlextApiClient]
            .ok(self._client)
            .flat_map(lambda client: client or self._create_authenticated_client())
        )

    def _create_authenticated_client(self) -> FlextResult[FlextApiClient]:
        """Create new authenticated client."""
        return self.authenticator.get_access_token().flat_map(
            self._build_client_with_token
        )

    def _build_client_with_token(self, token: str) -> FlextResult[FlextApiClient]:
        """Build client with access token."""
        try:
            client = FlextApiClient(
                base_url=self.get_base_url(),
                timeout=self.connection_config.request_timeout,
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
            )
            self._client = client
            return FlextResult[FlextApiClient].ok(client)
        except Exception as e:
            error_msg = f"Failed to create authenticated client: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextApiClient].fail(error_msg)

    def make_request(
        self,
        method: str,
        endpoint: str,
        params: FlextTypes.StringDict | None = None,
        data: FlextTypes.StringDict | None = None,
        json: FlextTypes.Dict | None = None,
    ) -> FlextResult[FlextTypes.Dict]:
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
        # Railway-oriented API request execution
        return (
            FlextResult[
                tuple[
                    str,
                    str,
                    FlextTypes.StringDict | None,
                    FlextTypes.StringDict | None,
                    FlextTypes.Dict | None,
                ]
            ]
            .ok((method, endpoint, params, data, json))
            .flat_map(
                lambda req_data: self.get_authenticated_client().map(
                    lambda client: (client, req_data)
                )
            )
            .flat_map(lambda client_req: self._execute_api_request(*client_req))
            .flat_map(self._parse_api_response)
        )

    def _execute_api_request(
        self,
        client: FlextApiClient,
        method: str,
        endpoint: str,
        params: FlextTypes.StringDict | None,
        data: FlextTypes.StringDict | None,
        json: FlextTypes.Dict | None,
    ) -> FlextResult[object]:
        """Execute the actual API request."""
        try:
            with client:
                response_result = client.request(
                    method=method,
                    url=endpoint,
                    params=params,
                    data=data,
                    json=cast("FlextTypes.StringDict | None", json),
                )

                if response_result.is_failure:
                    return FlextResult[object].fail(
                        f"Request failed: {response_result.error}"
                    )

                return FlextResult[object].ok(response_result.unwrap())
        except Exception as e:
            error_msg = f"OIC API request failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[object].fail(error_msg)

    def _parse_api_response(self, response: object) -> FlextResult[FlextTypes.Dict]:
        """Parse API response based on content type."""
        try:
            # Parse response body properly - it could be str, dict, or None
            if hasattr(response, "headers") and hasattr(response, "body"):
                headers = response.headers
                body = response.body

                if headers.get("content-type", "").startswith("application/json"):
                    if isinstance(body, dict):
                        return FlextResult[FlextTypes.Dict].ok(body)
                    if isinstance(body, str):
                        parsed_data = json_module.loads(body)
                        return FlextResult[FlextTypes.Dict].ok(parsed_data)
                    return FlextResult[FlextTypes.Dict].fail("Empty JSON response")

                # Non-JSON response
                if isinstance(body, str):
                    return FlextResult[FlextTypes.Dict].ok({"raw_content": body})
                if isinstance(body, dict):
                    return FlextResult[FlextTypes.Dict].ok(body)
                return FlextResult[FlextTypes.Dict].ok({"raw_content": str(body)})

            return FlextResult[FlextTypes.Dict].fail("Invalid response format")
        except Exception as e:
            error_msg = f"Failed to parse API response: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextTypes.Dict].fail(error_msg)

    def _build_request_url(self, endpoint: str) -> str:
        """Build full request URL."""
        base_url = self.get_base_url()
        return (
            f"{base_url}{endpoint}"
            if endpoint.startswith("/")
            else f"{base_url}/{endpoint}"
        )

    def paginate_request(
        self,
        endpoint: str,
        page_size: int = 100,
        params: FlextTypes.StringDict | None = None,
    ) -> FlextResult[list[FlextTypes.Dict]]:
        """Paginate through OIC API responses.

        Args:
            endpoint: API endpoint to paginate
            page_size: Number of records per page
            params: Additional query parameters

        Returns:
            FlextResult containing all paginated records or error

        """
        try:
            all_records: list[FlextTypes.Dict] = []
            offset = 0
            base_params: FlextTypes.StringDict = params or {}

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
                response_result = self.make_request(
                    "GET",
                    endpoint,
                    params=request_params,
                )
                if response_result.is_failure:
                    return FlextResult[list[FlextTypes.Dict]].fail(
                        response_result.error or "Request failed",
                    )

                response_data = response_result.unwrap()
                if response_data is None or not isinstance(response_data, dict):
                    return FlextResult[list[FlextTypes.Dict]].fail(
                        "Invalid response data format",
                    )

                items_raw = cast(
                    "list[FlextTypes.Dict]", response_data.get("items", [])
                )
                if not isinstance(items_raw, list):
                    return FlextResult[list[FlextTypes.Dict]].fail(
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

            return FlextResult[list[FlextTypes.Dict]].ok(all_records)

        except Exception as e:
            error_msg = f"OIC pagination failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[list[FlextTypes.Dict]].fail(error_msg)

    def __enter__(self) -> Self:
        """Context manager entry."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None:
        """Context manager exit."""
        if self._client:
            self._client.close()
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

    def get_oauth_scopes(self: Self) -> str:
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

    def get_integrations(
        self,
        status_filter: FlextTypes.StringList | None = None,
        page_size: int = 100,
    ) -> FlextResult[list[FlextTypes.Dict]]:
        """Get integration flows from OIC.

        Args:
            status_filter: Filter integrations by status
            page_size: Number of records per page

        Returns:
            FlextResult containing integrations or error

        """
        params: FlextTypes.StringDict = {}

        if status_filter:
            params["q"] = f"status in ({','.join(status_filter)})"

        return self.paginate_request(
            "/integrations",
            page_size=page_size,
            params=params,
        )

    def get_connections(
        self,
        type_filter: FlextTypes.StringList | None = None,
        page_size: int = 100,
    ) -> FlextResult[list[FlextTypes.Dict]]:
        """Get adapter connections from OIC.

        Args:
            type_filter: Filter connections by adapter type
            page_size: Number of records per page

        Returns:
            FlextResult containing connections or error

        """
        params: FlextTypes.StringDict = {}

        if type_filter:
            params["q"] = f"adapterType in ({','.join(type_filter)})"

        return self.paginate_request(
            "/connections",
            page_size=page_size,
            params=params,
        )

    def get_packages(
        self,
        page_size: int = 100,
    ) -> FlextResult[list[FlextTypes.Dict]]:
        """Get integration packages from OIC.

        Args:
            page_size: Number of records per page

        Returns:
            FlextResult containing packages or error

        """
        return self.paginate_request("/packages", page_size=page_size)

    def get_lookups(
        self,
        page_size: int = 100,
    ) -> FlextResult[list[FlextTypes.Dict]]:
        """Get lookup tables from OIC.

        Args:
            page_size: Number of records per page

        Returns:
            FlextResult containing lookups or error

        """
        return self.paginate_request("/lookups", page_size=page_size)

    def create_integration(
        self,
        integration_data: FlextTypes.Dict,
    ) -> FlextResult[FlextTypes.Dict]:
        """Create integration in OIC.

        Args:
            integration_data: Integration configuration data

        Returns:
            FlextResult containing created integration or error

        """
        return self.make_request("POST", "/integrations", json=integration_data)

    def update_integration(
        self,
        integration_id: str,
        integration_data: FlextTypes.Dict,
    ) -> FlextResult[FlextTypes.Dict]:
        """Update integration in OIC.

        Args:
            integration_id: Integration ID to update
            integration_data: Updated integration data

        Returns:
            FlextResult containing updated integration or error

        """
        endpoint = f"/integrations/{integration_id}"
        json_data: FlextTypes.Dict = {
            str(k): str(v) for k, v in integration_data.items()
        }
        return self.make_request("PUT", endpoint, json=json_data)

    def create_connection(
        self,
        connection_data: FlextTypes.Dict,
    ) -> FlextResult[FlextTypes.Dict]:
        """Create connection in OIC.

        Args:
            connection_data: Connection configuration data

        Returns:
            FlextResult containing created connection or error

        """
        json_data: FlextTypes.Dict = {
            str(k): str(v) for k, v in connection_data.items()
        }
        return self.make_request("POST", "/connections", json=json_data)


# Exports following EXTENSION pattern
__all__: FlextTypes.StringList = [
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
