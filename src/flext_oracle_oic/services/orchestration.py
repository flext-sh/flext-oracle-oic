"""FLEXT Oracle OIC Orchestration - App-driven, scheduled, and file transfer patterns.

Mixin providing orchestration execution operations for the FlextOracleOicService facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core import r
from flext_oracle_oic import c, p, t
from flext_oracle_oic.services.base import FlextOracleOicServiceBase

if TYPE_CHECKING:
    from collections.abc import Callable

    from flext_oracle_oic.ext_client import FlextOracleOicClient


class FlextOracleOicOrchestrationMixin(FlextOracleOicServiceBase):
    """Mixin providing orchestration execution for FlextOracleOicService facade."""

    def execute_app_driven_orchestration(
        self,
        integration_id: str,
        payload: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Execute app-driven orchestration pattern.

        Args:
        integration_id: The integration identifier.
        payload: Orchestration payload data.

        Returns:
        r containing execution result.

        """
        try:
            return self._execute_app_driven_orchestration(integration_id, payload)
        except c.EXC_NETWORK_TYPE as exc:
            self.logger.exception(
                "App-driven orchestration failed for %s",
                integration_id,
            )
            return r[t.JsonMapping].fail_op("Orchestration execution", exc)

    def _execute_app_driven_orchestration(
        self,
        integration_id: str,
        payload: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Execute app-driven orchestration without exception translation."""
        client_result = self._get_client()
        if client_result.failure:
            error_msg = client_result.error or "Client initialization failed"
            return r[t.JsonMapping].fail(error_msg)
        client = client_result.value
        endpoint = f"/integrations/{integration_id}/connections"
        payload_dict = {
            key: self._to_general_value(value) for key, value in payload.items()
        }
        orchestration_result = client.make_request(
            "POST",
            endpoint,
            json=payload_dict,
        )
        if orchestration_result.failure:
            return r[t.JsonMapping].fail(
                orchestration_result.error or "Orchestration request failed",
            )
        return r[t.JsonMapping].ok(orchestration_result.value)

    def execute_file_transfer(
        self,
        integration_id: str,
        file_config: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Execute file transfer pattern.

        Args:
        integration_id: The integration identifier.
        file_config: File transfer configuration.

        Returns:
        r containing execution result.

        """
        return self._execute_integration_operation(
            integration_id=integration_id,
            operation_config=file_config,
            operation=self._run_file_transfer,
            log_message="File transfer failed for %s",
            error_message="File transfer failed",
        )

    def execute_scheduled_orchestration(
        self,
        integration_id: str,
        schedule_config: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Execute scheduled orchestration pattern.

        Args:
        integration_id: The integration identifier.
        schedule_config: Schedule configuration.

        Returns:
        r containing execution result.

        """
        return self._execute_integration_operation(
            integration_id=integration_id,
            operation_config=schedule_config,
            operation=self._run_scheduled_orchestration,
            log_message="Scheduled orchestration failed for %s",
            error_message="Scheduled orchestration failed",
        )

    @staticmethod
    def _run_file_transfer(
        client: FlextOracleOicClient,
        integration_id: str,
        operation_config: t.JsonMapping,
    ) -> t.JsonMapping:
        return client.execute_file_transfer(integration_id, operation_config)

    @staticmethod
    def _run_scheduled_orchestration(
        client: FlextOracleOicClient,
        integration_id: str,
        operation_config: t.JsonMapping,
    ) -> t.JsonMapping:
        return client.execute_scheduled_orchestration(integration_id, operation_config)

    def _execute_integration_operation(
        self,
        integration_id: str,
        operation_config: t.JsonMapping,
        operation: Callable[
            [FlextOracleOicClient, str, t.JsonMapping],
            t.JsonMapping,
        ],
        log_message: str,
        error_message: str,
    ) -> p.Result[t.JsonMapping]:
        try:
            client_result = self._get_client()
            if client_result.failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[t.JsonMapping].fail(error_msg)
            client = client_result.value
            result = operation(client, integration_id, operation_config)
            return r[t.JsonMapping].ok(result)
        except c.EXC_NETWORK_TYPE as exc:
            self.logger.exception(log_message, integration_id)
            return r[t.JsonMapping].fail(f"{error_message}: {exc!s}")


__all__: list[str] = ["FlextOracleOicOrchestrationMixin"]
