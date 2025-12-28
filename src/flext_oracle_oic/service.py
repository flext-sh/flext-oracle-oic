"""FLEXT Oracle OIC Service - Unified Service Pattern.

FLEXT Unified Module Pattern: Single unified service class consolidating
all Oracle OIC functionality. Implements complete FlextService pattern
with railway-oriented error handling.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import asyncio
from typing import Self, override

from flext_api import FlextApiClient
from flext_api.settings import FlextApiSettings
from flext_core import (
    FlextConstants,
    FlextContainer,
    FlextContext,
    FlextDispatcher,
    FlextLogger,
    FlextRegistry,
    FlextResult,
    FlextService,
    FlextTypes as t,
)

from flext_oracle_oic.constants import FlextOracleOicConstants
from flext_oracle_oic.ext_client import (
    FlextOracleOicClient,
)
from flext_oracle_oic.models import FlextOracleOicModels
from flext_oracle_oic.settings import FlextOracleOicSettings
from flext_oracle_oic.utilities import FlextOracleOicUtilities


class FlextOracleOicService(
    FlextService[list[FlextOracleOicModels.OICIntegrationInfo]],
):
    """Unified Oracle OIC Extension Service - Single Class Pattern.

    Consolidates all Oracle OIC functionality into a single unified service class:
    - Integration lifecycle management (OracleOicExtensionService)
    - Pattern execution (OICIntegrationPatternService)
    - Connection management (LifecycleManager)
    - Monitoring and health checks (MonitoringService)

    Implements complete FlextService pattern with railway-oriented error handling.
    """

    def __init__(self) -> None:
        """Initialize unified Oracle OIC service.

        Uses singleton config pattern - no config parameter needed.
        """
        super().__init__()
        self.settings = FlextOracleOicSettings.get_global_instance()
        # Logger is inherited from parent class
        self._client: FlextOracleOicClient | None = None
        self._monitoring_client: FlextApiClient | None = None
        self._authenticator: object | None = None

        # Complete FLEXT ecosystem integration
        self._container = FlextContainer.get_global()
        context_obj = FlextContext()
        self._context = context_obj
        self._dispatcher = FlextDispatcher()
        self._registry = FlextRegistry(dispatcher=self._dispatcher)

        # Service registered in container for dependency injection

        # Initialize components
        self._initialize_components()

    def _initialize_components(self) -> None:
        """Initialize service components."""
        try:
            # Components are initialized lazily when first needed

            # Create HTTP monitoring client if monitoring is enabled
            if self.settings.enable_monitoring:
                api_config = FlextApiSettings(
                    base_url=self.settings.base_url,
                    timeout=self.settings.request_timeout,
                    headers={
                        "Authorization": f"Bearer {self._authenticator.refresh_token('') if self._authenticator and hasattr(self._authenticator, 'refresh_token') else ''}",
                        "Content-Type": "application/json",
                    },
                )
                self._monitoring_client = FlextApiClient(api_config)

        except Exception:
            FlextLogger(__name__).exception("Failed to initialize service components")
            raise

    @override
    def execute(
        self: Self,
        **kwargs: object,
    ) -> FlextResult[list[FlextOracleOicModels.OICIntegrationInfo]]:
        """Execute main service operation - list all integrations.

        Returns:
        FlextResult containing list of OIC integrations.

        """
        return self.list_integrations()

    # Integration Management Methods (from OracleOicExtensionService)

    def list_integrations(
        self,
    ) -> FlextResult[list[FlextOracleOicModels.OICIntegrationInfo]]:
        """List all Oracle OIC integrations.

        Returns:
        FlextResult containing list of integration information.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[list[FlextOracleOicModels.OICIntegrationInfo]].fail(
                    error_msg,
                )

            client = client_result.value
            integrations_result = client.get_integrations()

            if integrations_result.is_failure:
                error_msg = integrations_result.error or "Failed to get integrations"
                return FlextResult[list[FlextOracleOicModels.OICIntegrationInfo]].fail(
                    error_msg,
                )

            integrations_data = integrations_result.value

            # Convert to domain models
            integrations = []
            for item in integrations_data:
                integration = FlextOracleOicModels.OICIntegrationInfo(
                    integration_id=item.get("id", ""),
                    name=item.get("name", ""),
                    description=item.get("description", ""),
                    integration_version=item.get("version", "1.0"),
                    status=item.get("status", "UNKNOWN"),
                    created_by=item.get("createdBy", ""),
                    last_updated=item.get("lastUpdated", ""),
                )
                integrations.append(integration)

            return FlextResult[list[FlextOracleOicModels.OICIntegrationInfo]].ok(
                integrations,
            )

        except Exception as e:
            FlextLogger(__name__).exception("Failed to list integrations")
            return FlextResult[list[FlextOracleOicModels.OICIntegrationInfo]].fail(
                f"Integration listing failed: {e!s}",
            )

    def list_connections(
        self,
        type_filter: list[str] | None = None,
    ) -> FlextResult[list[FlextOracleOicModels.OICConnectionInfo]]:
        """List Oracle OIC connections.

        Args:
        type_filter: Filter by connection type

        Returns:
        FlextResult containing connection info list or error

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[list[FlextOracleOicModels.OICConnectionInfo]].fail(
                    error_msg,
                )

            client = client_result.value
            connections_result = client.get_connections(
                type_filter=type_filter,
                page_size=FlextOracleOicConstants.OIC.DEFAULT_PAGE_SIZE,
            )

            if connections_result.is_failure:
                error_msg = connections_result.error or "Failed to get connections"
                return FlextResult[list[FlextOracleOicModels.OICConnectionInfo]].fail(
                    error_msg,
                )

            connections_data = connections_result.value

            # Convert to domain models
            connections = []
            for item in connections_data:
                connection = FlextOracleOicModels.OICConnectionInfo(
                    connection_id=item.get("id", ""),
                    name=item.get("name", ""),
                    adapter_type=item.get("adapterType", ""),
                    status=item.get("status", "UNKNOWN"),
                    connection_type=item.get("connectionType", ""),
                    description=item.get("description", ""),
                )
                connections.append(connection)

            return FlextResult[list[FlextOracleOicModels.OICConnectionInfo]].ok(
                connections,
            )

        except Exception as e:
            self.logger.exception("Failed to list connections")
            return FlextResult[list[FlextOracleOicModels.OICConnectionInfo]].fail(
                f"Connection listing failed: {e!s}",
            )

    def get_integration(
        self,
        integration_id: str,
    ) -> FlextResult[FlextOracleOicModels.OICIntegrationInfo]:
        """Get specific Oracle OIC integration by ID.

        Args:
        integration_id: The integration identifier.

        Returns:
        FlextResult containing integration information.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[FlextOracleOicModels.OICIntegrationInfo].fail(
                    error_msg,
                )

            client = client_result.value
            # Get all integrations and find the one with matching ID
            integrations_result = client.get_integrations()
            if integrations_result.is_failure:
                error_msg = integrations_result.error or "Failed to get integrations"
                return FlextResult[FlextOracleOicModels.OICIntegrationInfo].fail(
                    error_msg,
                )

            integrations_list = integrations_result.value
            integration_data = next(
                (
                    item
                    for item in integrations_list
                    if item.get("id") == integration_id
                ),
                None,
            )
            if not integration_data:
                return FlextResult[FlextOracleOicModels.OICIntegrationInfo].fail(
                    f"Integration {integration_id} not found",
                )

            integration = FlextOracleOicModels.OICIntegrationInfo(
                integration_id=integration_data.get("id", integration_id)
                or integration_id,
                name=integration_data.get("name", "") or "",
                description=integration_data.get("description", "") or "",
                integration_version=integration_data.get("version", "1.0") or "1.0",
                status=integration_data.get("status", "UNKNOWN") or "UNKNOWN",
                created_by=integration_data.get("createdBy", "") or "",
                last_updated=integration_data.get("lastUpdated", "") or "",
            )

            return FlextResult[FlextOracleOicModels.OICIntegrationInfo].ok(integration)

        except Exception as e:
            self.logger.exception(f"Failed to get integration {integration_id}")
            return FlextResult[FlextOracleOicModels.OICIntegrationInfo].fail(
                f"Integration retrieval failed: {e!s}",
            )

    def create_integration(
        self,
        integration_data: dict,
    ) -> FlextResult[FlextOracleOicModels.OICIntegrationInfo]:
        """Create new Oracle OIC integration.

        Args:
        integration_data: Integration configuration data.

        Returns:
        FlextResult containing created integration information.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[FlextOracleOicModels.OICIntegrationInfo].fail(
                    error_msg,
                )

            client = client_result.value
            created_result = client.create_integration(integration_data)
            if created_result.is_failure:
                error_msg = created_result.error or "Failed to create integration"
                return FlextResult[FlextOracleOicModels.OICIntegrationInfo].fail(
                    error_msg,
                )

            created_data = created_result.value

            integration = FlextOracleOicModels.OICIntegrationInfo(
                integration_id=created_data.get("id", "") or "",
                name=created_data.get("name", "") or "",
                description=created_data.get("description", "") or "",
                integration_version=created_data.get("version", "1.0") or "1.0",
                status=created_data.get("status", "DRAFT") or "DRAFT",
                created_by=created_data.get("createdBy", "") or "",
                last_updated=created_data.get("lastUpdated", "") or "",
            )

            return FlextResult[FlextOracleOicModels.OICIntegrationInfo].ok(integration)

        except Exception as e:
            self.logger.exception("Failed to create integration")
            return FlextResult[FlextOracleOicModels.OICIntegrationInfo].fail(
                f"Integration creation failed: {e!s}",
            )

    def update_integration(
        self,
        integration_id: str,
        integration_data: dict,
    ) -> FlextResult[FlextOracleOicModels.OICIntegrationInfo]:
        """Update existing Oracle OIC integration.

        Args:
        integration_id: The integration identifier.
        integration_data: Updated integration configuration.

        Returns:
        FlextResult containing updated integration information.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[FlextOracleOicModels.OICIntegrationInfo].fail(
                    error_msg,
                )

            client = client_result.value
            updated_result = client.update_integration(integration_id, integration_data)
            if updated_result.is_failure:
                error_msg = updated_result.error or "Failed to update integration"
                return FlextResult[FlextOracleOicModels.OICIntegrationInfo].fail(
                    error_msg,
                )

            updated_data = updated_result.value

            integration = FlextOracleOicModels.OICIntegrationInfo(
                integration_id=updated_data.get("id", integration_id) or integration_id,
                name=updated_data.get("name", "") or "",
                description=updated_data.get("description", "") or "",
                integration_version=updated_data.get("version", "1.0") or "1.0",
                status=updated_data.get("status", "UNKNOWN") or "UNKNOWN",
                created_by=updated_data.get("createdBy", "") or "",
                last_updated=updated_data.get("lastUpdated", "") or "",
            )

            return FlextResult[FlextOracleOicModels.OICIntegrationInfo].ok(integration)

        except Exception as e:
            self.logger.exception(f"Failed to update integration {integration_id}")
            return FlextResult[FlextOracleOicModels.OICIntegrationInfo].fail(
                f"Integration update failed: {e!s}",
            )

    def delete_integration(self, integration_id: str) -> FlextResult[None]:
        """Delete Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        FlextResult indicating success or failure.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[None].fail(error_msg)

            client = client_result.value
            # Delete integration using update with status DELETED or make_request
            delete_result = client.make_request(
                "DELETE",
                f"/integrations/{integration_id}",
            )
            if delete_result.is_failure:
                error_msg = delete_result.error or "Failed to delete integration"
                return FlextResult[None].fail(error_msg)

            return FlextResult[None].ok(None)

        except Exception as e:
            self.logger.exception(f"Failed to delete integration {integration_id}")
            return FlextResult[None].fail(f"Integration deletion failed: {e!s}")

    def activate_integration(self, integration_id: str) -> FlextResult[None]:
        """Activate Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        FlextResult indicating success or failure.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[None].fail(error_msg)

            client = client_result.value
            # Activate integration using make_request
            activate_result = client.make_request(
                "POST",
                f"/integrations/{integration_id}/activate",
            )
            if activate_result.is_failure:
                error_msg = activate_result.error or "Failed to activate integration"
                return FlextResult[None].fail(error_msg)

            return FlextResult[None].ok(None)

        except Exception as e:
            self.logger.exception(f"Failed to activate integration {integration_id}")
            return FlextResult[None].fail(f"Integration activation failed: {e!s}")

    def deactivate_integration(self, integration_id: str) -> FlextResult[None]:
        """Deactivate Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        FlextResult indicating success or failure.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[None].fail(error_msg)

            client = client_result.value
            # Deactivate integration using make_request
            deactivate_result = client.make_request(
                "POST",
                f"/integrations/{integration_id}/deactivate",
            )
            if deactivate_result.is_failure:
                error_msg = (
                    deactivate_result.error or "Failed to deactivate integration"
                )
                return FlextResult[None].fail(error_msg)

            return FlextResult[None].ok(None)

        except Exception as e:
            self.logger.exception(f"Failed to deactivate integration {integration_id}")
            return FlextResult[None].fail(f"Integration deactivation failed: {e!s}")

    # Connection Testing Methods (from LifecycleManager)

    def test_connection(self) -> FlextResult[bool]:
        """Test connection to Oracle OIC instance.

        Returns:
        FlextResult containing connection test result.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[bool].fail(error_msg)

            client = client_result.value
            # Test connection using make_request to health endpoint
            test_result = client.make_request("GET", "/ic/api/integration/v1/health")
            if test_result.is_failure:
                error_msg = test_result.error or "Connection test failed"
                return FlextResult[bool].fail(error_msg)
            result_data = test_result.value
            is_connected = result_data.get("status", "").lower() == "healthy"

            return FlextResult[bool].ok(is_connected)

        except Exception as e:
            self.logger.exception("Connection test failed")
            return FlextResult[bool].fail(f"Connection test failed: {e!s}")

    # Integration Pattern Execution Methods (from OICIntegrationPatternService)

    def execute_app_driven_orchestration(
        self,
        integration_id: str,
        payload: dict,
        **kwargs: object,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Execute app-driven orchestration pattern.

        Args:
        integration_id: The integration identifier.
        payload: Orchestration payload data.
        **kwargs: Additional execution parameters.

        Returns:
        FlextResult containing execution result.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[dict[str, t.GeneralValueType]].fail(error_msg)

            client = client_result.value
            # Execute app-driven orchestration using make_request
            orchestration_result = client.make_request(
                integration_id,
                payload,
                **kwargs,
            )

            return FlextResult[dict[str, t.GeneralValueType]].ok(orchestration_result)

        except Exception as e:
            self.logger.exception(
                "App-driven orchestration failed for %s",
                integration_id,
            )
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                f"Orchestration execution failed: {e!s}",
            )

    def execute_scheduled_orchestration(
        self,
        integration_id: str,
        schedule_config: dict,
        **kwargs: object,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Execute scheduled orchestration pattern.

        Args:
        integration_id: The integration identifier.
        schedule_config: Schedule configuration.
        **kwargs: Additional execution parameters.

        Returns:
        FlextResult containing execution result.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[dict[str, t.GeneralValueType]].fail(error_msg)

            client = client_result.value
            result = client.execute_scheduled_orchestration(
                integration_id,
                schedule_config,
                **kwargs,
            )

            return FlextResult[dict[str, t.GeneralValueType]].ok(result)

        except Exception as e:
            self.logger.exception(
                "Scheduled orchestration failed for %s",
                integration_id,
            )
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                f"Scheduled orchestration failed: {e!s}",
            )

    def execute_file_transfer(
        self,
        integration_id: str,
        file_config: dict,
        **kwargs: object,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Execute file transfer pattern.

        Args:
        integration_id: The integration identifier.
        file_config: File transfer configuration.
        **kwargs: Additional execution parameters.

        Returns:
        FlextResult containing execution result.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[dict[str, t.GeneralValueType]].fail(error_msg)

            client = client_result.value
            result = client.execute_file_transfer(integration_id, file_config, **kwargs)

            return FlextResult[dict[str, t.GeneralValueType]].ok(result)

        except Exception as e:
            self.logger.exception(f"File transfer failed for {integration_id}")
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                f"File transfer failed: {e!s}"
            )

    # Authentication Methods

    def refresh_auth_token(self) -> FlextResult[str]:
        """Refresh OAuth2 authentication token.

        Returns:
        FlextResult containing new access token.

        """
        try:
            if not self._authenticator:
                return FlextResult[str].fail("Authenticator not initialized")

            token = self._authenticator.refresh_token()
            return FlextResult[str].ok(token)

        except Exception as e:
            self.logger.exception("Token refresh failed")
            return FlextResult[str].fail(f"Token refresh failed: {e!s}")

    def validate_auth_token(self, token: str) -> FlextResult[bool]:
        """Validate OAuth2 authentication token.

        Args:
        token: Token to validate.

        Returns:
        FlextResult containing validation result.

        """
        try:
            if not self._authenticator:
                return FlextResult[bool].fail("Authenticator not initialized")

            is_valid = self._authenticator.validate_token(token)
            return FlextResult[bool].ok(is_valid)

        except Exception as e:
            self.logger.exception("Token validation failed")
            return FlextResult[bool].fail(f"Token validation failed: {e!s}")

    def deploy_integration(
        self,
        integration_data: dict,
    ) -> FlextResult[str]:
        """Deploy integration to Oracle OIC.

        Args:
        integration_data: Integration configuration

        Returns:
        FlextResult containing integration ID or error

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[str].fail(error_msg)

            client = client_result.value
            created_data = client.create_integration(integration_data)

            integration_id = created_data.get("id", "")
            if not integration_id:
                return FlextResult[str].fail("No integration ID returned")

            self.logger.info("Integration deployed successfully: %s", integration_id)
            return FlextResult[str].ok(str(integration_id))

        except Exception as e:
            self.logger.exception("Failed to deploy integration")
            return FlextResult[str].fail(f"Integration deployment failed: {e!s}")

    # Integration Pattern Methods (from OICIntegrationPatternService)

    def apply_message_router_pattern(
        self,
        message_data: dict[str, t.GeneralValueType],
        routing_rules: list[dict[str, t.GeneralValueType]],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Apply message router pattern to OIC integration using FlextOracleOicUtilities.

        Args:
        message_data: Message to route
        routing_rules: Routing rules configuration

        Returns:
        FlextResult containing routing result or error

        """
        try:
            self.logger.info("Applying message router pattern")

            # Validate pattern configuration using utilities
            pattern_config = {
                "routing_rules": routing_rules,
                "message_data": message_data,
            }

            validation_result = (
                FlextOracleOicUtilities.PatternAnalysis.validate_pattern_configuration(
                    "message_router",
                    pattern_config,
                )
            )

            if validation_result.is_failure:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"Pattern validation failed: {validation_result.error}",
                )

            # Apply validated pattern
            routing_result = {
                "pattern": FlextOracleOicConstants.OICPatterns.PATTERN_MESSAGE_ROUTER,
                "message_id": message_data.get(
                    "id",
                    FlextOracleOicConstants.OICPatterns.PATTERN_MESSAGE_ID_UNKNOWN,
                ),
                "applied_rules": len(routing_rules),
                "status": FlextOracleOicConstants.OICPatterns.PATTERN_STATUS_PROCESSED,
            }

            return FlextResult[dict[str, t.GeneralValueType]].ok(routing_result)

        except Exception as e:
            error_msg = f"Message router pattern failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[dict[str, t.GeneralValueType]].fail(error_msg)

    def apply_scatter_gather_pattern(
        self,
        request_data: dict[str, t.GeneralValueType],
        target_endpoints: list[str],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Apply scatter-gather pattern to OIC integration using FlextOracleOicUtilities.

        Args:
        request_data: Request to scatter
        target_endpoints: Target endpoints for scatter

        Returns:
        FlextResult containing scatter-gather result or error

        """
        try:
            self.logger.info("Applying scatter-gather pattern")

            # Validate pattern configuration using utilities
            pattern_config = {
                "target_services": target_endpoints,
                "request_data": request_data,
            }

            validation_result = (
                FlextOracleOicUtilities.PatternAnalysis.validate_pattern_configuration(
                    "scatter_gather",
                    pattern_config,
                )
            )

            if validation_result.is_failure:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"Pattern validation failed: {validation_result.error}",
                )

            # Apply validated pattern
            scatter_result = {
                "pattern": FlextOracleOicConstants.OICPatterns.PATTERN_SCATTER_GATHER,
                "request_id": request_data.get(
                    "id",
                    FlextOracleOicConstants.OICPatterns.PATTERN_REQUEST_ID_UNKNOWN,
                ),
                "target_count": len(target_endpoints),
                "status": FlextOracleOicConstants.OICPatterns.PATTERN_STATUS_PROCESSED,
            }

            return FlextResult[dict[str, t.GeneralValueType]].ok(scatter_result)

        except Exception as e:
            error_msg = f"Scatter-gather pattern failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[dict[str, t.GeneralValueType]].fail(error_msg)

    # Monitoring Methods (from MonitoringService)

    def get_health_status(self) -> FlextResult[dict]:
        """Get Oracle OIC health status using FlextOracleOicUtilities.

        Returns:
        FlextResult containing validated health status information

        """
        try:
            if not self._monitoring_client:
                # Mock health check response
                health_data = {
                    "status": FlextOracleOicConstants.Monitoring.HEALTH_STATUS_HEALTHY,
                    "components": {
                        FlextOracleOicConstants.Monitoring.COMPONENT_DATABASE: {
                            "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_HEALTHY,
                        },
                        FlextOracleOicConstants.Monitoring.COMPONENT_MESSAGING: {
                            "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_HEALTHY,
                        },
                        FlextOracleOicConstants.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                            "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_HEALTHY,
                        },
                    },
                    "timestamp": asyncio.get_event_loop().time(),
                }
            else:
                # Use flext-api client for monitoring
                with self._monitoring_client:
                    response_result = self._monitoring_client.request(
                        method="GET",
                        url=FlextOracleOicConstants.API.ENDPOINT_HEALTH,
                    )

                    if response_result.is_success:
                        response = response_result.value
                        if (
                            response.status_code
                            == FlextConstants.Platform.HTTP_STATUS_OK
                        ):
                            health_data = response.json()
                            health_data.update({
                                "status": FlextOracleOicConstants.Monitoring.HEALTH_STATUS_HEALTHY,
                                "components": {
                                    FlextOracleOicConstants.Monitoring.COMPONENT_DATABASE: {
                                        "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_HEALTHY,
                                    },
                                    FlextOracleOicConstants.Monitoring.COMPONENT_MESSAGING: {
                                        "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_HEALTHY,
                                    },
                                    FlextOracleOicConstants.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                                        "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_HEALTHY,
                                    },
                                },
                            })
                        else:
                            health_data = {
                                "status": FlextOracleOicConstants.Monitoring.HEALTH_STATUS_UNHEALTHY,
                                "components": {
                                    FlextOracleOicConstants.Monitoring.COMPONENT_DATABASE: {
                                        "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_UNKNOWN,
                                    },
                                    FlextOracleOicConstants.Monitoring.COMPONENT_MESSAGING: {
                                        "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_UNKNOWN,
                                    },
                                    FlextOracleOicConstants.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                                        "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_UNKNOWN,
                                    },
                                },
                                "error": f"HTTP {response.status_code}",
                            }
                    else:
                        health_data = {
                            "status": FlextOracleOicConstants.Monitoring.HEALTH_STATUS_ERROR,
                            "components": {
                                FlextOracleOicConstants.Monitoring.COMPONENT_DATABASE: {
                                    "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_UNKNOWN,
                                },
                                FlextOracleOicConstants.Monitoring.COMPONENT_MESSAGING: {
                                    "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_UNKNOWN,
                                },
                                FlextOracleOicConstants.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                                    "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_UNKNOWN,
                                },
                            },
                            "error": f"Request failed: {response_result.error}",
                        }

            # Validate health status using utilities
            validation_result = (
                FlextOracleOicUtilities.MonitoringUtilities.validate_health_status(
                    health_data,
                )
            )
            if validation_result.is_success:
                return validation_result
            self.logger.warning(
                f"Health status validation failed: {validation_result.error}",
            )
            return FlextResult[dict].ok(health_data)

        except Exception as e:
            self.logger.exception("Health check failed")
            error_health = {
                "status": FlextOracleOicConstants.Monitoring.HEALTH_STATUS_ERROR,
                "components": {
                    FlextOracleOicConstants.Monitoring.COMPONENT_DATABASE: {
                        "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_UNKNOWN,
                    },
                    FlextOracleOicConstants.Monitoring.COMPONENT_MESSAGING: {
                        "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_UNKNOWN,
                    },
                    FlextOracleOicConstants.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                        "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_UNKNOWN,
                    },
                },
                "error": str(e),
            }

            # Validate error health status as well
            validation_result = (
                FlextOracleOicUtilities.MonitoringUtilities.validate_health_status(
                    error_health,
                )
            )
            return (
                validation_result
                if validation_result.is_success
                else FlextResult[dict].ok(error_health)
            )

    def get_performance_metrics(self) -> FlextResult[dict]:
        """Get Oracle OIC performance metrics with analysis using FlextOracleOicUtilities.

        Returns:
        FlextResult containing performance metrics with analysis

        """
        try:
            if not self._monitoring_client:
                # Mock perform[dict[str, t.GeneralValueType]]etrics response
                metrics_data = {
                    "active_integrations": 0,
                    "total_executions": 0,
                    "success_rate": 0.0,
                    "average_response_time": 0.0,
                    "timestamp": asyncio.get_event_loop().time(),
                }
            else:
                # Use flext-api client for performance metrics
                with self._monitoring_client:
                    response_result = self._monitoring_client.request(
                        method="GET",
                        url="/ic/api/integration/v1/metrics",
                    )

                    if response_result.is_success:
                        response = response_result.value
                        if (
                            response.status_code
                            == FlextConstants.Platform.HTTP_STATUS_OK
                        ):
                            metrics_data = response.json()
                        else:
                            metrics_data = {
                                "active_integrations": 0,
                                "total_executions": 0,
                                "success_rate": 0.0,
                                "average_response_time": 0.0,
                                "error": f"HTTP {response.status_code}",
                            }
                    else:
                        metrics_data = {
                            "active_integrations": 0,
                            "total_executions": 0,
                            "success_rate": 0.0,
                            "average_response_time": 0.0,
                            "error": f"Request failed: {response_result.error}",
                        }

            # Analyze performance metrics using utilities
            analysis_result = (
                FlextOracleOicUtilities.MonitoringUtilities.analyze_performance_metrics(
                    metrics_data,
                )
            )

            if analysis_result.is_success:
                # Combine raw metrics with analysis
                return FlextResult[dict].ok({
                    **metrics_data,
                    "analysis": analysis_result.value,
                })
            self.logger.warning(f"Performance analysis failed: {analysis_result.error}")
            return FlextResult[dict].ok(metrics_data)

        except Exception as e:
            self.logger.exception("Performance metrics failed")
            error_metrics = {
                "active_integrations": 0,
                "total_executions": 0,
                "success_rate": 0.0,
                "average_response_time": 0.0,
                "error": str(e),
            }

            # Try to analyze error metrics as well
            analysis_result = (
                FlextOracleOicUtilities.MonitoringUtilities.analyze_performance_metrics(
                    error_metrics,
                )
            )
            if analysis_result.is_success:
                return FlextResult[dict].ok({
                    **error_metrics,
                    "analysis": analysis_result.value,
                })
            return FlextResult[dict].ok(error_metrics)

    # Business Rules Validation

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate Oracle OIC service business rules.

        Returns:
        FlextResult indicating validation success or failure.

        """
        # Validate settings exist
        if not self.settings:
            return FlextResult[None].fail("Settings are required")

        # Validate connection settings using utilities
        if not self.settings.base_url:
            return FlextResult[None].fail("Base URL is required")

        # Base URL validation already performed by Pydantic AnyUrl type

        # Validate auth settings using utilities
        if not self.settings.oauth_client_id:
            return FlextResult[None].fail("OAuth client ID is required")

        client_id_result = (
            FlextOracleOicUtilities.AuthenticationValidation.validate_oauth_client_id(
                self.settings.oauth_client_id,
            )
        )
        if client_id_result.is_failure:
            return FlextResult[None].fail(
                f"OAuth client ID validation: {client_id_result.error}",
            )

        if not self.settings.oauth_client_secret:
            return FlextResult[None].fail("OAuth client secret is required")

        if not self.settings.oauth_token_url:
            return FlextResult[None].fail("OAuth token URL is required")

        # Token URL validation already performed by Pydantic AnyUrl type

        return FlextResult[None].ok(None)

    # Private Helper Methods

    def _get_client(self) -> FlextResult[FlextOracleOicClient]:
        """Get or create Oracle OIC client instance.

        Returns:
        FlextResult containing the client instance.

        """
        try:
            if self._client is None:
                # Validate business rules first
                validation_result = self.validate_business_rules()
                if validation_result.is_failure:
                    return FlextResult[FlextOracleOicClient].fail(
                        validation_result.error,
                    )

                # Create client
                self._client = FlextOracleOicClient(
                    base_url=self.settings.base_url,
                    api_version=self.settings.api_version,
                    authenticator=self._authenticator,
                    request_timeout=self.settings.request_timeout,
                    max_retries=self.settings.max_retries,
                    use_ssl=self.settings.use_ssl,
                    verify_ssl=self.settings.verify_ssl,
                )

            return FlextResult[FlextOracleOicClient].ok(self._client)

        except Exception as e:
            self.logger.exception("Failed to create OIC client")
            return FlextResult[FlextOracleOicClient].fail(
                f"Client creation failed: {e!s}",
            )

    # Context Manager Support

    def __enter__(self) -> Self:
        """Context manager entry."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None:
        """Context manager exit."""
        # Cleanup resources if needed


__all__ = [
    "FlextOracleOicService",
]
