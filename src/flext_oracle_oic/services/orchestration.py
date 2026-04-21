"""FLEXT Oracle OIC Orchestration - App-driven, scheduled, and file transfer patterns.

Mixin providing orchestration execution operations for the FlextOracleOicService facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import (
    Callable,
    Mapping,
)

from flext_oracle_oic import (
    FlextOracleOicClient,
    FlextOracleOicServiceBase,
    p,
    r,
    t,
)


class FlextOracleOicOrchestrationMixin(FlextOracleOicServiceBase):
    """Mixin providing orchestration execution for FlextOracleOicService facade."""

    def execute_app_driven_orchestration(
        self,
        integration_id: str,
        payload: Mapping[str, t.Container],
        **_kwargs: t.Scalar,
    ) -> p.Result[Mapping[str, t.Container]]:
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
            if client_result.failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[Mapping[str, t.Container]].fail(error_msg)
            client = client_result.value
            endpoint = f"/integrations/{integration_id}/connections"
            payload_dict: Mapping[str, t.Container] = {
                str(key): self._to_general_value(value)
                for key, value in payload.items()
            }
            orchestration_result = client.make_request(
                "POST",
                endpoint,
                json=payload_dict,
            )
            if orchestration_result.failure:
                return r[Mapping[str, t.Container]].fail(
                    orchestration_result.error or "Orchestration request failed",
                )
            return r[Mapping[str, t.Container]].ok(orchestration_result.value)
        except (ConnectionError, TimeoutError, ValueError) as exc:
            self.logger.exception(
                "App-driven orchestration failed for %s",
                integration_id,
            )
            return r[Mapping[str, t.Container]].fail(
                f"Orchestration execution failed: {exc!s}",
            )

    def execute_file_transfer(
        self,
        integration_id: str,
        file_config: Mapping[str, t.Container],
        **kwargs: t.Scalar,
    ) -> p.Result[Mapping[str, t.Container]]:
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
        schedule_config: Mapping[str, t.Container],
        **kwargs: t.Scalar,
    ) -> p.Result[Mapping[str, t.Container]]:
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
        operation_config: Mapping[str, t.Container],
        operation_kwargs: t.ConfigurationMapping,
    ) -> Mapping[str, t.Container]:
        return client.execute_file_transfer(
            integration_id,
            operation_config,
            **operation_kwargs,
        )

    @staticmethod
    def _run_scheduled_orchestration(
        client: FlextOracleOicClient,
        integration_id: str,
        operation_config: Mapping[str, t.Container],
        operation_kwargs: t.ConfigurationMapping,
    ) -> Mapping[str, t.Container]:
        return client.execute_scheduled_orchestration(
            integration_id,
            operation_config,
            **operation_kwargs,
        )

    def _execute_integration_operation(
        self,
        integration_id: str,
        operation_config: Mapping[str, t.Container],
        operation: Callable[
            [
                FlextOracleOicClient,
                str,
                Mapping[str, t.Container],
                t.ScalarMapping,
            ],
            Mapping[str, t.Container],
        ],
        log_message: str,
        error_message: str,
        **kwargs: t.Scalar,
    ) -> p.Result[Mapping[str, t.Container]]:
        try:
            client_result = self._get_client()
            if client_result.failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[Mapping[str, t.Container]].fail(error_msg)
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
            return r[Mapping[str, t.Container]].ok(result)
        except (ConnectionError, TimeoutError, ValueError) as exc:
            self.logger.exception(log_message, integration_id)
            return r[Mapping[str, t.Container]].fail(f"{error_message}: {exc!s}")


__all__: list[str] = ["FlextOracleOicOrchestrationMixin"]
