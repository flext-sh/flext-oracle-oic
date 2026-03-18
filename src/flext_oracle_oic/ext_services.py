"""Oracle OIC Extension Services - EXTENSION Pattern.

This module establishes the EXTENSION PEP8 pattern for specialized
Oracle OIC services. Serves as model for future extensions.


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping
from types import TracebackType
from typing import Protocol, Self, override

from flext_core import FlextContainer, FlextLogger, FlextService, r, t
from pydantic import ConfigDict

from flext_oracle_oic.constants import FlextOracleOicConstants
from flext_oracle_oic.ext_client import FlextOracleOicClient
from flext_oracle_oic.models import FlextOracleOicModels
from flext_oracle_oic.settings import FlextOracleOicSettings
from flext_oracle_oic.utilities import FlextOracleOicUtilities

logger = FlextLogger(__name__)


class FlextOracleOicExtServices(
    FlextService[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]]
):
    """Single unified Oracle OIC Extension services class.

    Contains all service functionality as nested classes following FLEXT principles.
    """

    @override
    def execute(
        self: Self,
    ) -> r[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]]:
        """Execute main service operation - delegates to nested service."""
        service = self.OracleOicExtensionService()
        return service.execute()

    class HTTPClient(Protocol):
        """Protocol for HTTP client used by MonitoringService."""

        def get(self, url: str) -> FlextOracleOicExtServices.HTTPResponse:
            """Execute HTTP GET request."""
            ...

    class HTTPResponse(Protocol):
        """Protocol for HTTP response."""

        status_code: int

        def json(self: Self) -> Mapping[str, t.NormalizedValue]:
            """Parse response as JSON."""
            ...

    class OracleOicExtensionService(
        FlextService[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]]
    ):
        """Main Oracle OIC Extension service.

        FLEXT Compliant: Domain service for Oracle OIC operations
        with complete enterprise functionality following FLEXT patterns.
        """

        model_config = ConfigDict(
            frozen=True,
            validate_assignment=True,
            extra="forbid",
            arbitrary_types_allowed=True,
        )
        _oic_settings: FlextOracleOicSettings | None = None
        _client: FlextOracleOicClient | None = None

        @override
        def __init__(self, **data: t.Scalar) -> None:
            """Initialize OIC extension service.

            Uses singleton config pattern - no config parameter needed.
            """
            _ = data
            super().__init__()
            settings = FlextOracleOicSettings.get_global()
            object.__setattr__(self, "_oic_settings", settings)
            object.__setattr__(self, "settings", settings)
            object.__setattr__(self, "_client", None)
            FlextContainer.get_global()

        def __enter__(self: Self) -> Self:
            """Context manager entry."""
            return self

        def __exit__(
            self,
            exc_type: type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None,
        ) -> None:
            """Context manager exit."""
            client = self._client if hasattr(self, "_client") else None
            if client:
                client.__exit__(exc_type, exc_val, exc_tb)
                object.__setattr__(self, "_client", None)

        def deploy_integration(
            self, integration_data: Mapping[str, t.NormalizedValue]
        ) -> r[str]:
            """Deploy integration to Oracle OIC.

            Args:
            integration_data: Integration configuration

            Returns:
            r containing integration ID or error

            """
            return (
                r[t.NormalizedValue]
                .ok(integration_data)
                .flat_map(
                    lambda data: self._get_oic_client().map(
                        lambda client: (client, data)
                    )
                )
                .flat_map(lambda client_data: self._create_integration(*client_data))
                .flat_map(self._extract_integration_id)
            )

        @override
        def execute(
            self: Self,
        ) -> r[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]]:
            """Execute the main domain service operation.

            Returns:
            r containing list of OIC integrations or error

            """
            return self.list_integrations()

        def list_connections(
            self, type_filter: list[str] | None = None
        ) -> r[list[FlextOracleOicModels.OracleOic.OICConnectionInfo]]:
            """List Oracle OIC connections.

            Args:
            type_filter: Filter by connection type

            Returns:
            r containing connection info list or error

            """
            return (
                self
                ._get_oic_client()
                .flat_map(lambda client: self._fetch_connections(client, type_filter))
                .flat_map(self._parse_connection_models)
            )

        def list_integrations(
            self, status_filter: list[str] | None = None
        ) -> r[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]]:
            """List Oracle OIC integrations.

            Args:
            status_filter: Filter by integration status

            Returns:
            r containing integration info list or error

            """
            return (
                self
                ._get_oic_client()
                .flat_map(
                    lambda client: self._fetch_integrations(client, status_filter)
                )
                .flat_map(self._parse_integration_models)
            )

        def test_connection(self) -> r[bool]:
            """Test connection to Oracle OIC.

            Returns:
            r containing connection status or error

            """
            return self._get_oic_client().flat_map(self._perform_connection_test)

        @override
        def validate_business_rules(self: Self) -> r[bool]:
            """Validate Oracle OIC service business rules using FlextOracleOicUtilities.

            Returns:
            r[bool]: The validation result (True if valid).

            """
            if self._oic_settings is None:
                return r[bool].fail("Settings are required")
            if not self._oic_settings.base_url:
                return r[bool].fail("Base URL is required")
            if not self._oic_settings.oauth_client_id:
                return r[bool].fail("OAuth client ID is required")
            client_id_result = FlextOracleOicUtilities.AuthenticationValidation.validate_oauth_client_id(
                self._oic_settings.oauth_client_id
            )
            if client_id_result.is_failure:
                return r[bool].fail(
                    f"OAuth client ID validation: {client_id_result.error}"
                )
            if not self._oic_settings.oauth_client_secret:
                return r[bool].fail("OAuth client secret is required")
            if not self._oic_settings.oauth_token_url:
                return r[bool].fail("OAuth token URL is required")
            return r[bool].ok(value=True)

        def validate_config(self: Self) -> r[None]:
            """Validate service configuration.

            Returns:
            r[None]: The validation result

            """
            result = self.validate_business_rules()
            return (
                r[None].ok(None)
                if result.is_success
                else r[None].fail(result.error or "Validation failed")
            )

        def _create_auth_config(
            self,
        ) -> r[FlextOracleOicModels.OracleOic.OICAuthConfig]:
            """Create authentication configuration."""
            if self._oic_settings is None:
                return r[FlextOracleOicModels.OracleOic.OICAuthConfig].fail(
                    "Settings are required"
                )
            try:
                auth_config = FlextOracleOicModels.OracleOic.OICAuthConfig(
                    oauth_client_id=self._oic_settings.oauth_client_id,
                    oauth_client_secret=self._oic_settings.oauth_client_secret,
                    oauth_token_url=str(self._oic_settings.oauth_token_url),
                    oauth_client_aud=self._oic_settings.oauth_client_aud,
                    oauth_scope=self._oic_settings.oauth_scope,
                )
                return r[FlextOracleOicModels.OracleOic.OICAuthConfig].ok(auth_config)
            except (
                ConnectionError,
                TimeoutError,
                ValueError,
            ) as e:
                error_msg = f"Failed to create auth config: {e}"
                self.logger.exception(error_msg)
                return r[FlextOracleOicModels.OracleOic.OICAuthConfig].fail(error_msg)

        def _create_client_instance(
            self,
            auth_config: FlextOracleOicModels.OracleOic.OICAuthConfig,
            connection_config: FlextOracleOicModels.OracleOic.OICConnectionConfig,
        ) -> r[FlextOracleOicClient]:
            """Create client instance."""
            try:
                client = FlextOracleOicClient(connection_config, auth_config)
                object.__setattr__(self, "_client", client)
                return r[FlextOracleOicClient].ok(client)
            except (
                ConnectionError,
                TimeoutError,
                ValueError,
            ) as e:
                error_msg = f"Failed to create OIC client instance: {e}"
                self.logger.exception(error_msg)
                return r[FlextOracleOicClient].fail(error_msg)

        def _create_connection_config(
            self,
        ) -> r[FlextOracleOicModels.OracleOic.OICConnectionConfig]:
            """Create connection configuration."""
            try:
                settings = self._oic_settings
                if settings is None:
                    return r[FlextOracleOicModels.OracleOic.OICConnectionConfig].fail(
                        "OIC settings not configured"
                    )
                connection_config = FlextOracleOicModels.OracleOic.OICConnectionConfig(
                    base_url=str(settings.base_url),
                    api_version=settings.api_version,
                    request_timeout=settings.request_timeout,
                    max_retries=settings.max_retries,
                    verify_ssl=settings.verify_ssl,
                )
                return r[FlextOracleOicModels.OracleOic.OICConnectionConfig].ok(
                    connection_config
                )
            except (
                ConnectionError,
                TimeoutError,
                ValueError,
            ) as e:
                error_msg = f"Failed to create connection config: {e}"
                self.logger.exception(error_msg)
                return r[FlextOracleOicModels.OracleOic.OICConnectionConfig].fail(
                    error_msg
                )

        def _create_integration(
            self, client: FlextOracleOicClient, data: Mapping[str, t.NormalizedValue]
        ) -> r[Mapping[str, t.NormalizedValue]]:
            """Create integration via OIC client."""
            integration_data_str: dict[str, t.NormalizedValue] = {
                k: str(v) for k, v in data.items()
            }
            create_result = client.create_integration(integration_data_str)
            if create_result.is_failure:
                return r[Mapping[str, t.NormalizedValue]].fail(
                    create_result.error or "Create integration failed"
                )
            created_integration = create_result.value
            if not created_integration:
                return r[Mapping[str, t.NormalizedValue]].fail(
                    "No integration data returned"
                )
            return r[Mapping[str, t.NormalizedValue]].ok(created_integration)

        def _extract_integration_id(
            self, integration_data: Mapping[str, t.NormalizedValue]
        ) -> r[str]:
            """Extract integration ID from creation result."""
            integration_id = integration_data.get("id", "")
            if not integration_id:
                return r[str].fail("No integration ID returned")
            self.logger.info(f"Integration deployed successfully: {integration_id!s}")
            return r[str].ok(str(integration_id))

        def _fetch_connections(
            self, client: FlextOracleOicClient, type_filter: list[str] | None
        ) -> r[list[Mapping[str, t.NormalizedValue]]]:
            """Fetch connections from OIC API."""
            connections_result = client.get_connections(
                type_filter=type_filter,
                page_size=FlextOracleOicConstants.OracleOic.DEFAULT_PAGE_SIZE,
            )
            if connections_result.is_failure:
                return r[list[Mapping[str, t.NormalizedValue]]].fail(
                    connections_result.error or "Connections fetch failed"
                )
            return r[list[Mapping[str, t.NormalizedValue]]].ok(
                connections_result.value or []
            )

        def _fetch_integrations(
            self, client: FlextOracleOicClient, status_filter: list[str] | None
        ) -> r[list[Mapping[str, t.NormalizedValue]]]:
            """Fetch integrations from OIC API."""
            integrations_result = client.get_integrations(
                status_filter=status_filter,
                page_size=FlextOracleOicConstants.OracleOic.DEFAULT_PAGE_SIZE,
            )
            if integrations_result.is_failure:
                return r[list[Mapping[str, t.NormalizedValue]]].fail(
                    integrations_result.error or "Failed to fetch integrations"
                )
            return r[list[Mapping[str, t.NormalizedValue]]].ok(
                integrations_result.value or []
            )

        def _get_client(self: Self) -> r[FlextOracleOicClient]:
            """Get authenticated OIC client.

            Returns:
            r containing client or error

            """
            return (
                r[FlextOracleOicClient]
                .ok(None)
                .flat_map(lambda _: self._get_or_create_client())
            )

        def _get_oic_client(self) -> r[FlextOracleOicClient]:
            """Get authenticated OIC client."""
            client_result = self._get_client()
            if client_result.is_failure:
                return r[FlextOracleOicClient].fail(
                    client_result.error or "Client creation failed"
                )
            client = client_result.value
            return r[FlextOracleOicClient].ok(client)

        def _get_or_create_client(self) -> r[FlextOracleOicClient]:
            """Get existing client or create new one."""
            client = self._client if hasattr(self, "_client") else None
            if client:
                return r[FlextOracleOicClient].ok(client)
            return (
                r[FlextOracleOicClient]
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

        def _parse_connection_models(
            self, connections_data: list[Mapping[str, t.NormalizedValue]]
        ) -> r[list[FlextOracleOicModels.OracleOic.OICConnectionInfo]]:
            """Parse connection data into domain models."""
            connection_infos: list[
                FlextOracleOicModels.OracleOic.OICConnectionInfo
            ] = []
            for connection in connections_data:
                try:
                    connection_info = FlextOracleOicModels.OracleOic.OICConnectionInfo(
                        connection_id=str(connection.get("id", "")),
                        name=str(connection.get("name", "")),
                        adapter_type=str(connection.get("adapterType", "")),
                        status=str(connection.get("status", "")),
                        connection_type=str(connection.get("connectionType", "")),
                        description=str(connection.get("description", "")),
                    )
                    connection_infos.append(connection_info)
                except (
                    ConnectionError,
                    TimeoutError,
                    ValueError,
                ) as e:
                    err_msg: str = str(e)
                    self.logger.warning(f"Failed to parse connection: {err_msg}")
                    continue
            self.logger.info(f"Retrieved {len(connection_infos)} connections")
            return r[list[FlextOracleOicModels.OracleOic.OICConnectionInfo]].ok(
                connection_infos
            )

        def _parse_integration_models(
            self, integrations_data: list[Mapping[str, t.NormalizedValue]]
        ) -> r[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]]:
            """Parse integration data into domain models."""
            integration_infos: list[
                FlextOracleOicModels.OracleOic.OICIntegrationInfo
            ] = []
            for integration in integrations_data:
                try:
                    integration_info = (
                        FlextOracleOicModels.OracleOic.OICIntegrationInfo(
                            integration_id=str(integration.get("id", "")),
                            name=str(integration.get("name", "")),
                            status=str(integration.get("status", "")),
                            integration_version=str(integration.get("version", "")),
                            description=str(integration.get("description", "")),
                            created_by=str(integration.get("createdBy", "")),
                            last_updated=str(integration.get("lastUpdated", "")),
                        )
                    )
                    integration_infos.append(integration_info)
                except (
                    ConnectionError,
                    TimeoutError,
                    ValueError,
                ) as e:
                    err_msg: str = str(e)
                    self.logger.warning(f"Failed to parse integration: {err_msg}")
                    continue
            self.logger.info(f"Retrieved {len(integration_infos)} integrations")
            return r[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]].ok(
                integration_infos
            )

        def _perform_connection_test(self, client: FlextOracleOicClient) -> r[bool]:
            """Perform actual connection test by fetching minimal data."""
            integrations_result = client.get_integrations(
                page_size=FlextOracleOicConstants.OracleOic.MIN_PAGE_SIZE
            )
            if integrations_result.is_success:
                self.logger.info("OIC connection test successful")
                return r[bool].ok(value=True)
            error_msg = f"OIC connection test failed: {integrations_result.error}"
            self.logger.error(error_msg)
            return r[bool].fail(error_msg)

    class OICIntegrationPatternService:
        """Oracle OIC Integration Pattern service.

        EXTENSION Pattern: Service for enterprise integration patterns
        Oracle OIC such as Message Router, Scatter-Gather, etc.
        """

        @override
        def __init__(
            self, oic_service: FlextOracleOicExtServices.OracleOicExtensionService
        ) -> None:
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
            message_data: Mapping[str, t.NormalizedValue],
            routing_rules: list[Mapping[str, t.NormalizedValue]],
        ) -> r[Mapping[str, t.NormalizedValue]]:
            """Apply message router pattern to OIC integration using FlextOracleOicUtilities.

            Args:
            message_data: Message to route
            routing_rules: Routing rules configuration

            Returns:
            r containing routing result or error

            """
            try:
                self.logger.info("Applying message router pattern")
                pattern_config: dict[str, t.NormalizedValue] = {
                    "routing_rules": routing_rules,
                    "message_data": message_data,
                }
                validation_result = FlextOracleOicUtilities.PatternAnalysis.validate_pattern_configuration(
                    "message_router", pattern_config
                )
                if validation_result.is_failure:
                    return r[Mapping[str, t.NormalizedValue]].fail(
                        f"Pattern validation failed: {validation_result.error}"
                    )
                routing_result = {
                    "pattern": FlextOracleOicConstants.Integration.PATTERN_MESSAGE_ROUTER,
                    "message_id": message_data.get(
                        "id",
                        FlextOracleOicConstants.OICPatterns.PATTERN_MESSAGE_ID_UNKNOWN,
                    ),
                    "applied_rules": len(routing_rules),
                    "status": FlextOracleOicConstants.OICPatterns.PatternStatus.PROCESSED,
                }
                return r[Mapping[str, t.NormalizedValue]].ok(routing_result)
            except (
                ConnectionError,
                TimeoutError,
                ValueError,
            ) as e:
                error_msg = f"Message router pattern failed: {e}"
                self.logger.exception(error_msg)
                return r[Mapping[str, t.NormalizedValue]].fail(error_msg)

        def apply_scatter_gather_pattern(
            self,
            request_data: Mapping[str, t.NormalizedValue],
            target_endpoints: list[str],
        ) -> r[Mapping[str, t.NormalizedValue]]:
            """Apply scatter-gather pattern to OIC integration using FlextOracleOicUtilities.

            Args:
            request_data: Request to scatter
            target_endpoints: Target endpoints for scatter

            Returns:
            r containing scatter-gather result or error

            """
            try:
                self.logger.info("Applying scatter-gather pattern")
                pattern_config: Mapping[str, t.NormalizedValue] = {
                    "target_services": target_endpoints,
                    "request_data": request_data,
                }
                validation_result = FlextOracleOicUtilities.PatternAnalysis.validate_pattern_configuration(
                    "scatter_gather", pattern_config
                )
                if validation_result.is_failure:
                    return r[Mapping[str, t.NormalizedValue]].fail(
                        f"Pattern validation failed: {validation_result.error}"
                    )
                scatter_result = {
                    "pattern": FlextOracleOicConstants.Integration.PATTERN_SCATTER_GATHER,
                    "request_id": request_data.get(
                        "id",
                        FlextOracleOicConstants.OICPatterns.PATTERN_REQUEST_ID_UNKNOWN,
                    ),
                    "target_count": len(target_endpoints),
                    "status": FlextOracleOicConstants.OICPatterns.PatternStatus.PROCESSED,
                }
                return r[Mapping[str, t.NormalizedValue]].ok(scatter_result)
            except (
                ConnectionError,
                TimeoutError,
                ValueError,
            ) as e:
                error_msg = f"Scatter-gather pattern failed: {e}"
                self.logger.exception(error_msg)
                return r[Mapping[str, t.NormalizedValue]].fail(error_msg)

    class LifecycleManager:
        """Oracle OIC Integration Lifecycle Manager.

        EXTENSION Pattern: Integration lifecycle manager
        Oracle OIC with activation, deactivation, and monitoring operations.
        """

        @override
        def __init__(self) -> None:
            """Initialize lifecycle manager.

            Uses singleton config pattern - no config parameter needed.
            """
            self.settings: FlextOracleOicSettings = FlextOracleOicSettings.get_global()
            self.logger = FlextLogger(f"{__name__}.{self.__class__.__name__}")
            self._client: FlextOracleOicClient | None = None

        def activate_integration(
            self, integration_id: str
        ) -> r[FlextOracleOicModels.OracleOic.IntegrationStatus]:
            """Activate an Oracle OIC integration."""
            return self._toggle_integration(
                integration_id,
                FlextOracleOicConstants.Integration.Status.ACTIVATED,
                "activated",
            )

        def deactivate_integration(
            self, integration_id: str
        ) -> r[FlextOracleOicModels.OracleOic.IntegrationStatus]:
            """Deactivate an Oracle OIC integration."""
            return self._toggle_integration(
                integration_id,
                FlextOracleOicConstants.Integration.Status.DEACTIVATED,
                "deactivated",
            )

        def _toggle_integration(
            self,
            integration_id: str,
            target_status: str,
            action_label: str,
        ) -> r[FlextOracleOicModels.OracleOic.IntegrationStatus]:
            """Set integration to *target_status* and return its new status."""
            try:
                client_result = self._get_client()
                if not client_result.is_success:
                    return r[FlextOracleOicModels.OracleOic.IntegrationStatus].fail(
                        client_result.error or "Client creation failed"
                    )
                client = client_result.value
                update_data: dict[str, t.NormalizedValue] = {"status": target_status}
                update_result = client.update_integration(integration_id, update_data)
                if not update_result.is_success:
                    return r[FlextOracleOicModels.OracleOic.IntegrationStatus].fail(
                        update_result.error or f"{action_label.capitalize()} failed"
                    )
                status = FlextOracleOicModels.OracleOic.IntegrationStatus(
                    integration_id=integration_id,
                    integration_version=FlextOracleOicConstants.Integration.DEFAULT_VERSION,
                    status=target_status,
                    last_updated=FlextOracleOicConstants.Integration.DEFAULT_LAST_UPDATED,
                    activated_by=FlextOracleOicConstants.Integration.DEFAULT_ACTIVATED_BY,
                )
                self.logger.info(
                    f"Integration {integration_id} {action_label} successfully"
                )
                return r[FlextOracleOicModels.OracleOic.IntegrationStatus].ok(status)
            except (
                ConnectionError,
                TimeoutError,
                ValueError,
            ) as e:
                error_msg = (
                    f"Failed to {action_label} integration {integration_id}: {e}"
                )
                self.logger.exception(error_msg)
                return r[FlextOracleOicModels.OracleOic.IntegrationStatus].fail(
                    error_msg
                )

        def _get_client(self: Self) -> r[FlextOracleOicClient]:
            """Get authenticated OIC client."""
            try:
                if not self._client:
                    auth_config = FlextOracleOicModels.OracleOic.OICAuthConfig(
                        oauth_client_id=self.settings.oauth_client_id,
                        oauth_client_secret=self.settings.oauth_client_secret,
                        oauth_token_url=str(self.settings.oauth_token_url),
                        oauth_client_aud=self.settings.oauth_client_aud,
                        oauth_scope=self.settings.oauth_scope,
                    )
                    connection_config = (
                        FlextOracleOicModels.OracleOic.OICConnectionConfig(
                            base_url=str(self.settings.base_url),
                            api_version=self.settings.api_version,
                            request_timeout=self.settings.request_timeout,
                            max_retries=self.settings.max_retries,
                            verify_ssl=self.settings.verify_ssl,
                        )
                    )
                    self._client = FlextOracleOicClient(connection_config, auth_config)
                return r[FlextOracleOicClient].ok(self._client)
            except (
                ConnectionError,
                TimeoutError,
                ValueError,
            ) as e:
                error_msg = f"Failed to create OIC client: {e}"
                self.logger.exception(error_msg)
                return r[FlextOracleOicClient].fail(error_msg)

    class MonitoringService:
        """Oracle OIC Monitoring Service.

        EXTENSION Pattern: Oracle OIC monitoring service
        with health checks and performance metrics.
        """

        @override
        def __init__(self, client: FlextOracleOicExtServices.HTTPClient) -> None:
            """Initialize monitoring service.

            Args:
            client: HTTP client (requests.Session or mock)

            """
            self.client = client
            self.logger = FlextLogger(f"{__name__}.{self.__class__.__name__}")

        def get_health_status(self: Self) -> Mapping[str, t.NormalizedValue]:
            """Get Oracle OIC health status using FlextOracleOicUtilities.

            Returns:
            Dictionary containing validated health status information

            """
            try:
                response = self.client.get(FlextOracleOicConstants.API.ENDPOINT_HEALTH)
                if response.status_code == FlextOracleOicConstants.API.HTTP_STATUS_OK:
                    health_data = response.json()
                    raw_health: dict[str, t.NormalizedValue] = {
                        "status": FlextOracleOicConstants.Monitoring.HealthStatus.HEALTHY,
                        "components": {
                            FlextOracleOicConstants.Monitoring.COMPONENT_DATABASE: {
                                "status": FlextOracleOicConstants.Monitoring.ComponentStatus.HEALTHY
                            },
                            FlextOracleOicConstants.Monitoring.COMPONENT_MESSAGING: {
                                "status": FlextOracleOicConstants.Monitoring.ComponentStatus.HEALTHY
                            },
                            FlextOracleOicConstants.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                                "status": FlextOracleOicConstants.Monitoring.ComponentStatus.HEALTHY
                            },
                        },
                        "timestamp": health_data.get("timestamp", ""),
                    }
                else:
                    raw_health = {
                        "status": FlextOracleOicConstants.Monitoring.HealthStatus.UNHEALTHY,
                        "components": {
                            FlextOracleOicConstants.Monitoring.COMPONENT_DATABASE: {
                                "status": FlextOracleOicConstants.Monitoring.ComponentStatus.UNKNOWN
                            },
                            FlextOracleOicConstants.Monitoring.COMPONENT_MESSAGING: {
                                "status": FlextOracleOicConstants.Monitoring.ComponentStatus.UNKNOWN
                            },
                            FlextOracleOicConstants.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                                "status": FlextOracleOicConstants.Monitoring.ComponentStatus.UNKNOWN
                            },
                        },
                        "error": f"HTTP {response.status_code}",
                    }
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
            except (
                ConnectionError,
                TimeoutError,
                ValueError,
            ) as e:
                self.logger.exception("Health check failed")
                error_health: dict[str, t.NormalizedValue] = {
                    "status": FlextOracleOicConstants.Monitoring.HealthStatus.ERROR,
                    "components": {
                        FlextOracleOicConstants.Monitoring.COMPONENT_DATABASE: {
                            "status": FlextOracleOicConstants.Monitoring.ComponentStatus.UNKNOWN
                        },
                        FlextOracleOicConstants.Monitoring.COMPONENT_MESSAGING: {
                            "status": FlextOracleOicConstants.Monitoring.ComponentStatus.UNKNOWN
                        },
                        FlextOracleOicConstants.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                            "status": FlextOracleOicConstants.Monitoring.ComponentStatus.UNKNOWN
                        },
                    },
                    "error": str(e),
                }
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

        def get_performance_metrics(self: Self) -> Mapping[str, t.NormalizedValue]:
            """Get Oracle OIC performance metrics with analysis using FlextOracleOicUtilities.

            Returns:
            Dictionary containing performance metrics with analysis

            """
            try:
                response = self.client.get("/ic/api/integration/v1/metrics")
                if response.status_code == FlextOracleOicConstants.API.HTTP_STATUS_OK:
                    metrics_data = response.json()
                    raw_metrics: dict[str, t.NormalizedValue] = {
                        "active_integrations": metrics_data.get(
                            "active_integrations", 0
                        ),
                        "total_executions": metrics_data.get("total_executions", 0),
                        "success_rate": metrics_data.get("success_rate", 0.0),
                        "average_response_time": metrics_data.get(
                            "avg_response_time", 0.0
                        ),
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
                analysis_result = FlextOracleOicUtilities.MonitoringUtilities.analyze_performance_metrics(
                    raw_metrics
                )
                if analysis_result.is_success:
                    analyzed_metrics: dict[str, t.NormalizedValue] = {
                        **raw_metrics,
                        "analysis": analysis_result.value,
                    }
                    return analyzed_metrics
                self.logger.warning(
                    f"Performance analysis failed: {analysis_result.error}"
                )
                return raw_metrics
            except (
                ConnectionError,
                TimeoutError,
                ValueError,
            ) as e:
                self.logger.exception("Performance metrics failed")
                error_metrics: dict[str, t.NormalizedValue] = {
                    "active_integrations": 0,
                    "total_executions": 0,
                    "success_rate": 0.0,
                    "average_response_time": 0.0,
                    "error": str(e),
                }
                analysis_result = FlextOracleOicUtilities.MonitoringUtilities.analyze_performance_metrics(
                    error_metrics
                )
                if analysis_result.is_success:
                    analyzed_error_metrics: dict[str, t.NormalizedValue] = {
                        **error_metrics,
                        "analysis": analysis_result.value,
                    }
                    return analyzed_error_metrics
                return error_metrics


__all__: list[str] = ["FlextOracleOicExtServices"]
