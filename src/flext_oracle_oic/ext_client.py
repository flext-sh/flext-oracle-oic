"""FLEXT Oracle OIC Client - Unified Client Pattern.

FLEXT Unified Module Pattern: Single unified client class consolidating
all Oracle OIC client functionality. Implements complete flext-api integration
with railway-oriented error handling.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import base64
import json as json_module
from typing import Self, cast

from flext_api import FlextApiClient
from flext_api.config import FlextApiConfig
from flext_core import FlextLogger, FlextResult

from flext_oracle_oic.constants import FlextOracleOicConstants
from flext_oracle_oic.models import FlextOracleOicModels

logger = FlextLogger(__name__)

# Constants - use centralized constants from FlextOracleOicConstants
# HTTP_ERROR_STATUS_THRESHOLD moved to constants.py as part of refactoring

# ================================
# FLEXT Oracle OIC Client - Unified Client Pattern
# ================================


class FlextOracleOicClient:
    """Unified Oracle OIC Client consolidating all client functionality.

    FLEXT Unified Module Pattern: Single unified client class consolidating
    all Oracle OIC client functionality including authentication, API operations,
    and enterprise error handling.
    """

    def __init__(
        self,
        connection_config: FlextOracleOicModels.OICConnectionConfig,
        auth_config: FlextOracleOicModels.OICAuthConfig,
    ) -> None:
        """Initialize unified Oracle OIC client.

        Args:
        connection_config: OIC connection configuration
        auth_config: OIC authentication configuration

        """
        self.connection_config = connection_config
        self.auth_config = auth_config
        self.logger = FlextLogger(f"{__name__}.{self.__class__.__name__}")
        self._client: object | None = None
        self._access_token: str | None = None

    # Authentication Methods
    def get_oauth_request_body(self) -> dict[str, str]:
        """Generate OAuth2 request body for client credentials flow."""
        # Inline OAuth scopes logic - build scope like: audience:443urn:opc:resource:consumer:all audience:443/ic/api/
        audience = self.auth_config.oauth_client_aud
        if audience:
            # Build scope like: audience:443urn:opc:resource:consumer:all audience:443/ic/api/
            resource_aud = f"{audience}:443urn:opc:resource:consumer:all"
            api_aud = f"{audience}:443/ic/api/"
            scope = f"{resource_aud} {api_aud}"
        else:
            # Fallback to simple scope
            scope = self.auth_config.oauth_scope or "urn:opc:resource:consumer:all"

        return {
            "grant_type": "client_credentials",
            "scope": scope,
        }

    def encode_client_credentials(self) -> str:
        """Encode client credentials for HTTP Basic authentication."""
        client_id = self.auth_config.oauth_client_id
        client_secret = self.auth_config.oauth_client_secret.get_secret_value()

        credentials = f"{client_id}:{client_secret}"
        return base64.b64encode(credentials.encode()).decode()

    def get_access_token(self) -> FlextResult[str]:
        """Get access token using OAuth2 client credentials flow."""
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
        self,
        request_data: tuple[dict, dict],
    ) -> FlextResult[object]:
        """Execute OAuth token request."""
        headers, data = request_data
        try:
            api_config = FlextApiConfig(base_url=self.auth_config.oauth_token_url)
            api_client = FlextApiClient(api_config)
            with api_client:
                response_result = api_client.post("", headers=headers, data=data)
                if response_result.is_failure:
                    return FlextResult[object].fail(
                        f"OAuth request failed: {response_result.error}",
                    )

                response = response_result.unwrap()
                if (
                    response.status_code
                    >= FlextOracleOicConstants.API.HTTP_ERROR_STATUS_THRESHOLD
                ):
                    return FlextResult[object].fail(
                        f"OAuth HTTP error: {response.status_code}",
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

    # Client Methods
    def _create_authenticated_client(self) -> FlextResult[object]:
        """Create new authenticated client."""
        return self.get_access_token().flat_map(self._build_client_with_token)

    def _build_client_with_token(self, token: str) -> FlextResult[object]:
        """Build client with access token."""
        try:
            # Inline base URL construction: f"{base_url.rstrip('/')}/ic/api/{api_version}"
            base_url = f"{self.connection_config.base_url.rstrip('/')}/ic/api/{self.connection_config.api_version}"

            api_config = FlextApiConfig(
                base_url=base_url,
                timeout=self.connection_config.request_timeout,
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
            )

            client = FlextApiClient(api_config)
            self._client = client
            return FlextResult[object].ok(client)
        except Exception as e:
            error_msg = f"Failed to create authenticated client: {e}"
            self.logger.exception(error_msg)
            return FlextResult[object].fail(error_msg)

    def make_request(
        self,
        method: str,
        endpoint: str,
        params: dict[str, str] | None = None,
        data: dict[str, str] | None = None,
        json: dict[str, object] | None = None,
    ) -> FlextResult[dict[str, object]]:
        """Make authenticated request to OIC API."""
        # Railway-oriented API request execution
        return (
            FlextResult[
                tuple[
                    str,
                    str,
                    dict[str, str] | None,
                    dict[str, str] | None,
                    dict[str, object] | None,
                ]
            ]
            .ok((method, endpoint, params, data, json))
            .flat_map(
                lambda req_data: (
                    # Inline get_authenticated_client logic
                    FlextResult[object].ok(self._client)
                    if self._client is not None
                    else self._create_authenticated_client()
                ).map(lambda client: (client, req_data)),
            )
            .flat_map(
                lambda client_req: self._execute_api_request(
                    client_req[0],
                    *client_req[1],
                ),
            )
            .flat_map(self._parse_api_response)
        )

    def _execute_api_request(
        self,
        client: FlextApiClient,
        method: str,
        endpoint: str,
        _params: dict[str, str] | None,
        _data: dict[str, str] | None,
        json: dict[str, object] | None,
    ) -> FlextResult[object]:
        """Execute the actual API request."""
        try:
            if client is None:
                return FlextResult[object].fail("Client not available")

            with client:
                # Build full URL from base URL and endpoint - inline base URL construction
                base_url = f"{self.connection_config.base_url.rstrip('/')}/ic/api/{self.connection_config.api_version}"
                full_url = f"{base_url}/{endpoint.lstrip('/')}"

                # Use appropriate method based on HTTP method
                if method.upper() == "GET":
                    response_result = client.get(full_url, headers=None)
                elif method.upper() == "POST":
                    response_result = client.post(full_url, data=json, headers=None)
                elif method.upper() == "PUT":
                    response_result = client.put(full_url, data=json, headers=None)
                elif method.upper() == "DELETE":
                    response_result = client.delete(full_url, headers=None)
                else:
                    return FlextResult[object].fail(
                        f"Unsupported HTTP method: {method}",
                    )

                if response_result.is_failure:
                    return FlextResult[object].fail(
                        f"Request failed: {response_result.error}",
                    )

                return FlextResult[object].ok(response_result.unwrap())
        except Exception as e:
            error_msg = f"OIC API request failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[object].fail(error_msg)

    def _parse_api_response(self, response: object) -> FlextResult[dict[str, object]]:
        """Parse API response based on content type."""
        try:
            # Parse response body properly - it could be str, dict, or None
            if hasattr(response, "headers") and hasattr(response, "body"):
                headers = response.headers
                body = response.body

                if headers.get("content-type", "").startswith("application/json"):
                    if isinstance(body, dict):
                        return FlextResult[dict[str, object]].ok(body)
                    if isinstance(body, str):
                        parsed_data = json_module.loads(body)
                        return FlextResult[dict[str, object]].ok(parsed_data)
                    return FlextResult[dict[str, object]].fail("Empty JSON response")

                # Non-JSON response
                if isinstance(body, str):
                    return FlextResult[dict[str, object]].ok({"raw_content": body})
                if isinstance(body, dict):
                    return FlextResult[dict[str, object]].ok(body)
                return FlextResult[dict[str, object]].ok({"raw_content": str(body)})

            return FlextResult[dict[str, object]].fail("Invalid response format")
        except Exception as e:
            error_msg = f"Failed to parse API response: {e}"
            self.logger.exception(error_msg)
            return FlextResult[dict[str, object]].fail(error_msg)

    def paginate_request(
        self,
        endpoint: str,
        page_size: int = 100,
        params: dict[str, str] | None = None,
    ) -> FlextResult[list[dict[str, object]]]:
        """Paginate through OIC API responses."""
        try:
            all_records: list[dict[str, object]] = []
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

                # Make request
                response_result = self.make_request(
                    "GET",
                    endpoint,
                    params=request_params,
                )
                if response_result.is_failure:
                    return FlextResult[list[dict[str, object]]].fail(
                        response_result.error or "Request failed",
                    )

                response_data = response_result.unwrap()
                if response_data is None or not isinstance(response_data, dict):
                    return FlextResult[list[dict[str, object]]].fail(
                        "Invalid response data format",
                    )

                items_raw = cast(
                    "list[dict[str, object]]",
                    response_data.get("items", []),
                )
                if not isinstance(items_raw, list):
                    return FlextResult[list[dict[str, object]]].fail(
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

            return FlextResult[list[dict[str, object]]].ok(all_records)

        except Exception as e:
            error_msg = f"OIC pagination failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[list[dict[str, object]]].fail(error_msg)

    # Integration Methods
    def get_integrations(
        self,
        status_filter: list[str] | None = None,
        page_size: int = 100,
    ) -> FlextResult[list[dict[str, object]]]:
        """Get integration flows from OIC."""
        params: dict[str, str] = {}

        if status_filter:
            params["q"] = f"status in ({','.join(status_filter)})"

        return self.paginate_request(
            "/integrations",
            page_size=page_size,
            params=params,
        )

    def get_connections(
        self,
        type_filter: list[str] | None = None,
        page_size: int = 100,
    ) -> FlextResult[list[dict[str, object]]]:
        """Get adapter connections from OIC."""
        params: dict[str, str] = {}

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
    ) -> FlextResult[list[dict[str, object]]]:
        """Get integration packages from OIC."""
        return self.paginate_request("/packages", page_size=page_size)

    def get_lookups(
        self,
        page_size: int = 100,
    ) -> FlextResult[list[dict[str, object]]]:
        """Get lookup tables from OIC."""
        return self.paginate_request("/lookups", page_size=page_size)

    def create_integration(
        self,
        integration_data: dict[str, object],
    ) -> FlextResult[dict[str, object]]:
        """Create integration in OIC."""
        return self.make_request("POST", "/integrations", json=integration_data)

    def update_integration(
        self,
        integration_id: str,
        integration_data: dict[str, object],
    ) -> FlextResult[dict[str, object]]:
        """Update integration in OIC."""
        endpoint = f"/integrations/{integration_id}"
        json_data: dict[str, object] = {
            str(k): str(v) for k, v in integration_data.items()
        }
        return self.make_request("PUT", endpoint, json=json_data)

    def create_connection(
        self,
        connection_data: dict[str, object],
    ) -> FlextResult[dict[str, object]]:
        """Create connection in OIC."""
        json_data: dict[str, object] = {
            str(k): str(v) for k, v in connection_data.items()
        }
        return self.make_request("POST", "/connections", json=json_data)

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
        if self._client is not None:
            self._client.close()
            self._client = None


# Exports following unified pattern
__all__ = [
    "FlextOracleOicClient",
]
