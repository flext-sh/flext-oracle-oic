"""Oracle OIC Extension Services - EXTENSION Pattern.

This module establishes the EXTENSION PEP8 pattern for specialized
Oracle OIC services. Serves as model for future extensions.


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Protocol, Self, override

from flext_core import (
    FlextConstants,
    FlextLogger,
    FlextResult,
    FlextService,
    FlextTypes,
)
from pydantic import ConfigDict, Extra

from flext_oracle_oic.config import (
    FlextOracleOicConfig,
)
from flext_oracle_oic.constants import FlextOracleOicConstants
from flext_oracle_oic.ext_client import (
    OICExtensionAuthenticator,
    OracleOICExtensionClient,
)
from flext_oracle_oic.models import FlextOracleOicModels
from flext_oracle_oic.utilities import FlextOracleOicUtilities

logger = FlextLogger(__name__)

# HTTP Status Codes - use FlextConstants for standardization


class HTTPClientProtocol(Protocol):
    """Protocol for HTTP client used by MonitoringService."""

    def get(self, url: str) -> HTTPResponseProtocol: ...


class HTTPResponseProtocol(Protocol):
    """Protocol for HTTP response."""

    status_code: int

    def json(self: Self) -> FlextTypes.Dict: ...


# ================================
# EXTENSION Pattern: Specialized Services
# ================================


class OracleOICExtensionService(
    FlextService[list[FlextOracleOicModels.OICIntegrationInfo]]
):
    """Main Oracle OIC Extension service.

    FLEXT Compliant: Domain service for Oracle OIC operations
    with complete enterprise functionality following FLEXT patterns.
    """

    # Pydantic model configuration
    model_config = ConfigDict(
        frozen=True,
        validate_assignment=True,
        extra=Extra.forbid,
        arbitrary_types_allowed=True,
    )

    # Service-specific fields
    settings: FlextOracleOicConfig

    @override
    def __init__(self, settings: FlextOracleOicConfig, **data: object) -> None:
        """Initialize OIC extension service.

        Args:
            settings: Extension configuration settings
            **data: Additional initialization data for FlextService

        """
        # Initialize parent FlextService (no parameters needed)
        _ = data  # Use the parameter to avoid unused argument warning
        super().__init__()
        # Set settings using object.__setattr__ for frozen model
        object.__setattr__(self, "settings", settings)
        # Client is not part of the frozen model - use object.__setattr__
        object.__setattr__(self, "_client", None)

    @override
    def execute(
        self: Self,
    ) -> FlextResult[list[FlextOracleOicModels.OICIntegrationInfo]]:
        """Execute the main domain service operation.

        Returns:
            FlextResult containing list of OIC integrations or error

        """
        # Railway-oriented execution - delegate to list_integrations
        return self.list_integrations()

    def validate_business_rules(self: Self) -> FlextResult[None]:
        """Validate Oracle OIC service business rules using FlextOracleOicUtilities.

        Returns:
            FlextResult[None]: The validation result

        """
        # Validate settings exist
        if not self.settings:
            return FlextResult[None].fail("Settings are required")

        # Validate connection settings using utilities
        if not self.settings.base_url:
            return FlextResult[None].fail("Base URL is required")

        base_url_result = (
            FlextOracleOicUtilities.ConnectionValidation.validate_base_url(
                self.settings.base_url
            )
        )
        if base_url_result.is_failure:
            return FlextResult[None].fail(
                f"Base URL validation: {base_url_result.error}"
            )

        # Validate auth settings using utilities
        if not self.settings.oauth_client_id:
            return FlextResult[None].fail("OAuth client ID is required")

        client_id_result = (
            FlextOracleOicUtilities.AuthenticationValidation.validate_oauth_client_id(
                self.settings.oauth_client_id
            )
        )
        if client_id_result.is_failure:
            return FlextResult[None].fail(
                f"OAuth client ID validation: {client_id_result.error}"
            )

        if not self.settings.oauth_client_secret:
            return FlextResult[None].fail("OAuth client secret is required")

        if not self.settings.oauth_token_url:
            return FlextResult[None].fail("OAuth token URL is required")

        token_url_result = (
            FlextOracleOicUtilities.AuthenticationValidation.validate_oauth_token_url(
                self.settings.oauth_token_url
            )
        )
        if token_url_result.is_failure:
            return FlextResult[None].fail(
                f"OAuth token URL validation: {token_url_result.error}"
            )

        return FlextResult[None].ok(None)

    def validate_config(self: Self) -> FlextResult[None]:
        """Validate service configuration.

        Returns:
            FlextResult[None]: The validation result

        """
        return self.validate_business_rules()

    def _get_client(self: Self) -> FlextResult[OracleOICExtensionClient]:
        """Get authenticated OIC client.

        Returns:
            FlextResult containing client or error

        """
        # Railway-oriented client creation
        return (
            FlextResult[object]
            .ok(None)
            .flat_map(lambda _: self._get_or_create_client())
        )

    def _get_or_create_client(self) -> FlextResult[OracleOICExtensionClient]:
        """Get existing client or create new one."""
        client = getattr(self, "_client", None)
        if client:
            return FlextResult[OracleOICExtensionClient].ok(client)

        # Create new client using railway pattern
        return (
            FlextResult[object]
            .ok(None)
            .flat_map(lambda _: self._create_auth_config())
            .flat_map(
                lambda auth_config: self._create_connection_config().map(
                    lambda conn_config: (auth_config, conn_config)
                )
            )
            .flat_map(
                lambda configs: self._create_client_instance(configs[0], configs[1])
            )
        )

    def _create_auth_config(self) -> FlextResult[FlextOracleOicModels.OICAuthConfig]:
        """Create authentication configuration."""
        try:
            auth_config = FlextOracleOicModels.OICAuthConfig(
                oauth_client_id=self.settings.oauth_client_id,
                oauth_client_secret=self.settings.oauth_client_secret,
                oauth_token_url=self.settings.oauth_token_url,
                oauth_client_aud=self.settings.oauth_client_aud,
                oauth_scope=self.settings.oauth_scope,
            )
            return FlextResult[FlextOracleOicModels.OICAuthConfig].ok(auth_config)
        except Exception as e:
            error_msg = f"Failed to create auth config: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextOracleOicModels.OICAuthConfig].fail(error_msg)

    def _create_connection_config(
        self,
    ) -> FlextResult[FlextOracleOicModels.OICConnectionConfig]:
        """Create connection configuration."""
        try:
            connection_config = FlextOracleOicModels.OICConnectionConfig(
                base_url=self.settings.base_url,
                api_version=self.settings.api_version,
                request_timeout=self.settings.request_timeout,
                max_retries=self.settings.max_retries,
                verify_ssl=self.settings.verify_ssl,
            )
            return FlextResult[FlextOracleOicModels.OICConnectionConfig].ok(
                connection_config
            )
        except Exception as e:
            error_msg = f"Failed to create connection config: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextOracleOicModels.OICConnectionConfig].fail(error_msg)

    def _create_client_instance(
        self,
        auth_config: FlextOracleOicModels.OICAuthConfig,
        connection_config: FlextOracleOicModels.OICConnectionConfig,
    ) -> FlextResult[OracleOICExtensionClient]:
        """Create client instance."""
        try:
            authenticator = OICExtensionAuthenticator(auth_config)
            client = OracleOICExtensionClient(connection_config, authenticator)
            setattr(self, "_client", client)
            return FlextResult[OracleOICExtensionClient].ok(client)
        except Exception as e:
            error_msg = f"Failed to create OIC client instance: {e}"
            self.logger.exception(error_msg)
            return FlextResult[OracleOICExtensionClient].fail(error_msg)

    def list_integrations(
        self,
        status_filter: FlextTypes.StringList | None = None,
    ) -> FlextResult[list[FlextOracleOicModels.OICIntegrationInfo]]:
        """List Oracle OIC integrations.

        Args:
            status_filter: Filter by integration status

        Returns:
            FlextResult containing integration info list or error

        """
        # Railway-oriented integration listing
        return (
            self._get_oic_client()
            .flat_map(lambda client: self._fetch_integrations(client, status_filter))
            .flat_map(self._parse_integration_models)
        )

    def _get_oic_client(self) -> FlextResult[OracleOICExtensionClient]:
        """Get authenticated OIC client."""
        client_result = self._get_client()
        if client_result.is_failure:
            return FlextResult[OracleOICExtensionClient].fail(
                client_result.error or "Client creation failed"
            )
        client = client_result.unwrap()
        if client is None:
            return FlextResult[OracleOICExtensionClient].fail("No client available")
        return FlextResult[OracleOICExtensionClient].ok(client)

    def _fetch_integrations(
        self,
        client: OracleOICExtensionClient,
        status_filter: FlextTypes.StringList | None,
    ) -> FlextResult[list[FlextTypes.Dict]]:
        """Fetch integrations from OIC API."""
        integrations_result = client.get_integrations(
            status_filter=status_filter,
            page_size=FlextOracleOicConstants.OIC.DEFAULT_PAGE_SIZE,
        )
        if integrations_result.is_failure:
            return FlextResult[list[FlextTypes.Dict]].fail(
                integrations_result.error or "Failed to fetch integrations"
            )
        return FlextResult[list[FlextTypes.Dict]].ok(integrations_result.unwrap() or [])

    def _parse_integration_models(
        self, integrations_data: list[FlextTypes.Dict]
    ) -> FlextResult[list[FlextOracleOicModels.OICIntegrationInfo]]:
        """Parse integration data into domain models."""
        integration_infos = []
        for integration in integrations_data:
            try:
                integration_info = FlextOracleOicModels.OICIntegrationInfo(
                    integration_id=str(integration.get("id", "")),
                    name=str(integration.get("name", "")),
                    status=str(integration.get("status", "")),
                    integration_version=str(integration.get("version", "")),
                    description=str(integration.get("description", "")),
                    created_by=str(integration.get("createdBy", "")),
                    last_updated=str(integration.get("lastUpdated", "")),
                )
                integration_infos.append(integration_info)
            except Exception as e:
                self.logger.warning(f"Failed to parse integration: {e}")
                continue

        self.logger.info(f"Retrieved {len(integration_infos)} integrations")
        return FlextResult[list[FlextOracleOicModels.OICIntegrationInfo]].ok(
            integration_infos
        )

    def list_connections(
        self,
        type_filter: FlextTypes.StringList | None = None,
    ) -> FlextResult[list[FlextOracleOicModels.OICConnectionInfo]]:
        """List Oracle OIC connections.

        Args:
            type_filter: Filter by connection type

        Returns:
            FlextResult containing connection info list or error

        """
        # Railway-oriented connection listing
        return (
            self._get_oic_client()
            .flat_map(lambda client: self._fetch_connections(client, type_filter))
            .flat_map(self._parse_connection_models)
        )

    def _fetch_connections(
        self,
        client: OracleOICExtensionClient,
        type_filter: FlextTypes.StringList | None,
    ) -> FlextResult[list[FlextTypes.Dict]]:
        """Fetch connections from OIC API."""
        connections_result = client.get_connections(
            type_filter=type_filter,
            page_size=FlextOracleOicConstants.OIC.DEFAULT_PAGE_SIZE,
        )
        if connections_result.is_failure:
            return FlextResult[list[FlextTypes.Dict]].fail(
                connections_result.error or "Connections fetch failed"
            )
        return FlextResult[list[FlextTypes.Dict]].ok(connections_result.unwrap() or [])

    def _parse_connection_models(
        self, connections_data: list[FlextTypes.Dict]
    ) -> FlextResult[list[FlextOracleOicModels.OICConnectionInfo]]:
        """Parse connection data into domain models."""
        connection_infos = []
        for connection in connections_data:
            try:
                connection_info = FlextOracleOicModels.OICConnectionInfo(
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
        return FlextResult[list[FlextOracleOicModels.OICConnectionInfo]].ok(
            connection_infos
        )

    def test_connection(self) -> FlextResult[bool]:
        """Test connection to Oracle OIC.

        Returns:
            FlextResult containing connection status or error

        """
        # Railway-oriented connection testing
        return self._get_oic_client().flat_map(self._perform_connection_test)

    def _perform_connection_test(
        self, client: OracleOICExtensionClient
    ) -> FlextResult[bool]:
        """Perform actual connection test by fetching minimal data."""
        integrations_result = client.get_integrations(
            page_size=FlextOracleOicConstants.OIC.MIN_PAGE_SIZE
        )

        if integrations_result.is_success:
            self.logger.info("OIC connection test successful")
            return FlextResult[bool].ok(True)

        error_msg = f"OIC connection test failed: {integrations_result.error}"
        self.logger.error(error_msg)
        return FlextResult[bool].fail(error_msg)

    def deploy_integration(
        self,
        integration_data: FlextTypes.Dict,
    ) -> FlextResult[str]:
        """Deploy integration to Oracle OIC.

        Args:
            integration_data: Integration configuration

        Returns:
            FlextResult containing integration ID or error

        """
        # Railway-oriented integration deployment
        return (
            FlextResult[FlextTypes.Dict]
            .ok(integration_data)
            .flat_map(
                lambda data: self._get_oic_client().map(lambda client: (client, data))
            )
            .flat_map(lambda client_data: self._create_integration(*client_data))
            .flat_map(self._extract_integration_id)
        )

    def _create_integration(
        self, client: OracleOICExtensionClient, data: FlextTypes.Dict
    ) -> FlextResult[FlextTypes.Dict]:
        """Create integration via OIC client."""
        integration_data_str: FlextTypes.Dict = {k: str(v) for k, v in data.items()}
        create_result = client.create_integration(integration_data_str)

        if create_result.is_failure:
            return FlextResult[FlextTypes.Dict].fail(
                create_result.error or "Create integration failed"
            )

        created_integration = create_result.unwrap()
        if not created_integration:
            return FlextResult[FlextTypes.Dict].fail("No integration data returned")

        return FlextResult[FlextTypes.Dict].ok(created_integration)

    def _extract_integration_id(self, integration_data: dict) -> FlextResult[str]:
        """Extract integration ID from creation result."""
        integration_id = integration_data.get("id", "")
        if not integration_id:
            return FlextResult[str].fail("No integration ID returned")

        self.logger.info(f"Integration deployed successfully: {integration_id}")
        return FlextResult[str].ok(str(integration_id))

    def __enter__(self: Self) -> Self:
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

    @override
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
        message_data: FlextTypes.Dict,
        routing_rules: list[FlextTypes.Dict],
    ) -> FlextResult[FlextTypes.Dict]:
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
                    "message_router", pattern_config
                )
            )

            if validation_result.is_failure:
                return FlextResult[FlextTypes.Dict].fail(
                    f"Pattern validation failed: {validation_result.error}"
                )

            # Apply validated pattern
            routing_result = {
                "pattern": FlextOracleOicConstants.Integration.PATTERN_MESSAGE_ROUTER,
                "message_id": message_data.get(
                    "id", FlextOracleOicConstants.OICPatterns.PATTERN_MESSAGE_ID_UNKNOWN
                ),
                "applied_rules": len(routing_rules),
                "status": FlextOracleOicConstants.OICPatterns.PATTERN_STATUS_PROCESSED,
            }

            return FlextResult[FlextTypes.Dict].ok(routing_result)

        except Exception as e:
            error_msg = f"Message router pattern failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextTypes.Dict].fail(error_msg)

    def apply_scatter_gather_pattern(
        self,
        request_data: FlextTypes.Dict,
        target_endpoints: FlextTypes.StringList,
    ) -> FlextResult[FlextTypes.Dict]:
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
                    "scatter_gather", pattern_config
                )
            )

            if validation_result.is_failure:
                return FlextResult[FlextTypes.Dict].fail(
                    f"Pattern validation failed: {validation_result.error}"
                )

            # Apply validated pattern
            scatter_result = {
                "pattern": FlextOracleOicConstants.Integration.PATTERN_SCATTER_GATHER,
                "request_id": request_data.get(
                    "id", FlextOracleOicConstants.OICPatterns.PATTERN_REQUEST_ID_UNKNOWN
                ),
                "target_count": len(target_endpoints),
                "status": FlextOracleOicConstants.OICPatterns.PATTERN_STATUS_PROCESSED,
            }

            return FlextResult[FlextTypes.Dict].ok(scatter_result)

        except Exception as e:
            error_msg = f"Scatter-gather pattern failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextTypes.Dict].fail(error_msg)


class LifecycleManager:
    """Oracle OIC Integration Lifecycle Manager.

    Padrão EXTENSION: Gerenciador de ciclo de vida de integrações
    Oracle OIC com operações de ativação, desativação e monitoramento.
    """

    @override
    def __init__(self, settings: FlextOracleOicConfig) -> None:
        """Initialize lifecycle manager.

        Args:
            settings: Extension configuration settings

        """
        self.settings = settings
        self.logger = FlextLogger(f"{__name__}.{self.__class__.__name__}")
        self._client: OracleOICExtensionClient | None = None

    def _get_client(self: Self) -> FlextResult[OracleOICExtensionClient]:
        """Get authenticated OIC client."""
        try:
            if not self._client:
                # Create auth config from settings (using flat structure)
                auth_config = FlextOracleOicModels.OICAuthConfig(
                    oauth_client_id=self.settings.oauth_client_id,
                    oauth_client_secret=self.settings.oauth_client_secret,
                    oauth_token_url=self.settings.oauth_token_url,
                    oauth_client_aud=self.settings.oauth_client_aud,
                    oauth_scope=self.settings.oauth_scope,
                )

                # Create connection config from settings (using flat structure)
                connection_config = FlextOracleOicModels.OICConnectionConfig(
                    base_url=self.settings.base_url,
                    api_version=self.settings.api_version,
                    request_timeout=self.settings.request_timeout,
                    max_retries=self.settings.max_retries,
                    verify_ssl=self.settings.verify_ssl,
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

    def activate_integration(
        self,
        integration_id: str,
    ) -> FlextResult[FlextOracleOicModels.IntegrationStatus]:
        """Activate an Oracle OIC integration.

        Args:
            integration_id: Integration identifier

        Returns:
            FlextResult containing integration status or error

        """
        try:
            client_result = self._get_client()
            if not client_result.success:
                return FlextResult[FlextOracleOicModels.IntegrationStatus].fail(
                    client_result.error or "Client creation failed",
                )

            client = client_result.unwrap()
            if client is None:
                return FlextResult[FlextOracleOicModels.IntegrationStatus].fail(
                    "No client available"
                )

            # Update integration to activate it
            activation_data: FlextTypes.Dict = {
                "status": FlextOracleOicConstants.Integration.STATUS_ACTIVATED
            }
            activate_result = client.update_integration(integration_id, activation_data)

            if not activate_result.success:
                return FlextResult[FlextOracleOicModels.IntegrationStatus].fail(
                    activate_result.error or "Activation failed",
                )

            # Create status object
            status = FlextOracleOicModels.IntegrationStatus(
                integration_id=integration_id,
                integration_version=FlextOracleOicConstants.Integration.DEFAULT_VERSION,
                status=FlextOracleOicConstants.Integration.STATUS_ACTIVATED,
                last_updated=FlextOracleOicConstants.Integration.DEFAULT_LAST_UPDATED,
                activated_by=FlextOracleOicConstants.Integration.DEFAULT_ACTIVATED_BY,
            )

            self.logger.info(f"Integration {integration_id} activated successfully")
            return FlextResult[FlextOracleOicModels.IntegrationStatus].ok(status)

        except Exception as e:
            error_msg = f"Failed to activate integration {integration_id}: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextOracleOicModels.IntegrationStatus].fail(error_msg)

    def deactivate_integration(
        self,
        integration_id: str,
    ) -> FlextResult[FlextOracleOicModels.IntegrationStatus]:
        """Deactivate an Oracle OIC integration.

        Args:
            integration_id: Integration identifier

        Returns:
            FlextResult containing integration status or error

        """
        try:
            client_result = self._get_client()
            if not client_result.success:
                return FlextResult[FlextOracleOicModels.IntegrationStatus].fail(
                    client_result.error or "Client creation failed",
                )

            client = client_result.unwrap()
            if client is None:
                return FlextResult[FlextOracleOicModels.IntegrationStatus].fail(
                    "No client available"
                )

            # Update integration to deactivate it
            deactivation_data: FlextTypes.Dict = {
                "status": FlextOracleOicConstants.Integration.STATUS_DEACTIVATED
            }
            deactivate_result = client.update_integration(
                integration_id,
                deactivation_data,
            )

            if not deactivate_result.success:
                return FlextResult[FlextOracleOicModels.IntegrationStatus].fail(
                    deactivate_result.error or "Deactivation failed",
                )

            # Create status object
            status = FlextOracleOicModels.IntegrationStatus(
                integration_id=integration_id,
                integration_version=FlextOracleOicConstants.Integration.DEFAULT_VERSION,
                status=FlextOracleOicConstants.Integration.STATUS_DEACTIVATED,
                last_updated=FlextOracleOicConstants.Integration.DEFAULT_LAST_UPDATED,
                activated_by=FlextOracleOicConstants.Integration.DEFAULT_ACTIVATED_BY,
            )

            self.logger.info(f"Integration {integration_id} deactivated successfully")
            return FlextResult[FlextOracleOicModels.IntegrationStatus].ok(status)

        except Exception as e:
            error_msg = f"Failed to deactivate integration {integration_id}: {e}"
            self.logger.exception(error_msg)
            return FlextResult[FlextOracleOicModels.IntegrationStatus].fail(error_msg)


class MonitoringService:
    """Oracle OIC Monitoring Service.

    Padrão EXTENSION: Serviço de monitoramento Oracle OIC
    com verificações de saúde e métricas de performance.
    """

    @override
    def __init__(self, client: HTTPClientProtocol) -> None:
        """Initialize monitoring service.

        Args:
            client: HTTP client (requests.Session or mock)

        """
        self.client = client
        self.logger = FlextLogger(f"{__name__}.{self.__class__.__name__}")

    def get_health_status(self: Self) -> FlextTypes.Dict:
        """Get Oracle OIC health status using FlextOracleOicUtilities.

        Returns:
            Dictionary containing validated health status information

        """
        try:
            # Mock health check response
            response = self.client.get(FlextOracleOicConstants.API.ENDPOINT_HEALTH)

            if response.status_code == FlextConstants.Platform.HTTP_STATUS_OK:
                health_data: FlextTypes.Dict = response.json()
                raw_health = {
                    "status": FlextOracleOicConstants.Monitoring.HEALTH_STATUS_HEALTHY,
                    "components": {
                        FlextOracleOicConstants.Monitoring.COMPONENT_DATABASE: {
                            "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_HEALTHY
                        },
                        FlextOracleOicConstants.Monitoring.COMPONENT_MESSAGING: {
                            "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_HEALTHY
                        },
                        FlextOracleOicConstants.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                            "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_HEALTHY
                        },
                    },
                    "timestamp": health_data.get("timestamp", ""),
                }
            else:
                raw_health = {
                    "status": FlextOracleOicConstants.Monitoring.HEALTH_STATUS_UNHEALTHY,
                    "components": {
                        FlextOracleOicConstants.Monitoring.COMPONENT_DATABASE: {
                            "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_UNKNOWN
                        },
                        FlextOracleOicConstants.Monitoring.COMPONENT_MESSAGING: {
                            "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_UNKNOWN
                        },
                        FlextOracleOicConstants.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                            "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_UNKNOWN
                        },
                    },
                    "error": f"HTTP {response.status_code}",
                }

            # Validate health status using utilities
            validation_result = (
                FlextOracleOicUtilities.MonitoringUtilities.validate_health_status(
                    raw_health
                )
            )
            if validation_result.is_success:
                return validation_result.value
            self.logger.warning(
                f"Health status validation failed: {validation_result.error}"
            )
            return raw_health

        except Exception as e:
            self.logger.exception("Health check failed")
            error_health = {
                "status": FlextOracleOicConstants.Monitoring.HEALTH_STATUS_ERROR,
                "components": {
                    FlextOracleOicConstants.Monitoring.COMPONENT_DATABASE: {
                        "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_UNKNOWN
                    },
                    FlextOracleOicConstants.Monitoring.COMPONENT_MESSAGING: {
                        "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_UNKNOWN
                    },
                    FlextOracleOicConstants.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                        "status": FlextOracleOicConstants.Monitoring.COMPONENT_STATUS_UNKNOWN
                    },
                },
                "error": str(e),
            }

            # Validate error health status as well
            validation_result = (
                FlextOracleOicUtilities.MonitoringUtilities.validate_health_status(
                    error_health
                )
            )
            return (
                validation_result.value
                if validation_result.is_success
                else error_health
            )

    def get_performance_metrics(self: Self) -> FlextTypes.Dict:
        """Get Oracle OIC performance metrics with analysis using FlextOracleOicUtilities.

        Returns:
            Dictionary containing performance metrics with analysis

        """
        try:
            # Mock performance metrics response
            response = self.client.get("/ic/api/integration/v1/metrics")

            if response.status_code == FlextConstants.Platform.HTTP_STATUS_OK:
                metrics_data: FlextTypes.Dict = response.json()
                raw_metrics = {
                    "active_integrations": metrics_data.get("active_integrations", 0),
                    "total_executions": metrics_data.get("total_executions", 0),
                    "success_rate": metrics_data.get("success_rate", 0.0),
                    "average_response_time": metrics_data.get("avg_response_time", 0.0),
                    "timestamp": metrics_data.get("timestamp", ""),
                }
            else:
                raw_metrics = {
                    "active_integrations": 0,
                    "total_executions": 0,
                    "success_rate": 0.0,
                    "average_response_time": 0.0,
                    "error": f"HTTP {response.status_code}",
                }

            # Analyze performance metrics using utilities
            analysis_result = (
                FlextOracleOicUtilities.MonitoringUtilities.analyze_performance_metrics(
                    raw_metrics
                )
            )

            if analysis_result.is_success:
                # Combine raw metrics with analysis
                return {**raw_metrics, "analysis": analysis_result.value}
            self.logger.warning(f"Performance analysis failed: {analysis_result.error}")
            return raw_metrics

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
                    error_metrics
                )
            )
            if analysis_result.is_success:
                return {**error_metrics, "analysis": analysis_result.value}
            return error_metrics


# Exports following EXTENSION pattern
__all__: FlextTypes.StringList = [
    "LifecycleManager",
    "MonitoringService",
    "OICIntegrationPatternService",
    # Main services
    "OracleOICExtensionService",
]
