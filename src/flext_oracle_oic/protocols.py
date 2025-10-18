"""Oracle OIC Extension protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextProtocols, FlextResult


class FlextOracleOicProtocols(FlextProtocols):
    """Oracle OIC Extension protocols extending FlextProtocols with Oracle OIC-specific interfaces.

    This class provides protocol definitions for Oracle Integration Cloud extension operations,
    integration management, connection handling, pattern implementation, and monitoring.
    """

    @runtime_checkable
    class ExtensionProtocol(Protocol):
        """Protocol for Oracle OIC extension operations."""

        def execute(
            self, operation: str, params: dict[str, object] | None = None
        ) -> FlextResult[dict[str, object]]:
            """Execute Oracle OIC extension operation.

            Args:
                operation: Operation name to execute
                params: Operation parameters

            Returns:
                FlextResult[dict[str, object]]: Operation result or error

            """
            ...

        def validate_business_rules(
            self, request_data: dict[str, object]
        ) -> FlextResult[bool]:
            """Validate Oracle OIC business rules.

            Args:
                request_data: Request data to validate

            Returns:
                FlextResult[bool]: Validation success status

            """
            ...

        def validate_config(self, config: dict[str, object]) -> FlextResult[bool]:
            """Validate Oracle OIC extension configuration."""
            ...

    @runtime_checkable
    class IntegrationProtocol(Protocol):
        """Protocol for Oracle OIC integration management operations."""

        def list_integrations(
            self, *, filters: dict[str, object] | None = None
        ) -> FlextResult[list[dict[str, object]]]:
            """List Oracle OIC integrations.

            Args:
                filters: Optional filters for integration listing

            Returns:
                FlextResult[list[dict[str, object]]]: Integration list or error

            """
            ...

        def deploy_integration(
            self, integration_id: str, deployment_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Deploy Oracle OIC integration.

            Args:
                integration_id: Integration identifier
                deployment_config: Deployment configuration

            Returns:
                FlextResult[dict[str, object]]: Deployment result or error

            """
            ...

        def get_integration_status(
            self, integration_id: str
        ) -> FlextResult[dict[str, object]]:
            """Get Oracle OIC integration status.

            Args:
                integration_id: Integration identifier

            Returns:
                FlextResult[dict[str, object]]: Integration status or error

            """
            ...

        def activate_integration(self, integration_id: str) -> FlextResult[bool]:
            """Activate Oracle OIC integration.

            Args:
                integration_id: Integration identifier

            Returns:
                FlextResult[bool]: Activation success status

            """
            ...

    @runtime_checkable
    class ConnectionProtocol(Protocol):
        """Protocol for Oracle OIC connection management operations."""

        def list_connections(
            self, *, connection_type: str | None = None
        ) -> FlextResult[list[dict[str, object]]]:
            """List Oracle OIC connections.

            Args:
                connection_type: Optional connection type filter

            Returns:
                FlextResult[list[dict[str, object]]]: Connection list or error

            """
            ...

        def test_connection(self, connection_id: str) -> FlextResult[dict[str, object]]:
            """Test Oracle OIC connection.

            Args:
                connection_id: Connection identifier

            Returns:
                FlextResult[dict[str, object]]: Connection test result or error

            """
            ...

        def create_connection(
            self, connection_config: dict[str, object]
        ) -> FlextResult[str]:
            """Create Oracle OIC connection.

            Args:
                connection_config: Connection configuration

            Returns:
                FlextResult[str]: Created connection ID or error

            """
            ...

        def update_connection(
            self, connection_id: str, connection_config: dict[str, object]
        ) -> FlextResult[bool]:
            """Update Oracle OIC connection.

            Args:
                connection_id: Connection identifier
                connection_config: Updated connection configuration

            Returns:
                FlextResult[bool]: Update success status

            """
            ...

        def delete_connection(self, connection_id: str) -> FlextResult[bool]:
            """Delete Oracle OIC connection.

            Args:
                connection_id: Connection identifier

            Returns:
                FlextResult[bool]: Deletion success status

            """
            ...

    @runtime_checkable
    class PatternProtocol(Protocol):
        """Protocol for Oracle OIC integration pattern operations."""

        def apply_message_router_pattern(
            self,
            integration_config: dict[str, object],
            routing_rules: list[dict[str, object]],
        ) -> FlextResult[dict[str, object]]:
            """Apply message router pattern to Oracle OIC integration.

            Args:
                integration_config: Integration configuration
                routing_rules: Message routing rules

            Returns:
                FlextResult[dict[str, object]]: Pattern application result or error

            """
            ...

        def apply_scatter_gather_pattern(
            self,
            integration_config: dict[str, object],
            scatter_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Apply scatter-gather pattern to Oracle OIC integration.

            Args:
                integration_config: Integration configuration
                scatter_config: Scatter-gather configuration

            Returns:
                FlextResult[dict[str, object]]: Pattern application result or error

            """
            ...

        def apply_aggregator_pattern(
            self,
            integration_config: dict[str, object],
            aggregation_rules: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Apply aggregator pattern to Oracle OIC integration.

            Args:
                integration_config: Integration configuration
                aggregation_rules: Aggregation rules

            Returns:
                FlextResult[dict[str, object]]: Pattern application result or error

            """
            ...

        def validate_pattern_compatibility(
            self, pattern_type: str, integration_config: dict[str, object]
        ) -> FlextResult[bool]:
            """Validate pattern compatibility with integration.

            Args:
                pattern_type: Integration pattern type
                integration_config: Integration configuration

            Returns:
                FlextResult[bool]: Compatibility validation status

            """
            ...

    @runtime_checkable
    class MonitoringProtocol(Protocol):
        """Protocol for Oracle OIC monitoring operations."""

        def get_integration_metrics(
            self, integration_id: str, *, time_range: str = "1h"
        ) -> FlextResult[dict[str, object]]:
            """Get Oracle OIC integration metrics.

            Args:
                integration_id: Integration identifier
                time_range: Time range for metrics

            Returns:
                FlextResult[dict[str, object]]: Integration metrics or error

            """
            ...

        def get_connection_health(
            self, connection_id: str
        ) -> FlextResult[dict[str, object]]:
            """Get Oracle OIC connection health status.

            Args:
                connection_id: Connection identifier

            Returns:
                FlextResult[dict[str, object]]: Connection health status or error

            """
            ...

        def get_system_status(self) -> FlextResult[dict[str, object]]:
            """Get Oracle OIC system status.

            Returns:
                FlextResult[dict[str, object]]: System status or error.

            """
            ...

        def start_monitoring(
            self, monitoring_config: dict[str, object]
        ) -> FlextResult[bool]:
            """Start Oracle OIC monitoring.

            Args:
                monitoring_config: Monitoring configuration

            Returns:
                FlextResult[bool]: Monitoring start status

            """
            ...

        def stop_monitoring(self) -> FlextResult[bool]:
            """Stop monitoring operations."""
            ...

    @runtime_checkable
    class LifecycleProtocol(FlextProtocols.Service, Protocol):
        """Protocol for Oracle OIC lifecycle management operations."""

        def initialize_environment(
            self, environment_config: dict[str, object]
        ) -> FlextResult[bool]:
            """Initialize Oracle OIC environment.

            Args:
                environment_config: Environment configuration

            Returns:
                FlextResult[bool]: Initialization success status

            """
            ...

        def shutdown_environment(self) -> FlextResult[bool]:
            """Shutdown the Oracle OIC environment."""
            ...

        def backup_configuration(
            self, backup_config: dict[str, object]
        ) -> FlextResult[str]:
            """Backup Oracle OIC configuration.

            Args:
                backup_config: Backup configuration

            Returns:
                FlextResult[str]: Backup location or error

            """
            ...

        def restore_configuration(self, backup_location: str) -> FlextResult[bool]:
            """Restore Oracle OIC configuration from backup."""
            ...

        def migrate_integrations(
            self, migration_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Migrate Oracle OIC integrations.

            Args:
                migration_config: Migration configuration

            Returns:
                FlextResult[dict[str, object]]: Migration result or error

            """
            ...

    @runtime_checkable
    class HTTPClientProtocol(FlextProtocols.Service, Protocol):
        """Protocol for HTTP client operations used by Oracle OIC services."""

        def get(
            self, url: str, *, headers: dict[str, str] | None = None
        ) -> FlextResult[object]:
            """Execute HTTP GET request.

            Args:
                url: Request URL
                headers: Optional HTTP headers

            Returns:
                FlextResult[object]: HTTP response or error

            """
            ...

        def post(
            self,
            url: str,
            data: dict[str, object] | None = None,
            *,
            headers: dict[str, str] | None = None,
        ) -> FlextResult[object]:
            """Execute HTTP POST request.

            Args:
                url: Request URL
                data: Request data
                headers: Optional HTTP headers

            Returns:
                FlextResult[object]: HTTP response or error

            """
            ...

        def put(
            self,
            url: str,
            data: dict[str, object] | None = None,
            *,
            headers: dict[str, str] | None = None,
        ) -> FlextResult[object]:
            """Execute HTTP PUT request.

            Args:
                url: Request URL
                data: Request data
                headers: Optional HTTP headers

            Returns:
                FlextResult[object]: HTTP response or error

            """
            ...

        def delete(
            self, url: str, *, headers: dict[str, str] | None = None
        ) -> FlextResult[bool]:
            """Execute HTTP DELETE request.

            Args:
                url: Request URL
                headers: Optional HTTP headers

            Returns:
                FlextResult[bool]: Delete success status

            """
            ...

    @runtime_checkable
    class AuthenticationProtocol(FlextProtocols.Service, Protocol):
        """Protocol for Oracle OIC authentication operations."""

        def authenticate(
            self, credentials: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Authenticate with Oracle OIC.

            Args:
                credentials: Authentication credentials

            Returns:
                FlextResult[dict[str, object]]: Authentication result or error

            """
            ...

        def refresh_token(self, refresh_token: str) -> FlextResult[dict[str, object]]:
            """Refresh OAuth2 access token."""
            ...


__all__ = [
    "FlextOracleOicProtocols",
]
