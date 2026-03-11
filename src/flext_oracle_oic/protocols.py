"""Oracle OIC protocols for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Protocol, runtime_checkable

from flext_core import FlextProtocols, FlextTypes


class FlextOracleOicProtocols(FlextProtocols):
    """Oracle OIC Extension protocols extending p with Oracle OIC-specific interfaces.

    This class provides protocol definitions for Oracle Integration Cloud extension operations,
    integration management, connection handling, pattern implementation, and monitoring.
    """

    class OracleOic:
        """OracleOic domain namespace."""

        @runtime_checkable
        class ExtensionProtocol(Protocol):
            """Protocol for Oracle OIC extension operations."""

            def execute(
                self,
                operation: str,
                params: Mapping[str, FlextTypes.ContainerValue] | None = None,
            ) -> FlextProtocols.Result[Mapping[str, FlextTypes.ContainerValue]]:
                """Execute Oracle OIC extension operation.

                Args:
                operation: Operation name to execute
                params: Operation parameters

                Returns:
                r[Mapping[str, FlextTypes.ContainerValue]]: Operation result or error

                """
                ...

            def validate_business_rules(
                self, request_data: Mapping[str, FlextTypes.ContainerValue]
            ) -> FlextProtocols.Result[bool]:
                """Validate Oracle OIC business rules.

                Args:
                request_data: Request data to validate

                Returns:
                r[bool]: Validation success status

                """
                ...

            def validate_config(
                self, config: Mapping[str, FlextTypes.ContainerValue]
            ) -> FlextProtocols.Result[bool]:
                """Validate Oracle OIC extension configuration."""
                ...

        @runtime_checkable
        class IntegrationProtocol(Protocol):
            """Protocol for Oracle OIC integration management operations."""

            def activate_integration(
                self, integration_id: str
            ) -> FlextProtocols.Result[bool]:
                """Activate Oracle OIC integration.

                Args:
                integration_id: Integration identifier

                Returns:
                r[bool]: Activation success status

                """
                ...

            def deploy_integration(
                self,
                integration_id: str,
                deployment_config: Mapping[str, FlextTypes.ContainerValue],
            ) -> FlextProtocols.Result[Mapping[str, FlextTypes.ContainerValue]]:
                """Deploy Oracle OIC integration.

                Args:
                integration_id: Integration identifier
                deployment_config: Deployment configuration

                Returns:
                r[Mapping[str, FlextTypes.ContainerValue]]: Deployment result or error

                """
                ...

            def get_integration_status(
                self, integration_id: str
            ) -> FlextProtocols.Result[Mapping[str, FlextTypes.ContainerValue]]:
                """Get Oracle OIC integration status.

                Args:
                integration_id: Integration identifier

                Returns:
                r[Mapping[str, FlextTypes.ContainerValue]]: Integration status or error

                """
                ...

            def list_integrations(
                self, *, filters: Mapping[str, FlextTypes.ContainerValue] | None = None
            ) -> FlextProtocols.Result[list[Mapping[str, FlextTypes.ContainerValue]]]:
                """List Oracle OIC integrations.

                Args:
                filters: Optional filters for integration listing

                Returns:
                r[list[Mapping[str, FlextTypes.ContainerValue]]]: Integration list or error

                """
                ...

        @runtime_checkable
        class ConnectionProtocol(Protocol):
            """Protocol for Oracle OIC connection management operations."""

            def create_connection(
                self, connection_config: Mapping[str, FlextTypes.ContainerValue]
            ) -> FlextProtocols.Result[str]:
                """Create Oracle OIC connection.

                Args:
                connection_config: Connection configuration

                Returns:
                r[str]: Created connection ID or error

                """
                ...

            def delete_connection(
                self, connection_id: str
            ) -> FlextProtocols.Result[bool]:
                """Delete Oracle OIC connection.

                Args:
                connection_id: Connection identifier

                Returns:
                r[bool]: Deletion success status

                """
                ...

            def list_connections(
                self, *, connection_type: str | None = None
            ) -> FlextProtocols.Result[list[Mapping[str, FlextTypes.ContainerValue]]]:
                """List Oracle OIC connections.

                Args:
                connection_type: Optional connection type filter

                Returns:
                r[list[Mapping[str, FlextTypes.ContainerValue]]]: Connection list or error

                """
                ...

            def test_connection(
                self, connection_id: str
            ) -> FlextProtocols.Result[Mapping[str, FlextTypes.ContainerValue]]:
                """Test Oracle OIC connection.

                Args:
                connection_id: Connection identifier

                Returns:
                r[Mapping[str, FlextTypes.ContainerValue]]: Connection test result or error

                """
                ...

            def update_connection(
                self,
                connection_id: str,
                connection_config: Mapping[str, FlextTypes.ContainerValue],
            ) -> FlextProtocols.Result[bool]:
                """Update Oracle OIC connection.

                Args:
                connection_id: Connection identifier
                connection_config: Updated connection configuration

                Returns:
                r[bool]: Update success status

                """
                ...

        @runtime_checkable
        class PatternProtocol(Protocol):
            """Protocol for Oracle OIC integration pattern operations."""

            def apply_aggregator_pattern(
                self,
                integration_config: Mapping[str, FlextTypes.ContainerValue],
                aggregation_rules: Mapping[str, FlextTypes.ContainerValue],
            ) -> FlextProtocols.Result[Mapping[str, FlextTypes.ContainerValue]]:
                """Apply aggregator pattern to Oracle OIC integration.

                Args:
                integration_config: Integration configuration
                aggregation_rules: Aggregation rules

                Returns:
                r[Mapping[str, FlextTypes.ContainerValue]]: Pattern application result or error

                """
                ...

            def apply_message_router_pattern(
                self,
                integration_config: Mapping[str, FlextTypes.ContainerValue],
                routing_rules: list[Mapping[str, FlextTypes.ContainerValue]],
            ) -> FlextProtocols.Result[Mapping[str, FlextTypes.ContainerValue]]:
                """Apply message router pattern to Oracle OIC integration.

                Args:
                integration_config: Integration configuration
                routing_rules: Message routing rules

                Returns:
                r[Mapping[str, FlextTypes.ContainerValue]]: Pattern application result or error

                """
                ...

            def apply_scatter_gather_pattern(
                self,
                integration_config: Mapping[str, FlextTypes.ContainerValue],
                scatter_config: Mapping[str, FlextTypes.ContainerValue],
            ) -> FlextProtocols.Result[Mapping[str, FlextTypes.ContainerValue]]:
                """Apply scatter-gather pattern to Oracle OIC integration.

                Args:
                integration_config: Integration configuration
                scatter_config: Scatter-gather configuration

                Returns:
                r[Mapping[str, FlextTypes.ContainerValue]]: Pattern application result or error

                """
                ...

            def validate_pattern_compatibility(
                self,
                pattern_type: str,
                integration_config: Mapping[str, FlextTypes.ContainerValue],
            ) -> FlextProtocols.Result[bool]:
                """Validate pattern compatibility with integration.

                Args:
                pattern_type: Integration pattern type
                integration_config: Integration configuration

                Returns:
                r[bool]: Compatibility validation status

                """
                ...

        @runtime_checkable
        class MonitoringProtocol(Protocol):
            """Protocol for Oracle OIC monitoring operations."""

            def get_connection_health(
                self, connection_id: str
            ) -> FlextProtocols.Result[Mapping[str, FlextTypes.ContainerValue]]:
                """Get Oracle OIC connection health status.

                Args:
                connection_id: Connection identifier

                Returns:
                r[Mapping[str, FlextTypes.ContainerValue]]: Connection health status or error

                """
                ...

            def get_integration_metrics(
                self, integration_id: str, *, time_range: str = "1h"
            ) -> FlextProtocols.Result[Mapping[str, FlextTypes.ContainerValue]]:
                """Get Oracle OIC integration metrics.

                Args:
                integration_id: Integration identifier
                time_range: Time range for metrics

                Returns:
                r[Mapping[str, FlextTypes.ContainerValue]]: Integration metrics or error

                """
                ...

            def get_system_status(
                self,
            ) -> FlextProtocols.Result[Mapping[str, FlextTypes.ContainerValue]]:
                """Get Oracle OIC system status.

                Returns:
                r[Mapping[str, FlextTypes.ContainerValue]]: System status or error.

                """
                ...

            def start_monitoring(
                self, monitoring_config: Mapping[str, FlextTypes.ContainerValue]
            ) -> FlextProtocols.Result[bool]:
                """Start Oracle OIC monitoring.

                Args:
                monitoring_config: Monitoring configuration

                Returns:
                r[bool]: Monitoring start status

                """
                ...

            def stop_monitoring(self) -> FlextProtocols.Result[bool]:
                """Stop monitoring operations."""
                ...

        @runtime_checkable
        class LifecycleProtocol(FlextProtocols.Service[bool], Protocol):
            """Protocol for Oracle OIC lifecycle management operations."""

            def backup_configuration(
                self, backup_config: Mapping[str, FlextTypes.ContainerValue]
            ) -> FlextProtocols.Result[str]:
                """Backup Oracle OIC configuration.

                Args:
                backup_config: Backup configuration

                Returns:
                r[str]: Backup location or error

                """
                ...

            def initialize_environment(
                self, environment_config: Mapping[str, FlextTypes.ContainerValue]
            ) -> FlextProtocols.Result[bool]:
                """Initialize Oracle OIC environment.

                Args:
                environment_config: Environment configuration

                Returns:
                r[bool]: Initialization success status

                """
                ...

            def migrate_integrations(
                self, migration_config: Mapping[str, FlextTypes.ContainerValue]
            ) -> FlextProtocols.Result[Mapping[str, FlextTypes.ContainerValue]]:
                """Migrate Oracle OIC integrations.

                Args:
                migration_config: Migration configuration

                Returns:
                r[Mapping[str, FlextTypes.ContainerValue]]: Migration result or error

                """
                ...

            def restore_configuration(
                self, backup_location: str
            ) -> FlextProtocols.Result[bool]:
                """Restore Oracle OIC configuration from backup."""
                ...

            def shutdown_environment(self) -> FlextProtocols.Result[bool]:
                """Shutdown the Oracle OIC environment."""
                ...

        @runtime_checkable
        class HTTPClientProtocol(FlextProtocols.Service[object], Protocol):
            """Protocol for HTTP client operations used by Oracle OIC services."""

            def delete(
                self, url: str, *, headers: Mapping[str, str] | None = None
            ) -> FlextProtocols.Result[bool]:
                """Execute HTTP DELETE request.

                Args:
                url: Request URL
                headers: Optional HTTP headers

                Returns:
                r[bool]: Delete success status

                """
                ...

            def get(
                self, url: str, *, headers: Mapping[str, str] | None = None
            ) -> FlextProtocols.Result[object]:
                """Execute HTTP GET request.

                Args:
                url: Request URL
                headers: Optional HTTP headers

                Returns:
                r[object]: HTTP response or error

                """
                ...

            def post(
                self,
                url: str,
                data: Mapping[str, FlextTypes.ContainerValue] | None = None,
                *,
                headers: Mapping[str, str] | None = None,
            ) -> FlextProtocols.Result[object]:
                """Execute HTTP POST request.

                Args:
                url: Request URL
                data: Request data
                headers: Optional HTTP headers

                Returns:
                r[object]: HTTP response or error

                """
                ...

            def put(
                self,
                url: str,
                data: Mapping[str, FlextTypes.ContainerValue] | None = None,
                *,
                headers: Mapping[str, str] | None = None,
            ) -> FlextProtocols.Result[object]:
                """Execute HTTP PUT request.

                Args:
                url: Request URL
                data: Request data
                headers: Optional HTTP headers

                Returns:
                r[object]: HTTP response or error

                """
                ...

        @runtime_checkable
        class AuthenticationProtocol(
            FlextProtocols.Service[Mapping[str, FlextTypes.ContainerValue]], Protocol
        ):
            """Protocol for Oracle OIC authentication operations."""

            def authenticate(
                self, credentials: Mapping[str, FlextTypes.ContainerValue]
            ) -> FlextProtocols.Result[Mapping[str, FlextTypes.ContainerValue]]:
                """Authenticate with Oracle OIC.

                Args:
                credentials: Authentication credentials

                Returns:
                r[Mapping[str, FlextTypes.ContainerValue]]: Authentication result or error

                """
                ...

            def refresh_token(
                self, refresh_token: str
            ) -> FlextProtocols.Result[Mapping[str, FlextTypes.ContainerValue]]:
                """Refresh OAuth2 access token."""
                ...


p = FlextOracleOicProtocols
__all__ = ["FlextOracleOicProtocols", "p"]
