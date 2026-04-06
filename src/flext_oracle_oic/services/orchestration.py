"""FLEXT Oracle OIC Orchestration - App-driven, scheduled, and file transfer patterns.

Mixin providing orchestration execution operations for the FlextOracleOicService facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Callable

from flext_core import r
from flext_oracle_oic import (
    FlextOracleOicClient,
    FlextOracleOicServiceBase,
    t,
)


class FlextOracleOicOrchestrationMixin(FlextOracleOicServiceBase):
    """Mixin providing orchestration execution for FlextOracleOicService facade."""

    def execute_app_driven_orchestration(
        self,
        integration_id: str,
        payload: t.ContainerMapping,
        **_kwargs: t.Scalar,
    ) -> r[t.ContainerMapping]:
        """Execute app-driven orchestration pattern.

        Args:
        integration_id: The integration identifier.
        payload: Orchestration payload data.
        **_kwargs: Additional execution parameters.

        Returns:
        r containing execution result.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[t.ContainerMapping].fail(error_msg)
            client = client_result.value
            endpoint = f"/integrations/{integration_id}/connections"
            payload_dict: t.ContainerMapping = {
                str(key): self._to_general_value(value)
                for key, value in payload.items()
            }
            orchestration_result = client.make_request(
                "POST",
                endpoint,
                json=payload_dict,
            )
            if orchestration_result.is_failure:
                return r[t.ContainerMapping].fail(
                    orchestration_result.error or "Orchestration request failed",
                )
            return r[t.ContainerMapping].ok(orchestration_result.value)
        except (ConnectionError, TimeoutError, ValueError) as exc:
            self.logger.exception(
                "App-driven orchestration failed for %s",
                integration_id,
            )
            return r[t.ContainerMapping].fail(
                f"Orchestration execution failed: {exc!s}",
            )

    def execute_file_transfer(
        self,
        integration_id: str,
        file_config: t.ContainerMapping,
        **kwargs: t.Scalar,
    ) -> r[t.ContainerMapping]:
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
        schedule_config: t.ContainerMapping,
        **kwargs: t.Scalar,
    ) -> r[t.ContainerMapping]:
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
        operation_config: t.ContainerMapping,
        operation_kwargs: t.ConfigurationMapping,
    ) -> t.ContainerMapping:
        return client.execute_file_transfer(
            integration_id,
            operation_config,
            **operation_kwargs,
        )

    @staticmethod
    def _run_scheduled_orchestration(
        client: FlextOracleOicClient,
        integration_id: str,
        operation_config: t.ContainerMapping,
        operation_kwargs: t.ConfigurationMapping,
    ) -> t.ContainerMapping:
        return client.execute_scheduled_orchestration(
            integration_id,
            operation_config,
            **operation_kwargs,
        )

    def _execute_integration_operation(
        self,
        integration_id: str,
        operation_config: t.ContainerMapping,
        operation: Callable[
            [
                FlextOracleOicClient,
                str,
                t.ContainerMapping,
                t.ScalarMapping,
            ],
            t.ContainerMapping,
        ],
        log_message: str,
        error_message: str,
        **kwargs: t.Scalar,
    ) -> r[t.ContainerMapping]:
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[t.ContainerMapping].fail(error_msg)
            client = client_result.value
            operation_kwargs: t.ConfigurationMapping = {
                str(key): value for key, value in kwargs.items()
            }
            result = operation(
                client,
                integration_id,
                operation_config,
                operation_kwargs,
            )
            return r[t.ContainerMapping].ok(result)
        except (ConnectionError, TimeoutError, ValueError) as exc:
            self.logger.exception(log_message, integration_id)
            return r[t.ContainerMapping].fail(f"{error_message}: {exc!s}")


__all__ = ["FlextOracleOicOrchestrationMixin"]
