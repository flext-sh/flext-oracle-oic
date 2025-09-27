"""Oracle OIC Extension Configuration - Unified Class Pattern.

FLEXT Unified Class Pattern: Single OracleOICExtensionConfig class
with nested configuration classes following FLEXT architectural standards.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Literal, Self

from pydantic import Field, SecretStr, field_validator, model_validator
from pydantic_settings import SettingsConfigDict

from flext_core import FlextConfig, FlextResult
from flext_oracle_oic_ext.constants import FlextOracleOicExtConstants
from flext_oracle_oic_ext.typings import FlextOracleOicExtTypes
from flext_oracle_oic_ext.utilities import FlextOracleOicExtUtilities

# Type definitions outside class to avoid Pydantic field errors
EnvironmentLiteral = Literal["development", "staging", "production"]
LogLevelLiteral = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
OICApiVersionLiteral = Literal["v1", "v2"]


class FlextOracleOicExtConfig(FlextConfig):
    """Single Pydantic 2 Settings class for flext-oracle-oic-ext extending FlextConfig.

    Follows standardized pattern:
    - Extends FlextConfig from flext-core
    - No nested classes within Config
    - All defaults from FlextOracleOicExtConstants
    - Uses enhanced singleton pattern with inverse dependency injection
    - Uses Pydantic 2.11+ features (field_validator, model_validator)
    """

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_ORACLE_OIC_EXT_",
        case_sensitive=False,
        extra="allow",
        # Inherit enhanced Pydantic 2.11+ features from FlextConfig
        validate_assignment=True,
        str_strip_whitespace=True,
        json_schema_extra={
            "title": "FLEXT Oracle OIC Extension Configuration",
            "description": "Oracle OIC Extension configuration extending FlextConfig",
        },
    )

    # Oracle OIC Connection Configuration using FlextOracleOicExtConstants for defaults
    base_url: str = Field(
        default=FlextOracleOicExtConstants.OIC.DEFAULT_BASE_URL,
        description="Oracle OIC base URL",
    )

    api_version: str = Field(
        default=FlextOracleOicExtConstants.OIC.DEFAULT_API_VERSION,
        description="Oracle OIC API version",
    )

    request_timeout: int = Field(
        default=FlextOracleOicExtConstants.OIC.DEFAULT_REQUEST_TIMEOUT,
        description="Request timeout in seconds",
        ge=1,
        le=300,
    )

    max_retries: int = Field(
        default=FlextOracleOicExtConstants.OIC.DEFAULT_MAX_RETRIES,
        description="Maximum number of retry attempts",
        ge=0,
        le=10,
    )

    use_ssl: bool = Field(
        default=FlextOracleOicExtConstants.OIC.DEFAULT_USE_SSL,
        description="Use SSL for connections",
    )

    verify_ssl: bool = Field(
        default=FlextOracleOicExtConstants.OIC.DEFAULT_VERIFY_SSL,
        description="Verify SSL certificates",
    )

    # Oracle OIC Authentication Configuration using FlextOracleOicExtConstants for defaults
    oauth_client_id: str = Field(
        default=FlextOracleOicExtConstants.Auth.DEFAULT_OAUTH_CLIENT_ID,
        description="OAuth2 client ID",
    )

    oauth_client_secret: SecretStr = Field(
        default_factory=lambda: SecretStr(
            FlextOracleOicExtConstants.Auth.DEFAULT_OAUTH_CLIENT_SECRET
        ),
        description="OAuth2 client secret (sensitive)",
    )

    oauth_token_url: str = Field(
        default=FlextOracleOicExtConstants.Auth.DEFAULT_OAUTH_TOKEN_URL,
        description="OAuth2 token URL",
    )

    oauth_client_aud: str | None = Field(
        default=FlextOracleOicExtConstants.Auth.DEFAULT_OAUTH_CLIENT_AUD,
        description="OAuth2 client audience",
    )

    oauth_scope: str = Field(
        default=FlextOracleOicExtConstants.Auth.DEFAULT_OAUTH_SCOPE,
        description="OAuth2 scope",
    )

    # Feature Configuration using FlextOracleOicExtConstants for defaults
    enable_monitoring: bool = Field(
        default=True, description="Enable monitoring features"
    )

    enable_enterprise_patterns: bool = Field(
        default=True, description="Enable enterprise patterns"
    )

    enable_orchestration: bool = Field(
        default=True, description="Enable orchestration features"
    )

    # Project Identification
    project_name: str = Field(
        default="flext-oracle-oic-ext",
        description="Project name",
    )

    project_version: str = Field(
        default="0.9.0",
        description="Project version",
    )

    # Pydantic 2.11+ field validators
    @field_validator("base_url")
    @classmethod
    def validate_base_url(cls, v: str) -> str:
        """Validate base URL format using FlextOracleOicExtUtilities."""
        result = FlextOracleOicExtUtilities.ConnectionValidation.validate_base_url(v)
        if result.is_failure:
            error_msg = result.error
            raise ValueError(error_msg)
        return result.value

    @field_validator("oauth_token_url")
    @classmethod
    def validate_oauth_token_url(cls, v: str) -> str:
        """Validate OAuth token URL format using FlextOracleOicExtUtilities."""
        result = FlextOracleOicExtUtilities.AuthenticationValidation.validate_oauth_token_url(
            v
        )
        if result.is_failure:
            error_msg = result.error
            raise ValueError(error_msg)
        return result.value

    @model_validator(mode="after")
    def validate_oracle_oic_configuration_consistency(self) -> Self:
        """Validate Oracle OIC configuration consistency."""
        # Validate OAuth configuration
        if self.oauth_client_id:
            # Validate client ID format
            client_id_result = FlextOracleOicExtUtilities.AuthenticationValidation.validate_oauth_client_id(
                self.oauth_client_id
            )
            if client_id_result.is_failure:
                error_msg = f"OAuth client ID validation: {client_id_result.error}"
                raise ValueError(error_msg)

        if self.oauth_client_id and not self.oauth_client_secret:
            error_msg = "OAuth client secret is required when client ID is provided"
            raise ValueError(error_msg)

        return self

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate Oracle OIC Extension specific business rules."""
        try:
            # Validate authentication requirements
            if (
                not self.oauth_client_id
                or not self.oauth_client_secret.get_secret_value()
            ):
                return FlextResult[None].fail("OAuth credentials are required")

            # Validate connection settings
            if self.request_timeout < 5:
                return FlextResult[None].fail(
                    "Request timeout too low (minimum 5 seconds)"
                )

            # Validate retry settings
            if self.max_retries > 10:
                return FlextResult[None].fail("Max retries too high (maximum 10)")

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Business rules validation failed: {e}")

    def get_connection_context(self) -> FlextOracleOicExtTypes.Core.ContextDict:
        """Get Oracle OIC connection configuration context."""
        return {
            "base_url": self.base_url,
            "api_version": self.api_version,
            "timeout": self.request_timeout,
            "max_retries": self.max_retries,
            "use_ssl": self.use_ssl,
            "verify_ssl": self.verify_ssl,
        }

    def get_auth_context(self) -> dict[str, object]:
        """Get Oracle OIC authentication configuration context (without secrets)."""
        return {
            "client_id": self.oauth_client_id,
            "token_url": self.oauth_token_url,
            "audience": self.oauth_client_aud,
            "scope": self.oauth_scope,
            "has_secret": self.oauth_client_secret is not None,
        }

    def get_features_context(self) -> dict[str, object]:
        """Get Oracle OIC feature configuration context."""
        return {
            "monitoring": self.enable_monitoring,
            "enterprise_patterns": self.enable_enterprise_patterns,
            "orchestration": self.enable_orchestration,
        }

    @classmethod
    def create_for_environment(
        cls, environment: str, **overrides: object
    ) -> FlextOracleOicExtConfig:
        """Create configuration for specific environment using enhanced singleton pattern."""
        return cls.get_or_create_shared_instance(
            project_name="flext-oracle-oic-ext", environment=environment, **overrides
        )

    @classmethod
    def create_default(cls) -> FlextOracleOicExtConfig:
        """Create default configuration instance using enhanced singleton pattern."""
        return cls.get_or_create_shared_instance(project_name="flext-oracle-oic-ext")

    @classmethod
    def create_for_development(cls) -> FlextOracleOicExtConfig:
        """Create configuration optimized for development using enhanced singleton pattern."""
        return cls.get_or_create_shared_instance(
            project_name="flext-oracle-oic-ext",
            request_timeout=10,
            max_retries=1,
            verify_ssl=False,
            enable_monitoring=True,
        )

    @classmethod
    def create_for_production(cls) -> FlextOracleOicExtConfig:
        """Create configuration optimized for production using enhanced singleton pattern."""
        return cls.get_or_create_shared_instance(
            project_name="flext-oracle-oic-ext",
            request_timeout=60,
            max_retries=5,
            verify_ssl=True,
            enable_monitoring=True,
            enable_enterprise_patterns=True,
            enable_orchestration=True,
        )

    @classmethod
    def create_for_testing(cls) -> FlextOracleOicExtConfig:
        """Create configuration optimized for testing using enhanced singleton pattern."""
        return cls.get_or_create_shared_instance(
            project_name="flext-oracle-oic-ext",
            base_url="https://test.example.com",
            oauth_client_id="test_client",
            oauth_client_secret=SecretStr("test_secret"),
            request_timeout=5,
            max_retries=1,
            verify_ssl=False,
            enable_monitoring=False,
        )

    @classmethod
    def get_global_instance(cls) -> FlextOracleOicExtConfig:
        """Get the global singleton instance using enhanced FlextConfig pattern."""
        return cls.get_or_create_shared_instance(project_name="flext-oracle-oic-ext")

    @classmethod
    def reset_global_instance(cls) -> None:
        """Reset the global FlextOracleOicExtConfig instance (mainly for testing)."""
        # Use the enhanced FlextConfig reset mechanism
        cls.reset_shared_instance()


__all__ = [
    "FlextOracleOicExtConfig",
]
