"""FLEXT Oracle OIC Monitoring - Health checks and performance metrics.

Mixin providing monitoring operations for the FlextOracleOicService facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import asyncio

from flext_api import FlextApiModels

from flext_core import p, r
from flext_oracle_oic import (
    FlextOracleOicServiceBase,
    FlextOracleOicUtilities,
    c,
    t,
)


class FlextOracleOicMonitoringMixin(FlextOracleOicServiceBase):
    """Mixin providing monitoring operations for FlextOracleOicService facade."""

    def get_health_status(self) -> p.Result[t.RecursiveContainerMapping]:
        """Get Oracle OIC health status using FlextOracleOicUtilities.

        Returns:
        r containing validated health status information

        """
        try:
            health_data: t.RecursiveContainerMapping
            if not self._monitoring_client:
                health_data = {
                    "status": c.Monitoring.HealthStatus.HEALTHY,
                    "components": {
                        c.Monitoring.COMPONENT_DATABASE: {
                            "status": c.Monitoring.ComponentStatus.HEALTHY,
                        },
                        c.Monitoring.COMPONENT_MESSAGING: {
                            "status": c.Monitoring.ComponentStatus.HEALTHY,
                        },
                        c.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                            "status": c.Monitoring.ComponentStatus.HEALTHY,
                        },
                    },
                    "timestamp": asyncio.get_event_loop().time(),
                }
            else:
                base = str(self._oic_settings.base_url).rstrip("/")
                health_url = f"{base}{c.API.ENDPOINT_HEALTH}"
                req = FlextApiModels.Api.HttpRequest(
                    method=c.API.Method.GET,
                    url=health_url,
                    headers={},
                    body={},
                    query_params={},
                    timeout=float(self._oic_settings.request_timeout),
                )
                response_result = self._monitoring_client.request(req)
                if response_result.success:
                    response = response_result.value
                    if response.status_code == c.API.HTTP_STATUS_OK:
                        base_health: t.RecursiveContainerMapping = (
                            {
                                str(k): self._to_general_value(v)
                                for k, v in response.body.items()
                            }
                            if isinstance(response.body, dict)
                            else {"raw": self._to_general_value(response.body)}
                        )
                        health_data = {
                            **base_health,
                            "status": c.Monitoring.HealthStatus.HEALTHY,
                            "components": {
                                c.Monitoring.COMPONENT_DATABASE: {
                                    "status": c.Monitoring.ComponentStatus.HEALTHY,
                                },
                                c.Monitoring.COMPONENT_MESSAGING: {
                                    "status": c.Monitoring.ComponentStatus.HEALTHY,
                                },
                                c.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                                    "status": c.Monitoring.ComponentStatus.HEALTHY,
                                },
                            },
                        }
                    else:
                        health_data = {
                            "status": c.Monitoring.HealthStatus.UNHEALTHY,
                            "components": {
                                c.Monitoring.COMPONENT_DATABASE: {
                                    "status": c.Monitoring.ComponentStatus.UNKNOWN,
                                },
                                c.Monitoring.COMPONENT_MESSAGING: {
                                    "status": c.Monitoring.ComponentStatus.UNKNOWN,
                                },
                                c.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                                    "status": c.Monitoring.ComponentStatus.UNKNOWN,
                                },
                            },
                            "error": f"HTTP {response.status_code}",
                        }
                else:
                    health_data = {
                        "status": c.Monitoring.HealthStatus.ERROR,
                        "components": {
                            c.Monitoring.COMPONENT_DATABASE: {
                                "status": c.Monitoring.ComponentStatus.UNKNOWN,
                            },
                            c.Monitoring.COMPONENT_MESSAGING: {
                                "status": c.Monitoring.ComponentStatus.UNKNOWN,
                            },
                            c.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                                "status": c.Monitoring.ComponentStatus.UNKNOWN,
                            },
                        },
                        "error": f"Request failed: {response_result.error}",
                    }
            health_data_dict: t.RecursiveContainerMapping = dict(health_data)
            validation_result = (
                FlextOracleOicUtilities.MonitoringUtilities.validate_health_status(
                    health_data_dict,
                )
            )
            if validation_result.success:
                return validation_result
            self.logger.warning(
                f"Health status validation failed: {validation_result.error}",
            )
            return r[t.RecursiveContainerMapping].ok(health_data_dict)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Health check failed")
            error_health: t.RecursiveContainerMapping = {
                "status": c.Monitoring.HealthStatus.ERROR,
                "components": {
                    c.Monitoring.COMPONENT_DATABASE: {
                        "status": c.Monitoring.ComponentStatus.UNKNOWN,
                    },
                    c.Monitoring.COMPONENT_MESSAGING: {
                        "status": c.Monitoring.ComponentStatus.UNKNOWN,
                    },
                    c.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                        "status": c.Monitoring.ComponentStatus.UNKNOWN,
                    },
                },
                "error": str(e),
            }
            validation_result = (
                FlextOracleOicUtilities.MonitoringUtilities.validate_health_status(
                    error_health,
                )
            )
            return (
                validation_result
                if validation_result.success
                else r[t.RecursiveContainerMapping].ok(error_health)
            )

    def get_performance_metrics(self) -> p.Result[t.RecursiveContainerMapping]:
        """Get Oracle OIC performance metrics with analysis using FlextOracleOicUtilities.

        Returns:
        r containing performance metrics with analysis

        """
        try:
            metrics_data: t.RecursiveContainerMapping
            if not self._monitoring_client:
                metrics_data = {
                    "active_integrations": 0,
                    "total_executions": 0,
                    "success_rate": 0.0,
                    "average_response_time": 0.0,
                    "timestamp": asyncio.get_event_loop().time(),
                }
            else:
                base = str(self._oic_settings.base_url).rstrip("/")
                metrics_url = f"{base}/ic/api/integration/v1/metrics"
                req = FlextApiModels.Api.HttpRequest(
                    method=c.API.Method.GET,
                    url=metrics_url,
                    headers={},
                    body={},
                    query_params={},
                    timeout=float(self._oic_settings.request_timeout),
                )
                response_result = self._monitoring_client.request(req)
                if response_result.success:
                    response = response_result.value
                    if response.status_code == c.API.HTTP_STATUS_OK:
                        if isinstance(response.body, dict):
                            metrics_data = {
                                str(k): self._to_general_value(v)
                                for k, v in response.body.items()
                            }
                        else:
                            fallback: t.RecursiveContainerMapping = {}
                            metrics_data = fallback
                    else:
                        metrics_data = {
                            "active_integrations": 0,
                            "total_executions": 0,
                            "success_rate": 0.0,
                            "average_response_time": 0.0,
                            "error": f"HTTP {response.status_code}",
                        }
                else:
                    metrics_data = {
                        "active_integrations": 0,
                        "total_executions": 0,
                        "success_rate": 0.0,
                        "average_response_time": 0.0,
                        "error": f"Request failed: {response_result.error}",
                    }
            metrics_dict: t.MutableRecursiveContainerMapping = {}
            for key, value in metrics_data.items():
                metrics_dict[str(key)] = self._to_general_value(value)
            analysis_result = (
                FlextOracleOicUtilities.MonitoringUtilities.analyze_performance_metrics(
                    metrics_dict,
                )
            )
            if analysis_result.success:
                return r[t.RecursiveContainerMapping].ok({
                    **metrics_dict,
                    "analysis": dict(analysis_result.value),
                })
            self.logger.warning(f"Performance analysis failed: {analysis_result.error}")
            return r[t.RecursiveContainerMapping].ok(metrics_dict)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Performance metrics failed")
            error_metrics: t.RecursiveContainerMapping = {
                "active_integrations": 0,
                "total_executions": 0,
                "success_rate": 0.0,
                "average_response_time": 0.0,
                "error": str(e),
            }
            analysis_result = (
                FlextOracleOicUtilities.MonitoringUtilities.analyze_performance_metrics(
                    error_metrics,
                )
            )
            if analysis_result.success:
                return r[t.RecursiveContainerMapping].ok({
                    **error_metrics,
                    "analysis": dict(analysis_result.value),
                })
            return r[t.RecursiveContainerMapping].ok(error_metrics)


__all__: list[str] = ["FlextOracleOicMonitoringMixin"]
