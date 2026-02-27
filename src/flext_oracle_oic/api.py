"""FLEXT Oracle OIC Extension API - Thin Facade Pattern.

FLEXT Unified Module Pattern: Thin facade exposing all domain functionality
through complete flext-core integration. Provides single entry point for all
Oracle OIC operations with enterprise patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Self, override

from flext_core import (
    FlextContainer,
    FlextContext,
    FlextRegistry,
    FlextResult,
    FlextService,
)
from flext_oracle_oic.models import FlextOracleOicModels
from flext_oracle_oic.service import FlextOracleOicService
from flext_oracle_oic.settings import FlextOracleOicSettings
from flext_oracle_oic.typings import t


class FlextOracleOicApi(FlextService[None]):
    """Thin facade for Oracle OIC operations with complete FLEXT integration.

    Integrates:
    - FlextBus: Event emission for OIC operations
    - FlextContainer: Dependency injection for OIC services
    - FlextContext: Operation context management
    - FlextDispatcher: Message routing for OIC patterns
    - FlextRegistry: Component registration for OIC extensions
    - FlextLogger: Structured logging for OIC operations

    Provides unified access to all Oracle OIC functionality:
    - Integration lifecycle management (create, update, delete, activate)
    - Authentication and authorization (OAuth2, IDCS)
    - Connection testing and health monitoring
    - Integration pattern execution (app-driven, scheduled, file transfer)
    - Enterprise orchestration patterns (Message Router, Scatter-Gather)
    - Monitoring and observability
    """

    def __init__(
        self,
        config: FlextOracleOicSettings | None = None,
    ) -> None:
        """Initialize FlextOracleOic facade with complete ecosystem integration.

        Args:
        config: Oracle OIC configuration. If None, uses global instance.

        """
        super().__init__()

        # Configuration with fallback to global instance
        self._oic_config: FlextOracleOicSettings = config or FlextOracleOicSettings()

        # Complete FLEXT ecosystem integration
        self._container = FlextContainer.get_global()
        self._context = FlextContext()
        self._dispatcher = None  # CommandBus not required for API facade
        self._registry = FlextRegistry(dispatcher=None)

        # Initialize Oracle OIC service
        self._service = FlextOracleOicService()

        # Initialize context with OIC-specific information
        self._context.set("oracle_oic_base_url", self._oic_config.base_url)
        self._context.set("oracle_oic_api_version", self._oic_config.api_version)

    @override
    @override
    def execute(self) -> FlextResult[None]:
        """Execute Oracle OIC API operations - delegates to service."""
        result = self._get_service().execute()
        return result.map(lambda _: None)  # Convert list result to None
        """Execute Oracle OIC API operations - delegates to service."""
        return self._get_service().execute()

    def _create_service(self) -> FlextOracleOicService:
        """Create unified Oracle OIC service instance."""
        return FlextOracleOicService()

    def list_integrations(
        self,
    ) -> FlextResult[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]]:
        """List all Oracle OIC integrations.

        Returns:
        FlextResult containing list of integration information.

        """
        return self._get_service().list_integrations()

    def get_integration(
        self,
        integration_id: str,
    ) -> FlextResult[FlextOracleOicModels.OracleOic.OICIntegrationInfo]:
        """Get specific Oracle OIC integration by ID.

        Args:
        integration_id: The integration identifier.

        Returns:
        FlextResult containing integration information.

        """
        return self._get_service().get_integration(integration_id)

    def create_integration(
        self,
        integration_data: Mapping[str, t.GeneralValueType],
    ) -> FlextResult[FlextOracleOicModels.OracleOic.OICIntegrationInfo]:
        """Create new Oracle OIC integration.

        Args:
        integration_data: Integration configuration data.

        Returns:
        FlextResult containing created integration information.

        """
        return self._get_service().create_integration(integration_data)

    def update_integration(
        self,
        integration_id: str,
        integration_data: Mapping[str, t.GeneralValueType],
    ) -> FlextResult[FlextOracleOicModels.OracleOic.OICIntegrationInfo]:
        """Update existing Oracle OIC integration.

        Args:
        integration_id: The integration identifier.
        integration_data: Updated integration configuration.

        Returns:
        FlextResult containing updated integration information.

        """
        return self._get_service().update_integration(integration_id, integration_data)

    def delete_integration(self, integration_id: str) -> FlextResult[bool]:
        """Delete Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        FlextResult indicating success or failure.

        """
        return self._get_service().delete_integration(integration_id)

    def activate_integration(self, integration_id: str) -> FlextResult[bool]:
        """Activate Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        FlextResult indicating success or failure.

        """
        return self._get_service().activate_integration(integration_id)

    def deactivate_integration(self, integration_id: str) -> FlextResult[bool]:
        """Deactivate Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        FlextResult indicating success or failure.

        """
        return self._get_service().deactivate_integration(integration_id)

    # Connection and Testing

    def test_connection(self) -> FlextResult[bool]:
        """Test connection to Oracle OIC instance.

        Returns:
        FlextResult containing connection test result.

        """
        return self._get_service().test_connection()

    # Integration Pattern Execution

    def execute_app_driven_orchestration(
        self,
        integration_id: str,
        payload: Mapping[str, t.GeneralValueType],
        **kwargs: object,
    ) -> FlextResult[Mapping[str, t.GeneralValueType]]:
        """Execute app-driven orchestration pattern.

        Args:
        integration_id: The integration identifier.
        payload: Orchestration payload data.
        **kwargs: Additional execution parameters.

        Returns:
        FlextResult containing execution result.

        """
        return self._get_service().execute_app_driven_orchestration(
            integration_id,
            payload,
            **kwargs,
        )

    def execute_scheduled_orchestration(
        self,
        integration_id: str,
        schedule_config: Mapping[str, t.GeneralValueType],
        **kwargs: object,
    ) -> FlextResult[Mapping[str, t.GeneralValueType]]:
        """Execute scheduled orchestration pattern.

        Args:
        integration_id: The integration identifier.
        schedule_config: Schedule configuration.
        **kwargs: Additional execution parameters.

        Returns:
        FlextResult containing execution result.

        """
        return self._get_service().execute_scheduled_orchestration(
            integration_id,
            schedule_config,
            **kwargs,
        )

    def execute_file_transfer(
        self,
        integration_id: str,
        file_config: Mapping[str, t.GeneralValueType],
        **kwargs: object,
    ) -> FlextResult[Mapping[str, t.GeneralValueType]]:
        """Execute file transfer pattern.

        Args:
        integration_id: The integration identifier.
        file_config: File transfer configuration.
        **kwargs: Additional execution parameters.

        Returns:
        FlextResult containing execution result.

        """
        return self._get_service().execute_file_transfer(
            integration_id,
            file_config,
            **kwargs,
        )

    # Monitoring and Health

    def get_health_status(self) -> FlextResult[Mapping[str, t.GeneralValueType]]:
        """Get Oracle OIC health status.

        Returns:
        FlextResult containing health status information.

        """
        return self._get_service().get_health_status()

    def get_performance_metrics(self) -> FlextResult[Mapping[str, t.GeneralValueType]]:
        """Get Oracle OIC performance metrics.

        Returns:
        FlextResult containing performance metrics.

        """
        return self._get_service().get_performance_metrics()

    # Authentication Management

    def refresh_auth_token(self) -> FlextResult[str]:
        """Refresh OAuth2 authentication token.

        Returns:
        FlextResult containing new access token.

        """
        return self._get_service().refresh_auth_token()

    def validate_auth_token(self, token: str) -> FlextResult[bool]:
        """Validate OAuth2 authentication token.

        Args:
        token: Token to validate.

        Returns:
        FlextResult containing validation result.

        """
        return self._get_service().validate_auth_token(token)

    # Context and Configuration

    def get_connection_context(self) -> Mapping[str, t.GeneralValueType]:
        """Get current connection configuration context.

        Returns:
        Dictionary containing connection context information.

        """
        return {
            "base_url": self._oic_config.base_url,
            "api_version": self._oic_config.api_version,
            "request_timeout": self._oic_config.request_timeout,
        }

    def get_auth_context(self) -> Mapping[str, t.GeneralValueType]:
        """Get current authentication configuration context.

        Returns:
        Dictionary containing authentication context information.

        """
        return {
            "oauth_client_id": self._oic_config.oauth_client_id,
            "oauth_token_url": self._oic_config.oauth_token_url,
            "oauth_scope": self._oic_config.oauth_scope,
        }

    def get_features_context(self) -> Mapping[str, t.GeneralValueType]:
        """Get current features configuration context.

        Returns:
        Dictionary containing features context information.

        """
        return {
            "enable_monitoring": self._oic_config.enable_monitoring,
            "use_ssl": self._oic_config.use_ssl,
            "verify_ssl": self._oic_config.verify_ssl,
        }

    # Service Access

    def _get_service(self) -> FlextOracleOicService:
        """Get the unified Oracle OIC service instance."""
        return self._service

    # Lifecycle Management

    def __aenter__(self) -> Self:
        """Async context manager entry."""
        # Log service start
        self.logger.info(
            "Oracle OIC service started",
            extra=self.get_connection_context(),
        )
        return self

    def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None:
        """Async context manager exit."""
        # Log service stop
        self.logger.info(
            "Oracle OIC service stopped",
            extra=self.get_connection_context(),
        )


__all__ = [
    "FlextOracleOicApi",
]
