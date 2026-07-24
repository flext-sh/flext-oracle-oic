"""FLEXT Oracle OIC Monitoring - Health checks and performance metrics.

Mixin providing monitoring operations for the FlextOracleOicService facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import asyncio
from collections.abc import Mapping

from flext_core import r
from flext_oracle_oic import c, m, p, t, u
from flext_oracle_oic.services.base import FlextOracleOicServiceBase


class FlextOracleOicMonitoringMixin(FlextOracleOicServiceBase):
    """Mixin providing monitoring operations for FlextOracleOicService facade."""

    def fetch_health_status(self) -> p.Result[t.JsonMapping]:
        """Get Oracle OIC health status using u.

        Returns:
        r containing validated health status information

        """
        try:
            health_data = self._fetch_health_status_data()
            return self._validate_health_status_data(health_data)
        except c.EXC_NETWORK_TYPE as e:
            self.logger.exception("Health check failed")
            return self._exception_health_status(e)

    @staticmethod
    def _component_statuses(status: str) -> t.JsonMapping:
        """Build canonical monitoring component status payload."""
        return t.json_mapping_adapter().validate_python({
            c.Monitoring.COMPONENT_DATABASE: {"status": status},
            c.Monitoring.COMPONENT_MESSAGING: {"status": status},
            c.Monitoring.COMPONENT_INTEGRATION_ENGINE: {"status": status},
        })

    def _fetch_health_status_data(self) -> t.JsonMapping:
        """Fetch health status payload without exception translation."""
        if not self._monitoring_client:
            return t.json_mapping_adapter().validate_python({
                "status": c.Monitoring.HealthStatus.HEALTHY.value,
                "components": self._component_statuses(
                    c.Monitoring.ComponentStatus.HEALTHY.value
                ),
                "timestamp": asyncio.get_event_loop().time(),
            })
        base = self._oic_settings.OracleOic.base_url.rstrip("/")
        health_url = f"{base}{c.API.ENDPOINT_HEALTH}"
        req = m.Api.HttpRequest(
            method=c.API.Method.GET,
            url=health_url,
            headers={},
            body={},
            query_params={},
            timeout=float(self._oic_settings.OracleOic.request_timeout),
        )
        response_result = self._monitoring_client.request(req)
        if response_result.failure:
            return t.json_mapping_adapter().validate_python({
                "status": c.Monitoring.HealthStatus.ERROR.value,
                "components": self._component_statuses(
                    c.Monitoring.ComponentStatus.UNKNOWN.value
                ),
                "error": f"Request failed: {response_result.error}",
            })
        response = response_result.value
        if response.status_code != c.API.HTTP_STATUS_OK:
            return t.json_mapping_adapter().validate_python({
                "status": c.Monitoring.HealthStatus.UNHEALTHY.value,
                "components": self._component_statuses(
                    c.Monitoring.ComponentStatus.UNKNOWN.value
                ),
                "error": f"HTTP {response.status_code}",
            })
        base_health: t.JsonMapping = (
            {k: self._to_general_value(v) for k, v in response.body.items()}
            if isinstance(response.body, Mapping)
            else {"raw": self._to_general_value(response.body)}
        )
        return t.json_mapping_adapter().validate_python({
            **base_health,
            "status": c.Monitoring.HealthStatus.HEALTHY.value,
            "components": self._component_statuses(
                c.Monitoring.ComponentStatus.HEALTHY.value
            ),
        })

    def _validate_health_status_data(
        self, health_data: t.JsonMapping
    ) -> p.Result[t.JsonMapping]:
        """Validate a health status payload."""
        validation_result: p.Result[t.JsonMapping] = (
            u.MonitoringUtilities.validate_health_status(health_data)
        )
        if validation_result.success:
            return validation_result
        self.logger.warning(
            f"Health status validation failed: {validation_result.error}"
        )
        return r[t.JsonMapping].ok(health_data)

    def _exception_health_status(self, exc: BaseException) -> p.Result[t.JsonMapping]:
        """Build health status result for translated exceptions."""
        error_health = t.json_mapping_adapter().validate_python({
            "status": c.Monitoring.HealthStatus.ERROR.value,
            "components": self._component_statuses(
                c.Monitoring.ComponentStatus.UNKNOWN.value
            ),
            "error": str(exc),
        })
        error_validation_result: p.Result[t.JsonMapping] = (
            u.MonitoringUtilities.validate_health_status(error_health)
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
        base_metrics = t.json_mapping_adapter().validate_python({
            "active_integrations": 0,
            "total_executions": 0,
            "success_rate": 0.0,
            "average_response_time": 0.0,
        })
        try:
            metrics_data = self._fetch_performance_metrics_data(base_metrics)
            metrics_dict = self._metrics_with_analysis(metrics_data)
        except c.EXC_NETWORK_TYPE as e:
            self.logger.exception("Performance metrics failed")
            metrics_dict = self._exception_metrics(base_metrics, e)
        return r[t.JsonMapping].ok(metrics_dict)

    def _fetch_performance_metrics_data(
        self, base_metrics: t.JsonMapping
    ) -> t.JsonMapping:
        """Fetch performance metrics without exception translation."""
        if not self._monitoring_client:
            return t.json_mapping_adapter().validate_python({
                **base_metrics,
                "timestamp": asyncio.get_event_loop().time(),
            })
        base = self._oic_settings.OracleOic.base_url.rstrip("/")
        metrics_url = f"{base}/ic/api/integration/v1/metrics"
        req = m.Api.HttpRequest(
            method=c.API.Method.GET,
            url=metrics_url,
            headers={},
            body={},
            query_params={},
            timeout=float(self._oic_settings.OracleOic.request_timeout),
        )
        response_result = self._monitoring_client.request(req)
        if response_result.failure:
            return t.json_mapping_adapter().validate_python({
                **base_metrics,
                "error": f"Request failed: {response_result.error}",
            })
        response = response_result.value
        if response.status_code != c.API.HTTP_STATUS_OK:
            return t.json_mapping_adapter().validate_python({
                **base_metrics,
                "error": f"HTTP {response.status_code}",
            })
        if isinstance(response.body, Mapping):
            return t.json_mapping_adapter().validate_python({
                key: self._to_general_value(value)
                for key, value in response.body.items()
            })
        return t.json_mapping_adapter().validate_python({})

    def _metrics_with_analysis(
        self, metrics_data: t.JsonMapping
    ) -> t.MutableJsonMapping:
        """Normalize performance metrics and attach analysis when available."""
        metrics_dict: t.MutableJsonMapping = {}
        for key, value in metrics_data.items():
            metrics_dict[key] = self._to_general_value(value)
        analysis_result: p.Result[t.JsonMapping] = (
            u.MonitoringUtilities.analyze_performance_metrics(metrics_dict)
        )
        if analysis_result.success:
            metrics_dict["analysis"] = dict(analysis_result.value)
        else:
            self.logger.warning(f"Performance analysis failed: {analysis_result.error}")
        return metrics_dict

    def _exception_metrics(
        self, base_metrics: t.JsonMapping, exc: BaseException
    ) -> t.MutableJsonMapping:
        """Build performance metrics result for translated exceptions."""
        error_metrics = t.json_mapping_adapter().validate_python({
            **base_metrics,
            "error": str(exc),
        })
        return self._metrics_with_analysis(error_metrics)


__all__: list[str] = ["FlextOracleOicMonitoringMixin"]
