"""FLEXT Module.

Copyright (c) 2025 FLEXT Team. All rights reserved. SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import base64
from abc import ABC, abstractmethod
from typing import Self

import httpx
from flext_core import FlextLogger, FlextResult, FlextTypes

from flext_oracle_oic_ext.ext_models import OICAuthConfig, OICConnectionConfig

logger = FlextLogger(__name__)
# ================================
# EXTENSION Pattern: Base Classes
# ================================


class BaseOICAuthenticator(ABC):
    """Base class for Oracle Integration Cloud authentication patterns.

    Padrão EXTENSION: Classe base para autenticação Oracle OIC
    com OAuth2 IDCS e gerenciamento de tokens.
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

    def get_oauth_request_body(self) -> FlextTypes.Core.Dict:
        """Generate OAuth2 request body for client credentials flow.

        Returns:
            Dict containing grant_type and scope for OAuth2 token request

        """
        return {
            "grant_type": "client_credentials",
            "scope": self.get_oauth_scopes(),
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
        try:
            if not self.auth_config.oauth_token_url:
                return FlextResult[str].fail("OAuth token URL not configured")

            # Encode client credentials for HTTP Basic authentication
            encoded_credentials = self.encode_client_credentials()

            headers = {
                "Authorization": f"Basic {encoded_credentials}",
                "Content-Type": "application/x-www-form-urlencoded",
            }

            # Make token request using httpx
            with httpx.Client() as client:
                response = client.post(
                    self.auth_config.oauth_token_url,
                    headers=headers,
                    data=self.get_oauth_request_body(),
                    timeout=30,
                )
                response.raise_for_status()

                token_data = response.json()
                self._access_token = token_data["access_token"]

                self.logger.info("OIC OAuth2 authentication successful")
                return FlextResult[str].ok(self._access_token)

        except httpx.TimeoutException as e:
            error_msg = f"OIC OAuth2 authentication timeout: {e}"
            self.logger.exception(error_msg)
            return FlextResult[str].fail(error_msg)
        except httpx.HTTPStatusError as e:
            error_msg = f"OIC OAuth2 authentication HTTP error: {e}"
            self.logger.exception(error_msg)
            return FlextResult[str].fail(error_msg)
        except httpx.RequestError as e:
            error_msg = f"OIC OAuth2 authentication request failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[str].fail(error_msg)
        except KeyError as e:
            error_msg = f"Invalid OAuth2 response format: missing {e}"
            self.logger.exception(error_msg)
            return FlextResult[str].fail(error_msg)
        except Exception as e:
            error_msg = f"OIC authentication error: {e}"
            self.logger.exception(error_msg)
            return FlextResult[str].fail(error_msg)


class BaseOICClient(ABC):
    """Base class for Oracle Integration Cloud API clients.

    Padrão EXTENSION: Classe base para clientes Oracle OIC API
    com autenticação, retry logic e tratamento de erros enterprise.
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
        self._client: httpx.Client | None = None

    @abstractmethod
    def get_base_url(self) -> str:
        """Get OIC API base URL."""

    def get_authenticated_client(self) -> FlextResult[httpx.Client]:
        """Get authenticated HTTP client.

        Returns:
            FlextResult containing authenticated client or error

        """
        try:
            if not self._client:
                # Get OAuth2 token
                token_result = self.authenticator.get_access_token()
                if not token_result.success:
                    return FlextResult[httpx.Client].fail(
                        f"Authentication failed: {token_result.error}",
                    )

                # Create authenticated client
                self._client = httpx.Client(
                    headers={
                        "Authorization": f"Bearer {token_result.data}",
                        "Content-Type": "application/json",
                        "Accept": "application/json",
                    },
                    timeout=self.connection_config.request_timeout,
                    verify=self.connection_config.verify_ssl,
                )

            return FlextResult[httpx.Client].ok(self._client)

        except Exception as e:
            error_msg = f"Failed to create authenticated client: {e}"
            self.logger.exception(error_msg)
            return FlextResult[httpx.Client].fail(error_msg)

    def make_request(
        self,
        method: str,
        endpoint: str,
        params: dict[str, str | int | float] | None = None,
        data: FlextTypes.Core.Dict | None = None,
        json: FlextTypes.Core.Dict | None = None,
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
            client_result = self.get_authenticated_client()
            if not client_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    client_result.error or "Client error"
                )

            client = client_result.data
            if client is None:
                return FlextResult[None].fail("Failed to get client")

            # Build full URL
            url = self._build_request_url(endpoint)

            # Make request
            response = client.request(
                method=method,
                url=url,
                params=params,
                data=data,
                json=json,
            )
            response.raise_for_status()

            # Parse response
            if response.headers.get("content-type", "").startswith("application/json"):
                return FlextResult[FlextTypes.Core.Dict].ok(response.json())
            return FlextResult[FlextTypes.Core.Dict].ok({"raw_content": response.text})

        except httpx.TimeoutException as e:
            error_msg = f"OIC API request timeout: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextTypes.Core.Dict].fail(error_msg)
        except httpx.HTTPStatusError as e:
            return self._handle_http_error(e)
        except httpx.RequestError as e:
            error_msg = f"OIC API request failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextTypes.Core.Dict].fail(error_msg)
        except Exception as e:
            error_msg = f"OIC API client error: {e}"
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

    def _handle_http_error(
        self,
        e: httpx.HTTPStatusError,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Handle HTTP errors."""
        try:
            error_data = e.response.json()
            error_msg = f"OIC API error: {error_data}"
        except Exception:
            error_msg = f"OIC API error: {e.response.text}"

        self.logger.error(error_msg)
        return FlextResult[FlextTypes.Core.Dict].fail(error_msg)

    def paginate_request(
        self,
        endpoint: str,
        page_size: int = 100,
        params: dict[str, str | int | float] | None = None,
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
            base_params: dict[str, str | int | float] = params or {}

            while True:
                # Prepare pagination parameters
                request_params = base_params.copy()
                request_params.update(
                    {
                        "offset": offset,
                        "limit": page_size,
                    },
                )

                # Make request
                response_result = self.make_request(
                    "GET",
                    endpoint,
                    params=request_params,
                )
                if not response_result.success:
                    return FlextResult[list[FlextTypes.Core.Dict]].fail(
                        response_result.error or "Request failed"
                    )

                response_data = response_result.data
                if response_data is None or not isinstance(response_data, dict):
                    return FlextResult[None].fail("Invalid response data format")

                items_raw = response_data.get("items", [])
                if not isinstance(items_raw, list):
                    return FlextResult[list[FlextTypes.Core.Dict]].fail(
                        "Invalid items format"
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

    Padrão EXTENSION: Authenticator padrão para extensions
    Oracle OIC com scopes apropriados.
    """

    def get_oauth_scopes(self) -> str:
        """Get OAuth2 scopes for OIC Extension."""
        return self.build_oauth_scopes()


class OICTapAuthenticator(BaseOICAuthenticator):
    """OIC Tap-specific authenticator with read scopes.

    Padrão EXTENSION: Authenticator para tap Oracle OIC
    focado em operações de leitura.
    """

    def get_oauth_scopes(self) -> str:
        """Get OAuth2 scopes for OIC Tap."""
        return self.build_oauth_scopes()


class OICTargetAuthenticator(BaseOICAuthenticator):
    """OIC Target-specific authenticator with write permissions.

    Padrão EXTENSION: Authenticator para target Oracle OIC
    com permissões de escrita.
    """

    def get_oauth_scopes(self) -> str:
        """Get OAuth2 scopes for OIC Target."""
        return self.build_oauth_scopes()


class OracleOICExtensionClient(BaseOICClient):
    """Main Oracle OIC Extension client.

    Padrão EXTENSION: Cliente principal para extension Oracle OIC
    com funcionalidades enterprise completas.
    """

    def get_base_url(self) -> str:
        """Get OIC API base URL."""
        return f"{self.connection_config.base_url.rstrip('/')}/ic/api/{self.connection_config.api_version}"

    def get_integrations(
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
        params: dict[str, str | int | float] = {}

        if status_filter:
            params["q"] = f"status in ({','.join(status_filter)})"

        return self.paginate_request(
            "/integrations",
            page_size=page_size,
            params=params,
        )

    def get_connections(
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
        params: dict[str, str | int | float] = {}

        if type_filter:
            params["q"] = f"adapterType in ({','.join(type_filter)})"

        return self.paginate_request("/connections", page_size=page_size, params=params)

    def get_packages(
        self,
        page_size: int = 100,
    ) -> FlextResult[list[FlextTypes.Core.Dict]]:
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
    ) -> FlextResult[list[FlextTypes.Core.Dict]]:
        """Get lookup tables from OIC.

        Args:
            page_size: Number of records per page

        Returns:
            FlextResult containing lookups or error

        """
        return self.paginate_request("/lookups", page_size=page_size)

    def create_integration(
        self,
        integration_data: FlextTypes.Core.Dict,
    ) -> FlextResult[FlextTypes.Core.Dict]:
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
        return self.make_request("PUT", endpoint, json=integration_data)

    def create_connection(
        self,
        connection_data: FlextTypes.Core.Dict,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Create connection in OIC.

        Args:
            connection_data: Connection configuration data

        Returns:
            FlextResult containing created connection or error

        """
        return self.make_request("POST", "/connections", json=connection_data)


# Exports seguindo padrão EXTENSION
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
