"""Modern Configuration System using flext-core patterns.

MIGRATED TO FLEXT-CORE: Uses flext-core BaseSettings and DomainValueObject patterns.
Zero tolerance for code duplication.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from pydantic import Field, field_validator, model_validator
from pydantic_settings import SettingsConfigDict

from flext_core.config import BaseSettings, singleton
from flext_core.domain.pydantic_base import DomainValueObject
from flext_core.domain.types import (
    FlextConstants,
    LogLevelLiteral,
)


class OICExtensionConnectionConfig(DomainValueObject):
    """Oracle Integration Cloud connection configuration using flext-core patterns."""

    base_url: str = Field(
        ...,
        description="OIC instance base URL (e.g., https://instance.integration.ocp.oraclecloud.com)",
        min_length=1,
    )

    oauth_client_id: str = Field(
        ...,
        description="OAuth2 client ID from IDCS application",
        min_length=1,
    )

    oauth_client_secret: str = Field(
        ...,
        description="OAuth2 client secret from IDCS application",
        min_length=1,
    )

    oauth_token_url: str = Field(
        ...,
        description="IDCS token endpoint URL",
        min_length=1,
    )

    oauth_scope: str | None = Field(
        None,
        description="OAuth2 scope for authentication",
    )

    @field_validator("base_url")
    @classmethod
    def validate_base_url(cls, v: str) -> str:
        """Validate base URL format.

        Args:
            v: The base URL to validate.

        Returns:
            The validated and normalized base URL.

        Raises:
            ValueError: If URL doesn't start with http:// or https://.

        """
        if not v.startswith(("http://", "https://")):
            msg = "base_url must start with http:// or https://"
            raise ValueError(msg)
        return v.rstrip("/")

    @field_validator("oauth_token_url")
    @classmethod
    def validate_oauth_token_url(cls, v: str) -> str:
        """Validate OAuth token URL format.

        Args:
            v: The OAuth token URL to validate.

        Returns:
            The validated OAuth token URL.

        Raises:
            ValueError: If URL doesn't start with http:// or https://.

        """
        if not v.startswith(("http://", "https://")):
            msg = "oauth_token_url must start with http:// or https://"
            raise ValueError(msg)
        return v


class OICExtensionLifecycleConfig(DomainValueObject):
    """Oracle Integration Cloud lifecycle configuration using flext-core patterns."""

    auto_activate: bool = Field(
        default=False,
        description="Automatically activate integrations after deployment",
    )

    health_check_interval: int = Field(
        default=300,
        ge=30,
        le=3600,
        description="Health check interval in seconds",
    )

    activation_timeout: int = Field(
        default=FlextConstants.DEFAULT_REQUEST_TIMEOUT,
        ge=30,
        le=600,
        description="Activation timeout in seconds",
    )

    validate_before_activate: bool = Field(
        default=True,
        description="Validate integration before activation",
    )

    rollback_on_failure: bool = Field(
        default=True,
        description="Rollback on activation failure",
    )


class OICExtensionMonitoringConfig(DomainValueObject):
    """Oracle Integration Cloud monitoring configuration using flext-core patterns."""

    enable_monitoring: bool = Field(
        default=True,
        description="Enable monitoring capabilities",
    )

    monitoring_interval: int = Field(
        default=60,
        ge=10,
        le=3600,
        description="Monitoring interval in seconds",
    )

    alert_threshold: int = Field(
        default=90,
        ge=50,
        le=100,
        description="Alert threshold percentage",
    )

    error_window_hours: int = Field(
        default=24,
        ge=1,
        le=168,
        description="Error analysis window in hours",
    )

    performance_window_hours: int = Field(
        default=6,
        ge=1,
        le=72,
        description="Performance analysis window in hours",
    )


class OICExtensionPerformanceConfig(DomainValueObject):
    """Oracle Integration Cloud performance configuration using flext-core patterns."""

    request_timeout: int = Field(
        default=FlextConstants.DEFAULT_REQUEST_TIMEOUT,
        ge=10,
        le=300,
        description="Request timeout in seconds",
    )

    max_retries: int = Field(
        default=FlextConstants.DEFAULT_MAX_RETRIES,
        ge=0,
        le=10,
        description="Maximum number of retry attempts",
    )

    retry_delay: float = Field(
        default=1.0,
        ge=0.1,
        le=60.0,
        description="Delay between retries in seconds",
    )

    batch_size: int = Field(
        default=1000,
        ge=1,
        le=10000,
        description="Batch size for bulk operations",
    )

    max_concurrent_requests: int = Field(
        default=5,
        ge=1,
        le=20,
        description="Maximum concurrent requests",
    )


class OICExtensionExtractionConfig(DomainValueObject):
    """Oracle Integration Cloud extraction configuration using flext-core patterns."""

    extract_artifacts: bool = Field(
        default=True,
        description="Enable artifact extraction",
    )

    extract_logs: bool = Field(
        default=True,
        description="Enable log extraction",
    )

    extract_metadata: bool = Field(
        default=True,
        description="Enable metadata extraction",
    )

    artifact_directory: str = Field(
        default="./artifacts",
        description="Directory for extracted artifacts",
    )

    log_window_hours: int = Field(
        default=24,
        ge=1,
        le=168,
        description="Log extraction window in hours",
    )


@singleton()
class OracleOICExtensionSettings(BaseSettings):
    """Oracle Integration Cloud extension configuration using flext-core patterns."""

    model_config = SettingsConfigDict(
        env_prefix="ORACLE_OIC_EXT_",
        env_nested_delimiter="__",
        case_sensitive=False,
        validate_assignment=True,
        extra="forbid",
        frozen=True,
    )

    # Core project metadata
    project_name: str = Field(
        default="flext-oracle-oic-ext",
        description="Project name",
    )

    version: str = Field(
        default="0.7.0",
        description="Project version",
    )

    # Connection configuration
    connection: OICExtensionConnectionConfig = Field(
        ...,
        description="Oracle Integration Cloud connection configuration",
    )

    # Lifecycle configuration
    lifecycle: OICExtensionLifecycleConfig = Field(
        default_factory=OICExtensionLifecycleConfig,
        description="Lifecycle management configuration",
    )

    # Monitoring configuration
    monitoring: OICExtensionMonitoringConfig = Field(
        default_factory=OICExtensionMonitoringConfig,
        description="Monitoring configuration",
    )

    # Performance configuration
    performance: OICExtensionPerformanceConfig = Field(
        default_factory=OICExtensionPerformanceConfig,
        description="Performance configuration",
    )

    # Extraction configuration
    extraction: OICExtensionExtractionConfig = Field(
        default_factory=OICExtensionExtractionConfig,
        description="Extraction configuration",
    )

    # Instance configuration
    instance_id: str | None = Field(
        None,
        description="OIC instance identifier",
    )

    region: str | None = Field(
        None,
        description="OIC region",
    )

    environment: Literal["dev", "test", "stage", "prod"] = Field(
        default="test",
        description="Environment name",
    )

    # Logging configuration
    log_level: LogLevelLiteral = Field(
        default=FlextConstants.DEFAULT_LOG_LEVEL,
        description="Log level",
    )

    debug: bool = Field(
        default=False,
        description="Enable debug mode",
    )

    @model_validator(mode="after")
    def validate_configuration(self) -> OracleOICExtensionSettings:
        """Validate configuration after model creation.

        Returns:
            The validated configuration instance.

        Raises:
            ValueError: If configuration validation fails.

        """
        # Validate artifact directory

        artifact_path = Path(self.extraction.artifact_directory)
        if not artifact_path.exists():
            try:
                artifact_path.mkdir(parents=True, exist_ok=True)
            except OSError as e:
                msg = f"Cannot create artifact directory {artifact_path}: {e}"
                raise ValueError(
                    msg,
                ) from e

        # Validate OAuth scope if not provided:
        if not self.connection.oauth_scope:
            # Set default scope based on base URL
            base_url = self.connection.base_url.rstrip("/")
            object.__setattr__(
                self.connection,
                "oauth_scope",
                f"{base_url}urn:opc:resource:consumer:all",
            )

        return self

    @classmethod
    def from_dict(cls, config_dict: dict[str, Any]) -> OracleOICExtensionSettings:
        """Create settings instance from dictionary.

        Args:
            config_dict: Dictionary containing configuration values.

        Returns:
            OracleOICExtensionSettings instance.

        """
        # Transform flat config to nested structure
        connection_config = {
            "base_url": config_dict.get("base_url"),
            "oauth_client_id": config_dict.get("oauth_client_id"),
            "oauth_client_secret": config_dict.get("oauth_client_secret"),
            "oauth_token_url": config_dict.get("oauth_token_url"),
            "oauth_scope": config_dict.get("oauth_scope"),
        }

        lifecycle_config = {
            "auto_activate": config_dict.get("auto_activate", False),
            "health_check_interval": config_dict.get("health_check_interval", 300),
            "activation_timeout": config_dict.get("activation_timeout", 60),
            "validate_before_activate": config_dict.get(
                "validate_before_activate",
                True,
            ),
            "rollback_on_failure": config_dict.get("rollback_on_failure", True),
        }

        monitoring_config = {
            "enable_monitoring": config_dict.get("enable_monitoring", True),
            "monitoring_interval": config_dict.get("monitoring_interval", 60),
            "alert_threshold": config_dict.get("alert_threshold", 90),
            "error_window_hours": config_dict.get("error_window_hours", 24),
            "performance_window_hours": config_dict.get("performance_window_hours", 6),
        }

        performance_config = {
            "request_timeout": config_dict.get("request_timeout", 60),
            "max_retries": config_dict.get("max_retries", 3),
            "retry_delay": config_dict.get("retry_delay", 1.0),
            "batch_size": config_dict.get("batch_size", 100),
            "max_concurrent_requests": config_dict.get("max_concurrent_requests", 5),
        }

        extraction_config = {
            "extract_artifacts": config_dict.get("extract_artifacts", True),
            "extract_logs": config_dict.get("extract_logs", True),
            "extract_metadata": config_dict.get("extract_metadata", True),
            "artifact_directory": config_dict.get("artifact_directory", "./artifacts"),
            "log_window_hours": config_dict.get("log_window_hours", 24),
        }

        return cls(
            connection=OICExtensionConnectionConfig(**connection_config),
            lifecycle=OICExtensionLifecycleConfig(**lifecycle_config),
            monitoring=OICExtensionMonitoringConfig(**monitoring_config),
            performance=OICExtensionPerformanceConfig(**performance_config),
            extraction=OICExtensionExtractionConfig(**extraction_config),
            instance_id=config_dict.get("instance_id"),
            region=config_dict.get("region"),
            environment=config_dict.get("environment", "test"),
            log_level=config_dict.get("log_level", "INFO"),
            debug=config_dict.get("debug", False),
        )

    def to_dict(self) -> dict[str, str | int | float | bool | None]:
        """Convert settings to dictionary format.

        Returns:
            Dictionary representation of all configuration values.

        """
        return {  # Connection config
            "base_url": self.connection.base_url,
            "oauth_client_id": self.connection.oauth_client_id,
            "oauth_client_secret": self.connection.oauth_client_secret,
            "oauth_token_url": self.connection.oauth_token_url,
            "oauth_scope": self.connection.oauth_scope,
            # Lifecycle config
            "auto_activate": self.lifecycle.auto_activate,
            "health_check_interval": self.lifecycle.health_check_interval,
            "activation_timeout": self.lifecycle.activation_timeout,
            "validate_before_activate": self.lifecycle.validate_before_activate,
            "rollback_on_failure": self.lifecycle.rollback_on_failure,
            # Monitoring config
            "enable_monitoring": self.monitoring.enable_monitoring,
            "monitoring_interval": self.monitoring.monitoring_interval,
            "alert_threshold": self.monitoring.alert_threshold,
            "error_window_hours": self.monitoring.error_window_hours,
            "performance_window_hours": self.monitoring.performance_window_hours,
            # Performance config
            "request_timeout": self.performance.request_timeout,
            "max_retries": self.performance.max_retries,
            "retry_delay": self.performance.retry_delay,
            "batch_size": self.performance.batch_size,
            "max_concurrent_requests": self.performance.max_concurrent_requests,
            # Extraction config
            "extract_artifacts": self.extraction.extract_artifacts,
            "extract_logs": self.extraction.extract_logs,
            "extract_metadata": self.extraction.extract_metadata,
            "artifact_directory": self.extraction.artifact_directory,
            "log_window_hours": self.extraction.log_window_hours,
            # Instance config
            "instance_id": self.instance_id,
            "region": self.region,
            "environment": self.environment,
            # Other config
            "log_level": self.log_level,
            "debug": self.debug,
        }

    def get_auth_config(self) -> dict[str, str]:
        """Get authentication configuration.

        Returns:
            Dictionary containing OAuth authentication configuration.

        """
        return {
            "oauth_client_id": self.connection.oauth_client_id,
            "oauth_client_secret": self.connection.oauth_client_secret,
            "oauth_token_url": self.connection.oauth_token_url,
            "oauth_scope": self.connection.oauth_scope or "",
        }


from pathlib import Path  # TODO: Move import to module level
from typing import Any

# Copyright (c) 2025 FLEXT Team
# Licensed under the MIT License
# SPDX-License-Identifier: MIT
