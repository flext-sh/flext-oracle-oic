"""FLEXT Oracle OIC Integration CRUD - Create, Read, Update, Delete operations.

Mixin providing integration CRUD operations for the FlextOracleOicService facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import (
    Mapping,
    MutableSequence,
    Sequence,
)

from flext_core import p, r
from flext_oracle_oic import (
    FlextOracleOicModels,
    FlextOracleOicServiceBase,
    c,
    t,
)


class FlextOracleOicIntegrationCrudMixin(FlextOracleOicServiceBase):
    """Mixin providing integration CRUD operations for FlextOracleOicService facade."""

    def create_integration(
        self,
        integration_data: Mapping[str, t.Container],
    ) -> p.Result[FlextOracleOicModels.OracleOic.OICIntegrationInfo]:
        """Create new Oracle OIC integration.

        Args:
        integration_data: Integration configuration data.

        Returns:
        r containing created integration information.

        """
        try:
            client_result = self._get_client()
            if client_result.failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[FlextOracleOicModels.OracleOic.OICIntegrationInfo].fail(
                    error_msg,
                )
            client = client_result.value
            created_result = client.create_integration(integration_data)
            if created_result.failure:
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

    def fetch_integration(
        self,
        integration_id: str,
    ) -> p.Result[FlextOracleOicModels.OracleOic.OICIntegrationInfo]:
        """Get specific Oracle OIC integration by ID.

        Args:
        integration_id: The integration identifier.

        Returns:
        r containing integration information.

        """
        try:
            client_result = self._get_client()
            if client_result.failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[FlextOracleOicModels.OracleOic.OICIntegrationInfo].fail(
                    error_msg,
                )
            client = client_result.value
            integrations_result = client.get_integrations()
            if integrations_result.failure:
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

    def update_integration(
        self,
        integration_id: str,
        integration_data: Mapping[str, t.Container],
    ) -> p.Result[FlextOracleOicModels.OracleOic.OICIntegrationInfo]:
        """Update existing Oracle OIC integration.

        Args:
        integration_id: The integration identifier.
        integration_data: Updated integration configuration.

        Returns:
        r containing updated integration information.

        """
        try:
            client_result = self._get_client()
            if client_result.failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[FlextOracleOicModels.OracleOic.OICIntegrationInfo].fail(
                    error_msg,
                )
            client = client_result.value
            updated_result = client.update_integration(integration_id, integration_data)
            if updated_result.failure:
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

    def delete_integration(self, integration_id: str) -> p.Result[bool]:
        """Delete Oracle OIC integration.

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
            delete_result = client.make_request(
                "DELETE",
                f"/integrations/{integration_id}",
            )
            if delete_result.failure:
                error_msg = delete_result.error or "Failed to delete integration"
                return r[bool].fail(error_msg)
            return r[bool].ok(value=True)
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Failed to delete integration %s", integration_id)
            return r[bool].fail(f"Integration deletion failed: {e!s}")

    def deploy_integration(
        self,
        integration_data: Mapping[str, t.Container],
    ) -> p.Result[str]:
        """Deploy integration to Oracle OIC.

        Args:
        integration_data: Integration configuration

        Returns:
        r containing integration ID or error

        """
        try:
            client_result = self._get_client()
            if client_result.failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[str].fail(error_msg)
            client = client_result.value
            created_result = client.create_integration(integration_data)
            if created_result.failure:
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

    def list_connections(
        self,
        type_filter: t.StrSequence | None = None,
    ) -> p.Result[Sequence[FlextOracleOicModels.OracleOic.OICConnectionInfo]]:
        """List Oracle OIC connections.

        Args:
        type_filter: Filter by connection type

        Returns:
        r containing connection info list or error

        """
        try:
            client_result = self._get_client()
            if client_result.failure:
                error_msg = client_result.error or "Client initialization failed"
                return r[
                    Sequence[FlextOracleOicModels.OracleOic.OICConnectionInfo]
                ].fail(
                    error_msg,
                )
            client = client_result.value
            connections_result = client.get_connections(
                type_filter=type_filter,
                page_size=c.OracleOic.DEFAULT_PAGE_SIZE,
            )
            if connections_result.failure:
                error_msg = connections_result.error or "Failed to get connections"
                return r[
                    Sequence[FlextOracleOicModels.OracleOic.OICConnectionInfo]
                ].fail(
                    error_msg,
                )
            connections_data = connections_result.value
            connections: MutableSequence[
                FlextOracleOicModels.OracleOic.OICConnectionInfo
            ] = []
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
            return r[Sequence[FlextOracleOicModels.OracleOic.OICConnectionInfo]].ok(
                connections,
            )
        except (ConnectionError, TimeoutError, ValueError) as e:
            self.logger.exception("Failed to list connections")
            return r[Sequence[FlextOracleOicModels.OracleOic.OICConnectionInfo]].fail(
                f"Connection listing failed: {e!s}",
            )


__all__: list[str] = ["FlextOracleOicIntegrationCrudMixin"]
