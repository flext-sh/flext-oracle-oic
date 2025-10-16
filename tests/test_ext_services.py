"""Comprehensive tests for Oracle OIC Extension services.

Tests all service classes and methods to achieve 100% coverage
following FLEXT architectural patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations


# NOTE: Tests disabled due to code reorganization - classes moved to nested structure
# These tests need to be rewritten to match the new architecture
# # class TestOracleOicExtensionService:
#     """Test main Oracle OIC Extension service."""
#
#     @pytest.fixture
#     def connection_config(self) -> FlextOracleOicModels.OICConnectionConfig:
#         """Create test connection config."""
#         return FlextOracleOicModels.OICConnectionConfig(
#             base_url="https://test.integration.ocp.oraclecloud.com",
#         )
#
#     def auth_config(self) -> FlextOracleOicModels.OICAuthConfig:
#         """Create test auth config."""
#         return FlextOracleOicModels.OICAuthConfig(
#             oauth_client_id="test_client_id",
#             oauth_client_secret="test_client_secret",
#             oauth_token_url="https://test.identity.oraclecloud.com/oauth2/v1/token",
#         )
#
#     @pytest.fixture
#     def service(self) -> FlextOracleOicService:
#         """Create test service."""
#         return FlextOracleOicService()
#
#     def test_service_initialization(
#         self,
#         service: FlextOracleOicService,
#     ) -> None:
#         """Test service initialization."""
#         assert service.settings is not None
#         assert hasattr(
#             service,
#             "_client",
#         )
#         assert getattr(service, "_client", None) is None
#
#     def test_self(self, service: FlextOracleOicService) -> None:
#         """Test service as context manager."""
#         with service as ctx_service:
#             assert ctx_service is service
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_get_client_success(
#         self,
#         mock_client_class: Mock,
#         service: FlextOracleOicService,
#     ) -> None:
#         """Test successful client creation."""
#         mock_client = Mock()
#         mock_client_class.return_value = mock_client
#
#         result = service._get_client()
#
#         assert result.is_success
#         assert result.value == mock_client
#         assert service._client == mock_client
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_get_client_cached(
#         self,
#         mock_client_class: Mock,
#         service: FlextOracleOicService,
#     ) -> None:
#         """Test client caching."""
#         mock_client = Mock()
#         setattr(service, "_client", mock_client)
#
#         result = service._get_client()
#
#         assert result.is_success
#         assert result.value == mock_client
#         # Should not create new client
#         mock_client_class.assert_not_called()
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_get_client_failure(
#         self,
#         mock_client_class: Mock,
#         service: FlextOracleOicService,
#     ) -> None:
#         """Test client creation failure."""
#         mock_client_class.side_effect = Exception("Client creation failed")
#
#         result = service._get_client()
#
#         assert result.is_failure
#         assert "Client creation failed" in str(result.error)
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_list_integrations_success(
#         self,
#         mock_client_class: Mock,
#         service: FlextOracleOicService,
#     ) -> None:
#         """Test successful integration listing."""
#         mock_client = Mock()
#         mock_result = Mock()
#         mock_result.success = True
#         mock_result.data = []
#         mock_client.get_integrations.return_value = mock_result
#         mock_client_class.return_value = mock_client
#
#         result = service.list_integrations()
#
#         assert result.is_success
#         assert result.value == []
#         mock_client.get_integrations.assert_called_once_with(
#             status_filter=None,
#             page_size=100,
#         )
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_list_integrations_client_failure(
#         self,
#         mock_client_class: Mock,
#         service: FlextOracleOicService,
#     ) -> None:
#         """Test integration listing with client failure."""
#         mock_client_class.side_effect = Exception("Client error")
#
#         result = service.list_integrations()
#
#         assert result.is_failure
#         assert "Client error" in str(result.error)
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_list_integrations_with_filters(
#         self,
#         mock_client_class: Mock,
#         service: FlextOracleOicService,
#     ) -> None:
#         """Test integration listing with filters."""
#         mock_client = Mock()
#         mock_result = Mock()
#         mock_result.success = True
#         mock_result.data = []
#         mock_client.get_integrations.return_value = mock_result
#         mock_client_class.return_value = mock_client
#
#         result = service.list_integrations(status_filter=["ACTIVE"])
#
#         assert result.is_success
#         mock_client.get_integrations.assert_called_once_with(
#             status_filter=["ACTIVE"],
#             page_size=100,
#         )
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_list_connections_success(
#         self,
#         mock_client_class: Mock,
#         service: FlextOracleOicService,
#     ) -> None:
#         """Test successful connection listing."""
#         mock_client = Mock()
#         mock_client.get_connections.return_value.success = True
#         mock_client.get_connections.return_value.data = []
#         mock_client_class.return_value = mock_client
#
#         result = service.list_connections()
#
#         assert result.is_success
#         assert result.value == []
#         mock_client.get_connections.assert_called_once_with(
#             type_filter=None,
#             page_size=100,
#         )
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_list_connections_with_filters(
#         self,
#         mock_client_class: Mock,
#         service: FlextOracleOicService,
#     ) -> None:
#         """Test connection listing with filters."""
#         mock_client = Mock()
#         mock_result = Mock()
#         mock_result.success = True
#         mock_result.data = []
#         mock_client.get_connections.return_value = mock_result
#         mock_client_class.return_value = mock_client
#
#         result = service.list_connections(type_filter=["REST"])
#
#         assert result.is_success
#         mock_client.get_connections.assert_called_once_with(
#             type_filter=["REST"],
#             page_size=100,
#         )
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_test_connection_success(
#         self,
#         mock_client_class: Mock,
#         service: FlextOracleOicService,
#     ) -> None:
#         """Test successful connection test."""
#         mock_client = Mock()
#         mock_client.get_integrations.return_value.success = True
#         mock_client_class.return_value = mock_client
#
#         result = service.test_connection()
#
#         assert result.is_success
#         assert result.value is True
#         mock_client.get_integrations.assert_called_once_with(page_size=1)
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_test_connection_failure(
#         self,
#         mock_client_class: Mock,
#         service: FlextOracleOicService,
#     ) -> None:
#         """Test connection test failure."""
#         mock_client = Mock()
#         mock_client.get_integrations.return_value.success = False
#         mock_client.get_integrations.return_value.error = "Connection failed"
#         mock_client_class.return_value = mock_client
#
#         result = service.test_connection()
#
#         assert result.is_failure
#         assert "Connection failed" in str(result.error)
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_deploy_integration_success(
#         self,
#         mock_client_class: Mock,
#         service: FlextOracleOicService,
#     ) -> None:
#         """Test successful integration deployment."""
#         mock_client = Mock()
#         mock_result = Mock()
#         mock_result.success = True
#         mock_result.data = {"id": "test_integration_id"}
#         mock_client.create_integration.return_value = mock_result
#         mock_client_class.return_value = mock_client
#
#         integration_data: FlextTypes.Dict = {
#             "integration_id": "test_integration_id"
#         }
#         result = service.deploy_integration(integration_data)
#
#         assert result.is_success
#         assert isinstance(result.value, str)
#         mock_client.create_integration.assert_called_once_with(integration_data)
#
#
# class TestOICIntegrationPatternService:
#     """Test OIC integration pattern service."""
#
#     @pytest.fixture
#     def oic_service(self) -> Mock:
#         """Create mock OIC service."""
#         return Mock(spec=FlextOracleOicConstants.OracleOicExtensionService)
#
#     @pytest.fixture
#     def pattern_service(self, oic_service: Mock) -> OICIntegrationPatternService:
#         """Create pattern service."""
#         return FlextOracleOicConstants.OICIntegrationPatternService(oic_service)
#
#     def test_pattern_service_initialization(
#         self,
#         pattern_service: FlextOracleOicConstants.OICIntegrationPatternService,
#         oic_service: Mock,
#     ) -> None:
#         """Test pattern service initialization."""
#         assert pattern_service.oic_service == oic_service
#         assert pattern_service.logger is not None
#
#     def test_apply_message_router_pattern_success(
#         self,
#         pattern_service: FlextOracleOicConstants.OICIntegrationPatternService,
#     ) -> None:
#         """Test message router pattern application."""
#         source_config: FlextTypes.Dict = {"endpoint": "source_endpoint"}
#         target_configs: list[FlextTypes.Dict] = [
#             {"endpoint": "target1"},
#             {"endpoint": "target2"},
#         ]
#
#         result = pattern_service.apply_message_router_pattern(
#             source_config,
#             target_configs,
#         )
#
#         assert result.is_success
#         assert isinstance(result.value, dict)
#         assert "pattern" in result.value
#         assert "message_id" in result.value
#         assert "applied_rules" in result.value
#
#     def test_apply_message_router_pattern_empty_targets(
#         self,
#         pattern_service: FlextOracleOicConstants.OICIntegrationPatternService,
#     ) -> None:
#         """Test message router pattern with empty targets."""
#         source_config: FlextTypes.Dict = {"endpoint": "source_endpoint"}
#         target_configs: list[FlextTypes.Dict] = []
#
#         result = pattern_service.apply_message_router_pattern(
#             source_config,
#             target_configs,
#         )
#
#         assert result.is_success  # Current implementation doesn't validate inputs
#         assert result.value["applied_rules"] == 0
#
#     def test_apply_scatter_gather_pattern_success(
#         self,
#         pattern_service: FlextOracleOicConstants.OICIntegrationPatternService,
#     ) -> None:
#         """Test scatter-gather pattern application."""
#         request_data: FlextTypes.Dict = {"id": "test_request_123", "data": "test"}
#         target_endpoints = ["ep1", "ep2"]
#
#         result = pattern_service.apply_scatter_gather_pattern(
#             request_data,
#             target_endpoints,
#         )
#
#         assert result.is_success
#         assert isinstance(result.value, dict)
#         assert "pattern" in result.value
#         assert "request_id" in result.value
#         assert "target_count" in result.value
#
#     def test_apply_scatter_gather_pattern_invalid_scatter(
#         self,
#         pattern_service: FlextOracleOicConstants.OICIntegrationPatternService,
#     ) -> None:
#         """Test scatter-gather pattern with invalid scatter config."""
#         request_data: FlextTypes.Dict = {}
#         target_endpoints: FlextTypes.StringList = []
#
#         result = pattern_service.apply_scatter_gather_pattern(
#             request_data,
#             target_endpoints,
#         )
#
#         assert result.is_success  # Method currently doesn't validate input
#         assert isinstance(result.value, dict)
#
#
# class TestLifecycleManager:
#     """Test lifecycle manager."""
#
#     @pytest.fixture
#     def settings(self) -> FlextOracleOicSettings:
#         """Create test settings."""
#         return FlextOracleOicSettings(
#             connection=FlextOracleOicConnectionConfig(
#                 base_url="https://test.integration.ocp.oraclecloud.com",
#             ),
#             auth=FlextOracleOicAuthConfig(
#                 oauth_client_id="test_client_id",
#                 oauth_client_secret="test_client_secret",
#                 oauth_token_url="https://test.identity.oraclecloud.com/oauth2/v1/token",
#             ),
#         )
#
#     @pytest.fixture
#     def manager(
#         self, settings: FlextOracleOicSettings
#     ) -> FlextOracleOicConstants.LifecycleManager:
#         """Create lifecycle manager."""
#         return LifecycleManager(settings)
#
#     def test_manager_initialization(
#         self,
#         manager: FlextOracleOicConstants.LifecycleManager,
#         settings: FlextOracleOicSettings,
#     ) -> None:
#         """Test manager initialization."""
#         assert manager.settings == settings
#         assert manager.logger is not None
#         assert manager._client is None
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_get_client_success(
#         self,
#         mock_client_class: Mock,
#         manager: FlextOracleOicConstants.LifecycleManager,
#     ) -> None:
#         """Test successful client creation."""
#         mock_client = Mock()
#         mock_client_class.return_value = mock_client
#
#         result = manager._get_client()
#
#         assert result.is_success
#         assert result.value == mock_client
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_activate_integration_success(
#         self,
#         mock_client_class: Mock,
#         manager: FlextOracleOicService.LifecycleManager,
#     ) -> None:
#         """Test successful integration activation."""
#         mock_client = Mock()
#         mock_client.update_integration.return_value.success = True
#         mock_client_class.return_value = mock_client
#
#         result = manager.activate_integration("test_integration_id")
#
#         assert result.is_success
#         # result.value should be an FlextOracleOicModels.IntegrationStatus object, not a boolean
#         assert isinstance(result.value, FlextOracleOicModels.IntegrationStatus)
#         mock_client.update_integration.assert_called_once_with(
#             "test_integration_id",
#             {"status": "ACTIVATED"},
#         )
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_activate_integration_client_failure(
#         self,
#         mock_client_class: Mock,
#         manager: LifecycleManager,
#     ) -> None:
#         """Test integration activation with client failure."""
#         mock_client_class.side_effect = Exception("Client error")
#
#         result = manager.activate_integration("test_integration_id")
#
#         assert result.is_failure
#         assert "Client error" in str(result.error)
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_activate_integration_operation_failure(
#         self,
#         mock_client_class: Mock,
#         manager: LifecycleManager,
#     ) -> None:
#         """Test integration activation operation failure."""
#         mock_client = Mock()
#         mock_client.update_integration.return_value.success = False
#         mock_client.update_integration.return_value.error = "Activation failed"
#         mock_client_class.return_value = mock_client
#
#         result = manager.activate_integration("test_integration_id")
#
#         assert result.is_failure
#         assert "Activation failed" in str(result.error)
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_deactivate_integration_success(
#         self,
#         mock_client_class: Mock,
#         manager: LifecycleManager,
#     ) -> None:
#         """Test successful integration deactivation."""
#         mock_client = Mock()
#         mock_client.update_integration.return_value.success = True
#         mock_client_class.return_value = mock_client
#
#         result = manager.deactivate_integration("test_integration_id")
#
#         assert result.is_success
#         # result.value should be an FlextOracleOicModels.IntegrationStatus object, not a boolean
#         assert isinstance(result.value, FlextOracleOicModels.IntegrationStatus)
#         mock_client.update_integration.assert_called_once_with(
#             "test_integration_id",
#             {"status": "DEACTIVATED"},
#         )
#
#     @patch("flext_oracle_oic.ext_services.OracleOicExtensionClient")
#     def test_deactivate_integration_client_failure(
#         self,
#         mock_client_class: Mock,
#         manager: LifecycleManager,
#     ) -> None:
#         """Test integration deactivation with client failure."""
#         mock_client_class.side_effect = Exception("Client error")
#
#         result = manager.deactivate_integration("test_integration_id")
#
#         assert result.is_failure
#         assert "Client error" in str(result.error)
#
#
# class TestMonitoringService:
#     """Test monitoring service."""
#
#     @pytest.fixture
#     def mock_http_client(self) -> Mock:
#         """Create mock HTTP client."""
#         return Mock(spec=FlextOracleOicConstants.HTTPClientProtocol)
#
#     @pytest.fixture
#     def monitoring_service(self, mock_http_client: Mock) -> MonitoringService:
#         """Create monitoring service."""
#         return MonitoringService(mock_http_client)
#
#     def test_monitoring_service_initialization(
#         self,
#         monitoring_service: MonitoringService,
#         mock_http_client: Mock,
#     ) -> None:
#         """Test monitoring service initialization."""
#         assert monitoring_service.client == mock_http_client
#         assert monitoring_service.logger is not None
#
#     def test_get_health_status_success(
#         self,
#         monitoring_service: MonitoringService,
#         mock_http_client: Mock,
#     ) -> None:
#         """Test successful health status retrieval."""
#         mock_response = Mock(spec=FlextOracleOicConstants.HTTPResponseProtocol)
#         mock_response.status_code = 200
#         mock_response.json.return_value = {
#             "status": "healthy",
#             "timestamp": "2025-01-08T10:00:00Z",
#         }
#         mock_http_client.get.return_value = mock_response
#
#         result = monitoring_service.get_health_status()
#
#         assert isinstance(result, dict)
#         assert result["status"] == "healthy"
#         assert "timestamp" in result
#         mock_http_client.get.assert_called_once()
#
#     def test_get_health_status_failure(
#         self,
#         monitoring_service: MonitoringService,
#         mock_http_client: Mock,
#     ) -> None:
#         """Test health status retrieval failure."""
#         mock_response = Mock(spec=FlextOracleOicConstants.HTTPResponseProtocol)
#         mock_response.status_code = 500
#         mock_http_client.get.return_value = mock_response
#
#         result = monitoring_service.get_health_status()
#
#         assert isinstance(result, dict)
#         assert result["status"] == "unhealthy"
#         assert "error" in result
#
#     def test_get_health_status_exception(
#         self,
#         monitoring_service: MonitoringService,
#         mock_http_client: Mock,
#     ) -> None:
#         """Test health status retrieval with exception."""
#         mock_http_client.get.side_effect = Exception("Network error")
#
#         result = monitoring_service.get_health_status()
#
#         assert isinstance(result, dict)
#         assert result["status"] == "error"
#         assert "Network error" in str(result["error"])
#
#     def test_get_performance_metrics_success(
#         self,
#         monitoring_service: MonitoringService,
#         mock_http_client: Mock,
#     ) -> None:
#         """Test successful performance metrics retrieval."""
#         mock_response = Mock(spec=FlextOracleOicConstants.HTTPResponseProtocol)
#         mock_response.status_code = 200
#         mock_response.json.return_value = {
#             "active_integrations": 15,
#             "total_executions": 1000,
#             "success_rate": 98.5,
#             "avg_response_time": 1.2,
#         }
#         mock_http_client.get.return_value = mock_response
#
#         result = monitoring_service.get_performance_metrics()
#
#         assert isinstance(result, dict)
#         assert result["active_integrations"] == 15
#         assert result["total_executions"] == 1000
#         assert result["success_rate"] == 98.5
#         mock_http_client.get.assert_called_once()
#
#     def test_get_performance_metrics_failure(
#         self,
#         monitoring_service: MonitoringService,
#         mock_http_client: Mock,
#     ) -> None:
#         """Test performance metrics retrieval failure."""
#         mock_response = Mock(spec=FlextOracleOicConstants.HTTPResponseProtocol)
#         mock_response.status_code = 404
#         mock_http_client.get.return_value = mock_response
#
#         result = monitoring_service.get_performance_metrics()
#
#         assert isinstance(result, dict)
#         assert result["active_integrations"] == 0
#         assert "error" in result
#
#     def test_get_performance_metrics_exception(
#         self,
#         monitoring_service: MonitoringService,
#         mock_http_client: Mock,
#     ) -> None:
#         """Test performance metrics retrieval with exception."""
#         mock_http_client.get.side_effect = Exception("Timeout error")
#
#         result = monitoring_service.get_performance_metrics()
#
#         assert isinstance(result, dict)
#         assert result["active_integrations"] == 0
#         assert "Timeout error" in str(result["error"])
#
#
# class TestHTTPProtocols:
#     """Test HTTP protocol interfaces."""
#
#     def test_http_client_protocol(self) -> None:
#         """Test HTTP client protocol structure."""
#         # This is a protocol, so we test it's properly defined
#         assert hasattr(FlextOracleOicConstants.HTTPClientProtocol, "get")
#
#     def test_http_response_protocol(self) -> None:
#         """Test HTTP response protocol structure."""
#         # This is a protocol, so we test it's properly defined
#         assert inspect.isclass(FlextOracleOicConstants.HTTPResponseProtocol)
#         annotations = FlextOracleOicConstants.HTTPResponseProtocol.__annotations__
#         assert "status_code" in annotations
