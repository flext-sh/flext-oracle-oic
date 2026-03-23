"""FLEXT Oracle OIC Client - Unified Client Pattern.

FLEXT Unified Module Pattern: Single unified client class consolidating
all Oracle OIC client functionality. Implements complete flext-api integration
with railway-oriented error handling.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import base64
from collections.abc import Mapping, Sequence
from types import TracebackType
from typing import Self

from flext_api import FlextApi, FlextApiSettings
from flext_core import FlextLogger, r
from pydantic import TypeAdapter

from flext_oracle_oic.constants import c
from flext_oracle_oic.models import FlextOracleOicModels
from flext_oracle_oic.typings import t

logger = FlextLogger(__name__)


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

    def __enter__(self) -> Self:
        """Context manager entry."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Context manager exit."""
        if self._client is not None:
            close_fn = getattr(self._client, "close", None)
            if callable(close_fn):
                close_fn()
            self._client = None

    def create_connection(
        self,
        connection_data: Mapping[str, t.NormalizedValue],
    ) -> r[Mapping[str, t.NormalizedValue]]:
        """Create connection in OIC."""
        json_data: Mapping[str, t.NormalizedValue] = {
            str(k): str(v) for k, v in connection_data.items()
        }
        return self.make_request(
            c.API.Method.POST,
            "/connections",
            json=json_data,
        )

    def create_integration(
        self,
        integration_data: Mapping[str, t.NormalizedValue],
    ) -> r[Mapping[str, t.NormalizedValue]]:
        """Create integration in OIC."""
        return self.make_request(
            c.API.Method.POST,
            "/integrations",
            json=integration_data,
        )

    def encode_client_credentials(self) -> str:
        """Encode client credentials for HTTP Basic authentication."""
        client_id = self.auth_config.oauth_client_id
        client_secret = self.auth_config.oauth_client_secret.get_secret_value()
        credentials = f"{client_id}:{client_secret}"
        return base64.b64encode(credentials.encode()).decode()

    def execute_file_transfer(
        self,
        integration_id: str,
        file_config: Mapping[str, t.NormalizedValue],
        **_kwargs: t.Scalar,
    ) -> Mapping[str, t.NormalizedValue]:
        """Execute file transfer pattern for an integration."""
        endpoint = f"/integrations/{integration_id}/files"
        result = self.make_request(
            c.API.Method.POST,
            endpoint,
            json=file_config,
        )
        return result.unwrap_or({})

    def execute_scheduled_orchestration(
        self,
        integration_id: str,
        schedule_config: Mapping[str, t.NormalizedValue],
        **_kwargs: t.Scalar,
    ) -> Mapping[str, t.NormalizedValue]:
        """Execute scheduled orchestration for an integration."""
        endpoint = f"/integrations/{integration_id}/schedules"
        result = self.make_request(
            c.API.Method.POST,
            endpoint,
            json=schedule_config,
        )
        return result.unwrap_or({})

    def get_access_token(self) -> r[str]:
        """Get access token using OAuth2 client credentials flow."""
        return (
            r[bool]
            .ok(True)
            .flat_map(lambda _: self._validate_token_url())
            .flat_map(lambda _: self._prepare_oauth_request())
            .flat_map(self._execute_token_request)
            .flat_map(self._parse_token_response)
            .map(self._store_and_return_token)
        )

    def get_connections(
        self,
        type_filter: Sequence[str] | None = None,
        page_size: int = 100,
    ) -> r[Sequence[Mapping[str, t.NormalizedValue]]]:
        """Get adapter connections from OIC."""
        params: dict[str, str] = {}
        if type_filter:
            params["q"] = f"adapterType in ({','.join(type_filter)})"
        return self.paginate_request("/connections", page_size=page_size, params=params)

    def get_integrations(
        self,
        status_filter: Sequence[str] | None = None,
        page_size: int = 100,
    ) -> r[Sequence[Mapping[str, t.NormalizedValue]]]:
        """Get integration flows from OIC."""
        params: dict[str, str] = {}
        if status_filter:
            params["q"] = f"status in ({','.join(status_filter)})"
        return self.paginate_request(
            "/integrations",
            page_size=page_size,
            params=params,
        )

    def get_lookups(
        self,
        page_size: int = 100,
    ) -> r[Sequence[Mapping[str, t.NormalizedValue]]]:
        """Get lookup tables from OIC."""
        return self.paginate_request("/lookups", page_size=page_size)

    def get_oauth_request_body(self) -> Mapping[str, str]:
        """Generate OAuth2 request body for client credentials flow."""
        audience = self.auth_config.oauth_client_aud
        if audience:
            resource_aud = f"{audience}:443urn:opc:resource:consumer:all"
            api_aud = f"{audience}:443/ic/api/"
            scope = f"{resource_aud} {api_aud}"
        else:
            scope = self.auth_config.oauth_scope or "urn:opc:resource:consumer:all"
        return {"grant_type": "client_credentials", "scope": scope}

    def get_packages(
        self,
        page_size: int = 100,
    ) -> r[Sequence[Mapping[str, t.NormalizedValue]]]:
        """Get integration packages from OIC."""
        return self.paginate_request("/packages", page_size=page_size)

    def make_request(
        self,
        method: str,
        endpoint: str,
        params: Mapping[str, str] | None = None,
        data: Mapping[str, str] | None = None,
        json: Mapping[str, t.NormalizedValue] | None = None,
    ) -> r[Mapping[str, t.NormalizedValue]]:
        """Make authenticated request to OIC API."""
        return (
            r[
                tuple[
                    str,
                    str,
                    Mapping[str, str] | None,
                    Mapping[str, str] | None,
                    Mapping[str, t.NormalizedValue] | None,
                ]
            ]
            .ok((method, endpoint, params, data, json))
            .flat_map(
                lambda req_data: (
                    r[FlextApi].ok(self._client)
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

    def paginate_request(
        self,
        endpoint: str,
        page_size: int = 100,
        params: Mapping[str, str] | None = None,
    ) -> r[Sequence[Mapping[str, t.NormalizedValue]]]:
        """Paginate through OIC API responses."""
        try:
            all_records: list[Mapping[str, t.NormalizedValue]] = []
            offset = 0
            base_params: dict[str, str] = dict(params) if params else {}
            while True:
                request_params = base_params.copy()
                request_params.update({"offset": str(offset), "limit": str(page_size)})
                response_result = self.make_request(
                    c.API.Method.GET,
                    endpoint,
                    params=request_params,
                )
                if response_result.is_failure:
                    return r[Sequence[Mapping[str, t.NormalizedValue]]].fail(
                        response_result.error or "Request failed",
                    )
                response_data = response_result.value
                if not isinstance(response_data, Mapping):
                    return r[Sequence[Mapping[str, t.NormalizedValue]]].fail(
                        "Invalid response data format",
                    )
                items_raw = response_data.get("items", [])
                if not isinstance(items_raw, list):
                    return r[Sequence[Mapping[str, t.NormalizedValue]]].fail(
                        "Invalid items format",
                    )
                items: Sequence[Mapping[str, t.NormalizedValue]] = [
                    dict(item) for item in items_raw if isinstance(item, dict)
                ]
                all_records.extend(items)
                has_more = response_data.get("hasMore", False)
                if not has_more or len(items) < page_size:
                    break
                offset += page_size
            return r[Sequence[Mapping[str, t.NormalizedValue]]].ok(all_records)
        except (
            ConnectionError,
            TimeoutError,
            ValueError,
        ) as e:
            error_msg = f"OIC pagination failed: {e}"
            self.logger.exception(error_msg)
            return r[Sequence[Mapping[str, t.NormalizedValue]]].fail(error_msg)

    def update_integration(
        self,
        integration_id: str,
        integration_data: Mapping[str, t.NormalizedValue],
    ) -> r[Mapping[str, t.NormalizedValue]]:
        """Update integration in OIC."""
        endpoint = f"/integrations/{integration_id}"
        json_data: Mapping[str, t.NormalizedValue] = {
            str(k): str(v) for k, v in integration_data.items()
        }
        return self.make_request(
            c.API.Method.PUT,
            endpoint,
            json=json_data,
        )

    def _build_client_with_token(self, token: str) -> r[FlextApi]:
        """Build client with access token."""
        try:
            base_url = f"{self.connection_config.base_url.rstrip('/')}/ic/api/{self.connection_config.api_version}"
            api_config = FlextApiSettings.model_validate({
                "base_url": base_url,
                "timeout": self.connection_config.request_timeout,
                "headers": {
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
            })
            client = FlextApi(api_config)
            self._client = client
            return r[FlextApi].ok(client)
        except (
            ConnectionError,
            TimeoutError,
            ValueError,
        ) as e:
            error_msg = f"Failed to create authenticated client: {e}"
            self.logger.exception(error_msg)
            return r[FlextApi].fail(error_msg)

    def _create_authenticated_client(self) -> r[FlextApi]:
        """Create new authenticated client."""
        return self.get_access_token().flat_map(self._build_client_with_token)

    def _execute_api_request(
        self,
        client: FlextApi,
        method: str,
        endpoint: str,
        _params: Mapping[str, str] | None,
        _data: Mapping[str, str] | None,
        json: Mapping[str, t.NormalizedValue] | None,
    ) -> r[t.NormalizedValue]:
        """Execute the actual API request."""
        try:
            request_body: Mapping[str, t.NormalizedValue] | None = (
                {key: self._to_api_payload(value) for key, value in json.items()}
                if json is not None
                else None
            )
            api_data: Mapping[str, t.ContainerValue] | None = request_body
            base_url = f"{self.connection_config.base_url.rstrip('/')}/ic/api/{self.connection_config.api_version}"
            full_url = f"{base_url}/{endpoint.lstrip('/')}"
            if method.upper() == "GET":
                response_result = client.get(full_url, headers=None)
            elif method.upper() == "POST":
                response_result = client.post(full_url, data=api_data, headers=None)
            elif method.upper() == "PUT":
                response_result = client.put(full_url, data=api_data, headers=None)
            elif method.upper() == "DELETE":
                response_result = client.delete(full_url, headers=None)
            else:
                return r[t.NormalizedValue].fail(f"Unsupported HTTP method: {method}")
            if response_result.is_failure:
                return r[t.NormalizedValue].fail(
                    f"Request failed: {response_result.error}",
                )
            response_value: t.NormalizedValue = response_result.value
            return r[t.NormalizedValue].ok(response_value)
        except (
            ConnectionError,
            TimeoutError,
            ValueError,
        ) as e:
            error_msg = f"OIC API request failed: {e}"
            self.logger.exception(error_msg)
            return r[t.NormalizedValue].fail(error_msg)

    def _execute_token_request(
        self,
        request_data: tuple[Mapping[str, str], Mapping[str, str]],
    ) -> r[t.NormalizedValue]:
        """Execute OAuth token request."""
        headers, data = request_data
        try:
            api_config = FlextApiSettings.model_validate({
                "base_url": self.auth_config.oauth_token_url
            })
            api_client = FlextApi(api_config)
            oauth_data: Mapping[str, t.ContainerValue] = {
                key: self._to_api_payload(value) for key, value in data.items()
            }
            response_result = api_client.post("", data=oauth_data, headers=headers)
            if response_result.is_failure:
                return r[t.NormalizedValue].fail(
                    f"OAuth request failed: {response_result.error}",
                )
            response = response_result.value
            if response.status_code >= c.API.HTTP_ERROR_STATUS_THRESHOLD:
                return r[t.NormalizedValue].fail(
                    f"OAuth HTTP error: {response.status_code}",
                )
            normalized_response: t.NormalizedValue = response
            return r[t.NormalizedValue].ok(normalized_response)
        except (
            ConnectionError,
            TimeoutError,
            ValueError,
        ) as e:
            error_msg = f"OAuth token request failed: {e}"
            self.logger.exception(error_msg)
            return r[t.NormalizedValue].fail(error_msg)

    def _parse_api_response(
        self,
        response: t.NormalizedValue,
    ) -> r[Mapping[str, t.NormalizedValue]]:
        """Parse API response based on content type."""
        try:
            headers: Mapping[str, t.NormalizedValue] | None = getattr(
                response,
                "headers",
                None,
            )
            body: t.NormalizedValue | None = getattr(response, "body", None)
            match headers:
                case Mapping():
                    content_type_val = headers.get("content-type", "")
                    content_type = str(content_type_val) if content_type_val else ""
                    if content_type.startswith("application/json"):
                        if isinstance(body, Mapping):
                            return r[Mapping[str, t.NormalizedValue]].ok(body)
                        match body:
                            case str():
                                json_parser: TypeAdapter[
                                    Mapping[str, t.NormalizedValue]
                                ] = TypeAdapter(Mapping[str, t.NormalizedValue])
                                parsed_data = json_parser.validate_json(body)
                                return r[Mapping[str, t.NormalizedValue]].ok(
                                    parsed_data,
                                )
                            case _:
                                return r[Mapping[str, t.NormalizedValue]].fail(
                                    "Empty JSON response",
                                )
                    match body:
                        case str():
                            return r[Mapping[str, t.NormalizedValue]].ok({
                                "raw_content": body,
                            })
                        case _ if isinstance(body, Mapping):
                            return r[Mapping[str, t.NormalizedValue]].ok(body)
                        case _:
                            return r[Mapping[str, t.NormalizedValue]].ok({
                                "raw_content": str(body),
                            })
                case _:
                    return r[Mapping[str, t.NormalizedValue]].fail(
                        "Invalid response format",
                    )
        except (
            ConnectionError,
            TimeoutError,
            ValueError,
        ) as e:
            error_msg = f"Failed to parse API response: {e}"
            self.logger.exception(error_msg)
            return r[Mapping[str, t.NormalizedValue]].fail(error_msg)

    def _parse_token_response(self, response: t.NormalizedValue) -> r[str]:
        """Parse access token from OAuth response."""
        try:
            body = getattr(response, "body", None)
            if body is None:
                return r[str].fail("Invalid response format")
            token_data: Mapping[str, t.NormalizedValue]
            if isinstance(body, dict):
                token_data = body
            else:
                match body:
                    case str():
                        token_parser: TypeAdapter[Mapping[str, t.NormalizedValue]] = (
                            TypeAdapter(Mapping[str, t.NormalizedValue])
                        )
                        token_data = token_parser.validate_json(body)
                    case _:
                        return r[str].fail("Empty or invalid OAuth response body")
            access_token = token_data.get("access_token")
            match access_token:
                case str() as token if token:
                    return r[str].ok(token)
                case _:
                    return r[str].fail("No valid access token in response")
        except (
            ConnectionError,
            TimeoutError,
            ValueError,
        ) as e:
            error_msg = f"Failed to parse OAuth response: {e}"
            self.logger.exception(error_msg)
            return r[str].fail(error_msg)

    def _prepare_oauth_request(
        self,
    ) -> r[tuple[Mapping[str, str], Mapping[str, str]]]:
        """Prepare OAuth request headers and data."""
        try:
            encoded_credentials = self.encode_client_credentials()
            headers = {
                "Authorization": f"Basic {encoded_credentials}",
                "Content-Type": "application/x-www-form-urlencoded",
            }
            data = self.get_oauth_request_body()
            return r[tuple[Mapping[str, str], Mapping[str, str]]].ok((
                headers,
                data,
            ))
        except (
            ConnectionError,
            TimeoutError,
            ValueError,
        ) as e:
            error_msg = f"Failed to prepare OAuth request: {e}"
            self.logger.exception(error_msg)
            return r[tuple[Mapping[str, str], Mapping[str, str]]].fail(error_msg)

    def _store_and_return_token(self, token: str) -> str:
        """Store token and return it."""
        self._access_token = token
        self.logger.info("OIC OAuth2 authentication successful")
        return token

    def _to_api_payload(self, value: t.NormalizedValue) -> t.NormalizedValue:
        """Normalize t.NormalizedValue into flext-api request body value type."""
        if isinstance(value, (str, int, float, bool)) or value is None:
            return value
        if isinstance(value, Mapping):
            return {str(key): self._to_api_payload(item) for key, item in value.items()}
        match value:
            case list() | tuple():
                return [self._to_api_payload(item) for item in value]
            case _:
                return str(value)

    def _validate_token_url(self) -> r[bool]:
        """Validate that OAuth token URL is configured."""
        if not self.auth_config.oauth_token_url:
            return r[bool].fail("OAuth token URL not configured")
        return r[bool].ok(value=True)


__all__ = ["FlextOracleOicClient"]
