"""Oracle OIC Extension Configuration - Unified Class Pattern.

FLEXT Unified Class Pattern: Single OracleOicExtensionConfig class
with nested configuration classes following FLEXT architectural standards.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Literal, Self

from flext_core import FlextCore
from pydantic import Field, SecretStr, field_validator, model_validator
from pydantic_settings import SettingsConfigDict

from flext_oracle_oic.constants import FlextOracleOicConstants
from flext_oracle_oic.utilities import FlextOracleOicUtilities

# Type definitions outside class to avoid Pydantic field errors
EnvironmentLiteral = Literal["development", "staging", "production"]
LogLevelLiteral = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
OICApiVersionLiteral = Literal["v1", "v2"]


class FlextOracleOicConfig(FlextCore.Config):
    """Single Pydantic 2 Settings class for flext-oracle-oic extending FlextCore.Config.

    Follows standardized pattern:
    - Extends FlextCore.Config from flext-core
    - No nested classes within Config
    - All defaults from FlextOracleOicConstants
    - Uses enhanced singleton pattern with inverse dependency injection
    - Uses Pydantic 2.11+ features (field_validator, model_validator)
    """

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_ORACLE_OIC_EXT_",
        case_sensitive=False,
        extra="allow",
        # Inherit enhanced Pydantic 2.11+ features from FlextCore.Config
        validate_assignment=True,
        str_strip_whitespace=True,
        json_schema_extra={
            "title": "FLEXT Oracle OIC Extension Configuration",
            "description": "Oracle OIC Extension configuration extending FlextCore.Config",
        },
    )

    # Oracle OIC Connection Configuration using FlextOracleOicConstants for defaults
    base_url: str = Field(
        default=FlextOracleOicConstants.OIC.DEFAULT_BASE_URL,
        description="Oracle OIC base URL",
    )

    api_version: str = Field(
        default=FlextOracleOicConstants.OIC.DEFAULT_API_VERSION,
        description="Oracle OIC API version",
    )

    request_timeout: int = Field(
        default=FlextOracleOicConstants.OIC.DEFAULT_REQUEST_TIMEOUT,
        description="Request timeout in seconds",
        ge=1,
        le=300,
    )

    max_retries: int = Field(
        default=FlextOracleOicConstants.OIC.DEFAULT_MAX_RETRIES,
        description="Maximum number of retry attempts",
        ge=0,
        le=10,
    )

    use_ssl: bool = Field(
        default=FlextOracleOicConstants.OIC.DEFAULT_USE_SSL,
        description="Use SSL for connections",
    )

    verify_ssl: bool = Field(
        default=FlextOracleOicConstants.OIC.DEFAULT_VERIFY_SSL,
        description="Verify SSL certificates",
    )

    # Oracle OIC Authentication Configuration using FlextOracleOicConstants for defaults
    oauth_client_id: str = Field(
        default=FlextOracleOicConstants.Auth.DEFAULT_OAUTH_CLIENT_ID,
        description="OAuth2 client ID",
    )

    oauth_client_secret: SecretStr = Field(
        default_factory=lambda: SecretStr(
            FlextOracleOicConstants.Auth.DEFAULT_OAUTH_CLIENT_SECRET
        ),
        description="OAuth2 client secret (sensitive)",
    )

    oauth_token_url: str = Field(
        default=FlextOracleOicConstants.Auth.DEFAULT_OAUTH_TOKEN_URL,
        description="OAuth2 token URL",
    )

    oauth_client_aud: str | None = Field(
        default=FlextOracleOicConstants.Auth.DEFAULT_OAUTH_CLIENT_AUD,
        description="OAuth2 client audience",
    )

    oauth_scope: str = Field(
        default=FlextOracleOicConstants.Auth.DEFAULT_OAUTH_SCOPE,
        description="OAuth2 scope",
    )

    # Feature Configuration using FlextOracleOicConstants for defaults
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
        default="flext-oracle-oic",
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
        """Validate base URL format using FlextOracleOicUtilities."""
        result = FlextOracleOicUtilities.ConnectionValidation.validate_base_url(v)
        if result.is_failure:
            error_msg = result.error
            raise ValueError(error_msg)
        return result.value

    @field_validator("oauth_token_url")
    @classmethod
    def validate_oauth_token_url(cls, v: str) -> str:
        """Validate OAuth token URL format using FlextOracleOicUtilities."""
        result = (
            FlextOracleOicUtilities.AuthenticationValidation.validate_oauth_token_url(v)
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
            client_id_result = FlextOracleOicUtilities.AuthenticationValidation.validate_oauth_client_id(
                self.oauth_client_id
            )
            if client_id_result.is_failure:
                error_msg = f"OAuth client ID validation: {client_id_result.error}"
                raise ValueError(error_msg)

        if self.oauth_client_id and not self.oauth_client_secret:
            error_msg = "OAuth client secret is required when client ID is provided"
            raise ValueError(error_msg)

        return self

    def validate_business_rules(self) -> FlextCore.Result[None]:
        """Validate Oracle OIC Extension specific business rules."""
        # Railway-oriented business rule validation - operations are safe
        return (
            FlextCore.Result[object]
            .ok(None)
            .flat_map(lambda _: self._validate_oauth_credentials())
            .flat_map(lambda _: self._validate_connection_settings())
            .flat_map(lambda _: self._validate_retry_settings())
        )

    def _validate_oauth_credentials(self) -> FlextCore.Result[None]:
        """Validate OAuth credentials are present."""
        if not self.oauth_client_id or not self.oauth_client_secret.get_secret_value():
            return FlextCore.Result[None].fail("OAuth credentials are required")
        return FlextCore.Result[None].ok(None)

    def _validate_connection_settings(self) -> FlextCore.Result[None]:
        """Validate connection settings are within acceptable ranges."""
        if self.request_timeout < FlextOracleOicConstants.OIC.MIN_REQUEST_TIMEOUT:
            return FlextCore.Result[None].fail(
                f"Request timeout too low (minimum {FlextOracleOicConstants.OIC.MIN_REQUEST_TIMEOUT} seconds)"
            )
        return FlextCore.Result[None].ok(None)

    def _validate_retry_settings(self) -> FlextCore.Result[None]:
        """Validate retry settings are within acceptable ranges."""
        if self.max_retries > FlextOracleOicConstants.OIC.MAX_MAX_RETRIES:
            return FlextCore.Result[None].fail(
                f"Max retries too high (maximum {FlextOracleOicConstants.OIC.MAX_MAX_RETRIES})"
            )
        return FlextCore.Result[None].ok(None)

    @classmethod
    def create_for_environment(
        cls, environment: str, **overrides: object
    ) -> FlextOracleOicConfig:
        """Create configuration for specific environment using enhanced singleton pattern."""
        return cls(**overrides)

    @classmethod
    def create_default(cls) -> FlextOracleOicConfig:
        """Create default configuration instance using enhanced singleton pattern."""
        return cls()

    @classmethod
    def create_for_development(cls) -> FlextOracleOicConfig:
        """Create configuration optimized for development using enhanced singleton pattern."""
        return cls(
            request_timeout=10,
            max_retries=1,
            verify_ssl=False,
            enable_monitoring=True,
        )

    @classmethod
    def create_for_production(cls) -> FlextOracleOicConfig:
        """Create configuration optimized for production using enhanced singleton pattern."""
        return cls(
            request_timeout=60,
            max_retries=5,
            verify_ssl=True,
            enable_monitoring=True,
            enable_enterprise_patterns=True,
            enable_orchestration=True,
        )

    @classmethod
    def create_for_testing(cls) -> FlextOracleOicConfig:
        """Create configuration optimized for testing using enhanced singleton pattern."""
        return cls(
            base_url="https://test.example.com",
            oauth_client_id="test_client",
            oauth_client_secret=SecretStr("test_secret"),
            request_timeout=5,
            max_retries=1,
            verify_ssl=False,
            enable_monitoring=False,
        )

    @classmethod
    def get_global_instance(cls) -> FlextOracleOicConfig:
        """Get the global singleton instance using enhanced FlextCore.Config pattern."""
        return cls()

    # Note: FlextOracleOicConfig follows direct instantiation pattern
    # No global instance methods needed - use FlextOracleOicConfig() directly


__all__ = [
    "FlextOracleOicConfig",
]
