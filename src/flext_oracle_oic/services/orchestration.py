"""FLEXT Oracle OIC Orchestration - App-driven, scheduled, and file transfer patterns.

Mixin providing orchestration execution operations for the FlextOracleOicService facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_oracle_oic import FlextOracleOicServiceBase, c, p, r, t

if TYPE_CHECKING:
    from collections.abc import Callable

    from flext_oracle_oic import FlextOracleOicClient


class FlextOracleOicOrchestrationMixin(FlextOracleOicServiceBase):
    """Mixin providing orchestration execution for FlextOracleOicService facade."""

    def execute_app_driven_orchestration(
        self,
        integration_id: str,
        payload: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Execute the app-driven orchestration pattern.

        Args:
            integration_id: Identifier of the target integration.
            payload: Orchestration payload data.

        Returns:
            Result wrapping the orchestration execution output.

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
        """Execute the app-driven orchestration without exception translation.

        Args:
            integration_id: Identifier of the target integration.
            payload: Orchestration payload data sent to the integration
                connections endpoint.

        Returns:
            Result wrapping the orchestration execution output.

        """
        client_result = self._get_client()
        if client_result.failure:
            error_msg = client_result.error or "Client initialization failed"
            return r[t.JsonMapping].fail(error_msg)
        client = client_result.value
        endpoint = f"/integrations/{integration_id}/connections"
        payload_dict = {
            key: self._to_general_value(value) for key, value in payload.items()
        }
        orchestration_result = client.make_request("POST", endpoint, json=payload_dict)
        if orchestration_result.failure:
            return r[t.JsonMapping].from_failure(orchestration_result)
        return r[t.JsonMapping].ok(orchestration_result.value)

    def execute_file_transfer(
        self,
        integration_id: str,
        file_config: t.JsonMapping,
    ) -> p.Result[t.JsonMapping]:
        """Execute the file transfer pattern.

        Args:
            integration_id: Identifier of the target integration.
            file_config: File transfer configuration.

        Returns:
            Result wrapping the file transfer execution output.

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
        """Execute the scheduled orchestration pattern.

        Args:
            integration_id: Identifier of the target integration.
            schedule_config: Schedule configuration.

        Returns:
            Result wrapping the scheduled orchestration execution output.

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
        """Run the file transfer operation against the given client.

        Args:
            client: OIC client used to perform the transfer.
            integration_id: Identifier of the target integration.
            operation_config: File transfer configuration.

        Returns:
            The OIC response payload for the file transfer request.

        """
        return client.execute_file_transfer(integration_id, operation_config)

    @staticmethod
    def _run_scheduled_orchestration(
        client: FlextOracleOicClient,
        integration_id: str,
        operation_config: t.JsonMapping,
    ) -> t.JsonMapping:
        """Run the scheduled orchestration operation against the given client.

        Args:
            client: OIC client used to perform the orchestration.
            integration_id: Identifier of the target integration.
            operation_config: Schedule configuration.

        Returns:
            The OIC response payload for the schedule request.

        """
        return client.execute_scheduled_orchestration(integration_id, operation_config)

    def _execute_integration_operation(
        self,
        integration_id: str,
        operation_config: t.JsonMapping,
        operation: Callable[[FlextOracleOicClient, str, t.JsonMapping], t.JsonMapping],
        log_message: str,
        error_message: str,
    ) -> p.Result[t.JsonMapping]:
        """Execute an integration operation, translating network exceptions.

        Args:
            integration_id: Identifier of the target integration.
            operation_config: Configuration payload passed to the operation.
            operation: Callable that performs the operation against the client.
            log_message: Message template logged when the operation raises.
            error_message: Prefix used in the failure result message.

        Returns:
            Result wrapping the operation output, or a failure result when the
            client is unavailable or the operation raises.

        """
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
