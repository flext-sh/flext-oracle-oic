"""Oracle OIC Extension protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextCore


class FlextOracleOicProtocols(FlextCore.Protocols):
    """Oracle OIC Extension protocols extending FlextCore.Protocols with Oracle OIC-specific interfaces.

    This class provides protocol definitions for Oracle Integration Cloud extension operations,
    integration management, connection handling, pattern implementation, and monitoring.
    """

    @runtime_checkable
    class ExtensionProtocol(Protocol):
        """Protocol for Oracle OIC extension operations."""

        def execute(
            self, operation: str, params: FlextCore.Types.Dict | None = None
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Execute Oracle OIC extension operation.

            Args:
                operation: Operation name to execute
                params: Operation parameters

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: Operation result or error

            """
            ...

        def validate_business_rules(
            self, request_data: FlextCore.Types.Dict
        ) -> FlextCore.Result[bool]:
            """Validate Oracle OIC business rules.

            Args:
                request_data: Request data to validate

            Returns:
                FlextCore.Result[bool]: Validation success status

            """
            ...

        def validate_config(
            self, config: FlextCore.Types.Dict
        ) -> FlextCore.Result[bool]:
            """Validate Oracle OIC extension configuration."""
            ...

    @runtime_checkable
    class IntegrationProtocol(Protocol):
        """Protocol for Oracle OIC integration management operations."""

        def list_integrations(
            self, *, filters: FlextCore.Types.Dict | None = None
        ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
            """List Oracle OIC integrations.

            Args:
                filters: Optional filters for integration listing

            Returns:
                FlextCore.Result[list[FlextCore.Types.Dict]]: Integration list or error

            """
            ...

        def deploy_integration(
            self, integration_id: str, deployment_config: FlextCore.Types.Dict
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Deploy Oracle OIC integration.

            Args:
                integration_id: Integration identifier
                deployment_config: Deployment configuration

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: Deployment result or error

            """
            ...

        def get_integration_status(
            self, integration_id: str
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Get Oracle OIC integration status.

            Args:
                integration_id: Integration identifier

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: Integration status or error

            """
            ...

        def activate_integration(self, integration_id: str) -> FlextCore.Result[bool]:
            """Activate Oracle OIC integration.

            Args:
                integration_id: Integration identifier

            Returns:
                FlextCore.Result[bool]: Activation success status

            """
            ...

    @runtime_checkable
    class ConnectionProtocol(Protocol):
        """Protocol for Oracle OIC connection management operations."""

        def list_connections(
            self, *, connection_type: str | None = None
        ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
            """List Oracle OIC connections.

            Args:
                connection_type: Optional connection type filter

            Returns:
                FlextCore.Result[list[FlextCore.Types.Dict]]: Connection list or error

            """
            ...

        def test_connection(
            self, connection_id: str
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Test Oracle OIC connection.

            Args:
                connection_id: Connection identifier

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: Connection test result or error

            """
            ...

        def create_connection(
            self, connection_config: FlextCore.Types.Dict
        ) -> FlextCore.Result[str]:
            """Create Oracle OIC connection.

            Args:
                connection_config: Connection configuration

            Returns:
                FlextCore.Result[str]: Created connection ID or error

            """
            ...

        def update_connection(
            self, connection_id: str, connection_config: FlextCore.Types.Dict
        ) -> FlextCore.Result[bool]:
            """Update Oracle OIC connection.

            Args:
                connection_id: Connection identifier
                connection_config: Updated connection configuration

            Returns:
                FlextCore.Result[bool]: Update success status

            """
            ...

        def delete_connection(self, connection_id: str) -> FlextCore.Result[bool]:
            """Delete Oracle OIC connection.

            Args:
                connection_id: Connection identifier

            Returns:
                FlextCore.Result[bool]: Deletion success status

            """
            ...

    @runtime_checkable
    class PatternProtocol(Protocol):
        """Protocol for Oracle OIC integration pattern operations."""

        def apply_message_router_pattern(
            self,
            integration_config: FlextCore.Types.Dict,
            routing_rules: list[FlextCore.Types.Dict],
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Apply message router pattern to Oracle OIC integration.

            Args:
                integration_config: Integration configuration
                routing_rules: Message routing rules

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: Pattern application result or error

            """
            ...

        def apply_scatter_gather_pattern(
            self,
            integration_config: FlextCore.Types.Dict,
            scatter_config: FlextCore.Types.Dict,
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Apply scatter-gather pattern to Oracle OIC integration.

            Args:
                integration_config: Integration configuration
                scatter_config: Scatter-gather configuration

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: Pattern application result or error

            """
            ...

        def apply_aggregator_pattern(
            self,
            integration_config: FlextCore.Types.Dict,
            aggregation_rules: FlextCore.Types.Dict,
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Apply aggregator pattern to Oracle OIC integration.

            Args:
                integration_config: Integration configuration
                aggregation_rules: Aggregation rules

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: Pattern application result or error

            """
            ...

        def validate_pattern_compatibility(
            self, pattern_type: str, integration_config: FlextCore.Types.Dict
        ) -> FlextCore.Result[bool]:
            """Validate pattern compatibility with integration.

            Args:
                pattern_type: Integration pattern type
                integration_config: Integration configuration

            Returns:
                FlextCore.Result[bool]: Compatibility validation status

            """
            ...

    @runtime_checkable
    class MonitoringProtocol(Protocol):
        """Protocol for Oracle OIC monitoring operations."""

        def get_integration_metrics(
            self, integration_id: str, *, time_range: str = "1h"
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Get Oracle OIC integration metrics.

            Args:
                integration_id: Integration identifier
                time_range: Time range for metrics

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: Integration metrics or error

            """
            ...

        def get_connection_health(
            self, connection_id: str
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Get Oracle OIC connection health status.

            Args:
                connection_id: Connection identifier

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: Connection health status or error

            """
            ...

        def get_system_status(self) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Get Oracle OIC system status.

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: System status or error.

            """
            ...

        def start_monitoring(
            self, monitoring_config: FlextCore.Types.Dict
        ) -> FlextCore.Result[bool]:
            """Start Oracle OIC monitoring.

            Args:
                monitoring_config: Monitoring configuration

            Returns:
                FlextCore.Result[bool]: Monitoring start status

            """
            ...

        def stop_monitoring(self) -> FlextCore.Result[bool]:
            """Stop monitoring operations."""
            ...

    @runtime_checkable
    class LifecycleProtocol(FlextCore.Protocols.Domain.Service, Protocol):
        """Protocol for Oracle OIC lifecycle management operations."""

        def initialize_environment(
            self, environment_config: FlextCore.Types.Dict
        ) -> FlextCore.Result[bool]:
            """Initialize Oracle OIC environment.

            Args:
                environment_config: Environment configuration

            Returns:
                FlextCore.Result[bool]: Initialization success status

            """
            ...

        def shutdown_environment(self) -> FlextCore.Result[bool]:
            """Shutdown the Oracle OIC environment."""
            ...

        def backup_configuration(
            self, backup_config: FlextCore.Types.Dict
        ) -> FlextCore.Result[str]:
            """Backup Oracle OIC configuration.

            Args:
                backup_config: Backup configuration

            Returns:
                FlextCore.Result[str]: Backup location or error

            """
            ...

        def restore_configuration(self, backup_location: str) -> FlextCore.Result[bool]:
            """Restore Oracle OIC configuration from backup."""
            ...

        def migrate_integrations(
            self, migration_config: FlextCore.Types.Dict
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Migrate Oracle OIC integrations.

            Args:
                migration_config: Migration configuration

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: Migration result or error

            """
            ...

    @runtime_checkable
    class HTTPClientProtocol(FlextCore.Protocols.Domain.Service, Protocol):
        """Protocol for HTTP client operations used by Oracle OIC services."""

        def get(
            self, url: str, *, headers: FlextCore.Types.StringDict | None = None
        ) -> FlextCore.Result[object]:
            """Execute HTTP GET request.

            Args:
                url: Request URL
                headers: Optional HTTP headers

            Returns:
                FlextCore.Result[object]: HTTP response or error

            """
            ...

        def post(
            self,
            url: str,
            data: FlextCore.Types.Dict | None = None,
            *,
            headers: FlextCore.Types.StringDict | None = None,
        ) -> FlextCore.Result[object]:
            """Execute HTTP POST request.

            Args:
                url: Request URL
                data: Request data
                headers: Optional HTTP headers

            Returns:
                FlextCore.Result[object]: HTTP response or error

            """
            ...

        def put(
            self,
            url: str,
            data: FlextCore.Types.Dict | None = None,
            *,
            headers: FlextCore.Types.StringDict | None = None,
        ) -> FlextCore.Result[object]:
            """Execute HTTP PUT request.

            Args:
                url: Request URL
                data: Request data
                headers: Optional HTTP headers

            Returns:
                FlextCore.Result[object]: HTTP response or error

            """
            ...

        def delete(
            self, url: str, *, headers: FlextCore.Types.StringDict | None = None
        ) -> FlextCore.Result[bool]:
            """Execute HTTP DELETE request.

            Args:
                url: Request URL
                headers: Optional HTTP headers

            Returns:
                FlextCore.Result[bool]: Delete success status

            """
            ...

    @runtime_checkable
    class AuthenticationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
        """Protocol for Oracle OIC authentication operations."""

        def authenticate(
            self, credentials: FlextCore.Types.Dict
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Authenticate with Oracle OIC.

            Args:
                credentials: Authentication credentials

            Returns:
                FlextCore.Result[FlextCore.Types.Dict]: Authentication result or error

            """
            ...

        def refresh_token(
            self, refresh_token: str
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Refresh OAuth2 access token."""
            ...


__all__ = [
    "FlextOracleOicProtocols",
]
