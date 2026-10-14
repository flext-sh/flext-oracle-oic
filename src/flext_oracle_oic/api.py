"""FLEXT Oracle OIC Extension API - Thin Facade Pattern.

FLEXT Unified Module Pattern: Thin facade exposing all domain functionality
through complete flext-core integration. Provides single entry point for all
Oracle OIC operations with enterprise patterns.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, override

from flext_oracle_oic import FlextOracleOicSettings, m, p, r, t
from flext_oracle_oic.services import FlextOracleOicService

if TYPE_CHECKING:
    from collections.abc import Sequence


class FlextOracleOicApi(FlextOracleOicService):
    """Thin facade for Oracle OIC operations with complete FLEXT integration.

    Integrates:
    - FlextBus: Event emission for OIC operations
    - FlextContainer: Dependency injection for OIC services
    - FlextContext: Operation context management
    - FlextDispatcher: Message routing for OIC patterns
    - FlextRegistry: Component registration for OIC extensions
    - `u.fetch_logger(...)` / `p.Logger`: Structured logging for OIC operations

    Provides unified access to all Oracle OIC functionality:
    - Integration lifecycle management (create, update, delete, activate)
    - Authentication and authorization (OAuth2, IDCS)
    - Connection testing and health monitoring
    - Integration pattern execution (app-driven, scheduled, file transfer)
    - Enterprise orchestration patterns (Message Router, Scatter-Gather)
    - Monitoring and observability
    """

    def __init__(self, settings: FlextOracleOicSettings | None = None) -> None:
        """Initialize the FlextOracleOic facade with ecosystem integration.

        Args:
            settings: Oracle OIC configuration. If None, uses global instance.

        """
        super().__init__()
        self._oic_config: FlextOracleOicSettings = (
            settings
            if settings is not None
            else FlextOracleOicSettings.model_validate({})
        )
        self._service = FlextOracleOicService()

    def __aenter__(self) -> Self:
        """Async context manager entry.

        Returns:
            The facade instance itself.
        """
        self.logger.info(
            "Oracle OIC service started",
            extra_info=str(self.fetch_connection_context().value),
        )
        return self

    def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: t.JsonValue,
    ) -> None:
        """Async context manager exit.

        Args:
            exc_type: Exception type if the body raised, else ``None``.
            exc_val: Exception instance if the body raised, else ``None``.
            exc_tb: Traceback if the body raised, else ``None``.
        """
        self.logger.info(
            "Oracle OIC service stopped",
            extra_info=str(self.fetch_connection_context().value),
        )

    @override
    def execute(
        self,
        **kwargs: t.Scalar,
    ) -> p.Result[Sequence[m.OracleOic.OICIntegrationInfo]]:
        """Execute Oracle OIC API operations - delegates to service.

        Args:
            **kwargs: Operation parameters forwarded to the service.

        Returns:
            Result wrapping the list of OIC integrations.
        """
        return self._service.execute(**kwargs)

    @override
    def execute_app_driven_orchestration(
        self,
        integration_id: str,
        payload: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Execute the app-driven orchestration pattern.

        Args:
            integration_id: The integration identifier.
            payload: Orchestration payload data.

        Returns:
            Result wrapping the orchestration execution output.
        """
        return self._service.execute_app_driven_orchestration(integration_id, payload)

    @override
    def execute_file_transfer(
        self,
        integration_id: str,
        file_config: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Execute the file transfer pattern.

        Args:
            integration_id: The integration identifier.
            file_config: File transfer configuration.

        Returns:
            Result wrapping the file transfer execution output.
        """
        return self._service.execute_file_transfer(integration_id, file_config)

    @override
    def execute_scheduled_orchestration(
        self,
        integration_id: str,
        schedule_config: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Execute the scheduled orchestration pattern.

        Args:
            integration_id: The integration identifier.
            schedule_config: Schedule configuration.

        Returns:
            Result wrapping the scheduled orchestration execution output.
        """
        return self._service.execute_scheduled_orchestration(
            integration_id,
            schedule_config,
        )

    def fetch_auth_context(self) -> p.Result[t.JsonMapping]:
        """Return the current authentication configuration context (ENFORCE-056).

        Returns:
            Result wrapping the authentication context mapping.
        """
        return r[t.JsonMapping].ok({
            "oauth_client_id": self._oic_config.OracleOic.oauth_client_id,
            "oauth_token_url": self._oic_config.OracleOic.oauth_token_url,
            "oauth_scope": self._oic_config.OracleOic.oauth_scope,
        })

    def fetch_connection_context(self) -> p.Result[t.JsonMapping]:
        """Return the current connection configuration context (ENFORCE-056).

        Returns:
            Result wrapping the connection context mapping.
        """
        return r[t.JsonMapping].ok({
            "base_url": self._oic_config.OracleOic.base_url,
            "api_version": self._oic_config.OracleOic.api_version,
            "request_timeout": self._oic_config.OracleOic.request_timeout,
        })

    def fetch_features_context(self) -> p.Result[t.JsonMapping]:
        """Return the current features configuration context (ENFORCE-056).

        Returns:
            Result wrapping the feature flags mapping.
        """
        return r[t.JsonMapping].ok({
            "enable_monitoring": self._oic_config.OracleOic.enable_monitoring,
            "use_ssl": self._oic_config.OracleOic.use_ssl,
            "verify_ssl": self._oic_config.OracleOic.verify_ssl,
        })

    @override
    def fetch_health_status(self) -> p.Result[t.JsonMapping]:
        """Fetch the Oracle OIC health status.

        Returns:
            Result wrapping the health status information.
        """
        return self._service.fetch_health_status()

    @override
    def fetch_integration(
        self,
        integration_id: str,
    ) -> p.Result[m.OracleOic.OICIntegrationInfo]:
        """Get a specific Oracle OIC integration by ID.

        Args:
            integration_id: The integration identifier.

        Returns:
            Result wrapping the integration information.
        """
        return self._service.fetch_integration(integration_id)

    @override
    def fetch_performance_metrics(self) -> p.Result[t.JsonMapping]:
        """Fetch Oracle OIC performance metrics.

        Returns:
            Result wrapping the performance metrics.
        """
        return self._service.fetch_performance_metrics()

    @override
    def list_integrations(self) -> p.Result[Sequence[m.OracleOic.OICIntegrationInfo]]:
        """List all Oracle OIC integrations.

        Returns:
            Result wrapping the list of integration information.
        """
        return self._service.list_integrations()

    @override
    def refresh_auth_token(self) -> p.Result[str]:
        """Refresh the OAuth2 authentication token.

        Returns:
            Result wrapping the new access token.
        """
        return self._service.refresh_auth_token()

    @override
    def test_connection(self) -> p.Result[bool]:
        """Test the connection to the Oracle OIC instance.

        Returns:
            Result holding the connection test verdict.
        """
        return self._service.test_connection()

    @override
    def update_integration(
        self,
        integration_id: str,
        integration_data: t.JsonMapping,
    ) -> p.Result[m.OracleOic.OICIntegrationInfo]:
        """Update an existing Oracle OIC integration.

        Args:
            integration_id: The integration identifier.
            integration_data: Updated integration configuration.

        Returns:
            Result wrapping the updated integration information.
        """
        return self._service.update_integration(integration_id, integration_data)

    @override
    def validate_auth_token(self, token: str) -> p.Result[bool]:
        """Validate an OAuth2 authentication token.

        Args:
            token: Token to validate.

        Returns:
            Result holding the validation verdict.
        """
        return self._service.validate_auth_token(token)


oracle_oic: FlextOracleOicApi = FlextOracleOicApi.fetch_global()
"""Process-wide Oracle OIC API facade singleton resolved from the global container."""

__all__: list[str] = ["FlextOracleOicApi", "oracle_oic"]
