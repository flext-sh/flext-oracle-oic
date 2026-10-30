"""FLEXT Oracle OIC Integration Lifecycle - Activate/Deactivate operations.

Mixin providing integration lifecycle management for the FlextOracleOicService facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_oracle_oic import FlextOracleOicServiceBase, c, p, r


class FlextOracleOicIntegrationLifecycle(FlextOracleOicServiceBase):
    """Mixin providing integration lifecycle operations for the OIC service."""

    def activate_integration(self, integration_id: str) -> p.Result[bool]:
        """Activate an Oracle OIC integration.

        Args:
            integration_id: The integration identifier.

        Returns:
            Result indicating success or failure.

        """
        try:
            return self._activate_integration(integration_id)
        except c.EXC_NETWORK_TYPE as e:
            self.logger.exception("Failed to activate integration %s", integration_id)
            return r[bool].fail_op("Integration activation", e)

    def _activate_integration(self, integration_id: str) -> p.Result[bool]:
        """Activate an Oracle OIC integration without exception translation.

        Args:
            integration_id: Identifier of the integration to activate.

        Returns:
            Result holding ``True`` when the activation request succeeds.

        """
        client_result = self._get_client()
        if client_result.failure:
            error_msg = client_result.error or "Client initialization failed"
            return r[bool].fail(error_msg)
        client = client_result.value
        activate_result = client.make_request(
            "POST",
            f"/integrations/{integration_id}/activate",
        )
        if activate_result.failure:
            error_msg = activate_result.error or "Failed to activate integration"
            return r[bool].fail(error_msg)
        return r[bool].ok(value=True)

    def deactivate_integration(self, integration_id: str) -> p.Result[bool]:
        """Deactivate an Oracle OIC integration.

        Args:
            integration_id: The integration identifier.

        Returns:
            Result indicating success or failure.

        """
        try:
            return self._deactivate_integration(integration_id)
        except c.EXC_NETWORK_TYPE as e:
            self.logger.exception("Failed to deactivate integration %s", integration_id)
            return r[bool].fail_op("Integration deactivation", e)

    def _deactivate_integration(self, integration_id: str) -> p.Result[bool]:
        """Deactivate an Oracle OIC integration without exception translation.

        Args:
            integration_id: Identifier of the integration to deactivate.

        Returns:
            Result holding ``True`` when the deactivation request succeeds.

        """
        client_result = self._get_client()
        if client_result.failure:
            error_msg = client_result.error or "Client initialization failed"
            return r[bool].fail(error_msg)
        client = client_result.value
        deactivate_result = client.make_request(
            "POST",
            f"/integrations/{integration_id}/deactivate",
        )
        if deactivate_result.failure:
            error_msg = deactivate_result.error or "Failed to deactivate integration"
            return r[bool].fail(error_msg)
        return r[bool].ok(value=True)

    def test_connection(self) -> p.Result[bool]:
        """Test the connection to the Oracle OIC instance.

        Returns:
            Result holding the connection test verdict.

        """
        try:
            return self._test_connection()
        except c.EXC_NETWORK_TYPE as e:
            self.logger.exception("Connection test failed")
            return r[bool].fail_op("Connection test", e)

    def _test_connection(self) -> p.Result[bool]:
        """Test the Oracle OIC connection without exception translation.

        Returns:
            Result holding ``True`` when the OIC health status reports healthy.

        """
        client_result = self._get_client()
        if client_result.failure:
            error_msg = client_result.error or "Client initialization failed"
            return r[bool].fail(error_msg)
        client = client_result.value
        test_result = client.make_request(
            c.OracleOic.API.Method.GET,
            "/ic/api/integration/v1/health",
        )
        if test_result.failure:
            error_msg = test_result.error or "Connection test failed"
            return r[bool].fail(error_msg)
        result_data = test_result.value
        status_value = result_data.get("status", "")
        match status_value:
            case str():
                is_connected = status_value.lower() == c.HealthStatus.HEALTHY.value
            case _:
                is_connected = False
        return r[bool].ok(is_connected)


__all__: list[str] = ["FlextOracleOicIntegrationLifecycle"]
