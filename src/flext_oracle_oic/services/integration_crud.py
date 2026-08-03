"""FLEXT Oracle OIC Integration CRUD - Create, Read, Update, Delete operations.

Mixin providing integration CRUD operations for the FlextOracleOicService facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import MutableSequence, Sequence

from flext_oracle_oic import c, m, p, r, t
from flext_oracle_oic.ext_client import FlextOracleOicClient
from flext_oracle_oic.services.base import FlextOracleOicServiceBase


class FlextOracleOicIntegrationCrudMixin(FlextOracleOicServiceBase):
    """Mixin providing integration CRUD operations for FlextOracleOicService facade."""

    def _get_client_or_fail(self) -> p.Result[FlextOracleOicClient]:
        """Resolve the API client or return a pre-failed result.

        Returns:
            r containing the client value, or a failure result.

        """
        client_result = self._get_client()
        if client_result.failure:
            error_msg = client_result.error or "Client initialization failed"
            return r[FlextOracleOicClient].fail(error_msg)
        return client_result

    def _create_integration_impl(
        self, integration_data: t.JsonMapping
    ) -> p.Result[m.OracleOic.OICIntegrationInfo]:
        """Core implementation for create_integration."""
        client_result = self._get_client_or_fail()
        if client_result.failure:
            return r[m.OracleOic.OICIntegrationInfo].fail(
                client_result.error or "Client initialization failed"
            )
        client = client_result.value
        created_result = client.create_integration(integration_data)
        if created_result.failure:
            error_msg = created_result.error or "Failed to create integration"
            return r[m.OracleOic.OICIntegrationInfo].fail(error_msg)
        created_data = created_result.value
        integration = self._build_integration_info(
            created_data, fallback_id="", default_status=c.Integration.Status.DRAFT
        )
        return r[m.OracleOic.OICIntegrationInfo].ok(integration)

    def create_integration(
        self, integration_data: t.JsonMapping
    ) -> p.Result[m.OracleOic.OICIntegrationInfo]:
        """Create new Oracle OIC integration.

        Args:
        integration_data: Integration configuration data.

        Returns:
        r containing created integration information.

        """
        try:
            return self._create_integration_impl(integration_data)
        except c.EXC_NETWORK_TYPE as e:
            self.logger.exception("Failed to create integration")
            return r[m.OracleOic.OICIntegrationInfo].fail_op("Integration creation", e)

    def _fetch_integration_impl(
        self, integration_id: str
    ) -> p.Result[m.OracleOic.OICIntegrationInfo]:
        """Core implementation for fetch_integration."""
        client_result = self._get_client_or_fail()
        if client_result.failure:
            return r[m.OracleOic.OICIntegrationInfo].fail(
                client_result.error or "Client initialization failed"
            )
        client = client_result.value
        integrations_result = client.get_integrations()
        if integrations_result.failure:
            error_msg = integrations_result.error or "Failed to get integrations"
            return r[m.OracleOic.OICIntegrationInfo].fail(error_msg)
        integrations_list = integrations_result.value
        integration_data = next(
            (item for item in integrations_list if item.get("id") == integration_id),
            None,
        )
        if not integration_data:
            return r[m.OracleOic.OICIntegrationInfo].fail(
                f"Integration {integration_id} not found"
            )
        integration = self._build_integration_info(
            integration_data,
            fallback_id=integration_id,
            default_status=c.Connection.Status.UNKNOWN,
        )
        return r[m.OracleOic.OICIntegrationInfo].ok(integration)

    def fetch_integration(
        self, integration_id: str
    ) -> p.Result[m.OracleOic.OICIntegrationInfo]:
        """Get specific Oracle OIC integration by ID.

        Args:
        integration_id: The integration identifier.

        Returns:
        r containing integration information.

        """
        try:
            return self._fetch_integration_impl(integration_id)
        except c.EXC_NETWORK_TYPE as e:
            self.logger.exception("Failed to get integration %s", integration_id)
            return r[m.OracleOic.OICIntegrationInfo].fail_op("Integration retrieval", e)

    def _update_integration_impl(
        self, integration_id: str, integration_data: t.JsonMapping
    ) -> p.Result[m.OracleOic.OICIntegrationInfo]:
        """Core implementation for update_integration."""
        client_result = self._get_client_or_fail()
        if client_result.failure:
            return r[m.OracleOic.OICIntegrationInfo].fail(
                client_result.error or "Client initialization failed"
            )
        client = client_result.value
        updated_result = client.update_integration(integration_id, integration_data)
        if updated_result.failure:
            error_msg = updated_result.error or "Failed to update integration"
            return r[m.OracleOic.OICIntegrationInfo].fail(error_msg)
        updated_data = updated_result.value
        integration = self._build_integration_info(
            updated_data,
            fallback_id=integration_id,
            default_status=c.Connection.Status.UNKNOWN,
        )
        return r[m.OracleOic.OICIntegrationInfo].ok(integration)

    def update_integration(
        self, integration_id: str, integration_data: t.JsonMapping
    ) -> p.Result[m.OracleOic.OICIntegrationInfo]:
        """Update existing Oracle OIC integration.

        Args:
        integration_id: The integration identifier.
        integration_data: Updated integration configuration.

        Returns:
        r containing updated integration information.

        """
        try:
            return self._update_integration_impl(integration_id, integration_data)
        except c.EXC_NETWORK_TYPE as e:
            self.logger.exception("Failed to update integration %s", integration_id)
            return r[m.OracleOic.OICIntegrationInfo].fail_op("Integration update", e)

    def _delete_integration_impl(self, integration_id: str) -> p.Result[bool]:
        """Core implementation for delete_integration."""
        client_result = self._get_client_or_fail()
        if client_result.failure:
            return r[bool].fail(client_result.error or "Client initialization failed")
        client = client_result.value
        delete_result = client.make_request("DELETE", f"/integrations/{integration_id}")
        if delete_result.failure:
            error_msg = delete_result.error or "Failed to delete integration"
            return r[bool].fail(error_msg)
        return r[bool].ok(value=True)

    def delete_integration(self, integration_id: str) -> p.Result[bool]:
        """Delete Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        r indicating success or failure.

        """
        try:
            return self._delete_integration_impl(integration_id)
        except c.EXC_NETWORK_TYPE as e:
            self.logger.exception("Failed to delete integration %s", integration_id)
            return r[bool].fail_op("Integration deletion", e)

    def _deploy_integration_impl(
        self, integration_data: t.JsonMapping
    ) -> p.Result[str]:
        """Core implementation for deploy_integration."""
        client_result = self._get_client_or_fail()
        if client_result.failure:
            return r[str].fail(client_result.error or "Client initialization failed")
        client = client_result.value
        created_result = client.create_integration(integration_data)
        if created_result.failure:
            return r[str].fail(created_result.error or "Create integration failed")
        created_data = created_result.value
        integration_id = str(created_data.get("id", ""))
        if not integration_id:
            return r[str].fail("No integration ID returned")
        self.logger.info("Integration deployed successfully: %s", integration_id)
        return r[str].ok(integration_id)

    def deploy_integration(self, integration_data: t.JsonMapping) -> p.Result[str]:
        """Deploy integration to Oracle OIC.

        Args:
        integration_data: Integration configuration

        Returns:
        r containing integration ID or error

        """
        try:
            return self._deploy_integration_impl(integration_data)
        except c.EXC_NETWORK_TYPE as e:
            self.logger.exception("Failed to deploy integration")
            return r[str].fail_op("Integration deployment", e)

    def _list_connections_impl(
        self, type_filter: t.StrSequence | None
    ) -> p.Result[Sequence[m.OracleOic.OICConnectionInfo]]:
        """Core implementation for list_connections."""
        client_result = self._get_client_or_fail()
        if client_result.failure:
            return r[Sequence[m.OracleOic.OICConnectionInfo]].fail(
                client_result.error or "Client initialization failed"
            )
        client = client_result.value
        connections_result = client.get_connections(
            type_filter=type_filter, page_size=c.DEFAULT_PAGE_SIZE
        )
        if connections_result.failure:
            error_msg = connections_result.error or "Failed to get connections"
            return r[Sequence[m.OracleOic.OICConnectionInfo]].fail(error_msg)
        connections_data = connections_result.value
        connections: MutableSequence[m.OracleOic.OICConnectionInfo] = []
        for item in connections_data:
            connection = m.OracleOic.OICConnectionInfo(
                connection_id=self._as_text(item.get("id"), ""),
                name=self._as_text(item.get("name"), ""),
                adapter_type=self._as_text(item.get("adapterType"), ""),
                status=self._as_text(item.get("status"), c.Connection.Status.UNKNOWN),
                connection_type=self._as_text(item.get("connectionType"), ""),
                description=self._as_text(item.get("description"), ""),
            )
            connections.append(connection)
        return r[Sequence[m.OracleOic.OICConnectionInfo]].ok(connections)

    def list_connections(
        self, type_filter: t.StrSequence | None = None
    ) -> p.Result[Sequence[m.OracleOic.OICConnectionInfo]]:
        """List Oracle OIC connections.

        Args:
        type_filter: Filter by connection type

        Returns:
        r containing connection info list or error

        """
        try:
            return self._list_connections_impl(type_filter=type_filter)
        except c.EXC_NETWORK_TYPE as e:
            self.logger.exception("Failed to list connections")
            return r[Sequence[m.OracleOic.OICConnectionInfo]].fail_op(
                "Connection listing", e
            )


__all__: list[str] = ["FlextOracleOicIntegrationCrudMixin"]
