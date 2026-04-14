"""Oracle OIC monitoring and health check utilities mixin."""

from __future__ import annotations

from collections.abc import MutableSequence
from datetime import UTC, datetime

from flext_core import p, r
from flext_oracle_oic import c, t


class FlextOracleOicUtilitiesMonitoring:
    """Oracle OIC monitoring and health check utilities."""

    @staticmethod
    def analyze_performance_metrics(
        metrics: t.RecursiveContainerMapping,
    ) -> p.Result[t.RecursiveContainerMapping]:
        """Analyze Oracle OIC performance metrics.

        Args:
        metrics: Performance metrics data

        Returns:
        r containing analysis results or error

        """
        overall_health: str = c.HealthStatus.HEALTHY.value
        warnings: MutableSequence[t.RecursiveContainer] = []
        critical_issues: MutableSequence[t.RecursiveContainer] = []
        recommendations: MutableSequence[t.RecursiveContainer] = []
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
                threshold = c.OracleOicValidation.PERFORMANCE_THRESHOLDS["success_rate"]
                if success_rate < threshold:
                    critical_issues.append(
                        f"Low success rate: {success_rate:.2%} (threshold: {threshold:.2%})",
                    )
                    overall_health = c.HealthStatus.UNHEALTHY.value
                    recommendations.append(
                        "Investigate integration failures and error patterns",
                    )
        if "error_rate" in metrics:
            error_rate = metrics["error_rate"]
            if isinstance(error_rate, (int, float)):
                threshold = c.OracleOicValidation.PERFORMANCE_THRESHOLDS["error_rate"]
                if error_rate > threshold:
                    warnings.append(
                        f"High error rate: {error_rate:.2%} (threshold: {threshold:.2%})",
                    )
                    recommendations.append(
                        "Review error logs and implement error handling improvements",
                    )
        analysis: t.RecursiveContainerMapping = {
            "overall_health": overall_health,
            "warnings": tuple(warnings),
            "critical_issues": tuple(critical_issues),
            "recommendations": tuple(recommendations),
        }
        return r[t.RecursiveContainerMapping].ok(analysis)

    @staticmethod
    def validate_health_status(
        health_data: t.RecursiveContainerMapping,
    ) -> p.Result[t.RecursiveContainerMapping]:
        """Validate Oracle OIC health check data.

        Args:
        health_data: Health check response data

        Returns:
        r containing validated health data or error

        """
        validated_data: t.MutableRecursiveContainerMapping = {
            str(key): value for key, value in health_data.items()
        }
        if "status" not in health_data:
            return r[t.RecursiveContainerMapping].fail(
                "Health data must include status",
            )
        status = health_data["status"]
        if status not in {
            c.Monitoring.HealthStatus.HEALTHY.value,
            c.Monitoring.HealthStatus.UNHEALTHY.value,
            c.Monitoring.HealthStatus.ERROR.value,
            c.Monitoring.HealthStatus.UNKNOWN.value,
        }:
            return r[t.RecursiveContainerMapping].fail(
                "Invalid health status. Valid: healthy, unhealthy, error, unknown",
            )
        if "components" in health_data:
            components = health_data["components"]
            if not isinstance(components, dict):
                return r[t.RecursiveContainerMapping].fail(
                    "Components must be a dictionary",
                )
            for component_name, component_data in components.items():
                if not isinstance(component_data, dict):
                    return r[t.RecursiveContainerMapping].fail(
                        f"Component {component_name} data must be a dictionary",
                    )
                if "status" not in component_data:
                    return r[t.RecursiveContainerMapping].fail(
                        f"Component {component_name} must have status",
                    )
        if "timestamp" not in validated_data:
            validated_data["timestamp"] = datetime.now(UTC).isoformat()
        return r[t.RecursiveContainerMapping].ok(validated_data)
