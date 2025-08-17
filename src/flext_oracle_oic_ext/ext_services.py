"""Oracle OIC Extension Services - EXTENSION Pattern.

Este módulo estabelece o padrão EXTENSION PEP8 para serviços
especializados Oracle OIC. Serve como modelo para futuras extensions.
"""

from __future__ import annotations

from typing import Any, Self

from flext_core import FlextResult, get_logger
from pydantic import SecretStr

from flext_oracle_oic_ext.ext_client import (
    OICExtensionAuthenticator,
    OracleOICExtensionClient,
)
from flext_oracle_oic_ext.ext_config import OracleOICExtensionSettings
from flext_oracle_oic_ext.ext_models import (
    OICAuthConfig,
    OICConnectionConfig,
    OICConnectionInfo,
    OICIntegrationInfo,
)

logger = get_logger(__name__)
# ================================
# EXTENSION Pattern: Specialized Services
# ================================


class OracleOICExtensionService:
    """Main Oracle OIC Extension service.

    Padrão EXTENSION: Serviço principal para operações Oracle OIC
    com integrações enterprise e padrões avançados.
    """

    def __init__(self, settings: OracleOICExtensionSettings) -> None:
      """Initialize OIC extension service.

      Args:
          settings: Extension configuration settings

      """
      self.settings = settings
      self.logger = get_logger(f"{__name__}.{self.__class__.__name__}")
      self._client: OracleOICExtensionClient | None = None

    def _get_client(self) -> FlextResult[OracleOICExtensionClient]:
      """Get authenticated OIC client.

      Returns:
          FlextResult containing client or error

      """
      try:
          if not self._client:
              # Create auth config from settings
              auth_config = OICAuthConfig(
                  oauth_client_id=self.settings.auth.oauth_client_id,
                  oauth_client_secret=SecretStr(
                      self.settings.auth.oauth_client_secret,
                  ),
                  oauth_token_url=self.settings.auth.oauth_token_url,
                  oauth_client_aud=self.settings.auth.oauth_client_aud,
                  oauth_scope=self.settings.auth.oauth_scope,
              )

              # Create connection config from settings
              connection_config = OICConnectionConfig(
                  base_url=self.settings.connection.base_url,
                  api_version=self.settings.connection.api_version,
                  request_timeout=self.settings.connection.request_timeout,
                  max_retries=self.settings.connection.max_retries,
                  verify_ssl=self.settings.connection.verify_ssl,
              )

              # Create authenticator and client
              authenticator = OICExtensionAuthenticator(auth_config)
              self._client = OracleOICExtensionClient(
                  connection_config,
                  authenticator,
              )

          return FlextResult.ok(self._client)

      except Exception as e:
          error_msg = f"Failed to create OIC client: {e}"
          self.logger.exception(error_msg)
          return FlextResult.fail(error_msg)

    def list_integrations(
      self,
      status_filter: list[str] | None = None,
    ) -> FlextResult[list[OICIntegrationInfo]]:
      """List Oracle OIC integrations.

      Args:
          status_filter: Filter by integration status

      Returns:
          FlextResult containing integration info list or error

      """
      try:
          client_result = self._get_client()
          if not client_result.success:
              return FlextResult.fail(client_result.error or "Client creation failed")

          client = client_result.data
          if client is None:
              return FlextResult.fail("No client available")

          # Get integrations from OIC
          integrations_result = client.get_integrations(
              status_filter=status_filter,
              page_size=100,
          )

          if not integrations_result.success:
              return FlextResult.fail(
                  integrations_result.error or "Failed to fetch integrations",
              )

          integrations_data = integrations_result.data or []

          # Convert to domain models
          integration_infos = []
          for integration in integrations_data:
              try:
                  integration_info = OICIntegrationInfo(
                      integration_id=integration.get("id", ""),
                      name=integration.get("name", ""),
                      status=integration.get("status", ""),
                      version=integration.get("version", ""),
                      description=integration.get("description", ""),
                      created_by=integration.get("createdBy", ""),
                      last_updated=integration.get("lastUpdated", ""),
                  )
                  integration_infos.append(integration_info)
              except Exception as e:
                  self.logger.warning(f"Failed to parse integration: {e}")
                  continue

          self.logger.info(f"Retrieved {len(integration_infos)} integrations")
          return FlextResult.ok(integration_infos)

      except Exception as e:
          error_msg = f"Failed to list integrations: {e}"
          self.logger.exception(error_msg)
          return FlextResult.fail(error_msg)

    def list_connections(
      self,
      type_filter: list[str] | None = None,
    ) -> FlextResult[list[OICConnectionInfo]]:
      """List Oracle OIC connections.

      Args:
          type_filter: Filter by connection type

      Returns:
          FlextResult containing connection info list or error

      """
      try:
          client_result = self._get_client()
          if not client_result.success:
              return FlextResult.fail(client_result.error or "Client creation failed")

          client = client_result.data
          if client is None:
              return FlextResult.fail("No client available")

          # Get connections from OIC
          connections_result = client.get_connections(
              type_filter=type_filter,
              page_size=100,
          )

          if not connections_result.success:
              return FlextResult.fail(
                  connections_result.error or "Connections fetch failed",
              )

          connections_data = connections_result.data or []

          # Convert to domain models
          connection_infos = []
          for connection in connections_data:
              try:
                  connection_info = OICConnectionInfo(
                      connection_id=connection.get("id", ""),
                      name=connection.get("name", ""),
                      adapter_type=connection.get("adapterType", ""),
                      status=connection.get("status", ""),
                      connection_type=connection.get("connectionType", ""),
                      description=connection.get("description", ""),
                  )
                  connection_infos.append(connection_info)
              except Exception as e:
                  self.logger.warning(f"Failed to parse connection: {e}")
                  continue

          self.logger.info(f"Retrieved {len(connection_infos)} connections")
          return FlextResult.ok(connection_infos)

      except Exception as e:
          error_msg = f"Failed to list connections: {e}"
          self.logger.exception(error_msg)
          return FlextResult.fail(error_msg)

    def test_connection(self) -> FlextResult[bool]:
      """Test connection to Oracle OIC.

      Returns:
          FlextResult containing connection status or error

      """
      try:
          client_result = self._get_client()
          if not client_result.success:
              return FlextResult.fail(client_result.error or "Client creation failed")

          client = client_result.data
          if client is None:
              return FlextResult.fail("No client available")

          # Try to get integrations as connection test
          integrations_result = client.get_integrations(page_size=1)

          if integrations_result.success:
              self.logger.info("OIC connection test successful")
              return FlextResult.ok(data=True)
          error_msg = f"OIC connection test failed: {integrations_result.error}"
          self.logger.error(error_msg)
          return FlextResult.fail(error_msg)

      except Exception as e:
          error_msg = f"Connection test error: {e}"
          self.logger.exception(error_msg)
          return FlextResult.fail(error_msg)

    def deploy_integration(
      self,
      integration_data: dict[str, Any],
    ) -> FlextResult[str]:
      """Deploy integration to Oracle OIC.

      Args:
          integration_data: Integration configuration

      Returns:
          FlextResult containing integration ID or error

      """
      try:
          client_result = self._get_client()
          if not client_result.success:
              return FlextResult.fail(client_result.error or "Client creation failed")

          client = client_result.data
          if client is None:
              return FlextResult.fail("No client available")

          # Create integration
          create_result = client.create_integration(integration_data)

          if not create_result.success:
              return FlextResult.fail(
                  create_result.error or "Create integration failed",
              )

          created_integration = create_result.data
          if not created_integration:
              return FlextResult.fail("No integration data returned")

          integration_id = created_integration.get("id", "")

          self.logger.info(f"Integration deployed successfully: {integration_id}")
          return FlextResult.ok(integration_id)

      except Exception as e:
          error_msg = f"Failed to deploy integration: {e}"
          self.logger.exception(error_msg)
          return FlextResult.fail(error_msg)

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
      if self._client:
          self._client.__exit__(exc_type, exc_val, exc_tb)
          self._client = None


class OICIntegrationPatternService:
    """Oracle OIC Integration Pattern service.

    Padrão EXTENSION: Serviço para padrões enterprise de integração
    Oracle OIC como Message Router, Scatter-Gather, etc.
    """

    def __init__(self, oic_service: OracleOICExtensionService) -> None:
      """Initialize OIC pattern service.

      Args:
          oic_service: Main OIC extension service

      """
      self.oic_service = oic_service
      self.logger = get_logger(f"{__name__}.{self.__class__.__name__}")

    def apply_message_router_pattern(
      self,
      message_data: dict[str, Any],
      routing_rules: list[dict[str, Any]],
    ) -> FlextResult[dict[str, Any]]:
      """Apply message router pattern to OIC integration.

      Args:
          message_data: Message to route
          routing_rules: Routing rules configuration

      Returns:
          FlextResult containing routing result or error

      """
      try:
          self.logger.info("Applying message router pattern")

          # Placeholder implementation - will be enhanced in future iterations
          routing_result = {
              "pattern": "message_router",
              "message_id": message_data.get("id", "unknown"),
              "applied_rules": len(routing_rules),
              "status": "processed",
          }

          return FlextResult.ok(routing_result)

      except Exception as e:
          error_msg = f"Message router pattern failed: {e}"
          self.logger.exception(error_msg)
          return FlextResult.fail(error_msg)

    def apply_scatter_gather_pattern(
      self,
      request_data: dict[str, Any],
      target_endpoints: list[str],
    ) -> FlextResult[dict[str, Any]]:
      """Apply scatter-gather pattern to OIC integration.

      Args:
          request_data: Request to scatter
          target_endpoints: Target endpoints for scatter

      Returns:
          FlextResult containing scatter-gather result or error

      """
      try:
          self.logger.info("Applying scatter-gather pattern")

          # Placeholder implementation - will be enhanced in future iterations
          scatter_result = {
              "pattern": "scatter_gather",
              "request_id": request_data.get("id", "unknown"),
              "target_count": len(target_endpoints),
              "status": "processed",
          }

          return FlextResult.ok(scatter_result)

      except Exception as e:
          error_msg = f"Scatter-gather pattern failed: {e}"
          self.logger.exception(error_msg)
          return FlextResult.fail(error_msg)


# Exports seguindo padrão EXTENSION
__all__: list[str] = [
    "OICIntegrationPatternService",
    # Main services
    "OracleOICExtensionService",
]
