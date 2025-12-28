"""Oracle OIC Extension protocols for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_core.protocols import FlextProtocols
from flext_core.typings import FlextTypes

p = FlextProtocols
t = FlextTypes


class FlextOracleOicProtocols(p):
    """Oracle OIC Extension protocols extending p with Oracle OIC-specific interfaces.

    This class provides protocol definitions for Oracle Integration Cloud extension operations,
    integration management, connection handling, pattern implementation, and monitoring.
    """

    @runtime_checkable
    class ExtensionProtocol(Protocol):
        """Protocol for Oracle OIC extension operations."""

        def execute(
            self,
            operation: str,
            params: dict[str, FlextTypes.GeneralValueType] | None = None,
        ) -> FlextProtocols.Result[dict[str, FlextTypes.GeneralValueType]]:
            """Execute Oracle OIC extension operation.

            Args:
            operation: Operation name to execute
            params: Operation parameters

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Operation result or error

            """
            ...

        def validate_business_rules(
            self,
            request_data: dict[str, t.GeneralValueType],
        ) -> FlextProtocols.Result[bool]:
            """Validate Oracle OIC business rules.

            Args:
            request_data: Request data to validate

            Returns:
            FlextResult[bool]: Validation success status

            """
            ...

        def validate_config(
            self,
            config: dict[str, t.GeneralValueType],
        ) -> FlextProtocols.Result[bool]:
            """Validate Oracle OIC extension configuration."""
            ...

    @runtime_checkable
    class IntegrationProtocol(Protocol):
        """Protocol for Oracle OIC integration management operations."""

        def list_integrations(
            self,
            *,
            filters: dict[str, t.GeneralValueType] | None = None,
        ) -> FlextProtocols.Result[list[dict[str, t.GeneralValueType]]]:
            """List Oracle OIC integrations.

            Args:
            filters: Optional filters for integration listing

            Returns:
            FlextResult[list[dict[str, t.GeneralValueType]]]: Integration list or error

            """
            ...

        def deploy_integration(
            self,
            integration_id: str,
            deployment_config: dict[str, t.GeneralValueType],
        ) -> FlextProtocols.Result[dict[str, t.GeneralValueType]]:
            """Deploy Oracle OIC integration.

            Args:
            integration_id: Integration identifier
            deployment_config: Deployment configuration

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Deployment result or error

            """
            ...

        def get_integration_status(
            self,
            integration_id: str,
        ) -> FlextProtocols.Result[dict[str, t.GeneralValueType]]:
            """Get Oracle OIC integration status.

            Args:
            integration_id: Integration identifier

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Integration status or error

            """
            ...

        def activate_integration(
            self,
            integration_id: str,
        ) -> FlextProtocols.Result[bool]:
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
            self,
            *,
            connection_type: str | None = None,
        ) -> FlextProtocols.Result[list[dict[str, t.GeneralValueType]]]:
            """List Oracle OIC connections.

            Args:
            connection_type: Optional connection type filter

            Returns:
            FlextResult[list[dict[str, t.GeneralValueType]]]: Connection list or error

            """
            ...

        def test_connection(
            self,
            connection_id: str,
        ) -> FlextProtocols.Result[dict[str, t.GeneralValueType]]:
            """Test Oracle OIC connection.

            Args:
            connection_id: Connection identifier

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Connection test result or error

            """
            ...

        def create_connection(
            self,
            connection_config: dict[str, t.GeneralValueType],
        ) -> FlextProtocols.Result[str]:
            """Create Oracle OIC connection.

            Args:
            connection_config: Connection configuration

            Returns:
            FlextResult[str]: Created connection ID or error

            """
            ...

        def update_connection(
            self,
            connection_id: str,
            connection_config: dict[str, t.GeneralValueType],
        ) -> FlextProtocols.Result[bool]:
            """Update Oracle OIC connection.

            Args:
            connection_id: Connection identifier
            connection_config: Updated connection configuration

            Returns:
            FlextResult[bool]: Update success status

            """
            ...

        def delete_connection(self, connection_id: str) -> FlextProtocols.Result[bool]:
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
            integration_config: dict[str, t.GeneralValueType],
            routing_rules: list[dict[str, t.GeneralValueType]],
        ) -> FlextProtocols.Result[dict[str, t.GeneralValueType]]:
            """Apply message router pattern to Oracle OIC integration.

            Args:
            integration_config: Integration configuration
            routing_rules: Message routing rules

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Pattern application result or error

            """
            ...

        def apply_scatter_gather_pattern(
            self,
            integration_config: dict[str, t.GeneralValueType],
            scatter_config: dict[str, t.GeneralValueType],
        ) -> FlextProtocols.Result[dict[str, t.GeneralValueType]]:
            """Apply scatter-gather pattern to Oracle OIC integration.

            Args:
            integration_config: Integration configuration
            scatter_config: Scatter-gather configuration

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Pattern application result or error

            """
            ...

        def apply_aggregator_pattern(
            self,
            integration_config: dict[str, t.GeneralValueType],
            aggregation_rules: dict[str, t.GeneralValueType],
        ) -> FlextProtocols.Result[dict[str, t.GeneralValueType]]:
            """Apply aggregator pattern to Oracle OIC integration.

            Args:
            integration_config: Integration configuration
            aggregation_rules: Aggregation rules

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Pattern application result or error

            """
            ...

        def validate_pattern_compatibility(
            self,
            pattern_type: str,
            integration_config: dict[str, t.GeneralValueType],
        ) -> FlextProtocols.Result[bool]:
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
            self,
            integration_id: str,
            *,
            time_range: str = "1h",
        ) -> FlextProtocols.Result[dict[str, t.GeneralValueType]]:
            """Get Oracle OIC integration metrics.

            Args:
            integration_id: Integration identifier
            time_range: Time range for metrics

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Integration metrics or error

            """
            ...

        def get_connection_health(
            self,
            connection_id: str,
        ) -> FlextProtocols.Result[dict[str, t.GeneralValueType]]:
            """Get Oracle OIC connection health status.

            Args:
            connection_id: Connection identifier

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Connection health status or error

            """
            ...

        def get_system_status(
            self,
        ) -> FlextProtocols.Result[dict[str, t.GeneralValueType]]:
            """Get Oracle OIC system status.

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: System status or error.

            """
            ...

        def start_monitoring(
            self,
            monitoring_config: dict[str, t.GeneralValueType],
        ) -> FlextProtocols.Result[bool]:
            """Start Oracle OIC monitoring.

            Args:
            monitoring_config: Monitoring configuration

            Returns:
            FlextResult[bool]: Monitoring start status

            """
            ...

        def stop_monitoring(self) -> FlextProtocols.Result[bool]:
            """Stop monitoring operations."""
            ...

    @runtime_checkable
    class LifecycleProtocol(p.Service, Protocol):
        """Protocol for Oracle OIC lifecycle management operations."""

        def initialize_environment(
            self,
            environment_config: dict[str, t.GeneralValueType],
        ) -> FlextProtocols.Result[bool]:
            """Initialize Oracle OIC environment.

            Args:
            environment_config: Environment configuration

            Returns:
            FlextResult[bool]: Initialization success status

            """
            ...

        def shutdown_environment(self) -> FlextProtocols.Result[bool]:
            """Shutdown the Oracle OIC environment."""
            ...

        def backup_configuration(
            self,
            backup_config: dict[str, t.GeneralValueType],
        ) -> FlextProtocols.Result[str]:
            """Backup Oracle OIC configuration.

            Args:
            backup_config: Backup configuration

            Returns:
            FlextResult[str]: Backup location or error

            """
            ...

        def restore_configuration(
            self,
            backup_location: str,
        ) -> FlextProtocols.Result[bool]:
            """Restore Oracle OIC configuration from backup."""
            ...

        def migrate_integrations(
            self,
            migration_config: dict[str, t.GeneralValueType],
        ) -> FlextProtocols.Result[dict[str, t.GeneralValueType]]:
            """Migrate Oracle OIC integrations.

            Args:
            migration_config: Migration configuration

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Migration result or error

            """
            ...

    @runtime_checkable
    class HTTPClientProtocol(p.Service, Protocol):
        """Protocol for HTTP client operations used by Oracle OIC services."""

        def get(
            self,
            url: str,
            *,
            headers: dict[str, str] | None = None,
        ) -> FlextProtocols.Result[object]:
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
            data: dict[str, t.GeneralValueType] | None = None,
            *,
            headers: dict[str, str] | None = None,
        ) -> FlextProtocols.Result[object]:
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
            data: dict[str, t.GeneralValueType] | None = None,
            *,
            headers: dict[str, str] | None = None,
        ) -> FlextProtocols.Result[object]:
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
            self,
            url: str,
            *,
            headers: dict[str, str] | None = None,
        ) -> FlextProtocols.Result[bool]:
            """Execute HTTP DELETE request.

            Args:
            url: Request URL
            headers: Optional HTTP headers

            Returns:
            FlextResult[bool]: Delete success status

            """
            ...

    @runtime_checkable
    class AuthenticationProtocol(p.Service, Protocol):
        """Protocol for Oracle OIC authentication operations."""

        def authenticate(
            self,
            credentials: dict[str, t.GeneralValueType],
        ) -> FlextProtocols.Result[dict[str, t.GeneralValueType]]:
            """Authenticate with Oracle OIC.

            Args:
            credentials: Authentication credentials

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Authentication result or error

            """
            ...

        def refresh_token(
            self,
            refresh_token: str,
        ) -> FlextProtocols.Result[dict[str, t.GeneralValueType]]:
            """Refresh OAuth2 access token."""
            ...


# Runtime alias for simplified usage
p = FlextOracleOicProtocols

__all__ = [
    "FlextOracleOicProtocols",
    "p",
]
