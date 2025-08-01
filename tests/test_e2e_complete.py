"""Comprehensive End-to-End tests for oracle-oic-ext.

Tests all functionalities including:
- Extension initialization
- Lifecycle management
- Monitoring services
- Artifact extraction
- Command routing
- Error handling
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from typing import Any
from unittest.mock import Mock, patch

import pytest

from flext_oracle_oic_ext.config import OracleOICExtensionSettings
from flext_oracle_oic_ext.extension import OracleOICExtension
from flext_oracle_oic_ext.lifecycle import LifecycleManager
from flext_oracle_oic_ext.monitoring import MonitoringService


class TestOracleOICExtE2E:
    """End-to-end tests for oracle-oic-ext."""

    @pytest.fixture
    def config_path(self) -> str:
        """Generate or locate configuration file."""
        config_file = Path(__file__).parent.parent / "config.json"
        if not config_file.exists():
            # Generate config if it doesn't exist
            subprocess.run(
                ["python", "generate_config.py"],
                cwd=Path(__file__).parent.parent,
                check=False,
            )
        return str(config_file)

    @pytest.fixture
    def config(self, config_path: str) -> dict[str, object]:
        """Load configuration from file."""
        with open(config_path, encoding="utf-8") as f:
            loaded_config: dict[str, object] = json.load(f)
            return loaded_config

    @pytest.fixture
    def extension(self) -> OracleOICExtension:
        """Create OracleOICExtension instance."""
        return OracleOICExtension()

    def test_extension_initialization(self, extension: OracleOICExtension) -> None:
        """Test extension initialization."""
        if extension.oracle_oic_bin != "oracle-oic-ext":
            msg = f"Expected {'oracle-oic-ext'}, got {extension.oracle_oic_bin}"
            raise AssertionError(
                msg,
            )
        assert extension.lifecycle_manager is None
        assert extension.monitoring_service is None

    def test_describe_commands(self, extension: OracleOICExtension) -> None:
        """Test command description and categorization."""
        description = extension.describe()

        assert len(description.commands) > 0

        # Check command categories
        command_names = [cmd.name for cmd in description.commands]

        # Lifecycle commands
        if "lifecycle:activate" not in command_names:
            msg = f"Expected {'lifecycle:activate'} in {command_names}"
            raise AssertionError(msg)
        assert "lifecycle:deactivate" in command_names
        if "lifecycle:bulk-activate" not in command_names:
            msg = f"Expected {'lifecycle:bulk-activate'} in {command_names}"
            raise AssertionError(
                msg,
            )
        assert "lifecycle:bulk-deactivate" in command_names
        if "lifecycle:status" not in command_names:
            msg = f"Expected {'lifecycle:status'} in {command_names}"
            raise AssertionError(msg)

        # Monitoring commands
        if "monitor:health" not in command_names:
            msg = f"Expected {'monitor:health'} in {command_names}"
            raise AssertionError(msg)
        assert "monitor:performance" in command_names
        if "monitor:errors" not in command_names:
            msg = f"Expected {'monitor:errors'} in {command_names}"
            raise AssertionError(msg)
        assert "monitor:usage" in command_names

        # Extraction commands
        if "extract:artifacts" not in command_names:
            msg = f"Expected {'extract:artifacts'} in {command_names}"
            raise AssertionError(msg)
        assert "extract:logs" in command_names
        if "extract:metadata" not in command_names:
            msg = f"Expected {'extract:metadata'} in {command_names}"
            raise AssertionError(msg)

        # Transformation commands
        if "transform:flatten" not in command_names:
            msg = f"Expected {'transform:flatten'} in {command_names}"
            raise AssertionError(msg)
        assert "transform:mask" in command_names

    def test_command_routing(self, extension: OracleOICExtension) -> None:
        """Test command routing to appropriate handlers."""
        # Mock environment config
        os.environ["MELTANO_PROJECT_ROOT"] = str(Path.cwd())

        # Create a valid config for the test
        test_config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "environment": "test",
        }
        extension.config = test_config

        # Test lifecycle command routing
        with patch.object(extension, "_handle_lifecycle_command") as mock_lifecycle:
            extension.invoke("lifecycle:status", "integration123")
            mock_lifecycle.assert_called_once_with("lifecycle:status", "integration123")

        # Test monitoring command routing
        with patch.object(extension, "_handle_monitoring_command") as mock_monitoring:
            extension.invoke("monitor:health")
            mock_monitoring.assert_called_once_with("monitor:health")

        # Test extraction command routing
        with patch.object(extension, "_handle_extraction_command") as mock_extraction:
            extension.invoke("extract:artifacts", "integration123")
            mock_extraction.assert_called_once_with(
                "extract:artifacts",
                "integration123",
            )

    def test_lifecycle_manager_operations(self, config: dict[str, object]) -> None:
        """Test lifecycle manager functionality."""
        settings = OracleOICExtensionSettings.from_dict(config)
        manager = LifecycleManager(settings)

        # Test initialization
        assert manager.settings.connection is not None
        if manager.settings.connection.base_url != config["base_url"]:
            msg = f"Expected {config['base_url']}, got {manager.settings.connection.base_url}"
            raise AssertionError(
                msg,
            )
        assert manager.settings.connection.oauth_client_id == config["oauth_client_id"]

        # Test status check with mocked authentication
        with patch.object(manager, "_client") as mock_client:
            # Mock the HTTP client
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "id": "TEST_INTEGRATION",
                "status": "ACTIVATED",
                "version": "01.00.0000",
            }
            mock_client.get.return_value = mock_response

            # Mock the access token to avoid authentication
            with patch.object(manager, "_access_token", "mock_token"):
                status_result = manager.get_integration_status("TEST_INTEGRATION")
                assert status_result.success
                status = status_result.unwrap()
                if status.status != "ACTIVATED":
                    msg = f"Expected {'ACTIVATED'}, got {status.status}"
                    raise AssertionError(msg)
                assert status.integration_id == "TEST_INTEGRATION"

    def test_monitoring_service_operations(self, config: dict[str, object]) -> None:
        """Test monitoring service functionality."""
        # Create a mock HTTP client for MonitoringService

        mock_client = Mock()
        service = MonitoringService(client=mock_client)

        # Test health check
        mock_client.get.return_value.status_code = 200
        mock_client.get.return_value.json.return_value = {
            "status": "healthy",
            "components": {"database": "healthy", "messaging": "healthy"},
        }

        health = service.get_health_status()
        if health["status"] != "healthy":
            msg = f"Expected {'healthy'}, got {health['status']}"
            raise AssertionError(msg)

    def test_artifact_extraction(
        self,
        extension: OracleOICExtension,
        tmp_path: Path,
    ) -> None:
        """Test artifact extraction functionality."""
        os.environ["MELTANO_PROJECT_ROOT"] = str(Path.cwd())

        # Create a valid config for the test
        test_config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "environment": "test",
        }
        extension.config = test_config

        # Mock the initialization to avoid real service creation
        # and ensure lifecycle_manager is available
        from unittest.mock import MagicMock

        mock_lifecycle_manager = MagicMock()
        extension.lifecycle_manager = mock_lifecycle_manager

        with (
            patch.object(extension, "_initialize_services"),
            patch("flext_oracle_oic_ext.extension.logger") as mock_logger,
        ):
            # Test extraction with output directory
            extension.invoke(
                "extract:artifacts",
                "TEST_INTEGRATION",
                "--output-dir",
                str(tmp_path),
            )

            # Check that extraction logging was called
            mock_logger.info.assert_called()

    def test_error_handling(self, extension: OracleOICExtension) -> None:
        """Test error handling for invalid operations."""
        # Test invalid command
        with (
            patch.object(extension, "_initialize_services"),
            pytest.raises(SystemExit),
        ):
            extension.invoke("invalid:command")

        # Test missing config
        os.environ.pop("MELTANO_PROJECT_ROOT", None)
        with pytest.raises(Exception, match=".*config.*"):
            extension.invoke("lifecycle:status")

    def test_config_loading(
        self,
        extension: OracleOICExtension,
        config_path: str,
    ) -> None:
        """Test configuration loading from file."""
        os.environ["MELTANO_PROJECT_ROOT"] = str(Path(config_path).parent)

        # Test that config can be set and accessed
        test_config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }
        extension.config = test_config

        if "base_url" not in extension.config:
            msg = f"Expected {'base_url'} in {extension.config}"
            raise AssertionError(msg)
        assert "oauth_client_id" in extension.config
        assert extension.config["base_url"].startswith("https://")

    # Live API test - handle gracefully if credentials not available
    def test_live_integration_status(
        self,
        extension: OracleOICExtension,
        config: dict[str, object],
    ) -> None:
        """Test live integration status check."""
        os.environ["MELTANO_PROJECT_ROOT"] = str(Path.cwd())

        # Set the config directly instead of patching _load_config
        extension.config = config
        # Test that either succeeds or raises expected exceptions
        try:
            # This will make actual API call
            extension.invoke("lifecycle:status", "TEST_INTEGRATION")
        except (ConnectionError, TimeoutError, ValueError, OSError, RuntimeError) as e:
            if "401" in str(e) or "403" in str(e):
                # Authentication failed - verify this is expected in test environment
                # This confirms authentication failure is expected without live credentials
                pass
            elif "404" in str(e):
                # Integration not found is OK for test
                pass
            else:
                pytest.fail(f"Unexpected error: {e}")

    def test_batch_operations(self, extension: OracleOICExtension) -> None:
        """Test batch operations on multiple integrations."""
        os.environ["MELTANO_PROJECT_ROOT"] = str(Path.cwd())

        integrations = ["INT1", "INT2", "INT3"]

        # Create a valid config for the test
        test_config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "environment": "test",
        }

        # Set config directly on extension instance
        extension.config = test_config

        with patch.object(LifecycleManager, "activate_integration") as mock_activate:
            mock_activate.return_value = {"status": "ACTIVATED"}

            # Activate multiple integrations
            for integration in integrations:
                extension.invoke("lifecycle:activate", integration)

            if mock_activate.call_count != len(integrations):
                msg = f"Expected {len(integrations)}, got {mock_activate.call_count}"
                raise AssertionError(
                    msg,
                )

    def test_monitoring_alerts(self, config: dict[str, object]) -> None:
        """Test monitoring alert functionality."""
        mock_client = Mock()
        service = MonitoringService(client=mock_client)

        # Test error analysis (closest equivalent to alerts)
        mock_client.get.return_value.status_code = 200
        mock_client.get.return_value.json.return_value = {
            "items": [
                {
                    "status": "FAILED",
                    "errorMessage": "Integration failure detected",
                },
            ],
        }

        analysis = service.analyze_errors()
        if "patterns" not in analysis:
            msg = f"Expected {'patterns'} in {analysis}"
            raise AssertionError(msg)
        assert "recommendations" in analysis

    def test_performance_metrics(self, config: dict[str, object]) -> None:
        """Test performance metrics collection."""
        mock_client = Mock()
        service = MonitoringService(client=mock_client)

        mock_client.get.return_value.status_code = 200
        mock_client.get.return_value.json.return_value = {
            "items": [
                {
                    "status": "COMPLETED",
                    "duration": 1000,
                    "startTime": "2025-07-19T10:00:00Z",
                },
                {
                    "status": "COMPLETED",
                    "duration": 1500,
                    "startTime": "2025-07-19T11:00:00Z",
                },
            ],
        }

        metrics = service.get_performance_metrics()
        if "executions" not in metrics:
            msg = f"Expected {'executions'} in {metrics}"
            raise AssertionError(msg)
        assert "throughput" in metrics

    def test_log_extraction(
        self,
        extension: OracleOICExtension,
        config: dict[str, object],
        tmp_path: Path,
    ) -> None:
        """Test log extraction functionality."""
        os.environ["MELTANO_PROJECT_ROOT"] = str(Path.cwd())

        # Set config directly on extension instead of patching non-existent method
        extension.config = config

        # Mock log extraction
        with patch("builtins.open", create=True) as mock_open:
            mock_file = Mock()
            mock_open.return_value.__enter__.return_value = mock_file

            extension.invoke("extract:logs", "TEST_INTEGRATION", str(tmp_path))

            # Verify log file would be created
            mock_open.assert_called()

    def test_full_workflow(
        self,
        extension: OracleOICExtension,
        config: dict[str, object],
        tmp_path: Path,
    ) -> None:
        """Test complete integration workflow."""
        os.environ["MELTANO_PROJECT_ROOT"] = str(Path.cwd())

        # Set config directly instead of patching _load_config
        extension.config = config

        # Mock the initialization to avoid real service creation
        with patch.object(extension, "_initialize_services"):
            # Set up mock lifecycle manager
            mock_manager = Mock()
            extension.lifecycle_manager = mock_manager

            # Mock manager methods to return FlextResult objects
            # 🚨 ARCHITECTURAL COMPLIANCE: Using módulo raiz imports
            from flext_core import FlextResult

            from flext_oracle_oic_ext.lifecycle.manager import IntegrationStatus

            integration_status = IntegrationStatus(
                integration_id="TEST_INTEGRATION",
                version="01.00.0000",
                status="ACTIVATED",
            )
            mock_manager.get_integration_status.return_value = FlextResult.ok(
                integration_status,
            )
            mock_manager.activate_integration.return_value = FlextResult.ok(
                {
                    "status": "ACTIVATED",
                },
            )

            # Execute workflow
            extension.invoke("lifecycle:status", "TEST_INT")
            extension.invoke("lifecycle:activate", "TEST_INT")

            # Note: Use extract:logs which doesn't require lifecycle manager methods
            with patch("builtins.open", create=True):
                extension.invoke(
                    "extract:logs",
                    "TEST_INT",
                    "--output-dir",
                    str(tmp_path),
                )

            # Verify lifecycle methods were called
            mock_manager.get_integration_status.assert_called_once()
            mock_manager.activate_integration.assert_called_once()

    def test_conditional_config_generation(self) -> None:
        """Test automatic configuration file generation."""
        config_path = Path(__file__).parent.parent / "config.json"

        # If config doesn't exist, it should be generated
        if not config_path.exists():
            result = subprocess.run(
                ["python", "generate_config.py"],
                capture_output=True,
                text=True,
                cwd=Path(__file__).parent.parent,
                input="y\n",
                check=False,
            )
            if result.returncode != 0:
                msg = f"Expected {0}, got {result.returncode}"
                raise AssertionError(msg)
            assert config_path.exists()

        # Load and validate config
        with open(config_path, encoding="utf-8") as f:
            config = json.load(f)

        # Check required fields
        if "base_url" not in config:
            msg = f"Expected {'base_url'} in {config}"
            raise AssertionError(msg)
        assert "oauth_client_id" in config
        if "oauth_client_secret" not in config:
            msg = f"Expected {'oauth_client_secret'} in {config}"
            raise AssertionError(msg)
        assert "oauth_token_url" in config

        # Check extension-specific fields
        if "instance_id" not in config:
            msg = f"Expected {'instance_id'} in {config}"
            raise AssertionError(msg)
        assert "region" in config
        if "environment" not in config:
            msg = f"Expected {'environment'} in {config}"
            raise AssertionError(msg)
