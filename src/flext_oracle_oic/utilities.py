"""Oracle OIC Extension utilities module.

This module provides domain-specific utilities for Oracle Integration Cloud (OIC)
operations, extending u with nested classes for complete
Oracle OIC integration functionality.

FLEXT COMPLIANCE: Follows [Project]Utilities pattern with:
- Single unified class extending u
- Nested classes for domain-specific functionality
- Python 3.13+ features and Pydantic 2.11+
- Railway-oriented programming with FlextResult
- Type-safe operations with proper validation
- SOLID principles with clean separation of concerns
"""

from __future__ import annotations

import re
from datetime import UTC, datetime
from typing import ClassVar
from urllib.parse import urljoin

from pydantic import SecretStr

from flext import r, t, u as u_core


class FlextOracleOicUtilities(u_core):
    """Unified Oracle OIC Extension utilities.

    Extends ue Oracle Integration Cloud
    functionality organized in domain-specific nested classes.

    DOMAIN COVERAGE:
    - Integration validation and lifecycle management
    - Connection testing and configuration validation
    - Authentication and security operations
    - API request construction and validation
    - Pattern-based integration analysis
    - Monitoring and health check utilities

    DESIGN PRINCIPLES:
    - Single responsibility per nested class
    - Immutable operations with FlextResult
    - Type-safe validation with Pydantic 2.11+
    - Railway-oriented error handling
    - No side effects in utility functions
    """

    class IntegrationValidation:
        """Oracle OIC integration validation utilities."""

        # Integration validation constants
        MIN_INTEGRATION_NAME_LENGTH: ClassVar[int] = 1
        MAX_INTEGRATION_NAME_LENGTH: ClassVar[int] = 100
        VALID_INTEGRATION_STATUSES: ClassVar[frozenset[str]] = frozenset({
            "ACTIVATED",
            "DEACTIVATED",
            "DRAFT",
            "PUBLISHED",
            "RUNNING",
            "STOPPED",
            "ERROR",
        })
        VERSION_PATTERN: ClassVar[re.Pattern[str]] = re.compile(
            r"^\d{2}\.\d{2}\.\d{4}$",
        )

        @staticmethod
        def validate_integration_name(name: str) -> r[str]:
            """Validate Oracle OIC integration name.

            Args:
            name: Integration name to validate

            Returns:
            FlextResult containing validated name or validation error

            """
            if not isinstance(name, str):
                return r[str].fail("Integration name must be a string")

            name = name.strip()
            if not name:
                return r[str].fail("Integration name cannot be empty")

            if (
                len(name)
                < FlextOracleOicUtilities.IntegrationValidation.MIN_INTEGRATION_NAME_LENGTH
            ):
                return r[str].fail("Integration name too short")

            if (
                len(name)
                > FlextOracleOicUtilities.IntegrationValidation.MAX_INTEGRATION_NAME_LENGTH
            ):
                return r[str].fail("Integration name too long")

            # Check for invalid characters (OIC naming rules)
            if not re.match(r"^[a-zA-Z0-9_\-\s]+$", name):
                return r[str].fail(
                    "Integration name contains invalid characters",
                )

            return r[str].ok(name)

        @staticmethod
        def validate_integration_status(status: str) -> r[str]:
            """Validate Oracle OIC integration status.

            Args:
            status: Integration status to validate

            Returns:
            FlextResult containing validated status or error

            """
            if not isinstance(status, str):
                return r[str].fail("Integration status must be a string")

            status = status.upper().strip()
            if (
                status
                not in FlextOracleOicUtilities.IntegrationValidation.VALID_INTEGRATION_STATUSES
            ):
                valid_statuses = ", ".join(
                    sorted(
                        FlextOracleOicUtilities.IntegrationValidation.VALID_INTEGRATION_STATUSES,
                    ),
                )
                return r[str].fail(
                    f"Invalid integration status. Valid: {valid_statuses}",
                )

            return r[str].ok(status)

        @staticmethod
        def validate_integration_version(version: str) -> r[str]:
            """Validate Oracle OIC integration version format.

            Args:
            version: Version string to validate (format: XX.XX.XXXX)

            Returns:
            FlextResult containing validated version or error

            """
            if not isinstance(version, str):
                return r[str].fail("Integration version must be a string")

            version = version.strip()
            if not FlextOracleOicUtilities.IntegrationValidation.VERSION_PATTERN.match(
                version,
            ):
                return r[str].fail(
                    "Invalid version format. Expected: XX.XX.XXXX",
                )

            return r[str].ok(version)

        @staticmethod
        def validate_integration_data(
            integration_data: dict[str, object],
        ) -> r[dict[str, object]]:
            """Validate complete Oracle OIC integration data.

            Args:
            integration_data: Integration configuration data

            Returns:
            FlextResult containing validated data or validation errors

            """
            if not isinstance(integration_data, dict):
                return r[dict[str, object]].fail(
                    "Integration data must be a dictionary",
                )

            errors: list[str] = []
            validated_data = integration_data.copy()

            # Validate required fields
            if "name" not in integration_data:
                errors.append("Integration name is required")
            else:
                name_result = FlextOracleOicUtilities.IntegrationValidation.validate_integration_name(
                    integration_data["name"],
                )
                if name_result.is_failure:
                    errors.append(f"Name validation: {name_result.error}")
                else:
                    validated_data["name"] = name_result.value

            if "version" in integration_data:
                version_result = FlextOracleOicUtilities.IntegrationValidation.validate_integration_version(
                    integration_data["version"],
                )
                if version_result.is_failure:
                    errors.append(f"Version validation: {version_result.error}")
                else:
                    validated_data["version"] = version_result.value

            if "status" in integration_data:
                status_result = FlextOracleOicUtilities.IntegrationValidation.validate_integration_status(
                    integration_data["status"],
                )
                if status_result.is_failure:
                    errors.append(f"Status validation: {status_result.error}")
                else:
                    validated_data["status"] = status_result.value

            if errors:
                return r[dict[str, object]].fail(
                    f"Integration validation failed: {'; '.join(errors)}",
                )

            return r[dict[str, object]].ok(validated_data)

    class ConnectionValidation:
        """Oracle OIC connection validation utilities."""

        # Connection validation constants
        VALID_CONNECTION_TYPES: ClassVar[frozenset[str]] = frozenset({
            "REST",
            "SOAP",
            "DATABASE",
            "FILE",
            "FTP",
            "SFTP",
        })
        VALID_CONNECTION_STATUSES: ClassVar[frozenset[str]] = frozenset({
            "ACTIVE",
            "INACTIVE",
            "ERROR",
            "UNKNOWN",
        })

        @staticmethod
        def validate_connection_type(connection_type: str) -> r[str]:
            """Validate Oracle OIC connection type.

            Args:
            connection_type: Connection type to validate

            Returns:
            FlextResult containing validated type or error

            """
            if not isinstance(connection_type, str):
                return r[str].fail("Connection type must be a string")

            connection_type = connection_type.upper().strip()
            if (
                connection_type
                not in FlextOracleOicUtilities.ConnectionValidation.VALID_CONNECTION_TYPES
            ):
                valid_types = ", ".join(
                    sorted(
                        FlextOracleOicUtilities.ConnectionValidation.VALID_CONNECTION_TYPES,
                    ),
                )
                return r[str].fail(
                    f"Invalid connection type. Valid: {valid_types}",
                )

            return r[str].ok(connection_type)

        @staticmethod
        def validate_connection_status(status: str) -> r[str]:
            """Validate Oracle OIC connection status.

            Args:
            status: Connection status to validate

            Returns:
            FlextResult containing validated status or error

            """
            if not isinstance(status, str):
                return r[str].fail("Connection status must be a string")

            status = status.upper().strip()
            if (
                status
                not in FlextOracleOicUtilities.ConnectionValidation.VALID_CONNECTION_STATUSES
            ):
                valid_statuses = ", ".join(
                    sorted(
                        FlextOracleOicUtilities.ConnectionValidation.VALID_CONNECTION_STATUSES,
                    ),
                )
                return r[str].fail(
                    f"Invalid connection status. Valid: {valid_statuses}",
                )

            return r[str].ok(status)

    class AuthenticationValidation:
        """Oracle OIC authentication validation utilities."""

        # Authentication validation constants
        MIN_CLIENT_ID_LENGTH: ClassVar[int] = 1
        MIN_TOKEN_URL_LENGTH: ClassVar[int] = 10
        MIN_CLIENT_SECRET_LENGTH: ClassVar[int] = 8
        VALID_AUTH_TYPES: ClassVar[frozenset[str]] = frozenset({
            "oauth2",
            "basic",
            "bearer",
        })

        @staticmethod
        def validate_oauth_client_id(client_id: str) -> r[str]:
            """Validate OAuth2 client ID.

            Args:
            client_id: OAuth2 client ID to validate

            Returns:
            FlextResult containing validated client ID or error

            """
            if not isinstance(client_id, str):
                return r[str].fail("OAuth client ID must be a string")

            client_id = client_id.strip()
            if (
                len(client_id)
                < FlextOracleOicUtilities.AuthenticationValidation.MIN_CLIENT_ID_LENGTH
            ):
                return r[str].fail("OAuth client ID cannot be empty")

            # Check for basic format (alphanumeric, hyphens, underscores)
            if not re.match(r"^[a-zA-Z0-9_\-\.]+$", client_id):
                return r[str].fail(
                    "OAuth client ID contains invalid characters",
                )

            return r[str].ok(client_id)

        @staticmethod
        def validate_oauth_client_secret(
            client_secret: SecretStr,
        ) -> r[SecretStr]:
            """Validate OAuth2 client secret.

            Args:
            client_secret: OAuth2 client secret to validate

            Returns:
            FlextResult containing validated secret or error

            """
            if not isinstance(client_secret, SecretStr):
                return r[SecretStr].fail(
                    "OAuth client secret must be SecretStr",
                )

            secret_value = client_secret.get_secret_value()
            if not secret_value or not secret_value.strip():
                return r[SecretStr].fail(
                    "OAuth client secret cannot be empty",
                )

            if (
                len(secret_value)
                < FlextOracleOicUtilities.AuthenticationValidation.MIN_CLIENT_SECRET_LENGTH
            ):
                return r[SecretStr].fail(
                    "OAuth client secret must be at least 8 characters",
                )

            return r[SecretStr].ok(client_secret)

    class APIRequestBuilder:
        """Oracle OIC API request construction utilities."""

        # API request constants
        DEFAULT_TIMEOUT: ClassVar[int] = 30
        MAX_TIMEOUT: ClassVar[int] = 300
        VALID_HTTP_METHODS: ClassVar[frozenset[str]] = frozenset({
            "GET",
            "POST",
            "PUT",
            "DELETE",
            "PATCH",
            "HEAD",
            "OPTIONS",
        })

        @staticmethod
        def build_integration_endpoint(
            base_url: str,
            api_version: str = "v1",
            integration_id: str | None = None,
        ) -> r[str]:
            """Build Oracle OIC integration API endpoint.

            Args:
            base_url: OIC instance base URL
            api_version: API version (default: v1)
            integration_id: Optional specific integration ID

            Returns:
            FlextResult containing constructed endpoint URL or error

            """
            # Validate base URL
            url_result = FlextOracleOicUtilities.ConnectionValidation.validate_base_url(
                base_url,
            )
            if url_result.is_failure:
                return r[str].fail(f"Base URL validation: {url_result.error}")

            validated_base_url = url_result.value

            # Build endpoint path
            path_parts = ["ic", "api", "integration", api_version, "integrations"]
            if integration_id:
                if not isinstance(integration_id, str) or not integration_id.strip():
                    return r[str].fail(
                        "Integration ID must be non-empty string",
                    )
                path_parts.append(integration_id.strip())

            endpoint_path = "/" + "/".join(path_parts)
            full_url = urljoin(validated_base_url + "/", endpoint_path.lstrip("/"))

            return r[str].ok(full_url)

        @staticmethod
        def build_connection_endpoint(
            base_url: str,
            api_version: str = "v1",
            connection_id: str | None = None,
        ) -> r[str]:
            """Build Oracle OIC connection API endpoint.

            Args:
            base_url: OIC instance base URL
            api_version: API version (default: v1)
            connection_id: Optional specific connection ID

            Returns:
            FlextResult containing constructed endpoint URL or error

            """
            # Validate base URL
            url_result = FlextOracleOicUtilities.ConnectionValidation.validate_base_url(
                base_url,
            )
            if url_result.is_failure:
                return r[str].fail(f"Base URL validation: {url_result.error}")

            validated_base_url = url_result.value

            # Build endpoint path
            path_parts = ["ic", "api", "integration", api_version, "connections"]
            if connection_id:
                if not isinstance(connection_id, str) or not connection_id.strip():
                    return r[str].fail(
                        "Connection ID must be non-empty string",
                    )
                path_parts.append(connection_id.strip())

            endpoint_path = "/" + "/".join(path_parts)
            full_url = urljoin(validated_base_url + "/", endpoint_path.lstrip("/"))

            return r[str].ok(full_url)

        @staticmethod
        def build_request_headers(
            auth_token: str | None = None,
            content_type: str = "application/json",
            additional_headers: dict[str, str] | None = None,
        ) -> r[dict[str, str]]:
            """Build Oracle OIC API request headers.

            Args:
            auth_token: Optional authentication token
            content_type: Content type header (default: application/json)
            additional_headers: Optional additional headers

            Returns:
            FlextResult containing constructed headers or error

            """
            headers: dict[str, str] = {
                "Accept": "application/json",
                "Content-Type": content_type,
                "User-Agent": "FlextOracleOicension/1.0.0",
            }

            if auth_token:
                if not isinstance(auth_token, str) or not auth_token.strip():
                    return r[dict[str, str]].fail(
                        "Auth token must be non-empty string",
                    )
                headers["Authorization"] = f"Bearer {auth_token.strip()}"

            if additional_headers:
                if not isinstance(additional_headers, dict):
                    return r[dict[str, str]].fail(
                        "Additional headers must be a dictionary",
                    )
                headers.update(additional_headers)

            return r[dict[str, str]].ok(headers)

    class PatternAnalysis:
        """Oracle OIC integration pattern analysis utilities."""

        # Pattern analysis constants
        SUPPORTED_PATTERNS: ClassVar[frozenset[str]] = frozenset({
            "message_router",
            "scatter_gather",
            "publish_subscribe",
            "request_reply",
        })
        MIN_ENDPOINTS_FOR_ROUTER: ClassVar[int] = 2

        @staticmethod
        def analyze_integration_pattern(
            integration_data: dict[str, object],
        ) -> r[str]:
            """Analyze Oracle OIC integration to determine pattern type.

            Args:
            integration_data: Integration configuration data

            Returns:
            FlextResult containing detected pattern or analysis error

            """
            if not isinstance(integration_data, dict):
                return r[str].fail("Integration data must be a dictionary")

            # Analyze based on common OIC integration characteristics
            endpoints = integration_data.get("endpoints", [])
            connections = integration_data.get("connections", [])
            mappings = integration_data.get("mappings", [])

            # Message Router: Multiple target endpoints from single source
            if (
                len(endpoints)
                > FlextOracleOicUtilities.PatternAnalysis.MIN_ENDPOINTS_FOR_ROUTER
                and any(
                    endpoint.get("direction") == "outbound" for endpoint in endpoints
                )
            ):
                return r[str].ok("message_router")

            # Scatter-Gather: Multiple parallel calls with aggregation
            if len(connections) > 1 and any(
                "aggregate" in str(mapping).lower() for mapping in mappings
            ):
                return r[str].ok("scatter_gather")

            # Publish-Subscribe: Event-driven pattern
            if any(
                "event" in str(endpoint).lower() or "publish" in str(endpoint).lower()
                for endpoint in endpoints
            ):
                return r[str].ok("publish_subscribe")

            # Request-Reply: Synchronous pattern (default)
            return r[str].ok("request_reply")

        @staticmethod
        def validate_pattern_configuration(
            pattern_type: str,
            configuration: dict[str, object] | object,
        ) -> r[dict[str, object]]:
            """Validate Oracle OIC integration pattern configuration.

            Args:
            pattern_type: Integration pattern type
            configuration: Pattern-specific configuration

            Returns:
            FlextResult containing validated configuration or error

            """
            if (
                pattern_type
                not in FlextOracleOicUtilities.PatternAnalysis.SUPPORTED_PATTERNS
            ):
                supported = ", ".join(
                    sorted(FlextOracleOicUtilities.PatternAnalysis.SUPPORTED_PATTERNS),
                )
                return r[dict[str, object]].fail(
                    f"Unsupported pattern type. Supported: {supported}",
                )

            if not isinstance(configuration, dict):
                return r[dict[str, object]].fail(
                    "Configuration must be a dictionary",
                )

            validated_config = configuration.copy()

            # Pattern-specific validation
            if pattern_type == "message_router":
                if "routing_rules" not in configuration:
                    return r[dict[str, object]].fail(
                        "Message router pattern requires routing_rules",
                    )

            elif pattern_type == "scatter_gather":
                if "target_services" not in configuration:
                    return r[dict[str, object]].fail(
                        "Scatter-gather pattern requires target_services",
                    )
                if "aggregation_strategy" not in configuration:
                    validated_config["aggregation_strategy"] = "collect_all"

            if (
                pattern_type == "publish_subscribe"
                and "event_types" not in configuration
            ):
                return r[dict[str, object]].fail(
                    "Publish-subscribe pattern requires event_types",
                )

            return r[dict[str, object]].ok(validated_config)

    class MonitoringUtilities:
        """Oracle OIC monitoring and health check utilities."""

        # Monitoring constants
        HEALTH_CHECK_TIMEOUT: ClassVar[int] = 10
        PERFORMANCE_THRESHOLDS: ClassVar[t.FloatDict] = {
            "response_time_ms": 5000.0,
            "success_rate": 0.95,
            "error_rate": 0.05,
        }

        @staticmethod
        def validate_health_status(
            health_data: dict[str, object],
        ) -> r[dict[str, object]]:
            """Validate Oracle OIC health check data.

            Args:
            health_data: Health check response data

            Returns:
            FlextResult containing validated health data or error

            """
            if not isinstance(health_data, dict):
                return r[dict[str, object]].fail(
                    "Health data must be a dictionary",
                )

            validated_data = health_data.copy()

            # Validate required health fields
            if "status" not in health_data:
                return r[dict[str, object]].fail(
                    "Health data must include status",
                )

            status = health_data["status"]
            if status not in {"healthy", "unhealthy", "error", "unknown"}:
                return r[dict[str, object]].fail(
                    "Invalid health status. Valid: healthy, unhealthy, error, unknown",
                )

            # Validate components if present
            if "components" in health_data:
                components = health_data["components"]
                if not isinstance(components, dict):
                    return r[dict[str, object]].fail(
                        "Components must be a dictionary",
                    )

                for component_name, component_data in components.items():
                    if not isinstance(component_data, dict):
                        return r[dict[str, object]].fail(
                            f"Component {component_name} data must be a dictionary",
                        )
                    if "status" not in component_data:
                        return r[dict[str, object]].fail(
                            f"Component {component_name} must have status",
                        )

            # Add timestamp if not present
            if "timestamp" not in validated_data:
                validated_data["timestamp"] = datetime.now(UTC).isoformat()

            return r[dict[str, object]].ok(validated_data)

        @staticmethod
        def analyze_performance_metrics(
            metrics: dict[str, object],
        ) -> r[dict[str, object]]:
            """Analyze Oracle OIC performance metrics.

            Args:
            metrics: Performance metrics data

            Returns:
            FlextResult containing analysis results or error

            """
            if not isinstance(metrics, dict):
                return r[dict[str, object]].fail(
                    "Metrics must be a dictionary",
                )

            analysis: dict[str, object] = {
                "overall_health": "healthy",
                "warnings": [],
                "critical_issues": [],
                "recommendations": [],
            }

            # Analyze response time
            if "average_response_time" in metrics:
                response_time = metrics["average_response_time"]
                if isinstance(response_time, (int, float)):
                    threshold = FlextOracleOicUtilities.MonitoringUtilities.PERFORMANCE_THRESHOLDS[
                        "response_time_ms"
                    ]
                    if response_time > threshold:
                        analysis["warnings"].append(
                            f"High response time: {response_time}ms (threshold: {threshold}ms)",
                        )
                        analysis["recommendations"].append(
                            "Consider optimizing integration mappings or connection pooling",
                        )

            # Analyze success rate
            if "success_rate" in metrics:
                success_rate = metrics["success_rate"]
                if isinstance(success_rate, (int, float)):
                    threshold = FlextOracleOicUtilities.MonitoringUtilities.PERFORMANCE_THRESHOLDS[
                        "success_rate"
                    ]
                    if success_rate < threshold:
                        analysis["critical_issues"].append(
                            f"Low success rate: {success_rate:.2%} (threshold: {threshold:.2%})",
                        )
                        analysis["overall_health"] = "unhealthy"
                        analysis["recommendations"].append(
                            "Investigate integration failures and error patterns",
                        )

            # Analyze error rate
            if "error_rate" in metrics:
                error_rate = metrics["error_rate"]
                if isinstance(error_rate, (int, float)):
                    threshold = FlextOracleOicUtilities.MonitoringUtilities.PERFORMANCE_THRESHOLDS[
                        "error_rate"
                    ]
                    if error_rate > threshold:
                        analysis["warnings"].append(
                            f"High error rate: {error_rate:.2%} (threshold: {threshold:.2%})",
                        )
                        analysis["recommendations"].append(
                            "Review error logs and implement error handling improvements",
                        )

            return r[dict[str, object]].ok(analysis)


u = FlextOracleOicUtilities

__all__ = ["FlextOracleOicUtilities", "u"]
