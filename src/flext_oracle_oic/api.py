"""FLEXT Oracle OIC Extension API - Thin Facade Pattern.

FLEXT Unified Module Pattern: Thin facade exposing all domain functionality
through complete flext-core integration. Provides single entry point for all
Oracle OIC operations with enterprise patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Self

from flext_core import (
    FlextBus,
    FlextContainer,
    FlextContext,
    FlextDispatcher,
    FlextLogger,
    FlextProcessors,
    FlextRegistry,
    FlextResult,
    FlextService,
    FlextTypes,
)

from flext_oracle_oic.config import FlextOracleOicExtConfig
from flext_oracle_oic.models import FlextOracleOicExtModels
from flext_oracle_oic.service import (
    FlextOracleOicService,  # Unified service class
)

# Type aliases for backward compatibility
FlextOracleOic = "FlextOracleOic"  # Forward reference for class name
FlextOracleOicAPI = FlextOracleOic  # Common alias pattern


class FlextOracleOic(FlextService[None]):
    """Thin facade for Oracle OIC operations with complete FLEXT integration.

    Integrates:
    - FlextBus: Event emission for OIC operations
    - FlextContainer: Dependency injection for OIC services
    - FlextContext: Operation context management
    - FlextDispatcher: Message routing for OIC patterns
    - FlextProcessors: Processing utilities for OIC data
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
        config: FlextOracleOicExtConfig | None = None,
    ) -> None:
        """Initialize FlextOracleOic facade with complete ecosystem integration.

        Args:
            config: Oracle OIC configuration. If None, uses global instance.

        """
        super().__init__()

        # Configuration with fallback to global instance
        self._config = config or FlextOracleOicExtConfig.get_global_instance()
        self._logger = FlextLogger(__name__)

        # Complete FLEXT ecosystem integration
        self._container = FlextContainer.get_global()
        self._context = FlextContext()
        self._bus = FlextBus()
        self._dispatcher = FlextDispatcher()
        self._processors = FlextProcessors()
        self._registry = FlextRegistry(dispatcher=self._dispatcher)

        # Register Oracle OIC service in container
        self._container.register_singleton(
            FlextOracleOicService, self._create_service()
        )

        # Initialize context with OIC-specific information
        self._context.set("oracle_oic_base_url", self._config.base_url)
        self._context.set("oracle_oic_api_version", self._config.api_version)

    def _create_service(self) -> FlextOracleOicService:
        """Create unified Oracle OIC service instance."""
        return FlextOracleOicService(settings=self._config)

    # Integration Management

    async def list_integrations(
        self,
    ) -> FlextResult[list[FlextOracleOicExtModels.OICIntegrationInfo]]:
        """List all Oracle OIC integrations.

        Returns:
            FlextResult containing list of integration information.

        """
        return self._get_service().list_integrations()

    async def get_integration(
        self,
        integration_id: str,
    ) -> FlextResult[FlextOracleOicExtModels.OICIntegrationInfo]:
        """Get specific Oracle OIC integration by ID.

        Args:
            integration_id: The integration identifier.

        Returns:
            FlextResult containing integration information.

        """
        return self._get_service().get_integration(integration_id)

    async def create_integration(
        self,
        integration_data: dict,
    ) -> FlextResult[FlextOracleOicExtModels.OICIntegrationInfo]:
        """Create new Oracle OIC integration.

        Args:
            integration_data: Integration configuration data.

        Returns:
            FlextResult containing created integration information.

        """
        return self._get_service().create_integration(integration_data)

    async def update_integration(
        self,
        integration_id: str,
        integration_data: dict,
    ) -> FlextResult[FlextOracleOicExtModels.OICIntegrationInfo]:
        """Update existing Oracle OIC integration.

        Args:
            integration_id: The integration identifier.
            integration_data: Updated integration configuration.

        Returns:
            FlextResult containing updated integration information.

        """
        return await self._get_service().update_integration(
            integration_id, integration_data
        )

    async def delete_integration(self, integration_id: str) -> FlextResult[None]:
        """Delete Oracle OIC integration.

        Args:
            integration_id: The integration identifier.

        Returns:
            FlextResult indicating success or failure.

        """
        return await self._get_service().delete_integration(integration_id)

    async def activate_integration(self, integration_id: str) -> FlextResult[None]:
        """Activate Oracle OIC integration.

        Args:
            integration_id: The integration identifier.

        Returns:
            FlextResult indicating success or failure.

        """
        return await self._get_service().activate_integration(integration_id)

    async def deactivate_integration(self, integration_id: str) -> FlextResult[None]:
        """Deactivate Oracle OIC integration.

        Args:
            integration_id: The integration identifier.

        Returns:
            FlextResult indicating success or failure.

        """
        return await self._get_service().deactivate_integration(integration_id)

    # Connection and Testing

    async def test_connection(self) -> FlextResult[bool]:
        """Test connection to Oracle OIC instance.

        Returns:
            FlextResult containing connection test result.

        """
        return await self._get_service().test_connection()

    # Integration Pattern Execution

    async def execute_app_driven_orchestration(
        self,
        integration_id: str,
        payload: dict,
        **kwargs: object,
    ) -> FlextResult[FlextTypes.Dict]:
        """Execute app-driven orchestration pattern.

        Args:
            integration_id: The integration identifier.
            payload: Orchestration payload data.
            **kwargs: Additional execution parameters.

        Returns:
            FlextResult containing execution result.

        """
        return await self._get_service().execute_app_driven_orchestration(
            integration_id, payload, **kwargs
        )

    async def execute_scheduled_orchestration(
        self,
        integration_id: str,
        schedule_config: dict,
        **kwargs: object,
    ) -> FlextResult[FlextTypes.Dict]:
        """Execute scheduled orchestration pattern.

        Args:
            integration_id: The integration identifier.
            schedule_config: Schedule configuration.
            **kwargs: Additional execution parameters.

        Returns:
            FlextResult containing execution result.

        """
        return await self._get_service().execute_scheduled_orchestration(
            integration_id, schedule_config, **kwargs
        )

    async def execute_file_transfer(
        self,
        integration_id: str,
        file_config: dict,
        **kwargs: object,
    ) -> FlextResult[FlextTypes.Dict]:
        """Execute file transfer pattern.

        Args:
            integration_id: The integration identifier.
            file_config: File transfer configuration.
            **kwargs: Additional execution parameters.

        Returns:
            FlextResult containing execution result.

        """
        return await self._get_service().execute_file_transfer(
            integration_id, file_config, **kwargs
        )

    # Monitoring and Health

    async def get_health_status(self) -> FlextResult[FlextTypes.Dict]:
        """Get Oracle OIC health status.

        Returns:
            FlextResult containing health status information.

        """
        return await self._get_service().get_health_status()

    async def get_performance_metrics(self) -> FlextResult[FlextTypes.Dict]:
        """Get Oracle OIC performance metrics.

        Returns:
            FlextResult containing performance metrics.

        """
        return await self._get_service().get_performance_metrics()

    # Authentication Management

    async def refresh_auth_token(self) -> FlextResult[str]:
        """Refresh OAuth2 authentication token.

        Returns:
            FlextResult containing new access token.

        """
        return await self._get_service().refresh_auth_token()

    async def validate_auth_token(self, token: str) -> FlextResult[bool]:
        """Validate OAuth2 authentication token.

        Args:
            token: Token to validate.

        Returns:
            FlextResult containing validation result.

        """
        return await self._get_service().validate_auth_token(token)

    # Context and Configuration

    def get_connection_context(self) -> dict:
        """Get current connection configuration context.

        Returns:
            Dictionary containing connection context information.

        """
        return self._config.get_connection_context()

    def get_auth_context(self) -> dict:
        """Get current authentication configuration context.

        Returns:
            Dictionary containing authentication context information.

        """
        return self._config.get_auth_context()

    def get_features_context(self) -> dict:
        """Get current features configuration context.

        Returns:
            Dictionary containing features context information.

        """
        return self._config.get_features_context()

    # Service Access

    def _get_service(self) -> FlextOracleOicService:
        """Get the unified Oracle OIC service instance."""
        return self._container.resolve(FlextOracleOicService)

    # Lifecycle Management

    async def __aenter__(self) -> Self:
        """Async context manager entry."""
        # Emit service start event
        await self._bus.publish_async(
            "oracle_oic.service.started",
            {
                "service": "FlextOracleOic",
                "config": self.get_connection_context(),
            },
        )
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None:
        """Async context manager exit."""
        # Emit service stop event
        await self._bus.publish_async(
            "oracle_oic.service.stopped",
            {
                "service": "FlextOracleOic",
                "config": self.get_connection_context(),
            },
        )


__all__ = [
    "FlextOracleOic",
    "FlextOracleOicAPI",  # Common alias pattern
]
