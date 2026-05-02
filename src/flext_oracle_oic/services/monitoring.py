"""FLEXT Oracle OIC Monitoring - Health checks and performance metrics.

Mixin providing monitoring operations for the FlextOracleOicService facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import asyncio
from collections.abc import Mapping

from flext_core import p, r
from flext_oracle_oic.constants import c
from flext_oracle_oic.models import m
from flext_oracle_oic.services.base import FlextOracleOicServiceBase
from flext_oracle_oic.typings import t
from flext_oracle_oic.utilities import u


class FlextOracleOicMonitoringMixin(FlextOracleOicServiceBase):
    """Mixin providing monitoring operations for FlextOracleOicService facade."""

    def fetch_health_status(self) -> p.Result[t.JsonMapping]:
        """Get Oracle OIC health status using u.

        Returns:
        r containing validated health status information

        """
        try:
            health_data: t.JsonMapping
            if not self._monitoring_client:
                health_data = t.CONTAINER_MAPPING_ADAPTER.validate_python({
                    "status": c.Monitoring.HealthStatus.HEALTHY.value,
                    "components": {
                        c.Monitoring.COMPONENT_DATABASE: {
                            "status": c.Monitoring.ComponentStatus.HEALTHY.value,
                        },
                        c.Monitoring.COMPONENT_MESSAGING: {
                            "status": c.Monitoring.ComponentStatus.HEALTHY.value,
                        },
                        c.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                            "status": c.Monitoring.ComponentStatus.HEALTHY.value,
                        },
                    },
                    "timestamp": asyncio.get_event_loop().time(),
                })
            else:
                base = self._oic_settings.base_url.rstrip("/")
                health_url = f"{base}{c.API.ENDPOINT_HEALTH}"
                req = m.Api.HttpRequest(
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
                        base_health: t.JsonMapping = (
                            {
                                k: self._to_general_value(v)
                                for k, v in response.body.items()
                            }
                            if isinstance(response.body, Mapping)
                            else {"raw": self._to_general_value(response.body)}
                        )
                        health_data = t.CONTAINER_MAPPING_ADAPTER.validate_python({
                            **base_health,
                            "status": c.Monitoring.HealthStatus.HEALTHY.value,
                            "components": {
                                c.Monitoring.COMPONENT_DATABASE: {
                                    "status": c.Monitoring.ComponentStatus.HEALTHY.value,
                                },
                                c.Monitoring.COMPONENT_MESSAGING: {
                                    "status": c.Monitoring.ComponentStatus.HEALTHY.value,
                                },
                                c.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                                    "status": c.Monitoring.ComponentStatus.HEALTHY.value,
                                },
                            },
                        })
                    else:
                        health_data = t.CONTAINER_MAPPING_ADAPTER.validate_python({
                            "status": c.Monitoring.HealthStatus.UNHEALTHY.value,
                            "components": {
                                c.Monitoring.COMPONENT_DATABASE: {
                                    "status": c.Monitoring.ComponentStatus.UNKNOWN.value,
                                },
                                c.Monitoring.COMPONENT_MESSAGING: {
                                    "status": c.Monitoring.ComponentStatus.UNKNOWN.value,
                                },
                                c.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                                    "status": c.Monitoring.ComponentStatus.UNKNOWN.value,
                                },
                            },
                            "error": f"HTTP {response.status_code}",
                        })
                else:
                    health_data = t.CONTAINER_MAPPING_ADAPTER.validate_python({
                        "status": c.Monitoring.HealthStatus.ERROR.value,
                        "components": {
                            c.Monitoring.COMPONENT_DATABASE: {
                                "status": c.Monitoring.ComponentStatus.UNKNOWN.value,
                            },
                            c.Monitoring.COMPONENT_MESSAGING: {
                                "status": c.Monitoring.ComponentStatus.UNKNOWN.value,
                            },
                            c.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                                "status": c.Monitoring.ComponentStatus.UNKNOWN.value,
                            },
                        },
                        "error": f"Request failed: {response_result.error}",
                    })
            validation_result: p.Result[t.JsonMapping] = (
                u.MonitoringUtilities.validate_health_status(
                    health_data,
                )
            )
            if validation_result.success:
                return validation_result
            self.logger.warning(
                f"Health status validation failed: {validation_result.error}",
            )
            return r[t.JsonMapping].ok(health_data)
        except c.EXC_NETWORK_TYPE as e:
            self.logger.exception("Health check failed")
            error_health = t.CONTAINER_MAPPING_ADAPTER.validate_python({
                "status": c.Monitoring.HealthStatus.ERROR.value,
                "components": {
                    c.Monitoring.COMPONENT_DATABASE: {
                        "status": c.Monitoring.ComponentStatus.UNKNOWN.value,
                    },
                    c.Monitoring.COMPONENT_MESSAGING: {
                        "status": c.Monitoring.ComponentStatus.UNKNOWN.value,
                    },
                    c.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                        "status": c.Monitoring.ComponentStatus.UNKNOWN.value,
                    },
                },
                "error": str(e),
            })
            error_validation_result: p.Result[t.JsonMapping] = (
                u.MonitoringUtilities.validate_health_status(
                    error_health,
                )
            )
            return (
                error_validation_result
                if error_validation_result.success
                else r[t.JsonMapping].ok(error_health)
            )

    def fetch_performance_metrics(self) -> p.Result[t.JsonMapping]:
        """Get Oracle OIC performance metrics with analysis using u.

        Returns:
        r containing performance metrics with analysis

        """
        base_metrics = t.CONTAINER_MAPPING_ADAPTER.validate_python({
            "active_integrations": 0,
            "total_executions": 0,
            "success_rate": 0.0,
            "average_response_time": 0.0,
        })
        metrics_data: t.JsonMapping = base_metrics
        try:
            if not self._monitoring_client:
                metrics_data = t.CONTAINER_MAPPING_ADAPTER.validate_python({
                    **base_metrics,
                    "timestamp": asyncio.get_event_loop().time(),
                })
            else:
                base = self._oic_settings.base_url.rstrip("/")
                metrics_url = f"{base}/ic/api/integration/v1/metrics"
                req = m.Api.HttpRequest(
                    method=c.API.Method.GET,
                    url=metrics_url,
                    headers={},
                    body={},
                    query_params={},
                    timeout=float(self._oic_settings.request_timeout),
                )
                response_result = self._monitoring_client.request(req)
                if response_result.failure:
                    metrics_data = t.CONTAINER_MAPPING_ADAPTER.validate_python({
                        **base_metrics,
                        "error": f"Request failed: {response_result.error}",
                    })
                else:
                    response = response_result.value
                    match (response.status_code, response.body):
                        case (c.API.HTTP_STATUS_OK, Mapping() as body):
                            metrics_data = t.CONTAINER_MAPPING_ADAPTER.validate_python(
                                {
                                    key: self._to_general_value(value)
                                    for key, value in body.items()
                                },
                            )
                        case (c.API.HTTP_STATUS_OK, _):
                            metrics_data = t.CONTAINER_MAPPING_ADAPTER.validate_python(
                                {},
                            )
                        case (status_code, _):
                            metrics_data = t.CONTAINER_MAPPING_ADAPTER.validate_python({
                                **base_metrics,
                                "error": f"HTTP {status_code}",
                            })
            metrics_dict: t.MutableJsonMapping = {}
            for key, value in metrics_data.items():
                metrics_dict[key] = self._to_general_value(value)
            analysis_result: p.Result[t.JsonMapping] = (
                u.MonitoringUtilities.analyze_performance_metrics(
                    metrics_dict,
                )
            )
            if analysis_result.success:
                metrics_dict["analysis"] = dict(analysis_result.value)
            else:
                self.logger.warning(
                    f"Performance analysis failed: {analysis_result.error}",
                )
        except c.EXC_NETWORK_TYPE as e:
            self.logger.exception("Performance metrics failed")
            error_metrics = t.CONTAINER_MAPPING_ADAPTER.validate_python({
                **base_metrics,
                "error": str(e),
            })
            metrics_dict = {
                key: self._to_general_value(value)
                for key, value in error_metrics.items()
            }
            error_analysis_result: p.Result[t.JsonMapping] = (
                u.MonitoringUtilities.analyze_performance_metrics(
                    metrics_dict,
                )
            )
            if error_analysis_result.success:
                metrics_dict["analysis"] = dict(error_analysis_result.value)
        return r[t.JsonMapping].ok(metrics_dict)


__all__: list[str] = ["FlextOracleOicMonitoringMixin"]
