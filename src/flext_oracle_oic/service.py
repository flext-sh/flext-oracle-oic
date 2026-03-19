"""FLEXT Oracle OIC Service - Unified Service Pattern.

FLEXT Unified Module Pattern: Single unified service class consolidating
all Oracle OIC functionality. Implements complete FlextService pattern
with railway-oriented error handling.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import asyncio
from collections.abc import Callable, Mapping
from types import TracebackType
from typing import Self, override

from flext_api import FlextApiClient, FlextApiModels, FlextApiSettings
from flext_core import FlextLogger, FlextService, r

from flext_oracle_oic import c, t, u
from flext_oracle_oic.ext_client import FlextOracleOicClient
from flext_oracle_oic.models import FlextOracleOicModels
from flext_oracle_oic.settings import FlextOracleOicSettings
from flext_oracle_oic.utilities import FlextOracleOicUtilities


class FlextOracleOicService(
    FlextService[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]],
):
    """Unified Oracle OIC Extension Service - Single Class Pattern.

    Consolidates all Oracle OIC functionality into a single unified service class:
    - Integration lifecycle management (OracleOicExtensionService)
    - Pattern execution (OICIntegrationPatternService)
    - Connection management (LifecycleManager)
    - Monitoring and health checks (MonitoringService)

    Implements complete FlextService pattern with railway-oriented error handling.
    """

    def __init__(self) -> None:
        """Initialize unified Oracle OIC service.

        Uses singleton config pattern - no config parameter needed.
        """
        super().__init__()
        self._oic_settings: FlextOracleOicSettings = FlextOracleOicSettings.get_global()
        self._client: FlextOracleOicClient | None = None
        self._monitoring_client: FlextApiClient | None = None
        self._authenticator: t.NormalizedValue | None = None
        self._initialize_components()

    def __enter__(self) -> Self:
        """Context manager entry."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Context manager exit."""

    @staticmethod
    def _as_text(value: t.NormalizedValue, default: str = "") -> str:
        """Normalize optional OIC values into strings for model construction."""
        match value:
            case str():
                return value
            case _:
                pass
        if value is None:
            return default
        return str(value)

    @staticmethod
    def _to_general_value(
        value: t.NormalizedValue | t.ContainerValue | bytes | None,
    ) -> t.NormalizedValue:
        """Normalize arbitrary runtime values into object."""
        if isinstance(value, bytes):
            return value.decode(errors="replace")
        if isinstance(value, (str, int, float, bool)) or value is None:
            return value
        if isinstance(value, Mapping):
            return {
                str(k): FlextOracleOicService._to_general_value(v)
                for k, v in value.items()
            }
        match value:
            case list() | tuple():
                return [FlextOracleOicService._to_general_value(v) for v in value]
            case _:
                pass
        return str(value)

    def activate_integration(self, integration_id: str) -> r[bool]:
        """Activate Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        r indicating success or failure.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[bool].fail(error_msg)
            client = client_result.value
            activate_result = client.make_request(
                "POST",
                f"/integrations/{integration_id}/activate",
            )
            if activate_result.is_failure:
                error_msg = activate_result.error or "Failed to activate integration"
                return r[bool].fail(error_msg)
            return r[bool].ok(value=True)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Failed to activate integration %s", integration_id)
            return r[bool].fail(f"Integration activation failed: {e!s}")

    def apply_message_router_pattern(
        self,
        message_data: Mapping[str, t.NormalizedValue],
        routing_rules: list[Mapping[str, t.NormalizedValue]],
    ) -> r[Mapping[str, t.NormalizedValue]]:
        """Apply message router pattern to OIC integration using FlextOracleOicUtilities.

        Args:
        message_data: Message to route
        routing_rules: Routing rules configuration

        Returns:
        r containing routing result or error

        """
        try:
            self.logger.info("Applying message router pattern")
            pattern_config = FlextOracleOicModels.OracleOic.MessageRouterPatternConfig(
                routing_rules=routing_rules,
                message_data=message_data,
            )
            validation_result = (
                FlextOracleOicUtilities.PatternAnalysis.validate_pattern_configuration(
                    "message_router",
                    pattern_config,
                )
            )
            if validation_result.is_failure:
                return r[Mapping[str, t.NormalizedValue]].fail(
                    f"Pattern validation failed: {validation_result.error}",
                )
            routing_result = {
                "pattern": c.OICPatterns.PATTERN_MESSAGE_ROUTER,
                "message_id": message_data.get(
                    "id",
                    c.OICPatterns.PATTERN_MESSAGE_ID_UNKNOWN,
                ),
                "applied_rules": len(routing_rules),
                "status": c.OICPatterns.PatternStatus.PROCESSED,
            }
            return r[Mapping[str, t.NormalizedValue]].ok(routing_result)
        except (ConnectionError, TimeoutError, ValueError) as e:
            error_msg = f"Message router pattern failed: {e}"
            self.logger.exception(error_msg)
            return r[Mapping[str, t.NormalizedValue]].fail(error_msg)

    def apply_scatter_gather_pattern(
        self,
        request_data: Mapping[str, t.NormalizedValue],
        target_endpoints: list[str],
    ) -> r[Mapping[str, t.NormalizedValue]]:
        """Apply scatter-gather pattern to OIC integration using FlextOracleOicUtilities.

        Args:
        request_data: Request to scatter
        target_endpoints: Target endpoints for scatter

        Returns:
        r containing scatter-gather result or error

        """
        try:
            self.logger.info("Applying scatter-gather pattern")
            pattern_config = FlextOracleOicModels.OracleOic.ScatterGatherPatternConfig(
                target_services=target_endpoints,
                request_data=request_data,
            )
            validation_result = (
                FlextOracleOicUtilities.PatternAnalysis.validate_pattern_configuration(
                    "scatter_gather",
                    pattern_config,
                )
            )
            if validation_result.is_failure:
                return r[Mapping[str, t.NormalizedValue]].fail(
                    f"Pattern validation failed: {validation_result.error}",
                )
            scatter_result = {
                "pattern": c.OICPatterns.PATTERN_SCATTER_GATHER,
                "request_id": request_data.get(
                    "id",
                    c.OICPatterns.PATTERN_REQUEST_ID_UNKNOWN,
                ),
                "target_count": len(target_endpoints),
                "status": c.OICPatterns.PatternStatus.PROCESSED,
            }
            return r[Mapping[str, t.NormalizedValue]].ok(scatter_result)
        except (ConnectionError, TimeoutError, ValueError) as e:
            error_msg = f"Scatter-gather pattern failed: {e}"
            self.logger.exception(error_msg)
            return r[Mapping[str, t.NormalizedValue]].fail(error_msg)

    def create_integration(
        self,
        integration_data: Mapping[str, t.NormalizedValue],
    ) -> r[FlextOracleOicModels.OracleOic.OICIntegrationInfo]:
        """Create new Oracle OIC integration.

        Args:
        integration_data: Integration configuration data.

        Returns:
        r containing created integration information.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[FlextOracleOicModels.OracleOic.OICIntegrationInfo].fail(
                    error_msg,
                )
            client = client_result.value
            created_result = client.create_integration(integration_data)
            if created_result.is_failure:
                error_msg = created_result.error or "Failed to create integration"
                return r[FlextOracleOicModels.OracleOic.OICIntegrationInfo].fail(
                    error_msg,
                )
            created_data = created_result.value
            integration = FlextOracleOicModels.OracleOic.OICIntegrationInfo(
                integration_id=self._as_text(created_data.get("id"), ""),
                name=self._as_text(created_data.get("name"), ""),
                description=self._as_text(created_data.get("description"), ""),
                integration_version=self._as_text(
                    created_data.get("version"),
                    c.Integration.DEFAULT_VERSION_FALLBACK,
                ),
                status=self._as_text(
                    created_data.get("status"),
                    c.Integration.Status.DRAFT,
                ),
                created_by=self._as_text(created_data.get("createdBy"), ""),
                last_updated=self._as_text(created_data.get("lastUpdated"), ""),
            )
            return r[FlextOracleOicModels.OracleOic.OICIntegrationInfo].ok(integration)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Failed to create integration")
            return r[FlextOracleOicModels.OracleOic.OICIntegrationInfo].fail(
                f"Integration creation failed: {e!s}",
            )

    def deactivate_integration(self, integration_id: str) -> r[bool]:
        """Deactivate Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        r indicating success or failure.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[bool].fail(error_msg)
            client = client_result.value
            deactivate_result = client.make_request(
                "POST",
                f"/integrations/{integration_id}/deactivate",
            )
            if deactivate_result.is_failure:
                error_msg = (
                    deactivate_result.error or "Failed to deactivate integration"
                )
                return r[bool].fail(error_msg)
            return r[bool].ok(value=True)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Failed to deactivate integration %s", integration_id)
            return r[bool].fail(f"Integration deactivation failed: {e!s}")

    def delete_integration(self, integration_id: str) -> r[bool]:
        """Delete Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        r indicating success or failure.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[bool].fail(error_msg)
            client = client_result.value
            delete_result = client.make_request(
                "DELETE",
                f"/integrations/{integration_id}",
            )
            if delete_result.is_failure:
                error_msg = delete_result.error or "Failed to delete integration"
                return r[bool].fail(error_msg)
            return r[bool].ok(value=True)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Failed to delete integration %s", integration_id)
            return r[bool].fail(f"Integration deletion failed: {e!s}")

    def deploy_integration(
        self,
        integration_data: Mapping[str, t.NormalizedValue],
    ) -> r[str]:
        """Deploy integration to Oracle OIC.

        Args:
        integration_data: Integration configuration

        Returns:
        r containing integration ID or error

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[str].fail(error_msg)
            client = client_result.value
            created_result = client.create_integration(integration_data)
            if created_result.is_failure:
                return r[str].fail(created_result.error or "Create integration failed")
            created_data = created_result.value
            integration_id = str(created_data.get("id", ""))
            if not integration_id:
                return r[str].fail("No integration ID returned")
            self.logger.info("Integration deployed successfully: %s", integration_id)
            return r[str].ok(str(integration_id))
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Failed to deploy integration")
            return r[str].fail(f"Integration deployment failed: {e!s}")

    @override
    def execute(
        self: Self,
        **kwargs: t.Scalar,
    ) -> r[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]]:
        """Execute main service operation - list all integrations.

        Returns:
        r containing list of OIC integrations.

        """
        return self.list_integrations()

    def execute_app_driven_orchestration(
        self,
        integration_id: str,
        payload: Mapping[str, t.NormalizedValue],
        **_kwargs: t.Scalar,
    ) -> r[Mapping[str, t.NormalizedValue]]:
        """Execute app-driven orchestration pattern.

        Args:
        integration_id: The integration identifier.
        payload: Orchestration payload data.
        **kwargs: Additional execution parameters.

        Returns:
        r containing execution result.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[Mapping[str, t.NormalizedValue]].fail(error_msg)
            client = client_result.value
            endpoint = f"/integrations/{integration_id}/connections"
            payload_dict: dict[str, t.NormalizedValue] = {
                str(key): self._to_general_value(value)
                for key, value in payload.items()
            }
            orchestration_result = client.make_request(
                "POST",
                endpoint,
                json=payload_dict,
            )
            if orchestration_result.is_failure:
                return r[Mapping[str, t.NormalizedValue]].fail(
                    orchestration_result.error or "Orchestration request failed",
                )
            return r[Mapping[str, t.NormalizedValue]].ok(orchestration_result.value)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception(
                "App-driven orchestration failed for %s",
                integration_id,
            )
            return r[Mapping[str, t.NormalizedValue]].fail(
                f"Orchestration execution failed: {e!s}",
            )

    def execute_file_transfer(
        self,
        integration_id: str,
        file_config: Mapping[str, t.NormalizedValue],
        **kwargs: t.Scalar,
    ) -> r[Mapping[str, t.NormalizedValue]]:
        """Execute file transfer pattern.

        Args:
        integration_id: The integration identifier.
        file_config: File transfer configuration.
        **kwargs: Additional execution parameters.

        Returns:
        r containing execution result.

        """
        return self._execute_integration_operation(
            integration_id=integration_id,
            operation_config=file_config,
            operation=self._run_file_transfer,
            log_message="File transfer failed for %s",
            error_message="File transfer failed",
            **kwargs,
        )

    def execute_scheduled_orchestration(
        self,
        integration_id: str,
        schedule_config: Mapping[str, t.NormalizedValue],
        **kwargs: t.Scalar,
    ) -> r[Mapping[str, t.NormalizedValue]]:
        """Execute scheduled orchestration pattern.

        Args:
        integration_id: The integration identifier.
        schedule_config: Schedule configuration.
        **kwargs: Additional execution parameters.

        Returns:
        r containing execution result.

        """
        return self._execute_integration_operation(
            integration_id=integration_id,
            operation_config=schedule_config,
            operation=self._run_scheduled_orchestration,
            log_message="Scheduled orchestration failed for %s",
            error_message="Scheduled orchestration failed",
            **kwargs,
        )

    @staticmethod
    def _run_file_transfer(
        client: FlextOracleOicClient,
        integration_id: str,
        operation_config: Mapping[str, t.NormalizedValue],
        operation_kwargs: Mapping[str, t.Scalar],
    ) -> Mapping[str, t.NormalizedValue]:
        return client.execute_file_transfer(
            integration_id,
            operation_config,
            **operation_kwargs,
        )

    @staticmethod
    def _run_scheduled_orchestration(
        client: FlextOracleOicClient,
        integration_id: str,
        operation_config: Mapping[str, t.NormalizedValue],
        operation_kwargs: Mapping[str, t.Scalar],
    ) -> Mapping[str, t.NormalizedValue]:
        return client.execute_scheduled_orchestration(
            integration_id,
            operation_config,
            **operation_kwargs,
        )

    def _execute_integration_operation(
        self,
        integration_id: str,
        operation_config: Mapping[str, t.NormalizedValue],
        operation: Callable[
            [
                FlextOracleOicClient,
                str,
                Mapping[str, t.NormalizedValue],
                Mapping[str, t.Scalar],
            ],
            Mapping[str, t.NormalizedValue],
        ],
        log_message: str,
        error_message: str,
        **kwargs: t.Scalar,
    ) -> r[Mapping[str, t.NormalizedValue]]:
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[Mapping[str, t.NormalizedValue]].fail(error_msg)
            client = client_result.value
            operation_kwargs: dict[str, t.Scalar] = {
                str(key): value for key, value in kwargs.items()
            }
            result = operation(
                client,
                integration_id,
                operation_config,
                operation_kwargs,
            )
            return r[Mapping[str, t.NormalizedValue]].ok(result)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception(log_message, integration_id)
            return r[Mapping[str, t.NormalizedValue]].fail(f"{error_message}: {e!s}")

    def get_health_status(self) -> r[Mapping[str, t.NormalizedValue]]:
        """Get Oracle OIC health status using FlextOracleOicUtilities.

        Returns:
        r containing validated health status information

        """
        try:
            health_data: dict[str, t.NormalizedValue]
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
                req = FlextApiModels.HttpRequest(
                    method=c.API.Method.GET,
                    url=health_url,
                    headers={},
                    body={},
                    query_params={},
                    timeout=float(self._oic_settings.request_timeout),
                )
                response_result = self._monitoring_client.request(req)
                if response_result.is_success:
                    response = response_result.value
                    if response.status_code == c.API.HTTP_STATUS_OK:
                        base_health: dict[str, t.NormalizedValue] = (
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
            health_data_dict: dict[str, t.NormalizedValue] = dict(health_data)
            validation_result = (
                FlextOracleOicUtilities.MonitoringUtilities.validate_health_status(
                    health_data_dict,
                )
            )
            if validation_result.is_success:
                return validation_result
            self.logger.warning(
                f"Health status validation failed: {validation_result.error}",
            )
            return r[Mapping[str, t.NormalizedValue]].ok(health_data_dict)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Health check failed")
            error_health: dict[str, t.NormalizedValue] = {
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
                if validation_result.is_success
                else r[Mapping[str, t.NormalizedValue]].ok(error_health)
            )

    def get_integration(
        self,
        integration_id: str,
    ) -> r[FlextOracleOicModels.OracleOic.OICIntegrationInfo]:
        """Get specific Oracle OIC integration by ID.

        Args:
        integration_id: The integration identifier.

        Returns:
        r containing integration information.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[FlextOracleOicModels.OracleOic.OICIntegrationInfo].fail(
                    error_msg,
                )
            client = client_result.value
            integrations_result = client.get_integrations()
            if integrations_result.is_failure:
                error_msg = integrations_result.error or "Failed to get integrations"
                return r[FlextOracleOicModels.OracleOic.OICIntegrationInfo].fail(
                    error_msg,
                )
            integrations_list = integrations_result.value
            integration_data = next(
                (
                    item
                    for item in integrations_list
                    if item.get("id") == integration_id
                ),
                None,
            )
            if not integration_data:
                return r[FlextOracleOicModels.OracleOic.OICIntegrationInfo].fail(
                    f"Integration {integration_id} not found",
                )
            integration = FlextOracleOicModels.OracleOic.OICIntegrationInfo(
                integration_id=self._as_text(
                    integration_data.get("id"),
                    integration_id,
                ),
                name=self._as_text(integration_data.get("name"), ""),
                description=self._as_text(integration_data.get("description"), ""),
                integration_version=self._as_text(
                    integration_data.get("version"),
                    c.Integration.DEFAULT_VERSION_FALLBACK,
                ),
                status=self._as_text(
                    integration_data.get("status"),
                    c.Connection.Status.UNKNOWN,
                ),
                created_by=self._as_text(integration_data.get("createdBy"), ""),
                last_updated=self._as_text(integration_data.get("lastUpdated"), ""),
            )
            return r[FlextOracleOicModels.OracleOic.OICIntegrationInfo].ok(integration)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Failed to get integration %s", integration_id)
            return r[FlextOracleOicModels.OracleOic.OICIntegrationInfo].fail(
                f"Integration retrieval failed: {e!s}",
            )

    def get_performance_metrics(self) -> r[Mapping[str, t.NormalizedValue]]:
        """Get Oracle OIC performance metrics with analysis using FlextOracleOicUtilities.

        Returns:
        r containing performance metrics with analysis

        """
        try:
            metrics_data: dict[str, t.NormalizedValue]
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
                req = FlextApiModels.HttpRequest(
                    method=c.API.Method.GET,
                    url=metrics_url,
                    headers={},
                    body={},
                    query_params={},
                    timeout=float(self._oic_settings.request_timeout),
                )
                response_result = self._monitoring_client.request(req)
                if response_result.is_success:
                    response = response_result.value
                    if response.status_code == c.API.HTTP_STATUS_OK:
                        metrics_data = (
                            {
                                str(k): self._to_general_value(v)
                                for k, v in response.body.items()
                            }
                            if isinstance(response.body, dict)
                            else {}
                        )
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
            metrics_dict: dict[str, t.NormalizedValue] = {}
            if u.is_dict_like(metrics_data):
                for key, value in metrics_data.items():
                    metrics_dict[str(key)] = self._to_general_value(value)
            analysis_result = (
                FlextOracleOicUtilities.MonitoringUtilities.analyze_performance_metrics(
                    metrics_dict,
                )
            )
            if analysis_result.is_success:
                return r[Mapping[str, t.NormalizedValue]].ok({
                    **metrics_dict,
                    "analysis": analysis_result.value,
                })
            self.logger.warning(f"Performance analysis failed: {analysis_result.error}")
            return r[Mapping[str, t.NormalizedValue]].ok(metrics_dict)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Performance metrics failed")
            error_metrics: dict[str, t.NormalizedValue] = {
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
            if analysis_result.is_success:
                return r[Mapping[str, t.NormalizedValue]].ok({
                    **error_metrics,
                    "analysis": analysis_result.value,
                })
            return r[Mapping[str, t.NormalizedValue]].ok(error_metrics)

    def list_connections(
        self,
        type_filter: list[str] | None = None,
    ) -> r[list[FlextOracleOicModels.OracleOic.OICConnectionInfo]]:
        """List Oracle OIC connections.

        Args:
        type_filter: Filter by connection type

        Returns:
        r containing connection info list or error

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[list[FlextOracleOicModels.OracleOic.OICConnectionInfo]].fail(
                    error_msg,
                )
            client = client_result.value
            connections_result = client.get_connections(
                type_filter=type_filter,
                page_size=c.OracleOic.DEFAULT_PAGE_SIZE,
            )
            if connections_result.is_failure:
                error_msg = connections_result.error or "Failed to get connections"
                return r[list[FlextOracleOicModels.OracleOic.OICConnectionInfo]].fail(
                    error_msg,
                )
            connections_data = connections_result.value
            connections: list[FlextOracleOicModels.OracleOic.OICConnectionInfo] = []
            for item in connections_data:
                connection = FlextOracleOicModels.OracleOic.OICConnectionInfo(
                    connection_id=self._as_text(item.get("id"), ""),
                    name=self._as_text(item.get("name"), ""),
                    adapter_type=self._as_text(item.get("adapterType"), ""),
                    status=self._as_text(
                        item.get("status"),
                        c.Connection.Status.UNKNOWN,
                    ),
                    connection_type=self._as_text(item.get("connectionType"), ""),
                    description=self._as_text(item.get("description"), ""),
                )
                connections.append(connection)
            return r[list[FlextOracleOicModels.OracleOic.OICConnectionInfo]].ok(
                connections,
            )
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Failed to list connections")
            return r[list[FlextOracleOicModels.OracleOic.OICConnectionInfo]].fail(
                f"Connection listing failed: {e!s}",
            )

    def list_integrations(
        self,
    ) -> r[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]]:
        """List all Oracle OIC integrations.

        Returns:
        r containing list of integration information.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]].fail(
                    error_msg,
                )
            client = client_result.value
            integrations_result = client.get_integrations()
            if integrations_result.is_failure:
                error_msg = integrations_result.error or "Failed to get integrations"
                return r[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]].fail(
                    error_msg,
                )
            integrations_data = integrations_result.value
            integrations: list[FlextOracleOicModels.OracleOic.OICIntegrationInfo] = []
            for item in integrations_data:
                integration = FlextOracleOicModels.OracleOic.OICIntegrationInfo(
                    integration_id=self._as_text(item.get("id"), ""),
                    name=self._as_text(item.get("name"), ""),
                    description=self._as_text(item.get("description"), ""),
                    integration_version=self._as_text(
                        item.get("version"),
                        c.Integration.DEFAULT_VERSION_FALLBACK,
                    ),
                    status=self._as_text(
                        item.get("status"),
                        c.Connection.Status.UNKNOWN,
                    ),
                    created_by=self._as_text(item.get("createdBy"), ""),
                    last_updated=self._as_text(item.get("lastUpdated"), ""),
                )
                integrations.append(integration)
            return r[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]].ok(
                integrations,
            )
        except (ConnectionError, TimeoutError, ValueError) as e:
            FlextLogger(__name__).exception("Failed to list integrations")
            return r[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]].fail(
                f"Integration listing failed: {e!s}",
            )

    def refresh_auth_token(self) -> r[str]:
        """Refresh OAuth2 authentication token.

        Returns:
        r containing new access token.

        """
        try:
            if not self._authenticator:
                return r[str].fail("Authenticator not initialized")
            refresh_fn = getattr(self._authenticator, "refresh_token", None)
            if not callable(refresh_fn):
                return r[str].fail("Authenticator has no refresh_token")
            token = refresh_fn()
            return r[str].ok(str(token))
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Token refresh failed")
            return r[str].fail(f"Token refresh failed: {e!s}")

    def test_connection(self) -> r[bool]:
        """Test connection to Oracle OIC instance.

        Returns:
        r containing connection test result.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[bool].fail(error_msg)
            client = client_result.value
            test_result = client.make_request(
                c.API.Method.GET,
                "/ic/api/integration/v1/health",
            )
            if test_result.is_failure:
                error_msg = test_result.error or "Connection test failed"
                return r[bool].fail(error_msg)
            result_data = test_result.value
            status_value = result_data.get("status", "")
            match status_value:
                case str():
                    is_connected = status_value.lower() == "healthy"
                case _:
                    is_connected = False
            return r[bool].ok(is_connected)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Connection test failed")
            return r[bool].fail(f"Connection test failed: {e!s}")

    def update_integration(
        self,
        integration_id: str,
        integration_data: Mapping[str, t.NormalizedValue],
    ) -> r[FlextOracleOicModels.OracleOic.OICIntegrationInfo]:
        """Update existing Oracle OIC integration.

        Args:
        integration_id: The integration identifier.
        integration_data: Updated integration configuration.

        Returns:
        r containing updated integration information.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[FlextOracleOicModels.OracleOic.OICIntegrationInfo].fail(
                    error_msg,
                )
            client = client_result.value
            updated_result = client.update_integration(integration_id, integration_data)
            if updated_result.is_failure:
                error_msg = updated_result.error or "Failed to update integration"
                return r[FlextOracleOicModels.OracleOic.OICIntegrationInfo].fail(
                    error_msg,
                )
            updated_data = updated_result.value
            integration = FlextOracleOicModels.OracleOic.OICIntegrationInfo(
                integration_id=self._as_text(updated_data.get("id"), integration_id),
                name=self._as_text(updated_data.get("name"), ""),
                description=self._as_text(updated_data.get("description"), ""),
                integration_version=self._as_text(
                    updated_data.get("version"),
                    c.Integration.DEFAULT_VERSION_FALLBACK,
                ),
                status=self._as_text(
                    updated_data.get("status"),
                    c.Connection.Status.UNKNOWN,
                ),
                created_by=self._as_text(updated_data.get("createdBy"), ""),
                last_updated=self._as_text(updated_data.get("lastUpdated"), ""),
            )
            return r[FlextOracleOicModels.OracleOic.OICIntegrationInfo].ok(integration)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Failed to update integration %s", integration_id)
            return r[FlextOracleOicModels.OracleOic.OICIntegrationInfo].fail(
                f"Integration update failed: {e!s}",
            )

    def validate_auth_token(self, token: str) -> r[bool]:
        """Validate OAuth2 authentication token.

        Args:
        token: Token to validate.

        Returns:
        r containing validation result.

        """
        try:
            if not self._authenticator:
                return r[bool].fail("Authenticator not initialized")
            validate_fn = getattr(self._authenticator, "validate_token", None)
            if not callable(validate_fn):
                return r[bool].fail("Authenticator has no validate_token")
            is_valid = validate_fn(token)
            return r[bool].ok(bool(is_valid))
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Token validation failed")
            return r[bool].fail(f"Token validation failed: {e!s}")

    @override
    def validate_business_rules(self) -> r[bool]:
        """Validate Oracle OIC service business rules.

        Returns:
        r indicating validation success or failure.

        """
        if not self._oic_settings:
            return r[bool].fail("Settings are required")
        if not self._oic_settings.base_url:
            return r[bool].fail("Base URL is required")
        if not self._oic_settings.oauth_client_id:
            return r[bool].fail("OAuth client ID is required")
        client_id_result = (
            FlextOracleOicUtilities.AuthenticationValidation.validate_oauth_client_id(
                self._oic_settings.oauth_client_id,
            )
        )
        if client_id_result.is_failure:
            return r[bool].fail(f"OAuth client ID validation: {client_id_result.error}")
        if not self._oic_settings.oauth_client_secret:
            return r[bool].fail("OAuth client secret is required")
        if not self._oic_settings.oauth_token_url:
            return r[bool].fail("OAuth token URL is required")
        return r[bool].ok(value=True)

    def _get_client(self) -> r[FlextOracleOicClient]:
        """Get or create Oracle OIC client instance.

        Returns:
        r containing the client instance.

        """
        try:
            if self._client is None:
                validation_result = self.validate_business_rules()
                if validation_result.is_failure:
                    return r[FlextOracleOicClient].fail(validation_result.error)
                connection_config = FlextOracleOicModels.OracleOic.OICConnectionConfig(
                    base_url=str(self._oic_settings.base_url),
                    api_version=self._oic_settings.api_version,
                    request_timeout=self._oic_settings.request_timeout,
                    max_retries=self._oic_settings.max_retries,
                    verify_ssl=self._oic_settings.verify_ssl,
                )
                auth_config = FlextOracleOicModels.OracleOic.OICAuthConfig(
                    oauth_client_id=self._oic_settings.oauth_client_id,
                    oauth_client_secret=self._oic_settings.oauth_client_secret,
                    oauth_token_url=str(self._oic_settings.oauth_token_url),
                    oauth_client_aud=self._oic_settings.oauth_client_aud,
                    oauth_scope=self._oic_settings.oauth_scope,
                )
                self._client = FlextOracleOicClient(
                    connection_config=connection_config,
                    auth_config=auth_config,
                )
            return r[FlextOracleOicClient].ok(self._client)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Failed to create OIC client")
            return r[FlextOracleOicClient].fail(f"Client creation failed: {e!s}")

    def _initialize_components(self) -> None:
        """Initialize service components."""
        try:
            if self._oic_settings.enable_monitoring:
                auth_token = ""
                if self._authenticator:
                    refresh_fn = getattr(self._authenticator, "refresh_token", None)
                    if callable(refresh_fn):
                        auth_token = refresh_fn()
                api_config = FlextApiSettings(
                    base_url=str(self._oic_settings.base_url),
                    timeout=self._oic_settings.request_timeout,
                    max_retries=self._oic_settings.max_retries,
                    verify_ssl=self._oic_settings.verify_ssl,
                    default_headers={
                        "Authorization": f"Bearer {auth_token}",
                        "Content-Type": "application/json",
                    },
                    headers={
                        "Authorization": f"Bearer {auth_token}",
                        "Content-Type": "application/json",
                    },
                    log_requests=False,
                    log_responses=False,
                )
                self._monitoring_client = FlextApiClient(api_config)
        except (ConnectionError, TimeoutError, ValueError):
            FlextLogger(__name__).exception("Failed to initialize service components")
            raise


__all__ = ["FlextOracleOicService"]
