"""FLEXT Oracle OIC Client - Unified Client Pattern.

FLEXT Unified Module Pattern: Single unified client class consolidating
all Oracle OIC client functionality. Implements complete flext-api integration
with railway-oriented error handling.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import base64
from collections.abc import (
    Mapping,
    MutableSequence,
    Sequence,
)
from types import TracebackType
from typing import Self

from flext_api import FlextApi, FlextApiConstants, FlextApiSettings

from flext_oracle_oic import c, m, p, r, t, u

logger = u.fetch_logger(__name__)


class FlextOracleOicClient:
    """Unified Oracle OIC Client consolidating all client functionality.

    FLEXT Unified Module Pattern: Single unified client class consolidating
    all Oracle OIC client functionality including authentication, API operations,
    and enterprise error handling.
    """

    def __init__(
        self,
        connection_config: m.OracleOic.OICConnectionConfig,
        auth_config: m.OracleOic.OICAuthConfig,
    ) -> None:
        """Initialize unified Oracle OIC client.

        Args:
        connection_config: OIC connection configuration
        auth_config: OIC authentication configuration

        """
        self.connection_config = connection_config
        self.auth_config = auth_config
        self.logger = u.fetch_logger(f"{__name__}.{self.__class__.__name__}")
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
        connection_data: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Create connection in OIC."""
        json_data = dict(connection_data.items())
        return self.make_request(
            c.API.Method.POST,
            "/connections",
            json=json_data,
        )

    def create_integration(
        self,
        integration_data: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
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
        file_config: t.JsonMapping,
    ) -> t.JsonMapping:
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
        schedule_config: t.JsonMapping,
    ) -> t.JsonMapping:
        """Execute scheduled orchestration for an integration."""
        endpoint = f"/integrations/{integration_id}/schedules"
        result = self.make_request(
            c.API.Method.POST,
            endpoint,
            json=schedule_config,
        )
        return result.unwrap_or({})

    def get_access_token(self) -> p.Result[str]:
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
        type_filter: t.StrSequence | None = None,
        page_size: int = 100,
    ) -> p.Result[Sequence[t.JsonMapping]]:
        """Get adapter connections from OIC."""
        params: t.MutableStrMapping = {}
        if type_filter:
            params["q"] = f"adapterType in ({','.join(type_filter)})"
        return self.paginate_request("/connections", page_size=page_size, params=params)

    def get_integrations(
        self,
        status_filter: t.StrSequence | None = None,
        page_size: int = 100,
    ) -> p.Result[Sequence[t.JsonMapping]]:
        """Get integration flows from OIC."""
        params: t.MutableStrMapping = {}
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
    ) -> p.Result[Sequence[t.JsonMapping]]:
        """Get lookup tables from OIC."""
        return self.paginate_request("/lookups", page_size=page_size)

    def get_oauth_request_body(self) -> t.StrMapping:
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
    ) -> p.Result[Sequence[t.JsonMapping]]:
        """Get integration packages from OIC."""
        return self.paginate_request("/packages", page_size=page_size)

    def make_request(
        self,
        method: str,
        endpoint: str,
        params: t.StrMapping | None = None,
        data: t.StrMapping | None = None,
        json: t.JsonMapping | None = None,
    ) -> p.Result[t.JsonMapping]:
        """Make authenticated request to OIC API."""
        return (
            r[
                tuple[
                    str,
                    str,
                    t.StrMapping | None,
                    t.StrMapping | None,
                    t.JsonMapping | None,
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
        params: t.StrMapping | None = None,
    ) -> p.Result[Sequence[t.JsonMapping]]:
        """Paginate through OIC API responses."""
        try:
            all_records: MutableSequence[t.JsonMapping] = []
            offset = 0
            base_params: t.StrMapping = dict(params) if params else {}
            while True:
                request_params: t.MutableStrMapping = dict(base_params)
                request_params.update({"offset": str(offset), "limit": str(page_size)})
                response_result = self.make_request(
                    c.API.Method.GET,
                    endpoint,
                    params=request_params,
                )
                if response_result.failure:
                    return r[Sequence[t.JsonMapping]].fail(
                        response_result.error or "Request failed",
                    )
                response_data = response_result.value
                items_raw = response_data.get("items", [])
                if not isinstance(items_raw, list):
                    return r[Sequence[t.JsonMapping]].fail(
                        "Invalid items format",
                    )
                items: t.SequenceOf[t.JsonMapping] = [
                    dict(item) for item in items_raw if isinstance(item, dict)
                ]
                all_records.extend(items)
                has_more = response_data.get("hasMore", False)
                if not has_more or len(items) < page_size:
                    break
                offset += page_size
            return r[Sequence[t.JsonMapping]].ok(all_records)
        except c.EXC_NETWORK_TYPE as exc:
            error_msg = f"OIC pagination failed: {exc}"
            self.logger.exception(error_msg)
            return r[Sequence[t.JsonMapping]].fail(error_msg)

    def update_integration(
        self,
        integration_id: str,
        integration_data: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Update integration in OIC."""
        endpoint = f"/integrations/{integration_id}"
        json_data = dict(integration_data.items())
        return self.make_request(
            c.API.Method.PUT,
            endpoint,
            json=json_data,
        )

    def _build_client_with_token(self, token: str) -> p.Result[FlextApi]:
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
            client = FlextApi(settings=api_config)
            self._client = client
            return r[FlextApi].ok(client)
        except c.EXC_NETWORK_TYPE as exc:
            error_msg = f"Failed to create authenticated client: {exc}"
            self.logger.exception(error_msg)
            return r[FlextApi].fail(error_msg)

    def _create_authenticated_client(self) -> p.Result[FlextApi]:
        """Create new authenticated client."""
        return self.get_access_token().flat_map(self._build_client_with_token)

    def _execute_api_request(
        self,
        client: FlextApi,
        method: str,
        endpoint: str,
        _params: t.StrMapping | None,
        _data: t.StrMapping | None,
        json: t.JsonMapping | None,
    ) -> p.Result[t.JsonValue]:
        """Execute the actual API request."""
        try:
            api_data: t.JsonDict | None = None
            if json is not None:
                api_data = {
                    key: str(self._to_api_payload(value)) for key, value in json.items()
                }
            base_url = f"{self.connection_config.base_url.rstrip('/')}/ic/api/{self.connection_config.api_version}"
            full_url = f"{base_url}/{endpoint.lstrip('/')}"
            if method.upper() == FlextApiConstants.Api.Method.GET.value:
                response_result = client.get(full_url, headers=None)
            elif method.upper() == FlextApiConstants.Api.Method.POST.value:
                response_result = client.post(full_url, data=api_data, headers=None)
            elif method.upper() == FlextApiConstants.Api.Method.PUT.value:
                response_result = client.put(full_url, data=api_data, headers=None)
            elif method.upper() == FlextApiConstants.Api.Method.DELETE.value:
                response_result = client.delete(full_url, headers=None)
            else:
                return r[t.JsonValue].fail(f"Unsupported HTTP method: {method}")
            if response_result.failure:
                return r[t.JsonValue].fail_op("Request", response_result.error)
            response = response_result.value
            body: t.JsonValue = getattr(response, "body", str(response))
            return r[t.JsonValue].ok(body)
        except c.EXC_NETWORK_TYPE as exc:
            error_msg = f"OIC API request failed: {exc}"
            self.logger.exception(error_msg)
            return r[t.JsonValue].fail(error_msg)

    def _execute_token_request(
        self,
        request_data: tuple[t.StrMapping, t.StrMapping],
    ) -> p.Result[t.JsonValue]:
        """Execute OAuth token request."""
        headers, data = request_data
        try:
            api_config = FlextApiSettings.model_validate({
                "base_url": self.auth_config.oauth_token_url,
            })
            api_client = FlextApi(settings=api_config)
            oauth_data: t.JsonDict = {
                key: str(self._to_api_payload(value)) for key, value in data.items()
            }
            response_result = api_client.post("", data=oauth_data, headers=headers)
            if response_result.failure:
                return r[t.JsonValue].fail_op("OAuth request", response_result.error)
            response = response_result.value
            if response.status_code >= c.API.HTTP_ERROR_STATUS_THRESHOLD:
                return r[t.JsonValue].fail(
                    f"OAuth HTTP error: {response.status_code}",
                )
            body: t.JsonValue = getattr(response, "body", str(response))
            return r[t.JsonValue].ok(body)
        except c.EXC_NETWORK_TYPE as exc:
            error_msg = f"OAuth token request failed: {exc}"
            self.logger.exception(error_msg)
            return r[t.JsonValue].fail(error_msg)

    def _parse_api_response(
        self,
        response: t.JsonValue,
    ) -> p.Result[t.JsonMapping]:
        """Parse API response based on content type."""
        try:
            headers: t.JsonMapping | None = getattr(response, "headers", None)
            body: t.JsonValue | None = getattr(response, "body", None)
            if not isinstance(headers, Mapping):
                return r[t.JsonMapping].fail("Invalid response format")
            content_type = str(headers.get("content-type", ""))
            is_json = content_type.startswith("application/json")
            if is_json and not isinstance(body, (str, Mapping)):
                return r[t.JsonMapping].fail("Empty JSON response")
            parsed_body: t.JsonMapping
            if isinstance(body, str) and is_json:
                parsed_body = t.CONTAINER_MAPPING_ADAPTER.validate_json(body)
            elif isinstance(body, Mapping):
                parsed_body = body
            else:
                parsed_body = {"raw_content": str(body) if body is not None else ""}
            return r[t.JsonMapping].ok(parsed_body)
        except c.EXC_NETWORK_TYPE as exc:
            error_msg = f"Failed to parse API response: {exc}"
            self.logger.exception(error_msg)
            return r[t.JsonMapping].fail(error_msg)

    def _parse_token_response(self, response: t.JsonValue) -> p.Result[str]:
        """Parse access token from OAuth response."""
        try:
            body_raw: t.JsonValue = getattr(response, "body", None)
            if body_raw is None:
                return r[str].fail("Invalid response format")
            token_data: t.JsonMapping
            if isinstance(body_raw, Mapping):
                token_data = {k: body_raw[k] for k in body_raw}
            elif isinstance(body_raw, str):
                token_data = t.CONTAINER_MAPPING_ADAPTER.validate_json(body_raw)
            else:
                return r[str].fail("Empty or invalid OAuth response body")
            access_token: t.JsonValue | None = token_data.get("access_token")
            if isinstance(access_token, str) and access_token:
                return r[str].ok(access_token)
            return r[str].fail("No valid access token in response")
        except c.EXC_NETWORK_TYPE as exc:
            error_msg = f"Failed to parse OAuth response: {exc}"
            self.logger.exception(error_msg)
            return r[str].fail(error_msg)

    def _prepare_oauth_request(
        self,
    ) -> p.Result[tuple[t.StrMapping, t.StrMapping]]:
        """Prepare OAuth request headers and data."""
        try:
            encoded_credentials = self.encode_client_credentials()
            headers = {
                "Authorization": f"Basic {encoded_credentials}",
                "Content-Type": "application/x-www-form-urlencoded",
            }
            data = self.get_oauth_request_body()
            return r[tuple[t.StrMapping, t.StrMapping]].ok((
                headers,
                data,
            ))
        except c.EXC_NETWORK_TYPE as exc:
            error_msg = f"Failed to prepare OAuth request: {exc}"
            self.logger.exception(error_msg)
            return r[tuple[t.StrMapping, t.StrMapping]].fail(error_msg)

    def _store_and_return_token(self, token: str) -> str:
        """Store token and return it."""
        self._access_token = token
        self.logger.info("OIC OAuth2 authentication successful")
        return token

    def _to_api_payload(self, value: t.JsonValue) -> t.JsonValue:
        """Normalize t.JsonValue into flext-api request body value type."""
        if isinstance(value, (str, int, float, bool)) or value is None:
            return value
        if isinstance(value, Mapping):
            return {key: self._to_api_payload(item) for key, item in value.items()}
        match value:
            case list() | tuple():
                return [self._to_api_payload(item) for item in value]
            case _:
                return str(value)

    def _validate_token_url(self) -> p.Result[bool]:
        """Validate that OAuth token URL is configured."""
        if not self.auth_config.oauth_token_url:
            return r[bool].fail("OAuth token URL not configured")
        return r[bool].ok(value=True)


__all__: list[str] = ["FlextOracleOicClient"]
