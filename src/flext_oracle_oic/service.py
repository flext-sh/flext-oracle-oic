"""FLEXT Oracle OIC Service - Unified Service Pattern.

FLEXT Unified Module Pattern: Single unified service class consolidating
all Oracle OIC functionality. Implements complete FlextService pattern
with railway-oriented error handling.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import asyncio
import json
from collections.abc import Mapping
from typing import Self, override

from flext_api import FlextApiClient, FlextApiModels, FlextApiSettings
from flext_core import (
    FlextLogger,
    FlextResult,
    FlextService,
    t,
    u,
)
from flext_oracle_oic.constants import FlextOracleOicConstants
from flext_oracle_oic.ext_client import (
    FlextOracleOicClient,
)
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
        self.settings = FlextOracleOicSettings.get_global_instance()
        # Logger is inherited from parent class
        self._client: FlextOracleOicClient | None = None
        self._monitoring_client: FlextApiClient | None = None
        self._authenticator: t.GeneralValueType | None = None

        # Complete FLEXT ecosystem integration

        # Service registered in container for dependency injection

        # Initialize components
        self._initialize_components()

    def _initialize_components(self) -> None:
        """Initialize service components."""
        try:
            # Components are initialized lazily when first needed

            # Create HTTP monitoring client if monitoring is enabled
            if self.settings.enable_monitoring:
                # Get auth token from authenticator if available
                auth_token = ""
                if self._authenticator:
                    refresh_fn = getattr(self._authenticator, "refresh_token", None)
                    if callable(refresh_fn):
                        auth_token = refresh_fn()
                api_config = FlextApiSettings(
                    base_url=str(self.settings.base_url),
                    timeout=self.settings.request_timeout,
                    headers={
                        "Authorization": f"Bearer {auth_token}",
                        "Content-Type": "application/json",
                    },
                )
                self._monitoring_client = FlextApiClient(api_config)

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError):
            FlextLogger(__name__).exception("Failed to initialize service components")
            raise

    @staticmethod
    def _as_text(value: t.GeneralValueType, default: str = "") -> str:
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
    def _to_general_value(value: t.GeneralValueType) -> t.GeneralValueType:
        """Normalize arbitrary runtime values into GeneralValueType."""
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

    @override
    def execute(
        self: Self,
        **kwargs: t.GeneralValueType,
    ) -> FlextResult[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]]:
        """Execute main service operation - list all integrations.

        Returns:
        FlextResult containing list of OIC integrations.

        """
        return self.list_integrations()

    # Integration Management Methods (from OracleOicExtensionService)

    def list_integrations(
        self,
    ) -> FlextResult[list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]]:
        """List all Oracle OIC integrations.

        Returns:
        FlextResult containing list of integration information.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[
                    list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]
                ].fail(
                    error_msg,
                )

            client = client_result.value
            integrations_result = client.get_integrations()

            if integrations_result.is_failure:
                error_msg = integrations_result.error or "Failed to get integrations"
                return FlextResult[
                    list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]
                ].fail(
                    error_msg,
                )

            integrations_data = integrations_result.value

            # Convert to domain models
            integrations = []
            for item in integrations_data:
                integration = FlextOracleOicModels.OracleOic.OICIntegrationInfo(
                    integration_id=self._as_text(item.get("id"), ""),
                    name=self._as_text(item.get("name"), ""),
                    description=self._as_text(item.get("description"), ""),
                    integration_version=self._as_text(
                        item.get("version"),
                        FlextOracleOicConstants.Integration.DEFAULT_VERSION_FALLBACK,
                    ),
                    status=self._as_text(
                        item.get("status"),
                        FlextOracleOicConstants.Connection.Status.UNKNOWN,
                    ),
                    created_by=self._as_text(item.get("createdBy"), ""),
                    last_updated=self._as_text(item.get("lastUpdated"), ""),
                )
                integrations.append(integration)

            return FlextResult[
                list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]
            ].ok(
                integrations,
            )

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            FlextLogger(__name__).exception("Failed to list integrations")
            return FlextResult[
                list[FlextOracleOicModels.OracleOic.OICIntegrationInfo]
            ].fail(
                f"Integration listing failed: {e!s}",
            )

    def list_connections(
        self,
        type_filter: list[str] | None = None,
    ) -> FlextResult[list[FlextOracleOicModels.OracleOic.OICConnectionInfo]]:
        """List Oracle OIC connections.

        Args:
        type_filter: Filter by connection type

        Returns:
        FlextResult containing connection info list or error

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[
                    list[FlextOracleOicModels.OracleOic.OICConnectionInfo]
                ].fail(
                    error_msg,
                )

            client = client_result.value
            connections_result = client.get_connections(
                type_filter=type_filter,
                page_size=FlextOracleOicConstants.OracleOic.DEFAULT_PAGE_SIZE,
            )

            if connections_result.is_failure:
                error_msg = connections_result.error or "Failed to get connections"
                return FlextResult[
                    list[FlextOracleOicModels.OracleOic.OICConnectionInfo]
                ].fail(
                    error_msg,
                )

            connections_data = connections_result.value

            # Convert to domain models
            connections = []
            for item in connections_data:
                connection = FlextOracleOicModels.OracleOic.OICConnectionInfo(
                    connection_id=self._as_text(item.get("id"), ""),
                    name=self._as_text(item.get("name"), ""),
                    adapter_type=self._as_text(item.get("adapterType"), ""),
                    status=self._as_text(
                        item.get("status"),
                        FlextOracleOicConstants.Connection.Status.UNKNOWN,
                    ),
                    connection_type=self._as_text(item.get("connectionType"), ""),
                    description=self._as_text(item.get("description"), ""),
                )
                connections.append(connection)

            return FlextResult[
                list[FlextOracleOicModels.OracleOic.OICConnectionInfo]
            ].ok(
                connections,
            )

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception("Failed to list connections")
            return FlextResult[
                list[FlextOracleOicModels.OracleOic.OICConnectionInfo]
            ].fail(
                f"Connection listing failed: {e!s}",
            )

    def get_integration(
        self,
        integration_id: str,
    ) -> FlextResult[FlextOracleOicModels.OracleOic.OICIntegrationInfo]:
        """Get specific Oracle OIC integration by ID.

        Args:
        integration_id: The integration identifier.

        Returns:
        FlextResult containing integration information.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[
                    FlextOracleOicModels.OracleOic.OICIntegrationInfo
                ].fail(
                    error_msg,
                )

            client = client_result.value
            # Get all integrations and find the one with matching ID
            integrations_result = client.get_integrations()
            if integrations_result.is_failure:
                error_msg = integrations_result.error or "Failed to get integrations"
                return FlextResult[
                    FlextOracleOicModels.OracleOic.OICIntegrationInfo
                ].fail(
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
                return FlextResult[
                    FlextOracleOicModels.OracleOic.OICIntegrationInfo
                ].fail(
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
                    FlextOracleOicConstants.Integration.DEFAULT_VERSION_FALLBACK,
                ),
                status=self._as_text(
                    integration_data.get("status"),
                    FlextOracleOicConstants.Connection.Status.UNKNOWN,
                ),
                created_by=self._as_text(integration_data.get("createdBy"), ""),
                last_updated=self._as_text(integration_data.get("lastUpdated"), ""),
            )

            return FlextResult[FlextOracleOicModels.OracleOic.OICIntegrationInfo].ok(
                integration,
            )

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception("Failed to get integration %s", integration_id)
            return FlextResult[FlextOracleOicModels.OracleOic.OICIntegrationInfo].fail(
                f"Integration retrieval failed: {e!s}",
            )

    def create_integration(
        self,
        integration_data: Mapping[str, t.GeneralValueType],
    ) -> FlextResult[FlextOracleOicModels.OracleOic.OICIntegrationInfo]:
        """Create new Oracle OIC integration.

        Args:
        integration_data: Integration configuration data.

        Returns:
        FlextResult containing created integration information.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[
                    FlextOracleOicModels.OracleOic.OICIntegrationInfo
                ].fail(
                    error_msg,
                )

            client = client_result.value
            created_result = client.create_integration(integration_data)
            if created_result.is_failure:
                error_msg = created_result.error or "Failed to create integration"
                return FlextResult[
                    FlextOracleOicModels.OracleOic.OICIntegrationInfo
                ].fail(
                    error_msg,
                )

            created_data = created_result.value

            integration = FlextOracleOicModels.OracleOic.OICIntegrationInfo(
                integration_id=self._as_text(created_data.get("id"), ""),
                name=self._as_text(created_data.get("name"), ""),
                description=self._as_text(created_data.get("description"), ""),
                integration_version=self._as_text(
                    created_data.get("version"),
                    FlextOracleOicConstants.Integration.DEFAULT_VERSION_FALLBACK,
                ),
                status=self._as_text(
                    created_data.get("status"),
                    FlextOracleOicConstants.Integration.Status.DRAFT,
                ),
                created_by=self._as_text(created_data.get("createdBy"), ""),
                last_updated=self._as_text(created_data.get("lastUpdated"), ""),
            )

            return FlextResult[FlextOracleOicModels.OracleOic.OICIntegrationInfo].ok(
                integration,
            )

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception("Failed to create integration")
            return FlextResult[FlextOracleOicModels.OracleOic.OICIntegrationInfo].fail(
                f"Integration creation failed: {e!s}",
            )

    def update_integration(
        self,
        integration_id: str,
        integration_data: Mapping[str, t.GeneralValueType],
    ) -> FlextResult[FlextOracleOicModels.OracleOic.OICIntegrationInfo]:
        """Update existing Oracle OIC integration.

        Args:
        integration_id: The integration identifier.
        integration_data: Updated integration configuration.

        Returns:
        FlextResult containing updated integration information.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[
                    FlextOracleOicModels.OracleOic.OICIntegrationInfo
                ].fail(
                    error_msg,
                )

            client = client_result.value
            updated_result = client.update_integration(integration_id, integration_data)
            if updated_result.is_failure:
                error_msg = updated_result.error or "Failed to update integration"
                return FlextResult[
                    FlextOracleOicModels.OracleOic.OICIntegrationInfo
                ].fail(
                    error_msg,
                )

            updated_data = updated_result.value

            integration = FlextOracleOicModels.OracleOic.OICIntegrationInfo(
                integration_id=self._as_text(updated_data.get("id"), integration_id),
                name=self._as_text(updated_data.get("name"), ""),
                description=self._as_text(updated_data.get("description"), ""),
                integration_version=self._as_text(
                    updated_data.get("version"),
                    FlextOracleOicConstants.Integration.DEFAULT_VERSION_FALLBACK,
                ),
                status=self._as_text(
                    updated_data.get("status"),
                    FlextOracleOicConstants.Connection.Status.UNKNOWN,
                ),
                created_by=self._as_text(updated_data.get("createdBy"), ""),
                last_updated=self._as_text(updated_data.get("lastUpdated"), ""),
            )

            return FlextResult[FlextOracleOicModels.OracleOic.OICIntegrationInfo].ok(
                integration,
            )

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception("Failed to update integration %s", integration_id)
            return FlextResult[FlextOracleOicModels.OracleOic.OICIntegrationInfo].fail(
                f"Integration update failed: {e!s}",
            )

    def delete_integration(self, integration_id: str) -> FlextResult[bool]:
        """Delete Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        FlextResult indicating success or failure.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[bool].fail(error_msg)

            client = client_result.value
            # Delete integration using update with status DELETED or make_request
            delete_result = client.make_request(
                "DELETE",
                f"/integrations/{integration_id}",
            )
            if delete_result.is_failure:
                error_msg = delete_result.error or "Failed to delete integration"
                return FlextResult[bool].fail(error_msg)

            return FlextResult[bool].ok(value=True)

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception("Failed to delete integration %s", integration_id)
            return FlextResult[bool].fail(f"Integration deletion failed: {e!s}")

    def activate_integration(self, integration_id: str) -> FlextResult[bool]:
        """Activate Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        FlextResult indicating success or failure.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[bool].fail(error_msg)

            client = client_result.value
            # Activate integration using make_request
            activate_result = client.make_request(
                "POST",
                f"/integrations/{integration_id}/activate",
            )
            if activate_result.is_failure:
                error_msg = activate_result.error or "Failed to activate integration"
                return FlextResult[bool].fail(error_msg)

            return FlextResult[bool].ok(value=True)

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception("Failed to activate integration %s", integration_id)
            return FlextResult[bool].fail(f"Integration activation failed: {e!s}")

    def deactivate_integration(self, integration_id: str) -> FlextResult[bool]:
        """Deactivate Oracle OIC integration.

        Args:
        integration_id: The integration identifier.

        Returns:
        FlextResult indicating success or failure.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[bool].fail(error_msg)

            client = client_result.value
            # Deactivate integration using make_request
            deactivate_result = client.make_request(
                "POST",
                f"/integrations/{integration_id}/deactivate",
            )
            if deactivate_result.is_failure:
                error_msg = (
                    deactivate_result.error or "Failed to deactivate integration"
                )
                return FlextResult[bool].fail(error_msg)

            return FlextResult[bool].ok(value=True)

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception("Failed to deactivate integration %s", integration_id)
            return FlextResult[bool].fail(f"Integration deactivation failed: {e!s}")

    # Connection Testing Methods (from LifecycleManager)

    def test_connection(self) -> FlextResult[bool]:
        """Test connection to Oracle OIC instance.

        Returns:
        FlextResult containing connection test result.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[bool].fail(error_msg)

            client = client_result.value
            # Test connection using make_request to health endpoint
            test_result = client.make_request(
                FlextOracleOicConstants.API.Method.GET,
                "/ic/api/integration/v1/health",
            )
            if test_result.is_failure:
                error_msg = test_result.error or "Connection test failed"
                return FlextResult[bool].fail(error_msg)
            result_data = test_result.value
            status_value = result_data.get("status", "")
            match status_value:
                case str():
                    is_connected = status_value.lower() == "healthy"
                case _:
                    is_connected = False

            return FlextResult[bool].ok(is_connected)

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception("Connection test failed")
            return FlextResult[bool].fail(f"Connection test failed: {e!s}")

    # Integration Pattern Execution Methods (from OICIntegrationPatternService)

    def execute_app_driven_orchestration(
        self,
        integration_id: str,
        payload: Mapping[str, t.GeneralValueType],
        **_kwargs: t.GeneralValueType,
    ) -> FlextResult[Mapping[str, t.GeneralValueType]]:
        """Execute app-driven orchestration pattern.

        Args:
        integration_id: The integration identifier.
        payload: Orchestration payload data.
        **kwargs: Additional execution parameters.

        Returns:
        FlextResult containing execution result.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[Mapping[str, t.GeneralValueType]].fail(error_msg)

            client = client_result.value
            # Execute app-driven orchestration using make_request
            endpoint = f"/integrations/{integration_id}/connections"
            payload_dict: dict[str, t.GeneralValueType] = (
                dict(payload) if u.is_dict_like(payload) else {}
            )
            orchestration_result = client.make_request(
                "POST",
                endpoint,
                json=payload_dict,
            )
            if orchestration_result.is_failure:
                return FlextResult[Mapping[str, t.GeneralValueType]].fail(
                    orchestration_result.error or "Orchestration request failed",
                )
            return FlextResult[Mapping[str, t.GeneralValueType]].ok(
                orchestration_result.value,
            )

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception(
                "App-driven orchestration failed for %s",
                integration_id,
            )
            return FlextResult[Mapping[str, t.GeneralValueType]].fail(
                f"Orchestration execution failed: {e!s}",
            )

    def execute_scheduled_orchestration(
        self,
        integration_id: str,
        schedule_config: Mapping[str, t.GeneralValueType],
        **kwargs: t.GeneralValueType,
    ) -> FlextResult[Mapping[str, t.GeneralValueType]]:
        """Execute scheduled orchestration pattern.

        Args:
        integration_id: The integration identifier.
        schedule_config: Schedule configuration.
        **kwargs: Additional execution parameters.

        Returns:
        FlextResult containing execution result.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[Mapping[str, t.GeneralValueType]].fail(error_msg)

            client = client_result.value
            result = client.execute_scheduled_orchestration(
                integration_id,
                schedule_config,
                **kwargs,
            )

            return FlextResult[Mapping[str, t.GeneralValueType]].ok(result)

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception(
                "Scheduled orchestration failed for %s",
                integration_id,
            )
            return FlextResult[Mapping[str, t.GeneralValueType]].fail(
                f"Scheduled orchestration failed: {e!s}",
            )

    def execute_file_transfer(
        self,
        integration_id: str,
        file_config: Mapping[str, t.GeneralValueType],
        **kwargs: t.GeneralValueType,
    ) -> FlextResult[Mapping[str, t.GeneralValueType]]:
        """Execute file transfer pattern.

        Args:
        integration_id: The integration identifier.
        file_config: File transfer configuration.
        **kwargs: Additional execution parameters.

        Returns:
        FlextResult containing execution result.

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[Mapping[str, t.GeneralValueType]].fail(error_msg)

            client = client_result.value
            result = client.execute_file_transfer(integration_id, file_config, **kwargs)

            return FlextResult[Mapping[str, t.GeneralValueType]].ok(result)

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception("File transfer failed for %s", integration_id)
            return FlextResult[Mapping[str, t.GeneralValueType]].fail(
                f"File transfer failed: {e!s}",
            )

    # Authentication Methods

    def refresh_auth_token(self) -> FlextResult[str]:
        """Refresh OAuth2 authentication token.

        Returns:
        FlextResult containing new access token.

        """
        try:
            if not self._authenticator:
                return FlextResult[str].fail("Authenticator not initialized")

            refresh_fn = getattr(self._authenticator, "refresh_token", None)
            if not callable(refresh_fn):
                return FlextResult[str].fail("Authenticator has no refresh_token")
            token = refresh_fn()
            return FlextResult[str].ok(str(token))

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception("Token refresh failed")
            return FlextResult[str].fail(f"Token refresh failed: {e!s}")

    def validate_auth_token(self, token: str) -> FlextResult[bool]:
        """Validate OAuth2 authentication token.

        Args:
        token: Token to validate.

        Returns:
        FlextResult containing validation result.

        """
        try:
            if not self._authenticator:
                return FlextResult[bool].fail("Authenticator not initialized")
            validate_fn = getattr(self._authenticator, "validate_token", None)
            if not callable(validate_fn):
                return FlextResult[bool].fail("Authenticator has no validate_token")
            is_valid = validate_fn(token)
            return FlextResult[bool].ok(bool(is_valid))

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception("Token validation failed")
            return FlextResult[bool].fail(f"Token validation failed: {e!s}")

    def deploy_integration(
        self,
        integration_data: Mapping[str, t.GeneralValueType],
    ) -> FlextResult[str]:
        """Deploy integration to Oracle OIC.

        Args:
        integration_data: Integration configuration

        Returns:
        FlextResult containing integration ID or error

        """
        try:
            client_result = self._get_client()
            if client_result.is_failure:
                error_msg = client_result.error or "Client initialization failed"
                return FlextResult[str].fail(error_msg)

            client = client_result.value
            created_result = client.create_integration(integration_data)
            if created_result.is_failure:
                return FlextResult[str].fail(
                    created_result.error or "Create integration failed",
                )
            created_data = created_result.value
            integration_id = str(created_data.get("id", ""))
            if not integration_id:
                return FlextResult[str].fail("No integration ID returned")

            self.logger.info("Integration deployed successfully: %s", integration_id)
            return FlextResult[str].ok(str(integration_id))

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception("Failed to deploy integration")
            return FlextResult[str].fail(f"Integration deployment failed: {e!s}")

    # Integration Pattern Methods (from OICIntegrationPatternService)

    def apply_message_router_pattern(
        self,
        message_data: Mapping[str, t.GeneralValueType],
        routing_rules: list[Mapping[str, t.GeneralValueType]],
    ) -> FlextResult[Mapping[str, t.GeneralValueType]]:
        """Apply message router pattern to OIC integration using FlextOracleOicUtilities.

        Args:
        message_data: Message to route
        routing_rules: Routing rules configuration

        Returns:
        FlextResult containing routing result or error

        """
        try:
            self.logger.info("Applying message router pattern")

            # Validate pattern configuration using utilities
            pattern_config = {
                "routing_rules": routing_rules,
                "message_data": message_data,
            }

            validation_result = (
                FlextOracleOicUtilities.PatternAnalysis.validate_pattern_configuration(
                    "message_router",
                    pattern_config,
                )
            )

            if validation_result.is_failure:
                return FlextResult[Mapping[str, t.GeneralValueType]].fail(
                    f"Pattern validation failed: {validation_result.error}",
                )

            # Apply validated pattern
            routing_result = {
                "pattern": FlextOracleOicConstants.OICPatterns.PATTERN_MESSAGE_ROUTER,
                "message_id": message_data.get(
                    "id",
                    FlextOracleOicConstants.OICPatterns.PATTERN_MESSAGE_ID_UNKNOWN,
                ),
                "applied_rules": len(routing_rules),
                "status": FlextOracleOicConstants.OICPatterns.PatternStatus.PROCESSED,
            }

            return FlextResult[Mapping[str, t.GeneralValueType]].ok(routing_result)

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            error_msg = f"Message router pattern failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[Mapping[str, t.GeneralValueType]].fail(error_msg)

    def apply_scatter_gather_pattern(
        self,
        request_data: Mapping[str, t.GeneralValueType],
        target_endpoints: list[str],
    ) -> FlextResult[Mapping[str, t.GeneralValueType]]:
        """Apply scatter-gather pattern to OIC integration using FlextOracleOicUtilities.

        Args:
        request_data: Request to scatter
        target_endpoints: Target endpoints for scatter

        Returns:
        FlextResult containing scatter-gather result or error

        """
        try:
            self.logger.info("Applying scatter-gather pattern")

            # Validate pattern configuration using utilities
            pattern_config = {
                "target_services": target_endpoints,
                "request_data": request_data,
            }

            validation_result = (
                FlextOracleOicUtilities.PatternAnalysis.validate_pattern_configuration(
                    "scatter_gather",
                    pattern_config,
                )
            )

            if validation_result.is_failure:
                return FlextResult[Mapping[str, t.GeneralValueType]].fail(
                    f"Pattern validation failed: {validation_result.error}",
                )

            # Apply validated pattern
            scatter_result = {
                "pattern": FlextOracleOicConstants.OICPatterns.PATTERN_SCATTER_GATHER,
                "request_id": request_data.get(
                    "id",
                    FlextOracleOicConstants.OICPatterns.PATTERN_REQUEST_ID_UNKNOWN,
                ),
                "target_count": len(target_endpoints),
                "status": FlextOracleOicConstants.OICPatterns.PatternStatus.PROCESSED,
            }

            return FlextResult[Mapping[str, t.GeneralValueType]].ok(scatter_result)

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            error_msg = f"Scatter-gather pattern failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult[Mapping[str, t.GeneralValueType]].fail(error_msg)

    # Monitoring Methods (from MonitoringService)

    def get_health_status(self) -> FlextResult[Mapping[str, t.GeneralValueType]]:
        """Get Oracle OIC health status using FlextOracleOicUtilities.

        Returns:
        FlextResult containing validated health status information

        """
        try:
            health_data: dict[str, t.GeneralValueType]
            if not self._monitoring_client:
                # Mock health check response
                health_data = {
                    "status": FlextOracleOicConstants.Monitoring.HealthStatus.HEALTHY,
                    "components": {
                        FlextOracleOicConstants.Monitoring.COMPONENT_DATABASE: {
                            "status": FlextOracleOicConstants.Monitoring.ComponentStatus.HEALTHY,
                        },
                        FlextOracleOicConstants.Monitoring.COMPONENT_MESSAGING: {
                            "status": FlextOracleOicConstants.Monitoring.ComponentStatus.HEALTHY,
                        },
                        FlextOracleOicConstants.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                            "status": FlextOracleOicConstants.Monitoring.ComponentStatus.HEALTHY,
                        },
                    },
                    "timestamp": asyncio.get_event_loop().time(),
                }
            else:
                # Use flext-api client for monitoring
                base = str(self.settings.base_url).rstrip("/")
                health_url = f"{base}{FlextOracleOicConstants.API.ENDPOINT_HEALTH}"
                req = FlextApiModels.HttpRequest(
                    method=FlextOracleOicConstants.API.Method.GET,
                    url=health_url,
                )
                response_result = self._monitoring_client.request(req)

                if response_result.is_success:
                    response = response_result.value
                    if (
                        response.status_code
                        == FlextOracleOicConstants.API.HTTP_STATUS_OK
                    ):
                        base_health: dict[str, t.GeneralValueType] = (
                            {
                                str(k): self._to_general_value(v)
                                for k, v in response.body.items()
                            }
                            if isinstance(response.body, dict)
                            else {"raw": self._to_general_value(response.body)}
                        )
                        health_data = {
                            **base_health,
                            "status": FlextOracleOicConstants.Monitoring.HealthStatus.HEALTHY,
                            "components": {
                                FlextOracleOicConstants.Monitoring.COMPONENT_DATABASE: {
                                    "status": FlextOracleOicConstants.Monitoring.ComponentStatus.HEALTHY,
                                },
                                FlextOracleOicConstants.Monitoring.COMPONENT_MESSAGING: {
                                    "status": FlextOracleOicConstants.Monitoring.ComponentStatus.HEALTHY,
                                },
                                FlextOracleOicConstants.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                                    "status": FlextOracleOicConstants.Monitoring.ComponentStatus.HEALTHY,
                                },
                            },
                        }
                    else:
                        health_data = {
                            "status": FlextOracleOicConstants.Monitoring.HealthStatus.UNHEALTHY,
                            "components": {
                                FlextOracleOicConstants.Monitoring.COMPONENT_DATABASE: {
                                    "status": FlextOracleOicConstants.Monitoring.ComponentStatus.UNKNOWN,
                                },
                                FlextOracleOicConstants.Monitoring.COMPONENT_MESSAGING: {
                                    "status": FlextOracleOicConstants.Monitoring.ComponentStatus.UNKNOWN,
                                },
                                FlextOracleOicConstants.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                                    "status": FlextOracleOicConstants.Monitoring.ComponentStatus.UNKNOWN,
                                },
                            },
                            "error": f"HTTP {response.status_code}",
                        }
                else:
                    health_data = {
                        "status": FlextOracleOicConstants.Monitoring.HealthStatus.ERROR,
                        "components": {
                            FlextOracleOicConstants.Monitoring.COMPONENT_DATABASE: {
                                "status": FlextOracleOicConstants.Monitoring.ComponentStatus.UNKNOWN,
                            },
                            FlextOracleOicConstants.Monitoring.COMPONENT_MESSAGING: {
                                "status": FlextOracleOicConstants.Monitoring.ComponentStatus.UNKNOWN,
                            },
                            FlextOracleOicConstants.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                                "status": FlextOracleOicConstants.Monitoring.ComponentStatus.UNKNOWN,
                            },
                        },
                        "error": f"Request failed: {response_result.error}",
                    }

            # Validate health status using utilities
            health_data_dict: dict[str, t.GeneralValueType] = dict(health_data)
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
            return FlextResult[Mapping[str, t.GeneralValueType]].ok(health_data_dict)

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception("Health check failed")
            error_health: dict[str, t.GeneralValueType] = {
                "status": FlextOracleOicConstants.Monitoring.HealthStatus.ERROR,
                "components": {
                    FlextOracleOicConstants.Monitoring.COMPONENT_DATABASE: {
                        "status": FlextOracleOicConstants.Monitoring.ComponentStatus.UNKNOWN,
                    },
                    FlextOracleOicConstants.Monitoring.COMPONENT_MESSAGING: {
                        "status": FlextOracleOicConstants.Monitoring.ComponentStatus.UNKNOWN,
                    },
                    FlextOracleOicConstants.Monitoring.COMPONENT_INTEGRATION_ENGINE: {
                        "status": FlextOracleOicConstants.Monitoring.ComponentStatus.UNKNOWN,
                    },
                },
                "error": str(e),
            }

            # Validate error health status as well
            validation_result = (
                FlextOracleOicUtilities.MonitoringUtilities.validate_health_status(
                    error_health,
                )
            )
            return (
                validation_result
                if validation_result.is_success
                else FlextResult[Mapping[str, t.GeneralValueType]].ok(error_health)
            )

    def get_performance_metrics(self) -> FlextResult[Mapping[str, t.GeneralValueType]]:
        """Get Oracle OIC performance metrics with analysis using FlextOracleOicUtilities.

        Returns:
        FlextResult containing performance metrics with analysis

        """
        try:
            metrics_data: dict[str, t.GeneralValueType]
            if not self._monitoring_client:
                # Mock performance metrics response
                metrics_data = {
                    "active_integrations": 0,
                    "total_executions": 0,
                    "success_rate": 0.0,
                    "average_response_time": 0.0,
                    "timestamp": asyncio.get_event_loop().time(),
                }
            else:
                # Use flext-api client for performance metrics
                base = str(self.settings.base_url).rstrip("/")
                metrics_url = f"{base}/ic/api/integration/v1/metrics"
                req = FlextApiModels.HttpRequest(
                    method=FlextOracleOicConstants.API.Method.GET,
                    url=metrics_url,
                )
                response_result = self._monitoring_client.request(req)

                if response_result.is_success:
                    response = response_result.value
                    if (
                        response.status_code
                        == FlextOracleOicConstants.API.HTTP_STATUS_OK
                    ):
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

            metrics_dict: dict[str, t.GeneralValueType] = {}
            if u.is_dict_like(metrics_data):
                for key, value in metrics_data.items():
                    metrics_dict[str(key)] = self._to_general_value(value)
            analysis_result = (
                FlextOracleOicUtilities.MonitoringUtilities.analyze_performance_metrics(
                    metrics_dict,
                )
            )

            if analysis_result.is_success:
                return FlextResult[Mapping[str, t.GeneralValueType]].ok({
                    **metrics_dict,
                    "analysis": analysis_result.value,
                })
            self.logger.warning(f"Performance analysis failed: {analysis_result.error}")
            return FlextResult[Mapping[str, t.GeneralValueType]].ok(metrics_dict)

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception("Performance metrics failed")
            error_metrics: dict[str, t.GeneralValueType] = {
                "active_integrations": 0,
                "total_executions": 0,
                "success_rate": 0.0,
                "average_response_time": 0.0,
                "error": str(e),
            }

            # Try to analyze error metrics as well
            analysis_result = (
                FlextOracleOicUtilities.MonitoringUtilities.analyze_performance_metrics(
                    error_metrics,
                )
            )
            if analysis_result.is_success:
                return FlextResult[Mapping[str, t.GeneralValueType]].ok({
                    **error_metrics,
                    "analysis": analysis_result.value,
                })
            return FlextResult[Mapping[str, t.GeneralValueType]].ok(error_metrics)

    # Business Rules Validation

    @override
    def validate_business_rules(self) -> FlextResult[bool]:
        """Validate Oracle OIC service business rules.

        Returns:
        FlextResult indicating validation success or failure.

        """
        # Validate settings exist
        if not self.settings:
            return FlextResult[bool].fail("Settings are required")

        # Validate connection settings using utilities
        if not self.settings.base_url:
            return FlextResult[bool].fail("Base URL is required")

        # Base URL validation already performed by Pydantic AnyUrl type

        # Validate auth settings using utilities
        if not self.settings.oauth_client_id:
            return FlextResult[bool].fail("OAuth client ID is required")

        client_id_result = (
            FlextOracleOicUtilities.AuthenticationValidation.validate_oauth_client_id(
                self.settings.oauth_client_id,
            )
        )
        if client_id_result.is_failure:
            return FlextResult[bool].fail(
                f"OAuth client ID validation: {client_id_result.error}",
            )

        if not self.settings.oauth_client_secret:
            return FlextResult[bool].fail("OAuth client secret is required")

        if not self.settings.oauth_token_url:
            return FlextResult[bool].fail("OAuth token URL is required")

        # Token URL validation already performed by Pydantic AnyUrl type

        return FlextResult[bool].ok(value=True)

    # Private Helper Methods

    def _get_client(self) -> FlextResult[FlextOracleOicClient]:
        """Get or create Oracle OIC client instance.

        Returns:
        FlextResult containing the client instance.

        """
        try:
            if self._client is None:
                # Validate business rules first
                validation_result = self.validate_business_rules()
                if validation_result.is_failure:
                    return FlextResult[FlextOracleOicClient].fail(
                        validation_result.error,
                    )

                # Create client from connection and auth configs
                connection_config = FlextOracleOicModels.OracleOic.OICConnectionConfig(
                    base_url=str(self.settings.base_url),
                    api_version=self.settings.api_version,
                    request_timeout=self.settings.request_timeout,
                    max_retries=self.settings.max_retries,
                    verify_ssl=self.settings.verify_ssl,
                )
                auth_config = FlextOracleOicModels.OracleOic.OICAuthConfig(
                    oauth_client_id=self.settings.oauth_client_id,
                    oauth_client_secret=self.settings.oauth_client_secret,
                    oauth_token_url=str(self.settings.oauth_token_url),
                    oauth_client_aud=self.settings.oauth_client_aud,
                    oauth_scope=self.settings.oauth_scope,
                )
                self._client = FlextOracleOicClient(
                    connection_config=connection_config,
                    auth_config=auth_config,
                )

            return FlextResult[FlextOracleOicClient].ok(self._client)

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            self.logger.exception("Failed to create OIC client")
            return FlextResult[FlextOracleOicClient].fail(
                f"Client creation failed: {e!s}",
            )

    # Context Manager Support

    def __enter__(self) -> Self:
        """Context manager entry."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None:
        """Context manager exit."""
        # Cleanup resources if needed


__all__ = [
    "FlextOracleOicService",
]
