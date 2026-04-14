"""FLEXT Oracle OIC Integration Lifecycle - Activate/Deactivate operations.

Mixin providing integration lifecycle management for the FlextOracleOicService facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import p, r
from flext_oracle_oic import FlextOracleOicServiceBase, c as oic_c


class FlextOracleOicIntegrationLifecycleMixin(FlextOracleOicServiceBase):
    """Mixin providing integration lifecycle operations for FlextOracleOicService facade."""

    def activate_integration(self, integration_id: str) -> p.Result[bool]:
        """Activate Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        r indicating success or failure.

        """
        try:
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
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Failed to activate integration %s", integration_id)
            return r[bool].fail(f"Integration activation failed: {e!s}")

    def deactivate_integration(self, integration_id: str) -> p.Result[bool]:
        """Deactivate Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        r indicating success or failure.

        """
        try:
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
                error_msg = (
                    deactivate_result.error or "Failed to deactivate integration"
                )
                return r[bool].fail(error_msg)
            return r[bool].ok(value=True)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Failed to deactivate integration %s", integration_id)
            return r[bool].fail(f"Integration deactivation failed: {e!s}")

    def test_connection(self) -> p.Result[bool]:
        """Test connection to Oracle OIC instance.

        Returns:
        r containing connection test result.

        """
        try:
            client_result = self._get_client()
            if client_result.failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[bool].fail(error_msg)
            client = client_result.value
            test_result = client.make_request(
                oic_c.API.Method.GET,
                "/ic/api/integration/v1/health",
            )
            if test_result.failure:
                error_msg = test_result.error or "Connection test failed"
                return r[bool].fail(error_msg)
            result_data = test_result.value
            status_value = result_data.get("status", "")
            match status_value:
                case str():
                    is_connected = (
                        status_value.lower() == oic_c.HealthStatus.HEALTHY.value
                    )
                case _:
                    is_connected = False
            return r[bool].ok(is_connected)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Connection test failed")
            return r[bool].fail(f"Connection test failed: {e!s}")


__all__: list[str] = ["FlextOracleOicIntegrationLifecycleMixin"]
