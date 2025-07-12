"""Oracle OIC Extension Monitoring Service.

Copyright (c) 2025 FLEXT Team. All rights reserved.

Professional monitoring service for Oracle Integration Cloud extensions
using FLEXT core patterns and standards.
"""

from __future__ import annotations

import operator
from datetime import UTC, datetime, timedelta
from typing import TYPE_CHECKING, Any

from flext_observability import get_logger

if TYPE_CHECKING:
    import requests

log = get_logger(__name__)


class MonitoringService:
    """Enterprise monitoring service for Oracle OIC extensions.

    Provides comprehensive health checks, performance metrics, and error analysis
    for Oracle Integration Cloud using FLEXT core patterns.
    """

    def __init__(self, client: requests.Session) -> None:
        """Initialize monitoring service with HTTP client.

        Args:
            client: Configured HTTP session for OIC API calls.

        """
        self.client = client

    def get_health_status(self, detailed: bool = False) -> dict[str, Any]:
        """Get comprehensive health status of OIC environment.

        Args:
            detailed: Whether to include detailed component health checks.

        Returns:
            Health status with overall status and component details.

        """
        health_status: dict[str, Any] = {
            "status": "healthy",
            "timestamp": datetime.now(UTC).isoformat(),
            "components": {},
        }

        components = health_status["components"]

        # Check API health
        try:
            response = self.client.get("/ic/api/integration/v1/integrations?limit=1")
            if response.status_code == 200:
                components["api"] = "healthy"
            else:
                components["api"] = "unhealthy"
                health_status["status"] = "degraded"
        except Exception as e:
            components["api"] = "error"
            health_status["status"] = "unhealthy"
            log.exception("API health check failed", error=str(e))

        if detailed:
            health_status.update(self._detailed_health_check())

        return health_status

    def _detailed_health_check(self) -> dict[str, Any]:
        """Perform detailed health checks on OIC components."""
        return {
            "connections": self._check_connections_health(),
            "integrations": self._check_integrations_health(),
            "execution": self._check_execution_health(),
        }

    def _check_connections_health(self) -> dict[str, Any]:
        """Check health of OIC connections."""
        try:
            response = self.client.get("/ic/api/integration/v1/connections?limit=100")
            if response.status_code == 200:
                connections = response.json().get("items", [])
                active = sum(1 for c in connections if c.get("status") == "ACTIVE")
                total = len(connections)
                return {
                    "status": "healthy" if active > 0 else "warning",
                    "active": active,
                    "total": total,
                }
            return {"status": "error", "error": f"HTTP {response.status_code}"}
        except Exception as e:
            log.exception("Failed to check connections health", error=str(e))
            return {"status": "error", "error": str(e)}

    def _check_integrations_health(self) -> dict[str, Any]:
        """Check health of OIC integrations."""
        try:
            response = self.client.get("/ic/api/integration/v1/integrations?limit=100")
            if response.status_code == 200:
                integrations = response.json().get("items", [])
                active = sum(1 for i in integrations if i.get("status") == "ACTIVE")
                configured = sum(1 for i in integrations if i.get("status") == "CONFIGURED")
                total = len(integrations)
                return {
                    "status": "healthy" if active > 0 else "warning",
                    "active": active,
                    "configured": configured,
                    "total": total,
                }
            return {"status": "error", "error": f"HTTP {response.status_code}"}
        except Exception as e:
            log.exception("Failed to check integrations health", error=str(e))
            return {"status": "error", "error": str(e)}

    def _check_execution_health(self) -> dict[str, Any]:
        """Check health of recent OIC executions."""
        try:
            end_time = datetime.now(UTC)
            start_time = end_time - timedelta(hours=1)

            params: dict[str, str | int] = {
                "startdate": start_time.isoformat(),
                "enddate": end_time.isoformat(),
                "limit": 100,
            }

            response = self.client.get(
                "/ic/api/integration/v1/monitoring/instances",
                params=params,
            )

            if response.status_code == 200:
                instances = response.json().get("items", [])
                successful = sum(1 for i in instances if i.get("status") == "COMPLETED")
                failed = sum(1 for i in instances if i.get("status") == "FAILED")
                in_progress = sum(1 for i in instances if i.get("status") == "IN_PROGRESS")

                return {
                    "status": "healthy" if failed < successful else "warning",
                    "successful": successful,
                    "failed": failed,
                    "in_progress": in_progress,
                    "window": "1h",
                }
            return {"status": "error", "error": f"HTTP {response.status_code}"}
        except Exception as e:
            log.exception("Failed to check execution health", error=str(e))
            return {"status": "error", "error": str(e)}

    def get_performance_metrics(self, window_hours: int = 24) -> dict[str, Any]:
        """Get performance metrics for specified time window.

        Args:
            window_hours: Time window in hours for metrics collection.

        Returns:
            Performance metrics including throughput and execution statistics.

        """
        end_time = datetime.now(UTC)
        start_time = end_time - timedelta(hours=window_hours)

        metrics: dict[str, Any] = {
            "window": f"{window_hours}h",
            "timestamp": end_time.isoformat(),
        }

        try:
            params: dict[str, str | int] = {
                "startdate": start_time.isoformat(),
                "enddate": end_time.isoformat(),
                "limit": 1000,
            }

            response = self.client.get(
                "/ic/api/integration/v1/monitoring/instances",
                params=params,
            )

            if response.status_code == 200:
                instances = response.json().get("items", [])

                total_executions = len(instances)
                successful = sum(1 for i in instances if i.get("status") == "COMPLETED")
                failed = sum(1 for i in instances if i.get("status") == "FAILED")

                durations = [
                    instance["duration"]
                    for instance in instances
                    if instance.get("status") == "COMPLETED" and instance.get("duration")
                ]

                metrics["executions"] = {
                    "total": total_executions,
                    "successful": successful,
                    "failed": failed,
                    "success_rate": (
                        (successful / total_executions * 100)
                        if total_executions > 0 else 0
                    ),
                    "avg_duration_ms": (
                        sum(durations) / len(durations) if durations else 0
                    ),
                }

                metrics["throughput"] = self._calculate_throughput(instances, window_hours)

        except Exception as e:
            log.exception("Failed to get performance metrics", error=str(e))
            metrics["error"] = str(e)

        return metrics

    def _calculate_throughput(self, instances: list[dict[str, Any]], window_hours: int) -> dict[str, Any]:
        """Calculate throughput metrics from execution instances."""
        hourly_counts: dict[str, int] = {}

        for instance in instances:
            start_time_obj = instance.get("startTime")
            if start_time_obj and isinstance(start_time_obj, str):
                hour_key = start_time_obj[:13]  # YYYY-MM-DDTHH format
                hourly_counts[hour_key] = hourly_counts.get(hour_key, 0) + 1

        if hourly_counts:
            return {
                "avg_per_hour": sum(hourly_counts.values()) / len(hourly_counts),
                "max_per_hour": max(hourly_counts.values()),
                "min_per_hour": min(hourly_counts.values()),
            }

        return {
            "avg_per_hour": 0,
            "max_per_hour": 0,
            "min_per_hour": 0,
        }

    def analyze_errors(self, window_hours: int = 24, integration_id: str | None = None) -> dict[str, Any]:
        """Analyze error patterns in OIC executions.

        Args:
            window_hours: Time window for error analysis.
            integration_id: Optional filter for specific integration.

        Returns:
            Error analysis with patterns and recommendations.

        """
        end_time = datetime.now(UTC)
        start_time = end_time - timedelta(hours=window_hours)

        error_analysis: dict[str, Any] = {
            "window": f"{window_hours}h",
            "integration_filter": integration_id,
            "patterns": {},
            "recommendations": [],
        }

        try:
            params: dict[str, str | int] = {
                "startdate": start_time.isoformat(),
                "enddate": end_time.isoformat(),
                "limit": 1000,
            }

            if integration_id:
                params["integrationId"] = integration_id

            response = self.client.get(
                "/ic/api/integration/v1/monitoring/instances",
                params=params,
            )

            if response.status_code == 200:
                instances = response.json().get("items", [])
                failed_instances = [i for i in instances if i.get("status") == "FAILED"]

                error_analysis["summary"] = {
                    "total_instances": len(instances),
                    "failed_instances": len(failed_instances),
                    "error_rate": (
                        len(failed_instances) / len(instances) * 100
                        if instances else 0
                    ),
                }

                # Analyze error patterns
                error_patterns: dict[str, int] = {}
                for instance in failed_instances:
                    error_msg = instance.get("errorMessage", "Unknown error")
                    error_patterns[error_msg] = error_patterns.get(error_msg, 0) + 1

                error_analysis["patterns"] = dict(
                    sorted(error_patterns.items(), key=operator.itemgetter(1), reverse=True),
                )

                # Generate recommendations
                if len(failed_instances) > len(instances) * 0.1:  # >10% error rate
                    error_analysis["recommendations"].append(
                        "High error rate detected. Review integration configurations.",
                    )

        except Exception as e:
            log.exception("Failed to analyze errors", error=str(e))
            error_analysis["error"] = str(e)

        return error_analysis
