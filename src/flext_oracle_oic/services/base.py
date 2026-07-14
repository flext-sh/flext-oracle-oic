"""FLEXT Oracle OIC Service Base - Shared infrastructure for service mixins.

Provides client management, value normalization, and component initialization
shared across all service mixins.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import (
    Mapping,
    Sequence,
)
from types import TracebackType
from typing import Self, override

from flext_api import FlextApi, FlextApiSettings

from flext_core import r, s
from flext_oracle_oic import c, m, p, t, u
from flext_oracle_oic._settings import FlextOracleOicSettings
from flext_oracle_oic.ext_client import FlextOracleOicClient


class FlextOracleOicServiceBase(
    s[Sequence[m.OracleOic.OICIntegrationInfo]],
):
    """Base service providing shared infrastructure for all OIC service mixins.

    Provides:
    - Client lifecycle management (_get_client, _initialize_components)
    - Value normalization helpers (_as_text, _to_general_value)
    - Context manager support
    - Settings access
    """

    def __init__(self) -> None:
        """Initialize base Oracle OIC service.

        Uses singleton settings pattern - no settings parameter needed.
        """
        super().__init__()
        # NOTE: singleton resolved via fetch_global(), matching the flext-auth
        # services pattern (no facade-level settings import in layer-1 code).
        self._oic_settings: FlextOracleOicSettings = (
            FlextOracleOicSettings.fetch_global()
        )
        self._client: FlextOracleOicClient | None = None
        self._monitoring_client: FlextApi | None = None
        self._authenticator: t.JsonValue | None = None
        self._initialize_components()

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

    @staticmethod
    def _as_text(value: t.JsonValue, default: str = "") -> str:
        """Normalize optional OIC values into strings for model construction."""
        match value:
            case str():
                return value
            case _:
                pass
        if value is None:
            return default
        return str(value)

    @staticmethod
    def _to_general_value(
        value: t.JsonValue | bytes | None,
    ) -> t.JsonValue:
        """Normalize arbitrary runtime values into t.JsonValue."""
        if isinstance(value, bytes):
            return value.decode(errors="replace")
        if isinstance(value, t.PRIMITIVES_TYPES) or value is None:
            return value
        if isinstance(value, Mapping):
            return {
                k: FlextOracleOicServiceBase._to_general_value(v)
                for k, v in value.items()
            }
        match value:
            case list() | tuple():
                return [FlextOracleOicServiceBase._to_general_value(v) for v in value]
            case _:
                pass
        return str(value)

    def _build_integration_info(
        self,
        data: t.JsonMapping,
        *,
        fallback_id: str,
        default_status: str,
    ) -> m.OracleOic.OICIntegrationInfo:
        """Build normalized integration model from API payload mapping."""
        return m.OracleOic.OICIntegrationInfo(
            integration_id=self._as_text(data.get("id"), fallback_id),
            name=self._as_text(data.get("name"), ""),
            description=self._as_text(data.get("description"), ""),
            integration_version=self._as_text(
                data.get("version"),
                c.Integration.DEFAULT_VERSION_FALLBACK,
            ),
            status=self._as_text(data.get("status"), default_status),
            created_by=self._as_text(data.get("createdBy"), ""),
            last_updated=self._as_text(data.get("lastUpdated"), ""),
        )

    @override
    def execute(
        self: Self,
    ) -> p.Result[Sequence[m.OracleOic.OICIntegrationInfo]]:
        """Execute main service operation - list all integrations.

        Returns:
        r containing list of OIC integrations.

        """
        return self.list_integrations()

    def list_integrations(
        self,
    ) -> p.Result[Sequence[m.OracleOic.OICIntegrationInfo]]:
        """List all Oracle OIC integrations.

        Returns:
        r containing list of integration information.

        """
        try:
            return self._list_integrations()
        except c.EXC_NETWORK_TYPE as exc:
            u.fetch_logger(__name__).exception("Failed to list integrations")
            return r[Sequence[m.OracleOic.OICIntegrationInfo]].fail_op(
                "Integration listing",
                exc,
            )

    def _list_integrations(
        self,
    ) -> p.Result[Sequence[m.OracleOic.OICIntegrationInfo]]:
        """List all Oracle OIC integrations without exception translation."""
        client_result = self._get_client()
        if client_result.failure:
            error_msg = client_result.error or "Client initialization failed"
            return r[Sequence[m.OracleOic.OICIntegrationInfo]].fail(
                error_msg,
            )
        client = client_result.value
        integrations_result = client.get_integrations()
        if integrations_result.failure:
            error_msg = integrations_result.error or "Failed to get integrations"
            return r[Sequence[m.OracleOic.OICIntegrationInfo]].fail(
                error_msg,
            )
        integrations_data = integrations_result.value
        integrations: list[m.OracleOic.OICIntegrationInfo] = []
        for item in integrations_data:
            integration = self._build_integration_info(
                item,
                fallback_id="",
                default_status=c.Connection.Status.UNKNOWN,
            )
            integrations.append(integration)
        return r[Sequence[m.OracleOic.OICIntegrationInfo]].ok(
            integrations,
        )

    def _get_client(self) -> p.Result[FlextOracleOicClient]:
        """Get or create Oracle OIC client instance.

        Returns:
        r containing the client instance.

        """
        try:
            return self._get_or_create_client()
        except c.EXC_NETWORK_TYPE as exc:
            self.logger.exception("Failed to create OIC client")
            return r[FlextOracleOicClient].fail_op("Client creation", exc)

    def _get_or_create_client(self) -> p.Result[FlextOracleOicClient]:
        """Get or create Oracle OIC client without exception translation."""
        if self._client is None:
            validation_result = self.validate_business_rules()
            if validation_result.failure:
                return r[FlextOracleOicClient].fail(validation_result.error)
            connection_config = m.OracleOic.OICConnectionConfig(
                base_url=self._oic_settings.OracleOic.base_url,
                api_version=self._oic_settings.OracleOic.api_version,
                request_timeout=self._oic_settings.OracleOic.request_timeout,
                max_retries=self._oic_settings.OracleOic.max_retries,
                verify_ssl=self._oic_settings.OracleOic.verify_ssl,
            )
            auth_config = m.OracleOic.OICAuthConfig(
                oauth_client_id=self._oic_settings.OracleOic.oauth_client_id,
                oauth_client_secret=self._oic_settings.OracleOic.oauth_client_secret,
                oauth_token_url=self._oic_settings.OracleOic.oauth_token_url,
                oauth_client_aud=self._oic_settings.OracleOic.oauth_client_aud,
                oauth_scope=self._oic_settings.OracleOic.oauth_scope,
            )
            self._client = FlextOracleOicClient(
                connection_config=connection_config,
                auth_config=auth_config,
            )
        return r[FlextOracleOicClient].ok(self._client)

    def validate_business_rules(self) -> p.Result[bool]:
        """Validate Oracle OIC service business rules.

        Returns:
        r indicating validation success or failure.

        """
        settings = self._oic_settings
        base_url_validation: p.Result[bool] = (
            u.ConnectionValidation
            .validate_base_url(settings.OracleOic.base_url)
            .map(lambda _: True)
            .lash(lambda error: r[bool].fail(f"Base URL validation: {error}"))
        )
        client_id_validation: p.Result[bool] = (
            u.AuthenticationValidation
            .validate_oauth_client_id(
                settings.OracleOic.oauth_client_id,
            )
            .map(lambda _: True)
            .lash(
                lambda error: r[bool].fail(
                    f"OAuth client ID validation: {error}",
                ),
            )
        )
        client_secret_validation: p.Result[bool] = (
            u.AuthenticationValidation
            .validate_oauth_client_secret(
                t.SecretStr(settings.OracleOic.oauth_client_secret),
            )
            .map(lambda _: True)
            .lash(
                lambda error: r[bool].fail(
                    f"OAuth client secret validation: {error}",
                ),
            )
        )
        token_url_validation: p.Result[bool] = (
            u.ConnectionValidation
            .validate_base_url(settings.OracleOic.oauth_token_url)
            .map(lambda _: True)
            .lash(
                lambda error: r[bool].fail(
                    f"OAuth token URL validation: {error}",
                ),
            )
        )
        return (
            base_url_validation
            .flat_map(lambda _: client_id_validation)
            .flat_map(lambda _: client_secret_validation)
            .flat_map(lambda _: token_url_validation)
        )

    def _initialize_components(self) -> None:
        """Initialize service components."""
        try:
            self._initialize_monitoring_client()
        except c.EXC_NETWORK_TYPE:
            u.fetch_logger(__name__).exception(
                "Failed to initialize service components",
            )
            raise

    def _initialize_monitoring_client(self) -> None:
        """Initialize the monitoring client when monitoring is enabled."""
        if not self._oic_settings.OracleOic.enable_monitoring:
            return
        auth_token = ""
        if self._authenticator:
            refresh_fn = getattr(self._authenticator, "refresh_token", None)
            if callable(refresh_fn):
                auth_token = refresh_fn()
        auth_headers: t.JsonMapping = {
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json",
        }
        api_config = FlextApiSettings.model_validate({
            "base_url": self._oic_settings.OracleOic.base_url,
            "timeout": self._oic_settings.OracleOic.request_timeout,
            "max_retries": self._oic_settings.OracleOic.max_retries,
            "verify_ssl": self._oic_settings.OracleOic.verify_ssl,
            "default_headers": auth_headers,
            "headers": auth_headers,
            "log_requests": False,
            "log_responses": False,
        })
        self._monitoring_client = FlextApi(settings=api_config)


__all__: list[str] = ["FlextOracleOicServiceBase"]
