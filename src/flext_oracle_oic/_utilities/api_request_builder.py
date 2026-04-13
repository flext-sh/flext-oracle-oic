"""Oracle OIC API request construction utilities mixin."""

from __future__ import annotations

from urllib.parse import urljoin

from flext_core import p, r
from flext_oracle_oic import (
    FlextOracleOicUtilitiesConnectionValidation,
    t,
)


class FlextOracleOicUtilitiesAPIRequestBuilder:
    """Oracle OIC API request construction utilities."""

    @staticmethod
    def build_resource_endpoint(
        base_url: str,
        *,
        api_version: str,
        resource_name: str,
        resource_label: str,
        resource_id: str | None = None,
    ) -> p.Result[str]:
        """Build Oracle OIC endpoint URL for a versioned resource path."""
        url_result = FlextOracleOicUtilitiesConnectionValidation.validate_base_url(
            base_url,
        )
        if url_result.failure:
            return r[str].fail(f"Base URL validation: {url_result.error}")
        validated_base_url = url_result.value
        path_parts = ["ic", "api", "integration", api_version, resource_name]
        if resource_id:
            match resource_id:
                case str() as raw_resource_id if raw_resource_id.strip():
                    path_parts.append(raw_resource_id.strip())
                case _:
                    return r[str].fail(f"{resource_label} must be non-empty string")
        endpoint_path = "/" + "/".join(path_parts)
        full_url = urljoin(validated_base_url + "/", endpoint_path.lstrip("/"))
        return r[str].ok(full_url)

    @staticmethod
    def build_connection_endpoint(
        base_url: str,
        api_version: str = "v1",
        connection_id: str | None = None,
    ) -> p.Result[str]:
        """Build Oracle OIC connection API endpoint.

        Args:
        base_url: OIC instance base URL
        api_version: API version (default: v1)
        connection_id: Optional specific connection ID

        Returns:
        r containing constructed endpoint URL or error

        """
        return FlextOracleOicUtilitiesAPIRequestBuilder.build_resource_endpoint(
            base_url=base_url,
            api_version=api_version,
            resource_name="connections",
            resource_label="Connection ID",
            resource_id=connection_id,
        )

    @staticmethod
    def build_integration_endpoint(
        base_url: str,
        api_version: str = "v1",
        integration_id: str | None = None,
    ) -> p.Result[str]:
        """Build Oracle OIC integration API endpoint.

        Args:
        base_url: OIC instance base URL
        api_version: API version (default: v1)
        integration_id: Optional specific integration ID

        Returns:
        r containing constructed endpoint URL or error

        """
        return FlextOracleOicUtilitiesAPIRequestBuilder.build_resource_endpoint(
            base_url=base_url,
            api_version=api_version,
            resource_name="integrations",
            resource_label="Integration ID",
            resource_id=integration_id,
        )

    @staticmethod
    def build_request_headers(
        auth_token: str | None = None,
        content_type: str = "application/json",
        additional_headers: t.StrMapping | None = None,
    ) -> p.Result[t.StrMapping]:
        """Build Oracle OIC API request headers.

        Args:
        auth_token: Optional authentication token
        content_type: Content type header (default: application/json)
        additional_headers: Optional additional headers

        Returns:
        r containing constructed headers or error

        """
        headers: t.MutableStrMapping = {
            "Accept": "application/json",
            "Content-Type": content_type,
            "User-Agent": "FlextOracleOicension/1.0.0",
        }
        if auth_token:
            match auth_token:
                case str() as raw_auth_token if raw_auth_token.strip():
                    headers["Authorization"] = f"Bearer {raw_auth_token.strip()}"
                case _:
                    return r[t.StrMapping].fail(
                        "Auth token must be non-empty string",
                    )
        if additional_headers:
            headers.update({str(k): str(v) for k, v in additional_headers.items()})
        return r[t.StrMapping].ok(headers)
