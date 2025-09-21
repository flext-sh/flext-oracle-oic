"""Oracle OIC Extension Services - EXTENSION Pattern.

This module establishes the EXTENSION PEP8 pattern for specialized
Oracle OIC services. Serves as model for future extensions.


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import asyncio
from typing import Protocol, Self

from pydantic import ConfigDict, SecretStr

from flext_core import (
    FlextConstants,
    FlextDomainService,
    FlextLogger,
    FlextResult,
    FlextTypes,
)
from flext_oracle_oic_ext.ext_client import (
    OICExtensionAuthenticator,
    OracleOICExtensionClient,
)
from flext_oracle_oic_ext.ext_config import (
    OracleOICExtensionSettings,
)
from flext_oracle_oic_ext.ext_models import (
    IntegrationStatus,
    OICAuthConfig,
    OICConnectionConfig,
    OICConnectionInfo,
    OICIntegrationInfo,
)

logger = FlextLogger(__name__)

# HTTP Status Codes - use FlextConstants for standardization


class HTTPClientProtocol(Protocol):
    """Protocol for HTTP client used by MonitoringService."""

    def get(self, url: str) -> HTTPResponseProtocol: ...


class HTTPResponseProtocol(Protocol):
    """Protocol for HTTP response."""

    status_code: int

    def json(self) -> FlextTypes.Core.Dict: ...


# ================================
# EXTENSION Pattern: Specialized Services
# ================================


class OracleOICExtensionService(FlextDomainService[list[OICIntegrationInfo]]):
    """Main Oracle OIC Extension service.

    FLEXT Compliant: Domain service for Oracle OIC operations
    with complete enterprise functionality following FLEXT patterns.
    """

    # Pydantic model configuration
    model_config = ConfigDict(
        frozen=True,
        validate_assignment=True,
        extra="forbid",
        arbitrary_types_allowed=True,
    )

    # Service-specific fields
    settings: OracleOICExtensionSettings

    def __init__(self, settings: OracleOICExtensionSettings, **data: object) -> None:
        """Initialize OIC extension service.

        Args:
            settings: Extension configuration settings
            **data: Additional initialization data for FlextDomainService

        """
        # Initialize parent FlextDomainService (no parameters needed)
        _ = data  # Use the parameter to avoid unused argument warning
        super().__init__()
        self.logger = FlextLogger(f"{__name__}.{self.__class__.__name__}")
        # Set settings using object.__setattr__ for frozen model
        object.__setattr__(self, "settings", settings)
        # Client is not part of the frozen model - use object.__setattr__
        object.__setattr__(self, "_client", None)

    def execute(self) -> FlextResult[list[OICIntegrationInfo]]:
        """Execute the main domain service operation.

        Returns:
            FlextResult containing list of OIC integrations or error

        """
        # Use asyncio.run to handle async call in sync method
        try:
            return asyncio.run(self.list_integrations())
        except Exception as e:
            return FlextResult[list[OICIntegrationInfo]].fail(f"Execution failed: {e}")

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate Oracle OIC service business rules.

        Returns:
            FlextResult[None]: The validation result

        """
        # Validate settings exist
        if not self.settings:
            return FlextResult[None].fail("Settings are required")

        # Validate connection settings
        if not self.settings.connection.base_url:
            return FlextResult[None].fail("Base URL is required")

        # Validate auth settings
        if not self.settings.auth.oauth_client_id:
            return FlextResult[None].fail("OAuth client ID is required")

        if not self.settings.auth.oauth_client_secret:
            return FlextResult[None].fail("OAuth client secret is required")

        if not self.settings.auth.oauth_token_url:
            return FlextResult[None].fail("OAuth token URL is required")

        return FlextResult[None].ok(None)

    def validate_config(self) -> FlextResult[None]:
        """Validate service configuration.

        Returns:
            FlextResult[None]: The validation result

        """
        return self.validate_business_rules()

    def _get_client(self) -> FlextResult[OracleOICExtensionClient]:
        """Get authenticated OIC client.

        Returns:
            FlextResult containing client or error

        """
        try:
            client = getattr(self, "_client", None)
            if not client:
                # Create auth config from settings
                auth_config = OICAuthConfig(
                    oauth_client_id=self.settings.auth.oauth_client_id,
                    oauth_client_secret=SecretStr(
                        self.settings.auth.oauth_client_secret,
                    ),
                    oauth_token_url=self.settings.auth.oauth_token_url,
                    oauth_client_aud=self.settings.auth.oauth_client_aud,
                    oauth_scope=self.settings.auth.oauth_scope,
                )

                # Create connection config from settings
                connection_config = OICConnectionConfig(
                    base_url=self.settings.connection.base_url,
                    api_version=self.settings.connection.api_version,
                    request_timeout=self.settings.connection.request_timeout,
                    max_retries=self.settings.connection.max_retries,
                    verify_ssl=self.settings.connection.verify_ssl,
                )

                # Create authenticator and client
                authenticator = OICExtensionAuthenticator(auth_config)
                client = OracleOICExtensionClient(
                    connection_config,
                    authenticator,
                )
                # Store client using setattr for frozen model
                setattr(self, "_client", client)

            return FlextResult[OracleOICExtensionClient].ok(client)

        except Exception as e:
            error_msg = f"Failed to create OIC client: {e}"
            self.logger.exception(error_msg)
            return FlextResult[OracleOICExtensionClient].fail(error_msg)

    async def list_integrations(
        self,
        status_filter: FlextTypes.Core.StringList | None = None,
    ) -> FlextResult[list[OICIntegrationInfo]]:
        """List Oracle OIC integrations.

        Args:
            status_filter: Filter by integration status

        Returns:
            FlextResult containing integration info list or error

        """
        try:
            client_result = self._get_client()
            if not client_result.success:
                return FlextResult[list[OICIntegrationInfo]].fail(
                    client_result.error or "Client creation failed",
                )

            client = client_result.data
            if client is None:
                return FlextResult[list[OICIntegrationInfo]].fail("No client available")

            # Get integrations from OIC
            integrations_result = await client.get_integrations(
                status_filter=status_filter,
                page_size=100,
            )

            if not integrations_result.success:
                return FlextResult[list[OICIntegrationInfo]].fail(
                    integrations_result.error or "Failed to fetch integrations",
                )

            integrations_data = integrations_result.data or []

            # Convert to domain models
            integration_infos = []
            for integration in integrations_data:
                try:
                    integration_info = OICIntegrationInfo(
                        integration_id=str(integration.get("id", "")),
                        name=str(integration.get("name", "")),
                        status=str(integration.get("status", "")),
                        version=str(integration.get("version", "")),
                        description=str(integration.get("description", "")),
                        created_by=str(integration.get("createdBy", "")),
                        last_updated=str(integration.get("lastUpdated", "")),
                    )
                    integration_infos.append(integration_info)
                except Exception as e:
                    self.logger.warning(f"Failed to parse integration: {e}")
                    continue

            self.logger.info(f"Retrieved {len(integration_infos)} integrations")
            return FlextResult[list[OICIntegrationInfo]].ok(integration_infos)

        except Exception as e:
            error_msg = f"Failed to list integrations: {e}"
            self.logger.exception(error_msg)
            return FlextResult[list[OICIntegrationInfo]].fail(error_msg)

    async def list_connections(
        self,
        type_filter: FlextTypes.Core.StringList | None = None,
    ) -> FlextResult[list[OICConnectionInfo]]:
        """List Oracle OIC connections.

        Args:
            type_filter: Filter by connection type

        Returns:
            FlextResult containing connection info list or error

        """
        try:
            client_result = self._get_client()
            if not client_result.success:
                return FlextResult[list[OICConnectionInfo]].fail(
                    client_result.error or "Client creation failed",
                )

            client = client_result.data
            if client is None:
                return FlextResult[list[OICConnectionInfo]].fail("No client available")

            # Get connections from OIC
            connections_result = await client.get_connections(
                type_filter=type_filter,
                page_size=100,
            )

            if not connections_result.success:
                return FlextResult[list[OICConnectionInfo]].fail(
                    connections_result.error or "Connections fetch failed",
                )

            connections_data = connections_result.data or []

            # Convert to domain models
            connection_infos = []
            for connection in connections_data:
                try:
                    connection_info = OICConnectionInfo(
                        connection_id=str(connection.get("id", "")),
                        name=str(connection.get("name", "")),
                        adapter_type=str(connection.get("adapterType", "")),
                        status=str(connection.get("status", "")),
                        connection_type=str(connection.get("connectionType", "")),
                        description=str(connection.get("description", "")),
                    )
                    connection_infos.append(connection_info)
                except Exception as e:
                    self.logger.warning(f"Failed to parse connection: {e}")
                    continue

            self.logger.info(f"Retrieved {len(connection_infos)} connections")
            return FlextResult[list[OICConnectionInfo]].ok(connection_infos)

        except Exception as e:
            error_msg = f"Failed to list connections: {e}"
            self.logger.exception(error_msg)
            return FlextResult[list[OICConnectionInfo]].fail(error_msg)

    async def test_connection(self) -> FlextResult[bool]:
        """Test connection to Oracle OIC.

        Returns:
            FlextResult containing connection status or error

        """
        try:
            client_result = self._get_client()
            if not client_result.success:
                return FlextResult[bool].fail(
                    client_result.error or "Client creation failed",
                )

            client = client_result.data
            if client is None:
                return FlextResult[bool].fail("No client available")

            # Try to get integrations as connection test
            integrations_result = await client.get_integrations(page_size=1)

            if integrations_result.success:
                self.logger.info("OIC connection test successful")
                return FlextResult[bool].ok(data=True)
            error_msg = f"OIC connection test failed: {integrations_result.error}"
            self.logger.error(error_msg)
            return FlextResult[bool].fail(error_msg)

        except Exception as e:
            error_msg = f"Connection test error: {e}"
            self.logger.exception(error_msg)
            return FlextResult[bool].fail(error_msg)

    async def deploy_integration(
        self,
        integration_data: FlextTypes.Core.Dict,
    ) -> FlextResult[str]:
        """Deploy integration to Oracle OIC.

        Args:
            integration_data: Integration configuration

        Returns:
            FlextResult containing integration ID or error

        """
        try:
            client_result = self._get_client()
            if not client_result.success:
                return FlextResult[str].fail(
                    client_result.error or "Client creation failed",
                )

            client = client_result.data
            if client is None:
                return FlextResult[str].fail("No client available")

            # Create integration - cast to expected type
            integration_data_str = {k: str(v) for k, v in integration_data.items()}
            create_result = await client.create_integration(integration_data_str)

            if not create_result.success:
                return FlextResult[str].fail(
                    create_result.error or "Create integration failed",
                )

            created_integration = create_result.data
            if not created_integration:
                return FlextResult[str].fail("No integration data returned")

            integration_id = created_integration.get("id", "")
            if not integration_id:
                return FlextResult[str].fail("No integration ID returned")

            self.logger.info(f"Integration deployed successfully: {integration_id}")
            return FlextResult[str].ok(str(integration_id))

        except Exception as e:
            error_msg = f"Failed to deploy integration: {e}"
            self.logger.exception(error_msg)
            return FlextResult[str].fail(error_msg)

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
        client = getattr(self, "_client", None)
        if client:
            client.__exit__(exc_type, exc_val, exc_tb)
            object.__setattr__(self, "_client", None)


class OICIntegrationPatternService:
    """Oracle OIC Integration Pattern service.

    Padrão EXTENSION: Serviço para padrões enterprise de integração
    Oracle OIC como Message Router, Scatter-Gather, etc.
    """

    def __init__(self, oic_service: OracleOICExtensionService) -> None:
        """Initialize OIC pattern service.

        Args:
            oic_service: Main OIC extension service

        Returns:
            object: Description of return value.

        """
        self.oic_service = oic_service
        self.logger = FlextLogger(f"{__name__}.{self.__class__.__name__}")

    def apply_message_router_pattern(
        self,
        message_data: FlextTypes.Core.Dict,
        routing_rules: list[FlextTypes.Core.Dict],
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Apply message router pattern to OIC integration.

        Args:
            message_data: Message to route
            routing_rules: Routing rules configuration

        Returns:
            FlextResult containing routing result or error

        """
        try:
            self.logger.info("Applying message router pattern")

            # Placeholder implementation - will be enhanced in future iterations
            routing_result = {
                "pattern": "message_router",
                "message_id": message_data.get("id", "unknown"),
                "applied_rules": len(routing_rules),
                "status": "processed",
            }

            return FlextResult[FlextTypes.Core.Dict].ok(routing_result)

        except Exception as e:
            error_msg = f"Message router pattern failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextTypes.Core.Dict].fail(error_msg)

    def apply_scatter_gather_pattern(
        self,
        request_data: FlextTypes.Core.Dict,
        target_endpoints: FlextTypes.Core.StringList,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Apply scatter-gather pattern to OIC integration.

        Args:
            request_data: Request to scatter
            target_endpoints: Target endpoints for scatter

        Returns:
            FlextResult containing scatter-gather result or error

        """
        try:
            self.logger.info("Applying scatter-gather pattern")

            # Placeholder implementation - will be enhanced in future iterations
            scatter_result = {
                "pattern": "scatter_gather",
                "request_id": request_data.get("id", "unknown"),
                "target_count": len(target_endpoints),
                "status": "processed",
            }

            return FlextResult[FlextTypes.Core.Dict].ok(scatter_result)

        except Exception as e:
            error_msg = f"Scatter-gather pattern failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextTypes.Core.Dict].fail(error_msg)


class LifecycleManager:
    """Oracle OIC Integration Lifecycle Manager.

    Padrão EXTENSION: Gerenciador de ciclo de vida de integrações
    Oracle OIC com operações de ativação, desativação e monitoramento.
    """

    def __init__(self, settings: OracleOICExtensionSettings) -> None:
        """Initialize lifecycle manager.

        Args:
            settings: Extension configuration settings

        """
        self.settings = settings
        self.logger = FlextLogger(f"{__name__}.{self.__class__.__name__}")
        self._client: OracleOICExtensionClient | None = None

    def _get_client(self) -> FlextResult[OracleOICExtensionClient]:
        """Get authenticated OIC client."""
        try:
            if not self._client:
                # Create auth config from settings
                auth_config = OICAuthConfig(
                    oauth_client_id=self.settings.auth.oauth_client_id,
                    oauth_client_secret=SecretStr(
                        self.settings.auth.oauth_client_secret,
                    ),
                    oauth_token_url=self.settings.auth.oauth_token_url,
                    oauth_client_aud=self.settings.auth.oauth_client_aud,
                    oauth_scope=self.settings.auth.oauth_scope,
                )

                # Create connection config from settings
                connection_config = OICConnectionConfig(
                    base_url=self.settings.connection.base_url,
                    api_version=self.settings.connection.api_version,
                    request_timeout=self.settings.connection.request_timeout,
                    max_retries=self.settings.connection.max_retries,
                    verify_ssl=self.settings.connection.verify_ssl,
                )

                # Create authenticator and client
                authenticator = OICExtensionAuthenticator(auth_config)
                self._client = OracleOICExtensionClient(
                    connection_config,
                    authenticator,
                )

            return FlextResult[OracleOICExtensionClient].ok(self._client)

        except Exception as e:
            error_msg = f"Failed to create OIC client: {e}"
            self.logger.exception(error_msg)
            return FlextResult[OracleOICExtensionClient].fail(error_msg)

    async def activate_integration(
        self,
        integration_id: str,
    ) -> FlextResult[IntegrationStatus]:
        """Activate an Oracle OIC integration.

        Args:
            integration_id: Integration identifier

        Returns:
            FlextResult containing integration status or error

        """
        try:
            client_result = self._get_client()
            if not client_result.success:
                return FlextResult[IntegrationStatus].fail(
                    client_result.error or "Client creation failed",
                )

            client = client_result.data
            if client is None:
                return FlextResult[IntegrationStatus].fail("No client available")

            # Update integration to activate it
            activation_data: FlextTypes.Core.Dict = {"status": "ACTIVATED"}
            activate_result = await client.update_integration(
                integration_id, activation_data
            )

            if not activate_result.success:
                return FlextResult[IntegrationStatus].fail(
                    activate_result.error or "Activation failed",
                )

            # Create status object
            status = IntegrationStatus(
                integration_id=integration_id,
                version="01.00.0000",  # Default version
                status="ACTIVATED",
                last_updated="",
                activated_by="system",
            )

            self.logger.info(f"Integration {integration_id} activated successfully")
            return FlextResult[IntegrationStatus].ok(status)

        except Exception as e:
            error_msg = f"Failed to activate integration {integration_id}: {e}"
            self.logger.exception(error_msg)
            return FlextResult[IntegrationStatus].fail(error_msg)

    async def deactivate_integration(
        self,
        integration_id: str,
    ) -> FlextResult[IntegrationStatus]:
        """Deactivate an Oracle OIC integration.

        Args:
            integration_id: Integration identifier

        Returns:
            FlextResult containing integration status or error

        """
        try:
            client_result = self._get_client()
            if not client_result.success:
                return FlextResult[IntegrationStatus].fail(
                    client_result.error or "Client creation failed",
                )

            client = client_result.data
            if client is None:
                return FlextResult[IntegrationStatus].fail("No client available")

            # Update integration to deactivate it
            deactivation_data: FlextTypes.Core.Dict = {"status": "DEACTIVATED"}
            deactivate_result = await client.update_integration(
                integration_id,
                deactivation_data,
            )

            if not deactivate_result.success:
                return FlextResult[IntegrationStatus].fail(
                    deactivate_result.error or "Deactivation failed",
                )

            # Create status object
            status = IntegrationStatus(
                integration_id=integration_id,
                version="01.00.0000",  # Default version
                status="DEACTIVATED",
                last_updated="",
                activated_by="system",
            )

            self.logger.info(f"Integration {integration_id} deactivated successfully")
            return FlextResult[IntegrationStatus].ok(status)

        except Exception as e:
            error_msg = f"Failed to deactivate integration {integration_id}: {e}"
            self.logger.exception(error_msg)
            return FlextResult[IntegrationStatus].fail(error_msg)


class MonitoringService:
    """Oracle OIC Monitoring Service.

    Padrão EXTENSION: Serviço de monitoramento Oracle OIC
    com verificações de saúde e métricas de performance.
    """

    def __init__(self, client: HTTPClientProtocol) -> None:
        """Initialize monitoring service.

        Args:
            client: HTTP client (requests.Session or mock)

        """
        self.client = client
        self.logger = FlextLogger(f"{__name__}.{self.__class__.__name__}")

    def get_health_status(self) -> FlextTypes.Core.Dict:
        """Get Oracle OIC health status.

        Returns:
            Dictionary containing health status information

        """
        try:
            # Mock health check response
            response = self.client.get("/ic/api/integration/v1/health")

            if response.status_code == FlextConstants.Platform.HTTP_STATUS_OK:
                health_data = response.json()
                return {
                    "status": "healthy",
                    "components": {
                        "database": "healthy",
                        "messaging": "healthy",
                        "integration_engine": "healthy",
                    },
                    "timestamp": health_data.get("timestamp", ""),
                }
            return {
                "status": "unhealthy",
                "components": {
                    "database": "unknown",
                    "messaging": "unknown",
                    "integration_engine": "unknown",
                },
                "error": f"HTTP {response.status_code}",
            }

        except Exception as e:
            self.logger.exception("Health check failed")
            return {
                "status": "error",
                "components": {
                    "database": "unknown",
                    "messaging": "unknown",
                    "integration_engine": "unknown",
                },
                "error": str(e),
            }

    def get_performance_metrics(self) -> FlextTypes.Core.Dict:
        """Get Oracle OIC performance metrics.

        Returns:
            Dictionary containing performance metrics

        """
        try:
            # Mock performance metrics response
            response = self.client.get("/ic/api/integration/v1/metrics")

            if response.status_code == FlextConstants.Platform.HTTP_STATUS_OK:
                metrics_data = response.json()
                return {
                    "active_integrations": metrics_data.get("active_integrations", 0),
                    "total_executions": metrics_data.get("total_executions", 0),
                    "success_rate": metrics_data.get("success_rate", 0.0),
                    "average_response_time": metrics_data.get("avg_response_time", 0.0),
                    "timestamp": metrics_data.get("timestamp", ""),
                }
            return {
                "active_integrations": 0,
                "total_executions": 0,
                "success_rate": 0.0,
                "average_response_time": 0.0,
                "error": f"HTTP {response.status_code}",
            }

        except Exception as e:
            self.logger.exception("Performance metrics failed")
            return {
                "active_integrations": 0,
                "total_executions": 0,
                "success_rate": 0.0,
                "average_response_time": 0.0,
                "error": str(e),
            }


# Exports following EXTENSION pattern
__all__: FlextTypes.Core.StringList = [
    "LifecycleManager",
    "MonitoringService",
    "OICIntegrationPatternService",
    # Main services
    "OracleOICExtensionService",
]
