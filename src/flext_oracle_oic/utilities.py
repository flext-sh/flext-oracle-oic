"""Oracle OIC Extension utilities module.

This module provides domain-specific utilities for Oracle Integration Cloud (OIC)
operations, extending FlextUtilities with nested classes for comprehensive
Oracle OIC integration functionality.

**FLEXT COMPLIANCE**: Follows [Project]Utilities pattern with:
- Single unified class extending FlextUtilities
- Nested classes for domain-specific functionality
- Python 3.13+ advanced features and Pydantic 2.11+
- Railway-oriented programming with FlextResult
- Type-safe operations with proper validation
- SOLID principles with clean separation of concerns
"""

from __future__ import annotations

import re
from datetime import UTC, datetime
from typing import ClassVar
from urllib.parse import urljoin, urlparse

from flext_core import (
    FlextLogger,
    FlextResult,
    FlextTypes,
    FlextUtilities,
)
from pydantic import SecretStr

__all__ = ["FlextOracleOicExtUtilities"]


class FlextOracleOicExtUtilities(FlextUtilities):
    """Unified Oracle OIC Extension utilities.

    Extends FlextUtilities with comprehensive Oracle Integration Cloud
    functionality organized in domain-specific nested classes.

    **DOMAIN COVERAGE**:
    - Integration validation and lifecycle management
    - Connection testing and configuration validation
    - Authentication and security operations
    - API request construction and validation
    - Pattern-based integration analysis
    - Monitoring and health check utilities

    **DESIGN PRINCIPLES**:
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
            r"^\d{2}\.\d{2}\.\d{4}$"
        )

        @staticmethod
        def validate_integration_name(name: str) -> FlextResult[str]:
            """Validate Oracle OIC integration name.

            Args:
                name: Integration name to validate

            Returns:
                FlextResult containing validated name or validation error

            """
            if not isinstance(name, str):
                return FlextResult[str].fail("Integration name must be a string")

            name = name.strip()
            if not name:
                return FlextResult[str].fail("Integration name cannot be empty")

            if (
                len(name)
                < FlextOracleOicExtUtilities.IntegrationValidation.MIN_INTEGRATION_NAME_LENGTH
            ):
                return FlextResult[str].fail("Integration name too short")

            if (
                len(name)
                > FlextOracleOicExtUtilities.IntegrationValidation.MAX_INTEGRATION_NAME_LENGTH
            ):
                return FlextResult[str].fail("Integration name too long")

            # Check for invalid characters (OIC naming rules)
            if not re.match(r"^[a-zA-Z0-9_\-\s]+$", name):
                return FlextResult[str].fail(
                    "Integration name contains invalid characters"
                )

            return FlextResult[str].ok(name)

        @staticmethod
        def validate_integration_status(status: str) -> FlextResult[str]:
            """Validate Oracle OIC integration status.

            Args:
                status: Integration status to validate

            Returns:
                FlextResult containing validated status or error

            """
            if not isinstance(status, str):
                return FlextResult[str].fail("Integration status must be a string")

            status = status.upper().strip()
            if (
                status
                not in FlextOracleOicExtUtilities.IntegrationValidation.VALID_INTEGRATION_STATUSES
            ):
                valid_statuses = ", ".join(
                    sorted(
                        FlextOracleOicExtUtilities.IntegrationValidation.VALID_INTEGRATION_STATUSES
                    )
                )
                return FlextResult[str].fail(
                    f"Invalid integration status. Valid: {valid_statuses}"
                )

            return FlextResult[str].ok(status)

        @staticmethod
        def validate_integration_version(version: str) -> FlextResult[str]:
            """Validate Oracle OIC integration version format.

            Args:
                version: Version string to validate (format: XX.XX.XXXX)

            Returns:
                FlextResult containing validated version or error

            """
            if not isinstance(version, str):
                return FlextResult[str].fail("Integration version must be a string")

            version = version.strip()
            if not FlextOracleOicExtUtilities.IntegrationValidation.VERSION_PATTERN.match(
                version
            ):
                return FlextResult[str].fail(
                    "Invalid version format. Expected: XX.XX.XXXX"
                )

            return FlextResult[str].ok(version)

        @staticmethod
        def validate_integration_data(
            integration_data: FlextTypes.Dict,
        ) -> FlextResult[FlextTypes.Dict]:
            """Validate complete Oracle OIC integration data.

            Args:
                integration_data: Integration configuration data

            Returns:
                FlextResult containing validated data or validation errors

            """
            if not isinstance(integration_data, dict):
                return FlextResult[FlextTypes.Dict].fail(
                    "Integration data must be a dictionary"
                )

            errors: FlextTypes.StringList = []
            validated_data = integration_data.copy()

            # Validate required fields
            if "name" not in integration_data:
                errors.append("Integration name is required")
            else:
                name_result = FlextOracleOicExtUtilities.IntegrationValidation.validate_integration_name(
                    integration_data["name"]
                )
                if name_result.is_failure:
                    errors.append(f"Name validation: {name_result.error}")
                else:
                    validated_data["name"] = name_result.value

            if "version" in integration_data:
                version_result = FlextOracleOicExtUtilities.IntegrationValidation.validate_integration_version(
                    integration_data["version"]
                )
                if version_result.is_failure:
                    errors.append(f"Version validation: {version_result.error}")
                else:
                    validated_data["version"] = version_result.value

            if "status" in integration_data:
                status_result = FlextOracleOicExtUtilities.IntegrationValidation.validate_integration_status(
                    integration_data["status"]
                )
                if status_result.is_failure:
                    errors.append(f"Status validation: {status_result.error}")
                else:
                    validated_data["status"] = status_result.value

            if errors:
                return FlextResult[FlextTypes.Dict].fail(
                    f"Integration validation failed: {'; '.join(errors)}"
                )

            return FlextResult[FlextTypes.Dict].ok(validated_data)

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
        def validate_connection_type(connection_type: str) -> FlextResult[str]:
            """Validate Oracle OIC connection type.

            Args:
                connection_type: Connection type to validate

            Returns:
                FlextResult containing validated type or error

            """
            if not isinstance(connection_type, str):
                return FlextResult[str].fail("Connection type must be a string")

            connection_type = connection_type.upper().strip()
            if (
                connection_type
                not in FlextOracleOicExtUtilities.ConnectionValidation.VALID_CONNECTION_TYPES
            ):
                valid_types = ", ".join(
                    sorted(
                        FlextOracleOicExtUtilities.ConnectionValidation.VALID_CONNECTION_TYPES
                    )
                )
                return FlextResult[str].fail(
                    f"Invalid connection type. Valid: {valid_types}"
                )

            return FlextResult[str].ok(connection_type)

        @staticmethod
        def validate_connection_status(status: str) -> FlextResult[str]:
            """Validate Oracle OIC connection status.

            Args:
                status: Connection status to validate

            Returns:
                FlextResult containing validated status or error

            """
            if not isinstance(status, str):
                return FlextResult[str].fail("Connection status must be a string")

            status = status.upper().strip()
            if (
                status
                not in FlextOracleOicExtUtilities.ConnectionValidation.VALID_CONNECTION_STATUSES
            ):
                valid_statuses = ", ".join(
                    sorted(
                        FlextOracleOicExtUtilities.ConnectionValidation.VALID_CONNECTION_STATUSES
                    )
                )
                return FlextResult[str].fail(
                    f"Invalid connection status. Valid: {valid_statuses}"
                )

            return FlextResult[str].ok(status)

        @staticmethod
        def validate_base_url(base_url: str) -> FlextResult[str]:
            """Validate Oracle OIC base URL format.

            Args:
                base_url: Base URL to validate

            Returns:
                FlextResult containing validated URL or error

            """
            if not isinstance(base_url, str):
                return FlextResult[str].fail("Base URL must be a string")

            base_url = base_url.strip()
            if not base_url:
                return FlextResult[str].fail("Base URL cannot be empty")

            # Parse URL
            try:
                parsed = urlparse(base_url)
                if not parsed.scheme:
                    return FlextResult[str].fail(
                        "Base URL must include protocol (https://)"
                    )

                if parsed.scheme not in {"http", "https"}:
                    return FlextResult[str].fail(
                        "Base URL must use HTTP or HTTPS protocol"
                    )

                if not parsed.netloc:
                    return FlextResult[str].fail("Base URL must include domain")

                # Oracle OIC URLs should typically use HTTPS
                if parsed.scheme == "http":
                    FlextLogger(__name__).warning(
                        "Base URL uses HTTP instead of HTTPS - consider security implications"
                    )

                return FlextResult[str].ok(base_url.rstrip("/"))

            except Exception as e:
                return FlextResult[str].fail(f"Invalid URL format: {e}")

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
        def validate_oauth_client_id(client_id: str) -> FlextResult[str]:
            """Validate OAuth2 client ID.

            Args:
                client_id: OAuth2 client ID to validate

            Returns:
                FlextResult containing validated client ID or error

            """
            if not isinstance(client_id, str):
                return FlextResult[str].fail("OAuth client ID must be a string")

            client_id = client_id.strip()
            if (
                len(client_id)
                < FlextOracleOicExtUtilities.AuthenticationValidation.MIN_CLIENT_ID_LENGTH
            ):
                return FlextResult[str].fail("OAuth client ID cannot be empty")

            # Check for basic format (alphanumeric, hyphens, underscores)
            if not re.match(r"^[a-zA-Z0-9_\-\.]+$", client_id):
                return FlextResult[str].fail(
                    "OAuth client ID contains invalid characters"
                )

            return FlextResult[str].ok(client_id)

        @staticmethod
        def validate_oauth_client_secret(
            client_secret: SecretStr,
        ) -> FlextResult[SecretStr]:
            """Validate OAuth2 client secret.

            Args:
                client_secret: OAuth2 client secret to validate

            Returns:
                FlextResult containing validated secret or error

            """
            if not isinstance(client_secret, SecretStr):
                return FlextResult[SecretStr].fail(
                    "OAuth client secret must be SecretStr"
                )

            secret_value = client_secret.get_secret_value()
            if not secret_value or not secret_value.strip():
                return FlextResult[SecretStr].fail(
                    "OAuth client secret cannot be empty"
                )

            if (
                len(secret_value)
                < FlextOracleOicExtUtilities.AuthenticationValidation.MIN_CLIENT_SECRET_LENGTH
            ):
                return FlextResult[SecretStr].fail(
                    "OAuth client secret must be at least 8 characters"
                )

            return FlextResult[SecretStr].ok(client_secret)

        @staticmethod
        def validate_oauth_token_url(token_url: str) -> FlextResult[str]:
            """Validate OAuth2 token endpoint URL.

            Args:
                token_url: OAuth2 token URL to validate

            Returns:
                FlextResult containing validated URL or error

            """
            if not isinstance(token_url, str):
                return FlextResult[str].fail("OAuth token URL must be a string")

            token_url = token_url.strip()
            if (
                len(token_url)
                < FlextOracleOicExtUtilities.AuthenticationValidation.MIN_TOKEN_URL_LENGTH
            ):
                return FlextResult[str].fail("OAuth token URL too short")

            # Validate URL format
            url_result = (
                FlextOracleOicExtUtilities.ConnectionValidation.validate_base_url(
                    token_url
                )
            )
            if url_result.is_failure:
                return FlextResult[str].fail(
                    f"Token URL validation: {url_result.error}"
                )

            # Additional OAuth-specific validation
            if "/oauth" not in token_url.lower() and "/token" not in token_url.lower():
                FlextLogger(__name__).warning(
                    "Token URL may not be a standard OAuth endpoint"
                )

            return FlextResult[str].ok(token_url)

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
            base_url: str, api_version: str = "v1", integration_id: str | None = None
        ) -> FlextResult[str]:
            """Build Oracle OIC integration API endpoint.

            Args:
                base_url: OIC instance base URL
                api_version: API version (default: v1)
                integration_id: Optional specific integration ID

            Returns:
                FlextResult containing constructed endpoint URL or error

            """
            # Validate base URL
            url_result = (
                FlextOracleOicExtUtilities.ConnectionValidation.validate_base_url(
                    base_url
                )
            )
            if url_result.is_failure:
                return FlextResult[str].fail(f"Base URL validation: {url_result.error}")

            validated_base_url = url_result.value

            # Build endpoint path
            path_parts = ["ic", "api", "integration", api_version, "integrations"]
            if integration_id:
                if not isinstance(integration_id, str) or not integration_id.strip():
                    return FlextResult[str].fail(
                        "Integration ID must be non-empty string"
                    )
                path_parts.append(integration_id.strip())

            endpoint_path = "/" + "/".join(path_parts)
            full_url = urljoin(validated_base_url + "/", endpoint_path.lstrip("/"))

            return FlextResult[str].ok(full_url)

        @staticmethod
        def build_connection_endpoint(
            base_url: str, api_version: str = "v1", connection_id: str | None = None
        ) -> FlextResult[str]:
            """Build Oracle OIC connection API endpoint.

            Args:
                base_url: OIC instance base URL
                api_version: API version (default: v1)
                connection_id: Optional specific connection ID

            Returns:
                FlextResult containing constructed endpoint URL or error

            """
            # Validate base URL
            url_result = (
                FlextOracleOicExtUtilities.ConnectionValidation.validate_base_url(
                    base_url
                )
            )
            if url_result.is_failure:
                return FlextResult[str].fail(f"Base URL validation: {url_result.error}")

            validated_base_url = url_result.value

            # Build endpoint path
            path_parts = ["ic", "api", "integration", api_version, "connections"]
            if connection_id:
                if not isinstance(connection_id, str) or not connection_id.strip():
                    return FlextResult[str].fail(
                        "Connection ID must be non-empty string"
                    )
                path_parts.append(connection_id.strip())

            endpoint_path = "/" + "/".join(path_parts)
            full_url = urljoin(validated_base_url + "/", endpoint_path.lstrip("/"))

            return FlextResult[str].ok(full_url)

        @staticmethod
        def build_request_headers(
            auth_token: str | None = None,
            content_type: str = "application/json",
            additional_headers: FlextTypes.StringDict | None = None,
        ) -> FlextResult[FlextTypes.StringDict]:
            """Build Oracle OIC API request headers.

            Args:
                auth_token: Optional authentication token
                content_type: Content type header (default: application/json)
                additional_headers: Optional additional headers

            Returns:
                FlextResult containing constructed headers or error

            """
            headers: FlextTypes.StringDict = {
                "Accept": "application/json",
                "Content-Type": content_type,
                "User-Agent": "FlextOracleOicExtension/1.0.0",
            }

            if auth_token:
                if not isinstance(auth_token, str) or not auth_token.strip():
                    return FlextResult[FlextTypes.StringDict].fail(
                        "Auth token must be non-empty string"
                    )
                headers["Authorization"] = f"Bearer {auth_token.strip()}"

            if additional_headers:
                if not isinstance(additional_headers, dict):
                    return FlextResult[FlextTypes.StringDict].fail(
                        "Additional headers must be a dictionary"
                    )
                headers.update(additional_headers)

            return FlextResult[FlextTypes.StringDict].ok(headers)

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
            integration_data: FlextTypes.Dict,
        ) -> FlextResult[str]:
            """Analyze Oracle OIC integration to determine pattern type.

            Args:
                integration_data: Integration configuration data

            Returns:
                FlextResult containing detected pattern or analysis error

            """
            if not isinstance(integration_data, dict):
                return FlextResult[str].fail("Integration data must be a dictionary")

            # Analyze based on common OIC integration characteristics
            endpoints = integration_data.get("endpoints", [])
            connections = integration_data.get("connections", [])
            mappings = integration_data.get("mappings", [])

            # Message Router: Multiple target endpoints from single source
            if (
                len(endpoints)
                > FlextOracleOicExtUtilities.PatternAnalysis.MIN_ENDPOINTS_FOR_ROUTER
                and any(
                    endpoint.get("direction") == "outbound" for endpoint in endpoints
                )
            ):
                return FlextResult[str].ok("message_router")

            # Scatter-Gather: Multiple parallel calls with aggregation
            if len(connections) > 1 and any(
                "aggregate" in str(mapping).lower() for mapping in mappings
            ):
                return FlextResult[str].ok("scatter_gather")

            # Publish-Subscribe: Event-driven pattern
            if any(
                "event" in str(endpoint).lower() or "publish" in str(endpoint).lower()
                for endpoint in endpoints
            ):
                return FlextResult[str].ok("publish_subscribe")

            # Request-Reply: Synchronous pattern (default)
            return FlextResult[str].ok("request_reply")

        @staticmethod
        def validate_pattern_configuration(
            pattern_type: str, configuration: FlextTypes.Dict
        ) -> FlextResult[FlextTypes.Dict]:
            """Validate Oracle OIC integration pattern configuration.

            Args:
                pattern_type: Integration pattern type
                configuration: Pattern-specific configuration

            Returns:
                FlextResult containing validated configuration or error

            """
            if (
                pattern_type
                not in FlextOracleOicExtUtilities.PatternAnalysis.SUPPORTED_PATTERNS
            ):
                supported = ", ".join(
                    sorted(
                        FlextOracleOicExtUtilities.PatternAnalysis.SUPPORTED_PATTERNS
                    )
                )
                return FlextResult[FlextTypes.Dict].fail(
                    f"Unsupported pattern type. Supported: {supported}"
                )

            if not isinstance(configuration, dict):
                return FlextResult[FlextTypes.Dict].fail(
                    "Configuration must be a dictionary"
                )

            validated_config = configuration.copy()

            # Pattern-specific validation
            if pattern_type == "message_router":
                if "routing_rules" not in configuration:
                    return FlextResult[FlextTypes.Dict].fail(
                        "Message router pattern requires routing_rules"
                    )

            elif pattern_type == "scatter_gather":
                if "target_services" not in configuration:
                    return FlextResult[FlextTypes.Dict].fail(
                        "Scatter-gather pattern requires target_services"
                    )
                if "aggregation_strategy" not in configuration:
                    validated_config["aggregation_strategy"] = "collect_all"

            if (
                pattern_type == "publish_subscribe"
                and "event_types" not in configuration
            ):
                return FlextResult[FlextTypes.Dict].fail(
                    "Publish-subscribe pattern requires event_types"
                )

            return FlextResult[FlextTypes.Dict].ok(validated_config)

    class MonitoringUtilities:
        """Oracle OIC monitoring and health check utilities."""

        # Monitoring constants
        HEALTH_CHECK_TIMEOUT: ClassVar[int] = 10
        PERFORMANCE_THRESHOLDS: ClassVar[FlextTypes.FloatDict] = {
            "response_time_ms": 5000.0,
            "success_rate": 0.95,
            "error_rate": 0.05,
        }

        @staticmethod
        def validate_health_status(
            health_data: FlextTypes.Dict,
        ) -> FlextResult[FlextTypes.Dict]:
            """Validate Oracle OIC health check data.

            Args:
                health_data: Health check response data

            Returns:
                FlextResult containing validated health data or error

            """
            if not isinstance(health_data, dict):
                return FlextResult[FlextTypes.Dict].fail(
                    "Health data must be a dictionary"
                )

            validated_data = health_data.copy()

            # Validate required health fields
            if "status" not in health_data:
                return FlextResult[FlextTypes.Dict].fail(
                    "Health data must include status"
                )

            status = health_data["status"]
            if status not in {"healthy", "unhealthy", "error", "unknown"}:
                return FlextResult[FlextTypes.Dict].fail(
                    "Invalid health status. Valid: healthy, unhealthy, error, unknown"
                )

            # Validate components if present
            if "components" in health_data:
                components = health_data["components"]
                if not isinstance(components, dict):
                    return FlextResult[FlextTypes.Dict].fail(
                        "Components must be a dictionary"
                    )

                for component_name, component_data in components.items():
                    if not isinstance(component_data, dict):
                        return FlextResult[FlextTypes.Dict].fail(
                            f"Component {component_name} data must be a dictionary"
                        )
                    if "status" not in component_data:
                        return FlextResult[FlextTypes.Dict].fail(
                            f"Component {component_name} must have status"
                        )

            # Add timestamp if not present
            if "timestamp" not in validated_data:
                validated_data["timestamp"] = datetime.now(UTC).isoformat()

            return FlextResult[FlextTypes.Dict].ok(validated_data)

        @staticmethod
        def analyze_performance_metrics(
            metrics: FlextTypes.Dict,
        ) -> FlextResult[FlextTypes.Dict]:
            """Analyze Oracle OIC performance metrics.

            Args:
                metrics: Performance metrics data

            Returns:
                FlextResult containing analysis results or error

            """
            if not isinstance(metrics, dict):
                return FlextResult[FlextTypes.Dict].fail("Metrics must be a dictionary")

            analysis: FlextTypes.Dict = {
                "overall_health": "healthy",
                "warnings": [],
                "critical_issues": [],
                "recommendations": [],
            }

            # Analyze response time
            if "average_response_time" in metrics:
                response_time = metrics["average_response_time"]
                if isinstance(response_time, (int, float)):
                    threshold = FlextOracleOicExtUtilities.MonitoringUtilities.PERFORMANCE_THRESHOLDS[
                        "response_time_ms"
                    ]
                    if response_time > threshold:
                        analysis["warnings"].append(
                            f"High response time: {response_time}ms (threshold: {threshold}ms)"
                        )
                        analysis["recommendations"].append(
                            "Consider optimizing integration mappings or connection pooling"
                        )

            # Analyze success rate
            if "success_rate" in metrics:
                success_rate = metrics["success_rate"]
                if isinstance(success_rate, (int, float)):
                    threshold = FlextOracleOicExtUtilities.MonitoringUtilities.PERFORMANCE_THRESHOLDS[
                        "success_rate"
                    ]
                    if success_rate < threshold:
                        analysis["critical_issues"].append(
                            f"Low success rate: {success_rate:.2%} (threshold: {threshold:.2%})"
                        )
                        analysis["overall_health"] = "unhealthy"
                        analysis["recommendations"].append(
                            "Investigate integration failures and error patterns"
                        )

            # Analyze error rate
            if "error_rate" in metrics:
                error_rate = metrics["error_rate"]
                if isinstance(error_rate, (int, float)):
                    threshold = FlextOracleOicExtUtilities.MonitoringUtilities.PERFORMANCE_THRESHOLDS[
                        "error_rate"
                    ]
                    if error_rate > threshold:
                        analysis["warnings"].append(
                            f"High error rate: {error_rate:.2%} (threshold: {threshold:.2%})"
                        )
                        analysis["recommendations"].append(
                            "Review error logs and implement error handling improvements"
                        )

            return FlextResult[FlextTypes.Dict].ok(analysis)
