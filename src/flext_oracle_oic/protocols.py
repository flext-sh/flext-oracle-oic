"""Oracle OIC Extension protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextProtocols, FlextResult, FlextTypes


class FlextOracleOicExtProtocols(FlextProtocols):
    """Oracle OIC Extension protocols extending FlextProtocols with Oracle OIC-specific interfaces.

    This class provides protocol definitions for Oracle Integration Cloud extension operations,
    integration management, connection handling, pattern implementation, and monitoring.
    """

    @runtime_checkable
    class ExtensionProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Oracle OIC extension operations."""

        def execute(
            self, operation: str, params: FlextTypes.Dict | None = None
        ) -> FlextResult[FlextTypes.Dict]:
            """Execute Oracle OIC extension operation.

            Args:
                operation: Operation name to execute
                params: Operation parameters

            Returns:
                FlextResult[FlextTypes.Dict]: Operation result or error

            """

        def validate_business_rules(
            self, request_data: FlextTypes.Dict
        ) -> FlextResult[bool]:
            """Validate Oracle OIC business rules.

            Args:
                request_data: Request data to validate

            Returns:
                FlextResult[bool]: Validation success status

            """

        def validate_config(self, config: FlextTypes.Dict) -> FlextResult[bool]:
            """Validate Oracle OIC configuration.

            Args:
                config: Configuration to validate

            Returns:
                FlextResult[bool]: Configuration validation status

            """

    @runtime_checkable
    class IntegrationProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Oracle OIC integration management operations."""

        def list_integrations(
            self, *, filters: FlextTypes.Dict | None = None
        ) -> FlextResult[list[FlextTypes.Dict]]:
            """List Oracle OIC integrations.

            Args:
                filters: Optional filters for integration listing

            Returns:
                FlextResult[list[FlextTypes.Dict]]: Integration list or error

            """

        def deploy_integration(
            self, integration_id: str, deployment_config: FlextTypes.Dict
        ) -> FlextResult[FlextTypes.Dict]:
            """Deploy Oracle OIC integration.

            Args:
                integration_id: Integration identifier
                deployment_config: Deployment configuration

            Returns:
                FlextResult[FlextTypes.Dict]: Deployment result or error

            """

        def get_integration_status(
            self, integration_id: str
        ) -> FlextResult[FlextTypes.Dict]:
            """Get Oracle OIC integration status.

            Args:
                integration_id: Integration identifier

            Returns:
                FlextResult[FlextTypes.Dict]: Integration status or error

            """

        def activate_integration(self, integration_id: str) -> FlextResult[bool]:
            """Activate Oracle OIC integration.

            Args:
                integration_id: Integration identifier

            Returns:
                FlextResult[bool]: Activation success status

            """

        def deactivate_integration(self, integration_id: str) -> FlextResult[bool]:
            """Deactivate Oracle OIC integration.

            Args:
                integration_id: Integration identifier

            Returns:
                FlextResult[bool]: Deactivation success status

            """

    @runtime_checkable
    class ConnectionProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Oracle OIC connection management operations."""

        def list_connections(
            self, *, connection_type: str | None = None
        ) -> FlextResult[list[FlextTypes.Dict]]:
            """List Oracle OIC connections.

            Args:
                connection_type: Optional connection type filter

            Returns:
                FlextResult[list[FlextTypes.Dict]]: Connection list or error

            """

        def test_connection(self, connection_id: str) -> FlextResult[FlextTypes.Dict]:
            """Test Oracle OIC connection.

            Args:
                connection_id: Connection identifier

            Returns:
                FlextResult[FlextTypes.Dict]: Connection test result or error

            """

        def create_connection(
            self, connection_config: FlextTypes.Dict
        ) -> FlextResult[str]:
            """Create Oracle OIC connection.

            Args:
                connection_config: Connection configuration

            Returns:
                FlextResult[str]: Created connection ID or error

            """

        def update_connection(
            self, connection_id: str, connection_config: FlextTypes.Dict
        ) -> FlextResult[bool]:
            """Update Oracle OIC connection.

            Args:
                connection_id: Connection identifier
                connection_config: Updated connection configuration

            Returns:
                FlextResult[bool]: Update success status

            """

        def delete_connection(self, connection_id: str) -> FlextResult[bool]:
            """Delete Oracle OIC connection.

            Args:
                connection_id: Connection identifier

            Returns:
                FlextResult[bool]: Deletion success status

            """

    @runtime_checkable
    class PatternProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Oracle OIC integration pattern operations."""

        def apply_message_router_pattern(
            self,
            integration_config: FlextTypes.Dict,
            routing_rules: list[FlextTypes.Dict],
        ) -> FlextResult[FlextTypes.Dict]:
            """Apply message router pattern to Oracle OIC integration.

            Args:
                integration_config: Integration configuration
                routing_rules: Message routing rules

            Returns:
                FlextResult[FlextTypes.Dict]: Pattern application result or error

            """

        def apply_scatter_gather_pattern(
            self,
            integration_config: FlextTypes.Dict,
            scatter_config: FlextTypes.Dict,
        ) -> FlextResult[FlextTypes.Dict]:
            """Apply scatter-gather pattern to Oracle OIC integration.

            Args:
                integration_config: Integration configuration
                scatter_config: Scatter-gather configuration

            Returns:
                FlextResult[FlextTypes.Dict]: Pattern application result or error

            """

        def apply_aggregator_pattern(
            self,
            integration_config: FlextTypes.Dict,
            aggregation_rules: FlextTypes.Dict,
        ) -> FlextResult[FlextTypes.Dict]:
            """Apply aggregator pattern to Oracle OIC integration.

            Args:
                integration_config: Integration configuration
                aggregation_rules: Aggregation rules

            Returns:
                FlextResult[FlextTypes.Dict]: Pattern application result or error

            """

        def validate_pattern_compatibility(
            self, pattern_type: str, integration_config: FlextTypes.Dict
        ) -> FlextResult[bool]:
            """Validate pattern compatibility with integration.

            Args:
                pattern_type: Integration pattern type
                integration_config: Integration configuration

            Returns:
                FlextResult[bool]: Compatibility validation status

            """

    @runtime_checkable
    class MonitoringProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Oracle OIC monitoring operations."""

        def get_integration_metrics(
            self, integration_id: str, *, time_range: str = "1h"
        ) -> FlextResult[FlextTypes.Dict]:
            """Get Oracle OIC integration metrics.

            Args:
                integration_id: Integration identifier
                time_range: Time range for metrics

            Returns:
                FlextResult[FlextTypes.Dict]: Integration metrics or error

            """

        def get_connection_health(
            self, connection_id: str
        ) -> FlextResult[FlextTypes.Dict]:
            """Get Oracle OIC connection health status.

            Args:
                connection_id: Connection identifier

            Returns:
                FlextResult[FlextTypes.Dict]: Connection health status or error

            """

        def get_system_status(self) -> FlextResult[FlextTypes.Dict]:
            """Get Oracle OIC system status.

            Returns:
                FlextResult[FlextTypes.Dict]: System status or error

            """

        def start_monitoring(
            self, monitoring_config: FlextTypes.Dict
        ) -> FlextResult[bool]:
            """Start Oracle OIC monitoring.

            Args:
                monitoring_config: Monitoring configuration

            Returns:
                FlextResult[bool]: Monitoring start status

            """

        def stop_monitoring(self) -> FlextResult[bool]:
            """Stop Oracle OIC monitoring.

            Returns:
                FlextResult[bool]: Monitoring stop status

            """

    @runtime_checkable
    class LifecycleProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Oracle OIC lifecycle management operations."""

        def initialize_environment(
            self, environment_config: FlextTypes.Dict
        ) -> FlextResult[bool]:
            """Initialize Oracle OIC environment.

            Args:
                environment_config: Environment configuration

            Returns:
                FlextResult[bool]: Initialization success status

            """

        def shutdown_environment(self) -> FlextResult[bool]:
            """Shutdown Oracle OIC environment.

            Returns:
                FlextResult[bool]: Shutdown success status

            """

        def backup_configuration(
            self, backup_config: FlextTypes.Dict
        ) -> FlextResult[str]:
            """Backup Oracle OIC configuration.

            Args:
                backup_config: Backup configuration

            Returns:
                FlextResult[str]: Backup location or error

            """

        def restore_configuration(self, backup_location: str) -> FlextResult[bool]:
            """Restore Oracle OIC configuration.

            Args:
                backup_location: Backup location

            Returns:
                FlextResult[bool]: Restore success status

            """

        def migrate_integrations(
            self, migration_config: FlextTypes.Dict
        ) -> FlextResult[FlextTypes.Dict]:
            """Migrate Oracle OIC integrations.

            Args:
                migration_config: Migration configuration

            Returns:
                FlextResult[FlextTypes.Dict]: Migration result or error

            """

    @runtime_checkable
    class HTTPClientProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for HTTP client operations used by Oracle OIC services."""

        def get(
            self, url: str, *, headers: FlextTypes.StringDict | None = None
        ) -> FlextResult[object]:
            """Execute HTTP GET request.

            Args:
                url: Request URL
                headers: Optional HTTP headers

            Returns:
                FlextResult[object]: HTTP response or error

            """

        def post(
            self,
            url: str,
            data: FlextTypes.Dict | None = None,
            *,
            headers: FlextTypes.StringDict | None = None,
        ) -> FlextResult[object]:
            """Execute HTTP POST request.

            Args:
                url: Request URL
                data: Request data
                headers: Optional HTTP headers

            Returns:
                FlextResult[object]: HTTP response or error

            """

        def put(
            self,
            url: str,
            data: FlextTypes.Dict | None = None,
            *,
            headers: FlextTypes.StringDict | None = None,
        ) -> FlextResult[object]:
            """Execute HTTP PUT request.

            Args:
                url: Request URL
                data: Request data
                headers: Optional HTTP headers

            Returns:
                FlextResult[object]: HTTP response or error

            """

        def delete(
            self, url: str, *, headers: FlextTypes.StringDict | None = None
        ) -> FlextResult[bool]:
            """Execute HTTP DELETE request.

            Args:
                url: Request URL
                headers: Optional HTTP headers

            Returns:
                FlextResult[bool]: Delete success status

            """

    @runtime_checkable
    class AuthenticationProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Oracle OIC authentication operations."""

        def authenticate(
            self, credentials: FlextTypes.Dict
        ) -> FlextResult[FlextTypes.Dict]:
            """Authenticate with Oracle OIC.

            Args:
                credentials: Authentication credentials

            Returns:
                FlextResult[FlextTypes.Dict]: Authentication result or error

            """

        def refresh_token(self, refresh_token: str) -> FlextResult[FlextTypes.Dict]:
            """Refresh Oracle OIC authentication token.

            Args:
                refresh_token: Refresh token

            Returns:
                FlextResult[FlextTypes.Dict]: New token information or error

            """

        def validate_token(self, token: str) -> FlextResult[bool]:
            """Validate Oracle OIC authentication token.

            Args:
                token: Authentication token

            Returns:
                FlextResult[bool]: Token validation status

            """

        def revoke_token(self, token: str) -> FlextResult[bool]:
            """Revoke Oracle OIC authentication token.

            Args:
                token: Authentication token to revoke

            Returns:
                FlextResult[bool]: Revocation success status

            """

    # Convenience aliases for easier downstream usage
    OicExtensionProtocol = ExtensionProtocol
    OicIntegrationProtocol = IntegrationProtocol
    OicConnectionProtocol = ConnectionProtocol
    OicPatternProtocol = PatternProtocol
    OicMonitoringProtocol = MonitoringProtocol
    OicLifecycleProtocol = LifecycleProtocol
    OicHttpClientProtocol = HTTPClientProtocol
    OicAuthenticationProtocol = AuthenticationProtocol


__all__ = [
    "FlextOracleOicExtProtocols",
]
