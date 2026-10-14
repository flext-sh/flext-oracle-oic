"""FLEXT Oracle OIC Client - Unified Client Pattern.

FLEXT Unified Module Pattern: Single unified client class consolidating
all Oracle OIC client functionality. Implements complete flext-api integration
with railway-oriented error handling.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import base64
from collections.abc import Mapping, MutableSequence
from typing import TYPE_CHECKING, Self

from flext_api import FlextApi, FlextApiSettings

from flext_oracle_oic import c, m, p, r, t, u

if TYPE_CHECKING:
    from types import TracebackType


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
        """Initialize the unified Oracle OIC client.

        Args:
            connection_config: OIC connection configuration.
            auth_config: OIC authentication configuration.

        """
        self.connection_config = connection_config
        self.auth_config = auth_config
        self.logger = u.fetch_logger(f"{__name__}.{self.__class__.__name__}")
        self._client: FlextApi | None = None
        self._access_token: str | None = None

    def __enter__(self) -> Self:
        """Enter the context-managed client session.

        Returns:
            The client instance itself.

        """
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Exit the context-managed session and close the underlying client."""
        self.close()

    def close(self) -> None:
        """Close the underlying HTTP session when one was opened."""
        if self._client is not None:
            close_fn = getattr(self._client, "close", None)
            if callable(close_fn):
                close_fn()
            self._client = None

    def create_connection(
        self,
        connection_data: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Create a connection in OIC.

        Args:
            connection_data: Connection payload sent to the OIC connections
                endpoint.

        Returns:
            Result wrapping the created connection payload.

        """
        json_data = u.json_dict_adapter().validate_python(connection_data)
        return self.make_request(
            c.OracleOic.API.Method.POST,
            "/connections",
            json=json_data,
        )

    def create_integration(
        self,
        integration_data: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Create an integration in OIC.

        Args:
            integration_data: Integration payload sent to the OIC integrations
                endpoint.

        Returns:
            Result wrapping the created integration payload.

        """
        return self.make_request(
            c.OracleOic.API.Method.POST,
            "/integrations",
            json=integration_data,
        )

    def encode_client_credentials(self) -> str:
        """Encode the client credentials for HTTP Basic authentication.

        Returns:
            Base64-encoded ``client_id:client_secret`` string.

        """
        client_id = self.auth_config.oauth_client_id
        client_secret = self.auth_config.oauth_client_secret.get_secret_value()
        credentials = f"{client_id}:{client_secret}"
        return base64.b64encode(credentials.encode()).decode()

    def execute_file_transfer(
        self,
        integration_id: str,
        file_config: t.JsonMapping,
    ) -> t.JsonMapping:
        """Execute the file transfer pattern for an integration.

        Args:
            integration_id: Identifier of the target integration.
            file_config: File transfer configuration sent to the OIC files
                endpoint.

        Returns:
            The OIC response payload for the file transfer request. The
            underlying result is unwrapped, so a failed request raises
            ``RuntimeError``.

        """
        endpoint = f"/integrations/{integration_id}/files"
        result = self.make_request(
            c.OracleOic.API.Method.POST,
            endpoint,
            json=file_config,
        )
        return result.unwrap()

    def execute_scheduled_orchestration(
        self,
        integration_id: str,
        schedule_config: t.JsonMapping,
    ) -> t.JsonMapping:
        """Execute the scheduled orchestration pattern for an integration.

        Args:
            integration_id: Identifier of the target integration.
            schedule_config: Schedule configuration sent to the OIC schedules
                endpoint.

        Returns:
            The OIC response payload for the schedule request. The underlying
            result is unwrapped, so a failed request raises ``RuntimeError``.

        """
        endpoint = f"/integrations/{integration_id}/schedules"
        result = self.make_request(
            c.OracleOic.API.Method.POST,
            endpoint,
            json=schedule_config,
        )
        return result.unwrap()

    def fetch_access_token(self) -> p.Result[str]:
        """Fetch an OAuth2 access token using the client credentials flow.

        Returns:
            Result wrapping the stored access token.

        """
        return (
            self
            ._validate_token_url()
            .flat_map(lambda _: self._prepare_oauth_request())
            .flat_map(self._execute_token_request)
            .flat_map(self._parse_token_response)
            .map(self._store_and_return_token)
        )

    def fetch_connections(
        self,
        type_filter: t.StrSequence | None = None,
        page_size: int = 100,
    ) -> p.Result[t.SequenceOf[t.JsonMapping]]:
        """Fetch adapter connections from OIC.

        Args:
            type_filter: Adapter types to filter on; all connections when
                omitted.
            page_size: Number of records requested per page.

        Returns:
            Result wrapping the collected connection records.

        """
        params: t.MutableStrMapping = {}
        if type_filter:
            params["q"] = f"adapterType in ({','.join(type_filter)})"
        return self.paginate_request("/connections", page_size=page_size, params=params)

    def fetch_integrations(
        self,
        status_filter: t.StrSequence | None = None,
        page_size: int = 100,
    ) -> p.Result[t.SequenceOf[t.JsonMapping]]:
        """Fetch integration flows from OIC.

        Args:
            status_filter: Integration statuses to filter on; all integrations
                when omitted.
            page_size: Number of records requested per page.

        Returns:
            Result wrapping the collected integration records.

        """
        params: t.MutableStrMapping = {}
        if status_filter:
            params["q"] = f"status in ({','.join(status_filter)})"
        return self.paginate_request(
            "/integrations",
            page_size=page_size,
            params=params,
        )

    def fetch_lookups(
        self,
        page_size: int = 100,
    ) -> p.Result[t.SequenceOf[t.JsonMapping]]:
        """Fetch lookup tables from OIC.

        Args:
            page_size: Number of records requested per page.

        Returns:
            Result wrapping the collected lookup records.

        """
        return self.paginate_request("/lookups", page_size=page_size)

    def compute_oauth_request_body(self) -> t.StrMapping:
        """Compute the OAuth2 request body for the client credentials flow.

        Returns:
            Mapping holding the grant type and the resolved scope.

        """
        audience = self.auth_config.oauth_client_aud
        if audience:
            resource_aud = f"{audience}:443urn:opc:resource:consumer:all"
            api_aud = f"{audience}:443/ic/api/"
            scope = f"{resource_aud} {api_aud}"
        else:
            scope = self.auth_config.oauth_scope or "urn:opc:resource:consumer:all"
        return {"grant_type": "client_credentials", "scope": scope}

    def fetch_packages(
        self,
        page_size: int = 100,
    ) -> p.Result[t.SequenceOf[t.JsonMapping]]:
        """Fetch integration packages from OIC.

        Args:
            page_size: Number of records requested per page.

        Returns:
            Result wrapping the collected package records.

        """
        return self.paginate_request("/packages", page_size=page_size)

    def make_request(
        self,
        method: str,
        endpoint: str,
        params: t.StrMapping | None = None,
        data: t.StrMapping | None = None,
        json: t.JsonMapping | None = None,
    ) -> p.Result[t.JsonMapping]:
        """Make an authenticated request against the OIC API.

        Args:
            method: HTTP method name (``GET``, ``POST``, ``PUT``, ``DELETE``).
            endpoint: Endpoint path relative to the OIC base URL.
            params: Optional query parameters.
            data: Optional form data payload.
            json: Optional JSON payload.

        Returns:
            Result wrapping the parsed OIC response payload.

        """
        # Why: annotate explicitly so pyrefly binds the flat_map generic to
        # FlextApi instead of leaving the ternary's join implicit (was
        # flagged implicit-any-lambda on the downstream `client` parameter).
        client_result: p.Result[FlextApi] = (
            r[FlextApi].ok(self._client)
            if self._client is not None
            else self._create_authenticated_client()
        )
        return client_result.flat_map(
            lambda client: self._execute_api_request(
                client,
                method,
                endpoint,
                params,
                data,
                json,
            ),
        ).flat_map(self._parse_api_response)

    def paginate_request(
        self,
        endpoint: str,
        page_size: int = 100,
        params: t.StrMapping | None = None,
    ) -> p.Result[t.SequenceOf[t.JsonMapping]]:
        """Paginate through OIC API responses, translating network exceptions.

        Args:
            endpoint: Endpoint path relative to the OIC base URL.
            page_size: Number of records requested per page.
            params: Optional query parameters applied to every page request.

        Returns:
            Result wrapping all collected records.

        """
        try:
            return self._paginate_request(endpoint, page_size, params)
        except c.EXC_NETWORK_TYPE as exc:
            error_msg = f"OIC pagination failed: {exc}"
            self.logger.exception(error_msg)
            return r[t.SequenceOf[t.JsonMapping]].fail(error_msg)

    def _paginate_request(
        self,
        endpoint: str,
        page_size: int,
        params: t.StrMapping | None,
    ) -> p.Result[t.SequenceOf[t.JsonMapping]]:
        """Paginate through OIC API responses without exception translation.

        Args:
            endpoint: Endpoint path relative to the OIC base URL.
            page_size: Number of records requested per page.
            params: Optional query parameters applied to every page request.

        Returns:
            Result wrapping all collected records.

        """
        all_records: MutableSequence[t.JsonMapping] = []
        offset = 0
        base_params: t.StrMapping = dict(params) if params else {}
        while True:
            request_params: t.MutableStrMapping = dict(base_params)
            request_params.update({"offset": str(offset), "limit": str(page_size)})
            response_result = self.make_request(
                c.OracleOic.API.Method.GET,
                endpoint,
                params=request_params,
            )
            if response_result.failure:
                return r[t.SequenceOf[t.JsonMapping]].from_failure(response_result)
            response_data = response_result.value
            items_raw = response_data.get("items", [])
            if not isinstance(items_raw, list):
                return r[t.SequenceOf[t.JsonMapping]].fail("Invalid items format")
            items: t.SequenceOf[t.JsonMapping] = [
                dict(item) for item in items_raw if isinstance(item, dict)
            ]
            all_records.extend(items)
            has_more = response_data.get("hasMore", False)
            if not has_more or len(items) < page_size:
                break
            offset += page_size
        return r[t.SequenceOf[t.JsonMapping]].ok(all_records)

    def update_integration(
        self,
        integration_id: str,
        integration_data: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Update an integration in OIC.

        Args:
            integration_id: Identifier of the target integration.
            integration_data: Updated integration payload.

        Returns:
            Result wrapping the updated integration payload.

        """
        endpoint = f"/integrations/{integration_id}"
        json_data = u.json_dict_adapter().validate_python(integration_data)
        return self.make_request(c.OracleOic.API.Method.PUT, endpoint, json=json_data)

    def _build_client_with_token(self, token: str) -> p.Result[FlextApi]:
        """Build an API client carrying the given access token.

        Args:
            token: OAuth2 access token placed in the Authorization header.

        Returns:
            Result wrapping the constructed client.

        """
        try:
            base_url = (
                f"{self.connection_config.base_url.rstrip('/')}"
                f"/ic/api/{self.connection_config.api_version}"
            )
            api_config = FlextApiSettings.model_validate({
                "base_url": base_url,
                "timeout": self.connection_config.request_timeout,
                "headers": {
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
            })
            client = FlextApi(runtime_settings=api_config)
            self._client = client
            return r[FlextApi].ok(client)
        except c.EXC_NETWORK_TYPE as exc:
            error_msg = f"Failed to create authenticated client: {exc}"
            self.logger.exception(error_msg)
            return r[FlextApi].fail(error_msg)

    def _create_authenticated_client(self) -> p.Result[FlextApi]:
        """Create a new authenticated API client.

        Returns:
            Result wrapping the constructed client.

        """
        return self.fetch_access_token().flat_map(self._build_client_with_token)

    def _execute_api_request(
        self,
        client: FlextApi,
        method: str,
        endpoint: str,
        _params: t.StrMapping | None,
        _data: t.StrMapping | None,
        json: t.JsonMapping | None,
    ) -> p.Result[t.JsonValue]:
        """Execute the actual API request, translating network exceptions.

        Args:
            client: flext-api client used to perform the request.
            method: HTTP method name.
            endpoint: Endpoint path relative to the OIC base URL.
            _params: Unused query parameters.
            _data: Unused form data.
            json: Optional JSON payload.

        Returns:
            Result wrapping the raw response body value.

        """
        try:
            return self._run_api_request(client, method, endpoint, json)
        except c.EXC_NETWORK_TYPE as exc:
            error_msg = f"OIC API request failed: {exc}"
            self.logger.exception(error_msg)
            return r[t.JsonValue].fail(error_msg)

    def _run_api_request(
        self,
        client: FlextApi,
        method: str,
        endpoint: str,
        json: t.JsonMapping | None,
    ) -> p.Result[t.JsonValue]:
        """Execute the API request without exception translation.

        Args:
            client: flext-api client used to perform the request.
            method: HTTP method name; unsupported names yield a failure result.
            endpoint: Endpoint path relative to the OIC base URL.
            json: Optional JSON payload converted to a string-valued form body.

        Returns:
            Result wrapping the raw response body value.

        """
        api_data: t.JsonDict | None = None
        if json is not None:
            api_data = {
                key: str(self._to_api_payload(value)) for key, value in json.items()
            }
        base_url = (
            f"{self.connection_config.base_url.rstrip('/')}"
            f"/ic/api/{self.connection_config.api_version}"
        )
        full_url = f"{base_url}/{endpoint.lstrip('/')}"
        if method.upper() == c.Api.Method.GET.value:
            response_result = client.get(full_url, headers=None)
        elif method.upper() == c.Api.Method.POST.value:
            response_result = client.post(full_url, data=api_data, headers=None)
        elif method.upper() == c.Api.Method.PUT.value:
            response_result = client.put(full_url, data=api_data, headers=None)
        elif method.upper() == c.Api.Method.DELETE.value:
            response_result = client.delete(full_url, headers=None)
        else:
            return r[t.JsonValue].fail(f"Unsupported HTTP method: {method}")
        if response_result.failure:
            return r[t.JsonValue].fail_op("Request", response_result.error)
        response = response_result.value
        body: t.JsonValue = getattr(response, "body", str(response))
        return r[t.JsonValue].ok(body)

    def _execute_token_request(
        self,
        request_data: tuple[t.StrMapping, t.StrMapping],
    ) -> p.Result[t.JsonValue]:
        """Execute the OAuth token request, translating network exceptions.

        Args:
            request_data: Tuple of request headers and form data.

        Returns:
            Result wrapping the raw token response body value.

        """
        try:
            return self._request_access_token(request_data)
        except c.EXC_NETWORK_TYPE as exc:
            error_msg = f"OAuth token request failed: {exc}"
            self.logger.exception(error_msg)
            return r[t.JsonValue].fail(error_msg)

    def _request_access_token(
        self,
        request_data: tuple[t.StrMapping, t.StrMapping],
    ) -> p.Result[t.JsonValue]:
        """Execute the OAuth token request without exception translation.

        Args:
            request_data: Tuple of request headers and form data.

        Returns:
            Result wrapping the raw token response body value.

        """
        headers, data = request_data
        api_config = FlextApiSettings.model_validate({
            "base_url": self.auth_config.oauth_token_url,
        })
        api_client = FlextApi(runtime_settings=api_config)
        oauth_data: t.JsonDict = {
            key: str(self._to_api_payload(value)) for key, value in data.items()
        }
        response_result = api_client.post("", data=oauth_data, headers=headers)
        if response_result.failure:
            return r[t.JsonValue].fail_op("OAuth request", response_result.error)
        response = response_result.value
        if response.status_code >= c.OracleOic.API.HTTP_ERROR_STATUS_THRESHOLD:
            return r[t.JsonValue].fail(f"OAuth HTTP error: {response.status_code}")
        body: t.JsonValue = getattr(response, "body", str(response))
        return r[t.JsonValue].ok(body)

    def _parse_api_response(self, response: t.JsonValue) -> p.Result[t.JsonMapping]:
        """Parse the API response according to its content type.

        Args:
            response: Raw response value to parse.

        Returns:
            Result wrapping the parsed mapping.

        """
        try:
            return self._parse_api_response_value(response)
        except c.EXC_NETWORK_TYPE as exc:
            error_msg = f"Failed to parse API response: {exc}"
            self.logger.exception(error_msg)
            return r[t.JsonMapping].fail(error_msg)

    @staticmethod
    def _parse_api_response_value(
        response: t.JsonValue,
    ) -> p.Result[t.JsonMapping]:
        """Parse the API response without exception translation.

        Args:
            response: Raw response value to parse.

        Returns:
            Result wrapping the parsed mapping.

        """
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
            parsed_body = u.json_mapping_adapter().validate_json(body)
        elif isinstance(body, Mapping):
            parsed_body = body
        else:
            parsed_body = {"raw_content": str(body) if body is not None else ""}
        return r[t.JsonMapping].ok(parsed_body)

    def _parse_token_response(self, response: t.JsonValue) -> p.Result[str]:
        """Parse the access token from an OAuth response.

        Args:
            response: Raw token response value.

        Returns:
            Result wrapping the access token string.

        """
        try:
            return self._parse_token_response_value(response)
        except c.EXC_NETWORK_TYPE as exc:
            error_msg = f"Failed to parse OAuth response: {exc}"
            self.logger.exception(error_msg)
            return r[str].fail(error_msg)

    @staticmethod
    def _parse_token_response_value(response: t.JsonValue) -> p.Result[str]:
        """Parse the access token without exception translation.

        Args:
            response: Raw token response value.

        Returns:
            Result wrapping the access token string.

        """
        body_raw: t.JsonValue = getattr(response, "body", None)
        if body_raw is None:
            return r[str].fail("Invalid response format")
        token_data: t.JsonMapping
        if isinstance(body_raw, Mapping):
            token_data = {k: body_raw[k] for k in body_raw}
        elif isinstance(body_raw, str):
            token_data = u.json_mapping_adapter().validate_json(body_raw)
        else:
            return r[str].fail("Empty or invalid OAuth response body")
        access_token: t.JsonValue | None = token_data.get("access_token")
        if isinstance(access_token, str) and access_token:
            return r[str].ok(access_token)
        return r[str].fail("No valid access token in response")

    def _prepare_oauth_request(self) -> p.Result[tuple[t.StrMapping, t.StrMapping]]:
        """Prepare the OAuth request headers and form data.

        Returns:
            Result wrapping the headers/data tuple.

        """
        try:
            encoded_credentials = self.encode_client_credentials()
            headers = {
                "Authorization": f"Basic {encoded_credentials}",
                "Content-Type": "application/x-www-form-urlencoded",
            }
            data = self.compute_oauth_request_body()
            return r[tuple[t.StrMapping, t.StrMapping]].ok((headers, data))
        except c.EXC_NETWORK_TYPE as exc:
            error_msg = f"Failed to prepare OAuth request: {exc}"
            self.logger.exception(error_msg)
            return r[tuple[t.StrMapping, t.StrMapping]].fail(error_msg)

    def _store_and_return_token(self, token: str) -> str:
        """Store the access token on the client and return it.

        Args:
            token: Access token to store.

        Returns:
            The stored token.

        """
        self._access_token = token
        self.logger.info("OIC OAuth2 authentication successful")
        return token

    def _to_api_payload(
        self,
        value: t.JsonValue | t.Scalar | t.ScalarMapping | t.ScalarList,
    ) -> t.JsonValue:
        """Normalize a payload value into a JSON-compatible request body value.

        Args:
            value: Payload value to normalize.

        Returns:
            The normalized JSON-compatible value.

        """
        if isinstance(value, c.PRIMITIVES_TYPES) or value is None:
            return value
        if isinstance(value, Mapping):
            return {key: self._to_api_payload(item) for key, item in value.items()}
        match value:
            case list() | tuple():
                return [self._to_api_payload(item) for item in value]
            case _:
                return str(value)

    def _validate_token_url(self) -> p.Result[bool]:
        """Validate that the OAuth token URL is configured.

        Returns:
            Result holding ``True`` when the token URL is present.

        """
        if not self.auth_config.oauth_token_url:
            return r[bool].fail("OAuth token URL not configured")
        return r[bool].ok(value=True)


__all__: list[str] = ["FlextOracleOicClient"]
