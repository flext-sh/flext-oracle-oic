"""FLEXT Oracle OIC Service Base - Shared infrastructure for service mixins.

Provides client management, value normalization, and component initialization
shared across all service mixins.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from types import TracebackType
from typing import Self, override

from flext_api import FlextApiClient, FlextApiSettings

from flext_core import p, r, s
from flext_oracle_oic import (
    FlextOracleOicClient,
    FlextOracleOicModels,
    FlextOracleOicSettings,
    FlextOracleOicUtilities,
    c,
    t,
    u,
)


class FlextOracleOicServiceBase(
    s[Sequence[FlextOracleOicModels.OracleOic.OICIntegrationInfo]],
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
        self._oic_settings: FlextOracleOicSettings = (
            FlextOracleOicSettings.fetch_global()
        )
        self._client: FlextOracleOicClient | None = None
        self._monitoring_client: FlextApiClient | None = None
        self._authenticator: t.Container | None = None
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
    def _as_text(value: t.Container, default: str = "") -> str:
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
        value: t.Container | t.ContainerValue | bytes | None,
    ) -> t.Container:
        """Normalize arbitrary runtime values into t.Container."""
        if isinstance(value, bytes):
            return value.decode(errors="replace")
        if isinstance(value, (str, int, float, bool)) or value is None:
            return value
        if isinstance(value, Mapping):
            return {
                str(k): FlextOracleOicServiceBase._to_general_value(v)
                for k, v in value.items()
            }
        match value:
            case list() | tuple():
                return [FlextOracleOicServiceBase._to_general_value(v) for v in value]
            case _:
                pass
        return str(value)

    @override
    def execute(
        self: Self,
        **kwargs: t.Scalar,
    ) -> p.Result[Sequence[FlextOracleOicModels.OracleOic.OICIntegrationInfo]]:
        """Execute main service operation - list all integrations.

        Returns:
        r containing list of OIC integrations.

        """
        return self.list_integrations()

    def list_integrations(
        self,
    ) -> p.Result[Sequence[FlextOracleOicModels.OracleOic.OICIntegrationInfo]]:
        """List all Oracle OIC integrations.

        Returns:
        r containing list of integration information.

        """
        try:
            client_result = self._get_client()
            if client_result.failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[
                    Sequence[FlextOracleOicModels.OracleOic.OICIntegrationInfo]
                ].fail(
                    error_msg,
                )
            client = client_result.value
            integrations_result = client.get_integrations()
            if integrations_result.failure:
                error_msg = integrations_result.error or "Failed to get integrations"
                return r[
                    Sequence[FlextOracleOicModels.OracleOic.OICIntegrationInfo]
                ].fail(
                    error_msg,
                )
            integrations_data = integrations_result.value
            integrations: list[FlextOracleOicModels.OracleOic.OICIntegrationInfo] = []
            for item in integrations_data:
                integration = FlextOracleOicModels.OracleOic.OICIntegrationInfo(
                    integration_id=self._as_text(item.get("id"), ""),
                    name=self._as_text(item.get("name"), ""),
                    description=self._as_text(item.get("description"), ""),
                    integration_version=self._as_text(
                        item.get("version"),
                        c.Integration.DEFAULT_VERSION_FALLBACK,
                    ),
                    status=self._as_text(
                        item.get("status"),
                        c.Connection.Status.UNKNOWN,
                    ),
                    created_by=self._as_text(item.get("createdBy"), ""),
                    last_updated=self._as_text(item.get("lastUpdated"), ""),
                )
                integrations.append(integration)
            return r[Sequence[FlextOracleOicModels.OracleOic.OICIntegrationInfo]].ok(
                integrations,
            )
        except (ConnectionError, TimeoutError, ValueError) as exc:
            u.fetch_logger(__name__).exception("Failed to list integrations")
            return r[Sequence[FlextOracleOicModels.OracleOic.OICIntegrationInfo]].fail(
                f"Integration listing failed: {exc!s}",
            )

    def _get_client(self) -> p.Result[FlextOracleOicClient]:
        """Get or create Oracle OIC client instance.

        Returns:
        r containing the client instance.

        """
        try:
            if self._client is None:
                validation_result = self.validate_business_rules()
                if validation_result.failure:
                    return r[FlextOracleOicClient].fail(validation_result.error)
                connection_config = FlextOracleOicModels.OracleOic.OICConnectionConfig(
                    base_url=str(self._oic_settings.base_url),
                    api_version=self._oic_settings.api_version,
                    request_timeout=self._oic_settings.request_timeout,
                    max_retries=self._oic_settings.max_retries,
                    verify_ssl=self._oic_settings.verify_ssl,
                )
                auth_config = FlextOracleOicModels.OracleOic.OICAuthConfig(
                    oauth_client_id=self._oic_settings.oauth_client_id,
                    oauth_client_secret=self._oic_settings.oauth_client_secret,
                    oauth_token_url=str(self._oic_settings.oauth_token_url),
                    oauth_client_aud=self._oic_settings.oauth_client_aud,
                    oauth_scope=self._oic_settings.oauth_scope,
                )
                self._client = FlextOracleOicClient(
                    connection_config=connection_config,
                    auth_config=auth_config,
                )
            return r[FlextOracleOicClient].ok(self._client)
        except (ConnectionError, TimeoutError, ValueError) as exc:
            self.logger.exception("Failed to create OIC client")
            return r[FlextOracleOicClient].fail(f"Client creation failed: {exc!s}")

    @override
    def validate_business_rules(self) -> p.Result[bool]:
        """Validate Oracle OIC service business rules.

        Returns:
        r indicating validation success or failure.

        """
        if not self._oic_settings:
            return r[bool].fail("Settings are required")
        if not self._oic_settings.base_url:
            return r[bool].fail("Base URL is required")
        if not self._oic_settings.oauth_client_id:
            return r[bool].fail("OAuth client ID is required")
        client_id_result = (
            FlextOracleOicUtilities.AuthenticationValidation.validate_oauth_client_id(
                self._oic_settings.oauth_client_id,
            )
        )
        if client_id_result.failure:
            return r[bool].fail(f"OAuth client ID validation: {client_id_result.error}")
        if not self._oic_settings.oauth_client_secret:
            return r[bool].fail("OAuth client secret is required")
        if not self._oic_settings.oauth_token_url:
            return r[bool].fail("OAuth token URL is required")
        return r[bool].ok(value=True)

    def _initialize_components(self) -> None:
        """Initialize service components."""
        try:
            if self._oic_settings.enable_monitoring:
                auth_token = ""
                if self._authenticator:
                    refresh_fn = getattr(self._authenticator, "refresh_token", None)
                    if callable(refresh_fn):
                        auth_token = refresh_fn()
                api_config = FlextApiSettings(
                    base_url=str(self._oic_settings.base_url),
                    timeout=self._oic_settings.request_timeout,
                    max_retries=self._oic_settings.max_retries,
                    verify_ssl=self._oic_settings.verify_ssl,
                    default_headers={
                        "Authorization": f"Bearer {auth_token}",
                        "Content-Type": "application/json",
                    },
                    headers={
                        "Authorization": f"Bearer {auth_token}",
                        "Content-Type": "application/json",
                    },
                    log_requests=False,
                    log_responses=False,
                )
                self._monitoring_client = FlextApiClient(settings=api_config)
        except (ConnectionError, TimeoutError, ValueError):
            u.fetch_logger(__name__).exception(
                "Failed to initialize service components"
            )
            raise


__all__: list[str] = ["FlextOracleOicServiceBase"]
