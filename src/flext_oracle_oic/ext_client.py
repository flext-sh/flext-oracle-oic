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
from collections.abc import Mapping, Sequence
from typing import Self

from flext_api import FlextApi
from flext_api.settings import FlextApiSettings
from flext_core import FlextLogger, FlextResult, t

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
        connection_config: FlextOracleOicModels.OracleOic.OICConnectionConfig,
        auth_config: FlextOracleOicModels.OracleOic.OICAuthConfig,
    ) -> None:
        """Initialize unified Oracle OIC client.

        Args:
        connection_config: OIC connection configuration
        auth_config: OIC authentication configuration

        """
        self.connection_config = connection_config
        self.auth_config = auth_config
        self.logger = FlextLogger(f"{__name__}.{self.__class__.__name__}")
        self._client: FlextApi | None = None
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
            FlextResult[bool]
            .ok(True)
            .flat_map(lambda _: self._validate_token_url())
            .flat_map(lambda _: self._prepare_oauth_request())
            .flat_map(self._execute_token_request)
            .flat_map(self._parse_token_response)
            .map(self._store_and_return_token)
        )

    def _validate_token_url(self) -> FlextResult[bool]:
        """Validate that OAuth token URL is configured."""
        if not self.auth_config.oauth_token_url:
            return FlextResult[bool].fail("OAuth token URL not configured")
        return FlextResult[bool].ok(value=True)

    def _prepare_oauth_request(
        self,
    ) -> FlextResult[tuple[dict[str, str], dict[str, str]]]:
        """Prepare OAuth request headers and data."""
        try:
            encoded_credentials = self.encode_client_credentials()
            headers = {
                "Authorization": f"Basic {encoded_credentials}",
                "Content-Type": "application/x-www-form-urlencoded",
            }
            data = self.get_oauth_request_body()
            return FlextResult[tuple[dict[str, str], dict[str, str]]].ok((
                headers,
                data,
            ))
        except Exception as e:
            error_msg = f"Failed to prepare OAuth request: {e}"
            self.logger.exception(error_msg)
            return FlextResult[tuple[dict[str, str], dict[str, str]]].fail(error_msg)

    def _execute_token_request(
        self,
        request_data: tuple[dict[str, str], dict[str, str]],
    ) -> FlextResult[object]:
        """Execute OAuth token request."""
        headers, data = request_data
        try:
            api_config = FlextApiSettings(base_url=self.auth_config.oauth_token_url)
            api_client = FlextApi(api_config)
            oauth_data = {
                key: self._to_api_payload(value) for key, value in data.items()
            }
            response_result = api_client.post("", data=oauth_data, headers=headers)
            if response_result.is_failure:
                return FlextResult[object].fail(
                    f"OAuth request failed: {response_result.error}",
                )
            response = response_result.value
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
            body = getattr(response, "body", None)
            if body is None:
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
    def _create_authenticated_client(self) -> FlextResult[FlextApi]:
        """Create new authenticated client."""
        return self.get_access_token().flat_map(self._build_client_with_token)

    def _build_client_with_token(self, token: str) -> FlextResult[FlextApi]:
        """Build client with access token."""
        try:
            # Inline base URL construction: f"{base_url.rstrip('/')}/ic/api/{api_version}"
            base_url = f"{self.connection_config.base_url.rstrip('/')}/ic/api/{self.connection_config.api_version}"

            api_config = FlextApiSettings(
                base_url=base_url,
                timeout=self.connection_config.request_timeout,
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
            )

            client = FlextApi(api_config)
            self._client = client
            return FlextResult[FlextApi].ok(client)
        except Exception as e:
            error_msg = f"Failed to create authenticated client: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextApi].fail(error_msg)

    def make_request(
        self,
        method: str,
        endpoint: str,
        params: dict[str, str] | None = None,
        data: dict[str, str] | None = None,
        json: dict[str, t.GeneralValueType] | None = None,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Make authenticated request to OIC API."""
        # Railway-oriented API request execution
        return (
            FlextResult[
                tuple[
                    str,
                    str,
                    dict[str, str] | None,
                    dict[str, str] | None,
                    dict[str, t.GeneralValueType] | None,
                ]
            ]
            .ok((method, endpoint, params, data, json))
            .flat_map(
                lambda req_data: (
                    FlextResult[FlextApi].ok(self._client)
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
        client: FlextApi,
        method: str,
        endpoint: str,
        _params: dict[str, str] | None,
        _data: dict[str, str] | None,
        json: dict[str, t.GeneralValueType] | None,
    ) -> FlextResult[object]:
        """Execute the actual API request."""
        try:
            if client is None:
                return FlextResult[object].fail("Client not available")
            request_data: (
                dict[
                    str,
                    Mapping[str, object]
                    | Sequence[object]
                    | bool
                    | float
                    | int
                    | str
                    | None,
                ]
                | None
            ) = (
                {key: self._to_api_payload(value) for key, value in json.items()}
                if json is not None
                else None
            )
            base_url = f"{self.connection_config.base_url.rstrip('/')}/ic/api/{self.connection_config.api_version}"
            full_url = f"{base_url}/{endpoint.lstrip('/')}"
            if method.upper() == "GET":
                response_result = client.get(full_url, headers=None)
            elif method.upper() == "POST":
                response_result = client.post(full_url, data=request_data, headers=None)
            elif method.upper() == "PUT":
                response_result = client.put(full_url, data=request_data, headers=None)
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
            return FlextResult[object].ok(response_result.value)
        except Exception as e:
            error_msg = f"OIC API request failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[object].fail(error_msg)

    def _to_api_payload(
        self,
        value: object,
    ) -> Mapping[str, object] | Sequence[object] | bool | float | int | str | None:
        """Normalize GeneralValueType into flext-api request body value type."""
        if isinstance(value, (str, int, float, bool)) or value is None:
            return value
        if isinstance(value, dict):
            return {str(key): self._to_api_payload(item) for key, item in value.items()}
        if isinstance(value, (list, tuple)):
            return [self._to_api_payload(item) for item in value]
        return str(value)

    def _parse_api_response(
        self, response: object
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Parse API response based on content type."""
        try:
            # Parse response body properly - it could be str, dict, or None
            headers = getattr(response, "headers", None)
            body = getattr(response, "body", None)
            if isinstance(headers, Mapping):
                content_type = str(headers.get("content-type", ""))

                if content_type.startswith("application/json"):
                    if isinstance(body, dict):
                        return FlextResult[dict[str, t.GeneralValueType]].ok(body)
                    if isinstance(body, str):
                        parsed_data = json_module.loads(body)
                        return FlextResult[dict[str, t.GeneralValueType]].ok(
                            parsed_data
                        )
                    return FlextResult[dict[str, t.GeneralValueType]].fail(
                        "Empty JSON response"
                    )

                # Non-JSON response
                if isinstance(body, str):
                    return FlextResult[dict[str, t.GeneralValueType]].ok({
                        "raw_content": body
                    })
                if isinstance(body, dict):
                    return FlextResult[dict[str, t.GeneralValueType]].ok(body)
                return FlextResult[dict[str, t.GeneralValueType]].ok({
                    "raw_content": str(body)
                })

            return FlextResult[dict[str, t.GeneralValueType]].fail(
                "Invalid response format"
            )
        except Exception as e:
            error_msg = f"Failed to parse API response: {e}"
            self.logger.exception(error_msg)
            return FlextResult[dict[str, t.GeneralValueType]].fail(error_msg)

    def paginate_request(
        self,
        endpoint: str,
        page_size: int = 100,
        params: dict[str, str] | None = None,
    ) -> FlextResult[list[dict[str, t.GeneralValueType]]]:
        """Paginate through OIC API responses."""
        try:
            all_records: list[dict[str, t.GeneralValueType]] = []
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
                    return FlextResult[list[dict[str, t.GeneralValueType]]].fail(
                        response_result.error or "Request failed",
                    )

                response_data = response_result.value
                if response_data is None or not isinstance(response_data, dict):
                    return FlextResult[list[dict[str, t.GeneralValueType]]].fail(
                        "Invalid response data format",
                    )

                items_raw = response_data.get("items", [])
                if not isinstance(items_raw, list):
                    return FlextResult[list[dict[str, t.GeneralValueType]]].fail(
                        "Invalid items format",
                    )
                # Build typed list from validated items
                items: list[dict[str, t.GeneralValueType]] = [
                    item for item in items_raw if isinstance(item, dict)
                ]

                # Add items to collection
                all_records.extend(items)

                # Check if we have more pages
                has_more = response_data.get("hasMore", False)
                if not has_more or len(items) < page_size:
                    break

                offset += page_size

            return FlextResult[list[dict[str, t.GeneralValueType]]].ok(all_records)

        except Exception as e:
            error_msg = f"OIC pagination failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[list[dict[str, t.GeneralValueType]]].fail(error_msg)

    # Integration Methods
    def get_integrations(
        self,
        status_filter: list[str] | None = None,
        page_size: int = 100,
    ) -> FlextResult[list[dict[str, t.GeneralValueType]]]:
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
    ) -> FlextResult[list[dict[str, t.GeneralValueType]]]:
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
    ) -> FlextResult[list[dict[str, t.GeneralValueType]]]:
        """Get integration packages from OIC."""
        return self.paginate_request("/packages", page_size=page_size)

    def get_lookups(
        self,
        page_size: int = 100,
    ) -> FlextResult[list[dict[str, t.GeneralValueType]]]:
        """Get lookup tables from OIC."""
        return self.paginate_request("/lookups", page_size=page_size)

    def create_integration(
        self,
        integration_data: dict[str, t.GeneralValueType],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Create integration in OIC."""
        return self.make_request("POST", "/integrations", json=integration_data)

    def update_integration(
        self,
        integration_id: str,
        integration_data: dict[str, t.GeneralValueType],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Update integration in OIC."""
        endpoint = f"/integrations/{integration_id}"
        json_data: dict[str, t.GeneralValueType] = {
            str(k): str(v) for k, v in integration_data.items()
        }
        return self.make_request("PUT", endpoint, json=json_data)

    def create_connection(
        self,
        connection_data: dict[str, t.GeneralValueType],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Create connection in OIC."""
        json_data: dict[str, t.GeneralValueType] = {
            str(k): str(v) for k, v in connection_data.items()
        }
        return self.make_request("POST", "/connections", json=json_data)

    def execute_scheduled_orchestration(
        self,
        integration_id: str,
        schedule_config: dict[str, t.GeneralValueType],
        **_kwargs: object,
    ) -> dict[str, t.GeneralValueType]:
        """Execute scheduled orchestration for an integration."""
        endpoint = f"/integrations/{integration_id}/schedules"
        result = self.make_request("POST", endpoint, json=schedule_config)
        return result.value if result.is_success else {}

    def execute_file_transfer(
        self,
        integration_id: str,
        file_config: dict[str, t.GeneralValueType],
        **_kwargs: object,
    ) -> dict[str, t.GeneralValueType]:
        """Execute file transfer pattern for an integration."""
        endpoint = f"/integrations/{integration_id}/files"
        result = self.make_request("POST", endpoint, json=file_config)
        return result.value if result.is_success else {}

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
            close_fn = getattr(self._client, "close", None)
            if callable(close_fn):
                close_fn()
            self._client = None


# Exports following unified pattern
__all__ = [
    "FlextOracleOicClient",
]
