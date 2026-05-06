"""Oracle OIC monitoring and health check utilities mixin."""

from __future__ import annotations

from datetime import UTC, datetime

from flext_oracle_oic import c, p, r, t


class FlextOracleOicUtilitiesMonitoring:
    """Oracle OIC monitoring and health check utilities."""

    @staticmethod
    def _assess_metric(
        metric_key: str,
        metric_value: float,
    ) -> tuple[str | None, str | None, bool]:
        """Return warning/critical/recommendation for one metric."""
        match metric_key:
            case "average_response_time":
                threshold = c.OracleOicValidation.PERFORMANCE_THRESHOLDS[
                    "response_time_ms"
                ]
                if metric_value > threshold:
                    return (
                        f"High response time: {metric_value}ms (threshold: {threshold}ms)",
                        "Consider optimizing integration mappings or connection pooling",
                        False,
                    )
            case "success_rate":
                threshold = c.OracleOicValidation.PERFORMANCE_THRESHOLDS["success_rate"]
                if metric_value < threshold:
                    return (
                        f"Low success rate: {metric_value:.2%} (threshold: {threshold:.2%})",
                        "Investigate integration failures and error patterns",
                        True,
                    )
            case "error_rate":
                threshold = c.OracleOicValidation.PERFORMANCE_THRESHOLDS["error_rate"]
                if metric_value > threshold:
                    return (
                        f"High error rate: {metric_value:.2%} (threshold: {threshold:.2%})",
                        "Review error logs and implement error handling improvements",
                        False,
                    )
            case _:
                pass
        return (None, None, False)

    @staticmethod
    def _components_validation_error(components: p.AttributeProbe) -> str | None:
        """Return first component-validation error, if any."""
        if not isinstance(components, dict):
            return "Components must be a dictionary"
        for component_name, component_data in components.items():
            if not isinstance(component_data, dict):
                return f"Component {component_name} data must be a dictionary"
            if "status" not in component_data:
                return f"Component {component_name} must have status"
        return None

    @staticmethod
    def analyze_performance_metrics(
        metrics: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Analyze Oracle OIC performance metrics.

        Args:
        metrics: Performance metrics data

        Returns:
        r containing analysis results or error

        """
        overall_health: str = c.HealthStatus.HEALTHY.value
        warnings: list[str] = []
        critical_issues: list[str] = []
        recommendations: list[str] = []
        for metric_key in ("average_response_time", "success_rate", "error_rate"):
            metric_value_raw = metrics.get(metric_key)
            if not isinstance(metric_value_raw, (int, float)):
                continue
            metric_value = float(metric_value_raw)
            issue, recommendation, is_critical = (
                FlextOracleOicUtilitiesMonitoring._assess_metric(
                    metric_key,
                    metric_value,
                )
            )
            if issue is None:
                continue
            if is_critical:
                critical_issues.append(issue)
                overall_health = c.HealthStatus.UNHEALTHY.value
            else:
                warnings.append(issue)
            if recommendation is not None:
                recommendations.append(recommendation)
        analysis = {
            "overall_health": overall_health,
            "warnings": list(warnings),
            "critical_issues": list(critical_issues),
            "recommendations": list(recommendations),
        }
        return r[t.JsonMapping].ok(
            t.CONTAINER_MAPPING_ADAPTER.validate_python(analysis),
        )

    @staticmethod
    def validate_health_status(
        health_data: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Validate Oracle OIC health check data.

        Args:
        health_data: Health check response data

        Returns:
        r containing validated health data or error

        """
        validated_data = t.json_dict_adapter().validate_python(health_data)
        error_message: str | None = None
        status = health_data.get("status")
        valid_statuses = {
            c.Monitoring.HealthStatus.HEALTHY.value,
            c.Monitoring.HealthStatus.UNHEALTHY.value,
            c.Monitoring.HealthStatus.ERROR.value,
            c.Monitoring.HealthStatus.UNKNOWN.value,
        }
        if status is None:
            error_message = "Health data must include status"
        elif status not in valid_statuses:
            error_message = (
                "Invalid health status. Valid: healthy, unhealthy, error, unknown"
            )
        else:
            components = health_data.get("components")
            if components is not None:
                error_message = (
                    FlextOracleOicUtilitiesMonitoring._components_validation_error(
                        components,
                    )
                )
        if error_message is not None:
            return r[t.JsonMapping].fail(error_message)
        if "timestamp" not in validated_data:
            validated_data["timestamp"] = datetime.now(UTC).isoformat()
        return r[t.JsonMapping].ok(validated_data)
