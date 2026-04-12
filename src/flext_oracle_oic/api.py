"""FLEXT Oracle OIC Extension API - Thin Facade Pattern.

FLEXT Unified Module Pattern: Thin facade exposing all domain functionality
through complete flext-core integration. Provides single entry point for all
Oracle OIC operations with enterprise patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Self, override

from flext_core import r, s
from flext_oracle_oic import (
    FlextOracleOicModels,
    FlextOracleOicService,
    FlextOracleOicSettings,
    t,
)


class FlextOracleOicApi(s[None]):
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
        """Initialize FlextOracleOic facade with complete ecosystem integration.

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
        if self._context is not None:
            self._context.set("oracle_oic_base_url", self._oic_config.base_url)
            self._context.set("oracle_oic_api_version", self._oic_config.api_version)

    def __aenter__(self) -> Self:
        """Async context manager entry."""
        self.logger.info(
            "Oracle OIC service started",
            extra_info=str(self.get_connection_context()),
        )
        return self

    def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: t.RecursiveContainer,
    ) -> None:
        """Async context manager exit."""
        self.logger.info(
            "Oracle OIC service stopped",
            extra_info=str(self.get_connection_context()),
        )

    def activate_integration(self, integration_id: str) -> r[bool]:
        """Activate Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        r indicating success or failure.

        """
        return self._service.activate_integration(integration_id)

    def create_integration(
        self,
        integration_data: t.RecursiveContainerMapping,
    ) -> r[FlextOracleOicModels.OracleOic.OICIntegrationInfo]:
        """Create new Oracle OIC integration.

        Args:
        integration_data: Integration configuration data.

        Returns:
        r containing created integration information.

        """
        return self._service.create_integration(integration_data)

    def deactivate_integration(self, integration_id: str) -> r[bool]:
        """Deactivate Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        r indicating success or failure.

        """
        return self._service.deactivate_integration(integration_id)

    def delete_integration(self, integration_id: str) -> r[bool]:
        """Delete Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        r indicating success or failure.

        """
        return self._service.delete_integration(integration_id)

    @override
    def execute(self) -> r[None]:
        """Execute Oracle OIC API operations - delegates to service."""
        result = self._service.execute()
        return result.map(lambda _: None)

    def execute_app_driven_orchestration(
        self,
        integration_id: str,
        payload: t.RecursiveContainerMapping,
        **kwargs: t.Scalar,
    ) -> r[t.RecursiveContainerMapping]:
        """Execute app-driven orchestration pattern.

        Args:
        integration_id: The integration identifier.
        payload: Orchestration payload data.
        **kwargs: Additional execution parameters.

        Returns:
        r containing execution result.

        """
        return self._service.execute_app_driven_orchestration(
            integration_id,
            payload,
            **kwargs,
        )

    def execute_file_transfer(
        self,
        integration_id: str,
        file_config: t.RecursiveContainerMapping,
        **kwargs: t.Scalar,
    ) -> r[t.RecursiveContainerMapping]:
        """Execute file transfer pattern.

        Args:
        integration_id: The integration identifier.
        file_config: File transfer configuration.
        **kwargs: Additional execution parameters.

        Returns:
        r containing execution result.

        """
        return self._service.execute_file_transfer(
            integration_id,
            file_config,
            **kwargs,
        )

    def execute_scheduled_orchestration(
        self,
        integration_id: str,
        schedule_config: t.RecursiveContainerMapping,
        **kwargs: t.Scalar,
    ) -> r[t.RecursiveContainerMapping]:
        """Execute scheduled orchestration pattern.

        Args:
        integration_id: The integration identifier.
        schedule_config: Schedule configuration.
        **kwargs: Additional execution parameters.

        Returns:
        r containing execution result.

        """
        return self._service.execute_scheduled_orchestration(
            integration_id,
            schedule_config,
            **kwargs,
        )

    def get_auth_context(self) -> t.RecursiveContainerMapping:
        """Get current authentication configuration context.

        Returns:
        Dictionary containing authentication context information.

        """
        return {
            "oauth_client_id": self._oic_config.oauth_client_id,
            "oauth_token_url": self._oic_config.oauth_token_url,
            "oauth_scope": self._oic_config.oauth_scope,
        }

    def get_connection_context(self) -> t.RecursiveContainerMapping:
        """Get current connection configuration context.

        Returns:
        Dictionary containing connection context information.

        """
        return {
            "base_url": self._oic_config.base_url,
            "api_version": self._oic_config.api_version,
            "request_timeout": self._oic_config.request_timeout,
        }

    def get_features_context(self) -> t.RecursiveContainerMapping:
        """Get current features configuration context.

        Returns:
        Dictionary containing features context information.

        """
        return {
            "enable_monitoring": self._oic_config.enable_monitoring,
            "use_ssl": self._oic_config.use_ssl,
            "verify_ssl": self._oic_config.verify_ssl,
        }

    def get_health_status(self) -> r[t.RecursiveContainerMapping]:
        """Get Oracle OIC health status.

        Returns:
        r containing health status information.

        """
        return self._service.get_health_status()

    def get_integration(
        self,
        integration_id: str,
    ) -> r[FlextOracleOicModels.OracleOic.OICIntegrationInfo]:
        """Get specific Oracle OIC integration by ID.

        Args:
        integration_id: The integration identifier.

        Returns:
        r containing integration information.

        """
        return self._service.get_integration(integration_id)

    def get_performance_metrics(self) -> r[t.RecursiveContainerMapping]:
        """Get Oracle OIC performance metrics.

        Returns:
        r containing performance metrics.

        """
        return self._service.get_performance_metrics()

    def list_integrations(
        self,
    ) -> r[Sequence[FlextOracleOicModels.OracleOic.OICIntegrationInfo]]:
        """List all Oracle OIC integrations.

        Returns:
        r containing list of integration information.

        """
        return self._service.list_integrations()

    def refresh_auth_token(self) -> r[str]:
        """Refresh OAuth2 authentication token.

        Returns:
        r containing new access token.

        """
        return self._service.refresh_auth_token()

    def test_connection(self) -> r[bool]:
        """Test connection to Oracle OIC instance.

        Returns:
        r containing connection test result.

        """
        return self._service.test_connection()

    def update_integration(
        self,
        integration_id: str,
        integration_data: t.RecursiveContainerMapping,
    ) -> r[FlextOracleOicModels.OracleOic.OICIntegrationInfo]:
        """Update existing Oracle OIC integration.

        Args:
        integration_id: The integration identifier.
        integration_data: Updated integration configuration.

        Returns:
        r containing updated integration information.

        """
        return self._service.update_integration(integration_id, integration_data)

    def validate_auth_token(self, token: str) -> r[bool]:
        """Validate OAuth2 authentication token.

        Args:
        token: Token to validate.

        Returns:
        r containing validation result.

        """
        return self._service.validate_auth_token(token)


oracle_oic = FlextOracleOicApi

__all__: list[str] = ["FlextOracleOicApi", "oracle_oic"]
