"""Oracle OIC Extension utilities module.

This module provides domain-specific utilities for Oracle Integration Cloud (OIC)
operations, extending u with nested classes for complete
Oracle OIC integration functionality.

FLEXT COMPLIANCE: Follows [Project]Utilities pattern with:
- Single unified class extending u
- Nested classes for domain-specific functionality
- Python 3.13+ features and Pydantic 2.11+
- Railway-oriented programming with r
- Type-safe operations with proper validation
- SOLID principles with clean separation of concerns
"""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from datetime import UTC, datetime
from urllib.parse import urljoin

from flext_core import FlextUtilities, r
from pydantic import SecretStr

from flext_oracle_oic import c, m, t


class FlextOracleOicUtilities(FlextUtilities):
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
    - Immutable operations with r
    - Type-safe validation with Pydantic 2.11+
    - Railway-oriented error handling
    - No side effects in utility functions
    """

    class OracleOic:
        """Oracle OIC integration validation utilities."""

        @staticmethod
        def validate_integration_data(
            integration_data: Mapping[str, t.NormalizedValue],
        ) -> r[Mapping[str, t.NormalizedValue]]:
            """Validate complete Oracle OIC integration data.

            Args:
            integration_data: Integration configuration data

            Returns:
            r containing validated data or validation errors

            """
            if not isinstance(integration_data, Mapping):
                return r[Mapping[str, t.NormalizedValue]].fail(
                    "Integration data must be a dictionary",
                )
            errors: list[str] = []
            validated_data: dict[str, t.NormalizedValue] = {
                str(key): value for key, value in integration_data.items()
            }
            if "name" not in integration_data:
                errors.append("Integration name is required")
            else:
                raw_name = integration_data["name"]
                match raw_name:
                    case str():
                        name_result = (
                            FlextOracleOicUtilities.OracleOic.validate_integration_name(
                                raw_name,
                            )
                        )
                        if name_result.is_failure:
                            errors.append(f"Name validation: {name_result.error}")
                        else:
                            validated_data["name"] = name_result.value
                    case _:
                        errors.append(
                            "Name validation: Integration name must be a string",
                        )
            if "version" in integration_data:
                raw_version = integration_data["version"]
                match raw_version:
                    case str():
                        version_result = FlextOracleOicUtilities.OracleOic.validate_integration_version(
                            raw_version,
                        )
                        if version_result.is_failure:
                            errors.append(f"Version validation: {version_result.error}")
                        else:
                            validated_data["version"] = version_result.value
                    case _:
                        errors.append(
                            "Version validation: Integration version must be a string",
                        )
            if "status" in integration_data:
                raw_status = integration_data["status"]
                match raw_status:
                    case str():
                        status_result = FlextOracleOicUtilities.OracleOic.validate_integration_status(
                            raw_status,
                        )
                        if status_result.is_failure:
                            errors.append(f"Status validation: {status_result.error}")
                        else:
                            validated_data["status"] = status_result.value
                    case _:
                        errors.append(
                            "Status validation: Integration status must be a string",
                        )
            if errors:
                return r[Mapping[str, t.NormalizedValue]].fail(
                    f"Integration validation failed: {'; '.join(errors)}",
                )
            return r[Mapping[str, t.NormalizedValue]].ok(validated_data)

        @staticmethod
        def validate_integration_name(name: str) -> r[str]:
            """Validate Oracle OIC integration name.

            Args:
            name: Integration name to validate

            Returns:
            r containing validated name or validation error

            """
            match name:
                case str():
                    pass
                case _:
                    return r[str].fail("Integration name must be a string")
            name = name.strip()
            if not name:
                return r[str].fail("Integration name cannot be empty")
            if len(name) < c.OracleOicValidation.MIN_INTEGRATION_NAME_LENGTH:
                return r[str].fail("Integration name too short")
            if len(name) > c.OracleOicValidation.MAX_INTEGRATION_NAME_LENGTH:
                return r[str].fail("Integration name too long")
            if not re.match(r"^[a-zA-Z0-9_\\-\\s]+$", name):
                return r[str].fail("Integration name contains invalid characters")
            return r[str].ok(name)

        @staticmethod
        def validate_integration_status(status: str) -> r[str]:
            """Validate Oracle OIC integration status.

            Args:
            status: Integration status to validate

            Returns:
            r containing validated status or error

            """
            match status:
                case str():
                    pass
                case _:
                    return r[str].fail("Integration status must be a string")
            status = status.upper().strip()
            if status not in c.OracleOicValidation.VALID_INTEGRATION_STATUSES:
                valid_statuses = ", ".join(
                    sorted(c.OracleOicValidation.VALID_INTEGRATION_STATUSES),
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
            r containing validated version or error

            """
            match version:
                case str():
                    pass
                case _:
                    return r[str].fail("Integration version must be a string")
            version = version.strip()
            if not c.OracleOicValidation.VERSION_PATTERN.match(version):
                return r[str].fail("Invalid version format. Expected: XX.XX.XXXX")
            return r[str].ok(version)

    class ConnectionValidation:
        """Oracle OIC connection validation utilities."""

        @staticmethod
        def validate_base_url(base_url: str) -> r[str]:
            """Validate Oracle OIC base URL.

            Args:
            base_url: Base URL to validate

            Returns:
            r containing validated URL or error

            """
            match base_url:
                case str():
                    pass
                case _:
                    return r[str].fail("Base URL must be a string")
            base_url = base_url.strip()
            if not base_url:
                return r[str].fail("Base URL cannot be empty")
            if not base_url.startswith(("http://", "https://")):
                return r[str].fail("Base URL must start with http:// or https://")
            return r[str].ok(base_url)

        @staticmethod
        def validate_connection_status(status: str) -> r[str]:
            """Validate Oracle OIC connection status.

            Args:
            status: Connection status to validate

            Returns:
            r containing validated status or error

            """
            match status:
                case str():
                    pass
                case _:
                    return r[str].fail("Connection status must be a string")
            status = status.upper().strip()
            if status not in c.OracleOicValidation.VALID_CONNECTION_STATUSES:
                valid_statuses = ", ".join(
                    sorted(c.OracleOicValidation.VALID_CONNECTION_STATUSES),
                )
                return r[str].fail(
                    f"Invalid connection status. Valid: {valid_statuses}",
                )
            return r[str].ok(status)

        @staticmethod
        def validate_connection_type(connection_type: str) -> r[str]:
            """Validate Oracle OIC connection type.

            Args:
            connection_type: Connection type to validate

            Returns:
            r containing validated type or error

            """
            match connection_type:
                case str():
                    pass
                case _:
                    return r[str].fail("Connection type must be a string")
            connection_type = connection_type.upper().strip()
            if connection_type not in c.OracleOicValidation.VALID_CONNECTION_TYPES:
                valid_types = ", ".join(
                    sorted(c.OracleOicValidation.VALID_CONNECTION_TYPES),
                )
                return r[str].fail(f"Invalid connection type. Valid: {valid_types}")
            return r[str].ok(connection_type)

    class AuthenticationValidation:
        """Oracle OIC authentication validation utilities."""

        @staticmethod
        def validate_oauth_client_id(client_id: str) -> r[str]:
            """Validate OAuth2 client ID.

            Args:
            client_id: OAuth2 client ID to validate

            Returns:
            r containing validated client ID or error

            """
            match client_id:
                case str():
                    pass
                case _:
                    return r[str].fail("OAuth client ID must be a string")
            client_id = client_id.strip()
            if len(client_id) < c.OracleOicValidation.MIN_CLIENT_ID_LENGTH:
                return r[str].fail("OAuth client ID cannot be empty")
            if not re.match(r"^[a-zA-Z0-9_\\-\\.]+$", client_id):
                return r[str].fail("OAuth client ID contains invalid characters")
            return r[str].ok(client_id)

        @staticmethod
        def validate_oauth_client_secret(client_secret: SecretStr) -> r[SecretStr]:
            """Validate OAuth2 client secret.

            Args:
            client_secret: OAuth2 client secret to validate

            Returns:
            r containing validated secret or error

            """
            secret_value = client_secret.get_secret_value()
            if not secret_value or not secret_value.strip():
                return r[SecretStr].fail("OAuth client secret cannot be empty")
            if len(secret_value) < c.OracleOicValidation.MIN_CLIENT_SECRET_LENGTH:
                return r[SecretStr].fail(
                    "OAuth client secret must be at least 8 characters",
                )
            return r[SecretStr].ok(client_secret)

    class APIRequestBuilder:
        """Oracle OIC API request construction utilities."""

        @staticmethod
        def build_resource_endpoint(
            base_url: str,
            *,
            api_version: str,
            resource_name: str,
            resource_label: str,
            resource_id: str | None = None,
        ) -> r[str]:
            """Build Oracle OIC endpoint URL for a versioned resource path."""
            url_result = FlextOracleOicUtilities.ConnectionValidation.validate_base_url(
                base_url,
            )
            if url_result.is_failure:
                return r[str].fail(f"Base URL validation: {url_result.error}")
            validated_base_url = url_result.value
            path_parts = ["ic", "api", "integration", api_version, resource_name]
            if resource_id:
                match resource_id:
                    case str() as raw_resource_id if raw_resource_id.strip():
                        path_parts.append(raw_resource_id.strip())
                    case _:
                        return r[str].fail(f"{resource_label} must be non-empty string")
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
            r containing constructed endpoint URL or error

            """
            return FlextOracleOicUtilities.APIRequestBuilder.build_resource_endpoint(
                base_url=base_url,
                api_version=api_version,
                resource_name="connections",
                resource_label="Connection ID",
                resource_id=connection_id,
            )

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
            r containing constructed endpoint URL or error

            """
            return FlextOracleOicUtilities.APIRequestBuilder.build_resource_endpoint(
                base_url=base_url,
                api_version=api_version,
                resource_name="integrations",
                resource_label="Integration ID",
                resource_id=integration_id,
            )

        @staticmethod
        def build_request_headers(
            auth_token: str | None = None,
            content_type: str = "application/json",
            additional_headers: Mapping[str, str] | None = None,
        ) -> r[Mapping[str, str]]:
            """Build Oracle OIC API request headers.

            Args:
            auth_token: Optional authentication token
            content_type: Content type header (default: application/json)
            additional_headers: Optional additional headers

            Returns:
            r containing constructed headers or error

            """
            headers: dict[str, str] = {
                "Accept": "application/json",
                "Content-Type": content_type,
                "User-Agent": "FlextOracleOicension/1.0.0",
            }
            if auth_token:
                match auth_token:
                    case str() as raw_auth_token if raw_auth_token.strip():
                        headers["Authorization"] = f"Bearer {raw_auth_token.strip()}"
                    case _:
                        return r[Mapping[str, str]].fail(
                            "Auth token must be non-empty string",
                        )
            if additional_headers:
                if not isinstance(additional_headers, Mapping):
                    return r[Mapping[str, str]].fail(
                        "Additional headers must be a dictionary",
                    )
                headers.update({str(k): str(v) for k, v in additional_headers.items()})
            return r[Mapping[str, str]].ok(headers)

    class PatternAnalysis:
        """Oracle OIC integration pattern analysis utilities."""

        @staticmethod
        def analyze_integration_pattern(
            integration_data: Mapping[str, t.NormalizedValue],
        ) -> r[str]:
            """Analyze Oracle OIC integration to determine pattern type.

            Args:
            integration_data: Integration configuration data

            Returns:
            r containing detected pattern or analysis error

            """
            if not isinstance(integration_data, Mapping):
                return r[str].fail("Integration data must be a dictionary")
            endpoints_raw = integration_data.get("endpoints", [])
            connections_raw = integration_data.get("connections", [])
            mappings_raw = integration_data.get("mappings", [])
            endpoints: Sequence[Mapping[str, t.NormalizedValue]] = (
                [
                    dict(endpoint)
                    for endpoint in endpoints_raw
                    if isinstance(endpoint, dict)
                ]
                if isinstance(endpoints_raw, list)
                else []
            )
            connections: Sequence[t.NormalizedValue] = (
                list(connections_raw) if isinstance(connections_raw, list) else []
            )
            mappings: Sequence[t.NormalizedValue] = (
                list(mappings_raw) if isinstance(mappings_raw, list) else []
            )
            if len(endpoints) > c.OracleOicValidation.MIN_ENDPOINTS_FOR_ROUTER and any(
                endpoint.get("direction") == "outbound" for endpoint in endpoints
            ):
                return r[str].ok("message_router")
            if len(connections) > 1 and any(
                "aggregate" in str(mapping).lower() for mapping in mappings
            ):
                return r[str].ok("scatter_gather")
            if any(
                "event" in str(endpoint).lower() or "publish" in str(endpoint).lower()
                for endpoint in endpoints
            ):
                return r[str].ok("publish_subscribe")
            return r[str].ok("request_reply")

        @staticmethod
        def validate_pattern_configuration(
            pattern_type: str,
            configuration: m.OracleOic.MessageRouterPatternConfig
            | m.OracleOic.ScatterGatherPatternConfig,
        ) -> r[
            m.OracleOic.MessageRouterPatternConfig
            | m.OracleOic.ScatterGatherPatternConfig
        ]:
            """Validate Oracle OIC integration pattern configuration.

            Args:
            pattern_type: Integration pattern type
            configuration: Pattern-specific configuration

            Returns:
            r containing validated configuration or error

            """
            if pattern_type not in c.OracleOicValidation.SUPPORTED_PATTERNS:
                supported = ", ".join(sorted(c.OracleOicValidation.SUPPORTED_PATTERNS))
                return r[
                    m.OracleOic.MessageRouterPatternConfig
                    | m.OracleOic.ScatterGatherPatternConfig
                ].fail(
                    f"Unsupported pattern type. Supported: {supported}",
                )
            if pattern_type == "message_router":
                if not isinstance(
                    configuration,
                    m.OracleOic.MessageRouterPatternConfig,
                ):
                    return r[
                        m.OracleOic.MessageRouterPatternConfig
                        | m.OracleOic.ScatterGatherPatternConfig
                    ].fail(
                        "Message router pattern requires MessageRouterPatternConfig",
                    )
            elif pattern_type == "scatter_gather":
                if not isinstance(
                    configuration,
                    m.OracleOic.ScatterGatherPatternConfig,
                ):
                    return r[
                        m.OracleOic.MessageRouterPatternConfig
                        | m.OracleOic.ScatterGatherPatternConfig
                    ].fail(
                        "Scatter-gather pattern requires ScatterGatherPatternConfig",
                    )
            elif pattern_type == "publish_subscribe":
                configuration_data = configuration.model_dump(mode="python")
                if "event_types" not in configuration_data:
                    return r[
                        m.OracleOic.MessageRouterPatternConfig
                        | m.OracleOic.ScatterGatherPatternConfig
                    ].fail(
                        "Publish-subscribe pattern requires event_types",
                    )
            return r[
                m.OracleOic.MessageRouterPatternConfig
                | m.OracleOic.ScatterGatherPatternConfig
            ].ok(configuration)

    class MonitoringUtilities:
        """Oracle OIC monitoring and health check utilities."""

        @staticmethod
        def analyze_performance_metrics(
            metrics: Mapping[str, t.NormalizedValue],
        ) -> r[Mapping[str, t.NormalizedValue]]:
            """Analyze Oracle OIC performance metrics.

            Args:
            metrics: Performance metrics data

            Returns:
            r containing analysis results or error

            """
            if not isinstance(metrics, Mapping):
                return r[Mapping[str, t.NormalizedValue]].fail(
                    "Metrics must be a dictionary",
                )
            overall_health = "healthy"
            warnings: list[t.NormalizedValue] = []
            critical_issues: list[t.NormalizedValue] = []
            recommendations: list[t.NormalizedValue] = []
            if "average_response_time" in metrics:
                response_time = metrics["average_response_time"]
                if isinstance(response_time, (int, float)):
                    threshold = c.OracleOicValidation.PERFORMANCE_THRESHOLDS[
                        "response_time_ms"
                    ]
                    if response_time > threshold:
                        warnings.append(
                            f"High response time: {response_time}ms (threshold: {threshold}ms)",
                        )
                        recommendations.append(
                            "Consider optimizing integration mappings or connection pooling",
                        )
            if "success_rate" in metrics:
                success_rate = metrics["success_rate"]
                if isinstance(success_rate, (int, float)):
                    threshold = c.OracleOicValidation.PERFORMANCE_THRESHOLDS[
                        "success_rate"
                    ]
                    if success_rate < threshold:
                        critical_issues.append(
                            f"Low success rate: {success_rate:.2%} (threshold: {threshold:.2%})",
                        )
                        overall_health = "unhealthy"
                        recommendations.append(
                            "Investigate integration failures and error patterns",
                        )
            if "error_rate" in metrics:
                error_rate = metrics["error_rate"]
                if isinstance(error_rate, (int, float)):
                    threshold = c.OracleOicValidation.PERFORMANCE_THRESHOLDS[
                        "error_rate"
                    ]
                    if error_rate > threshold:
                        warnings.append(
                            f"High error rate: {error_rate:.2%} (threshold: {threshold:.2%})",
                        )
                        recommendations.append(
                            "Review error logs and implement error handling improvements",
                        )
            analysis: Mapping[str, t.NormalizedValue] = {
                "overall_health": overall_health,
                "warnings": tuple(warnings),
                "critical_issues": tuple(critical_issues),
                "recommendations": tuple(recommendations),
            }
            return r[Mapping[str, t.NormalizedValue]].ok(analysis)

        @staticmethod
        def validate_health_status(
            health_data: Mapping[str, t.NormalizedValue],
        ) -> r[Mapping[str, t.NormalizedValue]]:
            """Validate Oracle OIC health check data.

            Args:
            health_data: Health check response data

            Returns:
            r containing validated health data or error

            """
            if not isinstance(health_data, Mapping):
                return r[Mapping[str, t.NormalizedValue]].fail(
                    "Health data must be a dictionary",
                )
            validated_data: dict[str, t.NormalizedValue] = {
                str(key): value for key, value in health_data.items()
            }
            if "status" not in health_data:
                return r[Mapping[str, t.NormalizedValue]].fail(
                    "Health data must include status",
                )
            status = health_data["status"]
            if status not in {"healthy", "unhealthy", "error", "unknown"}:
                return r[Mapping[str, t.NormalizedValue]].fail(
                    "Invalid health status. Valid: healthy, unhealthy, error, unknown",
                )
            if "components" in health_data:
                components = health_data["components"]
                if not isinstance(components, dict):
                    return r[Mapping[str, t.NormalizedValue]].fail(
                        "Components must be a dictionary",
                    )
                for component_name, component_data in components.items():
                    if not isinstance(component_data, dict):
                        return r[Mapping[str, t.NormalizedValue]].fail(
                            f"Component {component_name} data must be a dictionary",
                        )
                    if "status" not in component_data:
                        return r[Mapping[str, t.NormalizedValue]].fail(
                            f"Component {component_name} must have status",
                        )
            if "timestamp" not in validated_data:
                validated_data["timestamp"] = datetime.now(UTC).isoformat()
            return r[Mapping[str, t.NormalizedValue]].ok(validated_data)


u = FlextOracleOicUtilities
__all__ = ["FlextOracleOicUtilities", "u"]
