"""Simple API for FLEXT Oracle OIC Extension setup and configuration.

Provides a simple interface for setting up Oracle Integration Cloud extensions.
Uses flext-core patterns for configuration and error handling.
"""

from __future__ import annotations

from typing import Any

from flext_core import ServiceResult
from flext_observability.logging import get_logger, setup_logging
from flext_oracle_oic_ext.config import OracleOICExtensionSettings

logger = get_logger(__name__)


def setup_oic_extension(
    settings: OracleOICExtensionSettings | None = None,
) -> ServiceResult[OracleOICExtensionSettings]:
    """Setup Oracle OIC extension with logging and configuration validation."""
    try:
        if settings is None:
            # This will fail if required connection params aren't in environment
            settings = OracleOICExtensionSettings()

        # Setup logging using flext-observability
        setup_logging(level=settings.log_level, format="json")

        return ServiceResult.ok(settings)

    except Exception as e:
        return ServiceResult.fail(f"Failed to setup OIC extension: {e}")


def create_development_oic_config(
    base_url: str = "https://dev-instance.integration.ocp.oraclecloud.com",
    oauth_client_id: str = "dev_client_id",
    oauth_client_secret: str = "dev_client_secret",
    oauth_token_url: str = "https://idcs-dev.identity.oraclecloud.com/oauth2/v1/token",
    **overrides: Any,
) -> OracleOICExtensionSettings:
    """Create development configuration with conservative settings."""
    config = {
        "connection": {
            "base_url": base_url,
            "oauth_client_id": oauth_client_id,
            "oauth_client_secret": oauth_client_secret,
            "oauth_token_url": oauth_token_url,
        },
        "lifecycle": {
            "auto_activate": False,
            "health_check_interval": 300,
            "activation_timeout": 60,
            "validate_before_activate": True,
            "rollback_on_failure": True,
        },
        "monitoring": {
            "enable_monitoring": True,
            "monitoring_interval": 60,
            "alert_threshold": 80,
            "error_window_hours": 12,
            "performance_window_hours": 3,
        },
        "performance": {
            "request_timeout": 30,
            "max_retries": 3,
            "retry_delay": 1.0,
            "batch_size": 50,
            "max_concurrent_requests": 3,
        },
        "extraction": {
            "extract_artifacts": True,
            "extract_logs": True,
            "extract_metadata": True,
            "artifact_directory": "./dev_artifacts",
            "log_window_hours": 12,
        },
        "environment": "dev",
        "log_level": "DEBUG",
        "debug": True,
    }

    # Override with provided values
    for key, value in overrides.items():
        if isinstance(value, dict) and key in config and isinstance(config[key], dict):
            config[key].update(value)
        else:
            config[key] = value

    return OracleOICExtensionSettings(**config)


def create_production_oic_config(
    base_url: str,
    oauth_client_id: str,
    oauth_client_secret: str,
    oauth_token_url: str,
    **overrides: Any,
) -> OracleOICExtensionSettings:
    """Create production configuration with performance optimizations."""
    config = {
        "connection": {
            "base_url": base_url,
            "oauth_client_id": oauth_client_id,
            "oauth_client_secret": oauth_client_secret,
            "oauth_token_url": oauth_token_url,
        },
        "lifecycle": {
            "auto_activate": True,
            "health_check_interval": 600,
            "activation_timeout": 120,
            "validate_before_activate": True,
            "rollback_on_failure": True,
        },
        "monitoring": {
            "enable_monitoring": True,
            "monitoring_interval": 300,
            "alert_threshold": 95,
            "error_window_hours": 24,
            "performance_window_hours": 6,
        },
        "performance": {
            "request_timeout": 60,
            "max_retries": 5,
            "retry_delay": 2.0,
            "batch_size": 100,
            "max_concurrent_requests": 10,
        },
        "extraction": {
            "extract_artifacts": True,
            "extract_logs": True,
            "extract_metadata": True,
            "artifact_directory": "/opt/oic/artifacts",
            "log_window_hours": 24,
        },
        "environment": "prod",
        "log_level": "INFO",
        "debug": False,
    }

    # Override with provided values
    for key, value in overrides.items():
        if isinstance(value, dict) and key in config and isinstance(config[key], dict):
            config[key].update(value)
        else:
            config[key] = value

    return OracleOICExtensionSettings(**config)


def create_test_oic_config(**overrides: Any) -> OracleOICExtensionSettings:
    """Create test configuration with minimal resource usage."""
    config = {
        "connection": {
            "base_url": "https://test-instance.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://idcs-test.identity.oraclecloud.com/oauth2/v1/token",
        },
        "lifecycle": {
            "auto_activate": False,
            "health_check_interval": 3600,
            "activation_timeout": 30,
            "validate_before_activate": False,
            "rollback_on_failure": False,
        },
        "monitoring": {
            "enable_monitoring": False,
            "monitoring_interval": 3600,
            "alert_threshold": 50,
            "error_window_hours": 1,
            "performance_window_hours": 1,
        },
        "performance": {
            "request_timeout": 10,
            "max_retries": 1,
            "retry_delay": 0.5,
            "batch_size": 10,
            "max_concurrent_requests": 1,
        },
        "extraction": {
            "extract_artifacts": False,
            "extract_logs": False,
            "extract_metadata": True,
            "artifact_directory": "./test_artifacts",
            "log_window_hours": 1,
        },
        "environment": "test",
        "log_level": "WARNING",
        "debug": False,
    }

    # Override with provided values
    for key, value in overrides.items():
        if isinstance(value, dict) and key in config and isinstance(config[key], dict):
            config[key].update(value)
        else:
            config[key] = value

    return OracleOICExtensionSettings(**config)


def create_sandbox_oic_config(**overrides: Any) -> OracleOICExtensionSettings:
    """Create sandbox configuration for experimentation and learning."""
    config = {
        "connection": {
            "base_url": "https://sandbox.integration.ocp.oraclecloud.com",
            "oauth_client_id": "sandbox_client",
            "oauth_client_secret": "sandbox_secret",
            "oauth_token_url": "https://idcs-sandbox.identity.oraclecloud.com/oauth2/v1/token",
        },
        "lifecycle": {
            "auto_activate": False,
            "health_check_interval": 60,
            "activation_timeout": 30,
            "validate_before_activate": False,
            "rollback_on_failure": False,
        },
        "monitoring": {
            "enable_monitoring": True,
            "monitoring_interval": 30,
            "alert_threshold": 70,
            "error_window_hours": 2,
            "performance_window_hours": 1,
        },
        "performance": {
            "request_timeout": 20,
            "max_retries": 2,
            "retry_delay": 0.5,
            "batch_size": 25,
            "max_concurrent_requests": 2,
        },
        "extraction": {
            "extract_artifacts": True,
            "extract_logs": True,
            "extract_metadata": True,
            "artifact_directory": "./sandbox_artifacts",
            "log_window_hours": 4,
        },
        "environment": "dev",  # Sandbox uses dev environment
        "log_level": "DEBUG",
        "debug": True,
    }

    # Override with provided values
    for key, value in overrides.items():
        if isinstance(value, dict) and key in config and isinstance(config[key], dict):
            config[key].update(value)
        else:
            config[key] = value

    return OracleOICExtensionSettings(**config)


def configure_for_meltano(
    config_dict: dict[str, Any],
) -> ServiceResult[OracleOICExtensionSettings]:
    """Configure Oracle OIC extension from Meltano configuration dictionary."""
    try:
        settings = OracleOICExtensionSettings.from_dict(config_dict)
        return ServiceResult.ok(settings)
    except Exception as e:
        return ServiceResult.fail(f"Failed to configure from Meltano: {e}")


# Export convenience functions
__all__ = [
    "configure_for_meltano",
    "create_development_oic_config",
    "create_production_oic_config",
    "create_sandbox_oic_config",
    "create_test_oic_config",
    "setup_oic_extension",
]
