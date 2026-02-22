"""Oracle OIC Extension Configuration - Unified Class Pattern.

FLEXT Unified Class Pattern: Single OracleOicExtensionConfig class
with nested configuration classes following FLEXT architectural standards.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal, Self

from flext_core import FlextResult, FlextSettings
from pydantic import Field, SecretStr, model_validator
from pydantic_settings import SettingsConfigDict

from flext_oracle_oic.constants import FlextOracleOicConstants
from flext_oracle_oic.utilities import FlextOracleOicUtilities

# Type definitions outside class to avoid Pydantic field errors
EnvironmentLiteral = Literal["development", "staging", "production"]
LogLevelLiteral = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
OICApiVersionLiteral = Literal["v1", "v2"]


class FlextOracleOicSettings(FlextSettings):
    """Single Pydantic 2 Settings class for flext-oracle-oic extending FlextSettings.

    Follows standardized pattern:
    - Extends FlextSettings from flext-core
    - No nested classes within Config
    - All defaults from FlextOracleOicConstants
    - Uses enhanced singleton pattern with inverse dependency injection
    - Uses Pydantic 2.11+ features (field_validator, model_validator)
    """

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_ORACLE_OIC_EXT_",
        case_sensitive=False,
        extra="allow",
        # Inherit enhanced Pydantic 2.11+ features from FlextSettings
        validate_assignment=True,
        str_strip_whitespace=True,
        json_schema_extra={
            "title": "FLEXT Oracle OIC Extension Configuration",
            "description": "Oracle OIC Extension configuration extending FlextSettings",
        },
    )

    # Oracle OIC Connection Configuration using FlextOracleOicConstants for defaults
    base_url: str = Field(
        default=FlextOracleOicConstants.OracleOic.DEFAULT_BASE_URL,
        description="Oracle OIC base URL",
    )

    api_version: str = Field(
        default=FlextOracleOicConstants.OracleOic.DEFAULT_API_VERSION,
        description="Oracle OIC API version",
    )

    request_timeout: int = Field(
        default=FlextOracleOicConstants.OracleOic.DEFAULT_REQUEST_TIMEOUT,
        description="Request timeout in seconds",
        ge=1,
        le=300,
    )

    max_retries: int = Field(
        default=FlextOracleOicConstants.OracleOic.DEFAULT_MAX_RETRIES,
        description="Maximum number of retry attempts",
        ge=0,
        le=10,
    )

    use_ssl: bool = Field(
        default=FlextOracleOicConstants.OracleOic.DEFAULT_USE_SSL,
        description="Use SSL for connections",
    )

    verify_ssl: bool = Field(
        default=FlextOracleOicConstants.OracleOic.DEFAULT_VERIFY_SSL,
        description="Verify SSL certificates",
    )

    # Oracle OIC Authentication Configuration using FlextOracleOicConstants for defaults
    oauth_client_id: str = Field(
        default=FlextOracleOicConstants.Auth.DEFAULT_OAUTH_CLIENT_ID,
        description="OAuth2 client ID",
    )

    oauth_client_secret: SecretStr = Field(
        default_factory=lambda: SecretStr(
            FlextOracleOicConstants.Auth.DEFAULT_OAUTH_CLIENT_SECRET,
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
        default=True,
        description="Enable monitoring features",
    )

    enable_enterprise_patterns: bool = Field(
        default=True,
        description="Enable enterprise patterns",
    )

    enable_orchestration: bool = Field(
        default=True,
        description="Enable orchestration features",
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

    @model_validator(mode="after")
    def validate_oracle_oic_configuration_consistency(self) -> Self:
        """Validate Oracle OIC configuration consistency."""
        # Validate OAuth configuration
        if self.oauth_client_id:
            # Validate client ID format
            client_id_result = FlextOracleOicUtilities.AuthenticationValidation.validate_oauth_client_id(
                self.oauth_client_id,
            )
            if client_id_result.is_failure:
                error_msg = f"OAuth client ID validation: {client_id_result.error}"
                raise ValueError(error_msg)

        if self.oauth_client_id and not self.oauth_client_secret:
            error_msg = "OAuth client secret is required when client ID is provided"
            raise ValueError(error_msg)

        return self

    def validate_business_rules(self) -> FlextResult[bool]:
        """Validate Oracle OIC Extension specific business rules."""
        # Railway-oriented business rule validation - operations are safe
        return (
            FlextResult[object]
            .ok(None)
            .flat_map(lambda _: self._validate_oauth_credentials())
            .flat_map(lambda _: self._validate_connection_settings())
            .flat_map(lambda _: self._validate_retry_settings())
        )

    def _validate_oauth_credentials(self) -> FlextResult[bool]:
        """Validate OAuth credentials are present."""
        if not self.oauth_client_id or not self.oauth_client_secret.get_secret_value():
            return FlextResult[bool].fail("OAuth credentials are required")
        return FlextResult[bool].ok(value=True)

    def _validate_connection_settings(self) -> FlextResult[bool]:
        """Validate connection settings are within acceptable ranges."""
        if self.request_timeout < FlextOracleOicConstants.OracleOic.MIN_REQUEST_TIMEOUT:
            return FlextResult[bool].fail(
                f"Request timeout too low (minimum {FlextOracleOicConstants.OracleOic.MIN_REQUEST_TIMEOUT} seconds)",
            )
        return FlextResult[bool].ok(value=True)

    def _validate_retry_settings(self) -> FlextResult[bool]:
        """Validate retry settings are within acceptable ranges."""
        if self.max_retries > FlextOracleOicConstants.OracleOic.MAX_MAX_RETRIES:
            return FlextResult[bool].fail(
                f"Max retries too high (maximum {FlextOracleOicConstants.OracleOic.MAX_MAX_RETRIES})",
            )
        return FlextResult[bool].ok(value=True)

    @classmethod
    def create_for_environment(
        cls,
        environment: str,
        overrides: dict[str, str | int | float | bool | bytes | bytearray | None]
        | None = None,
    ) -> FlextOracleOicSettings:
        """Create configuration for specific environment using enhanced singleton pattern."""
        # Environment parameter reserved for future use - validate it's not empty
        if not environment.strip():
            msg = "Environment name cannot be empty"
            raise ValueError(msg)
        base = cls()
        if overrides:
            return base.model_copy(update=overrides)
        return base

    @classmethod
    def create_default(cls) -> FlextOracleOicSettings:
        """Create default configuration instance using enhanced singleton pattern."""
        return cls()

    @classmethod
    def create_for_development(cls) -> FlextOracleOicSettings:
        """Create configuration optimized for development using enhanced singleton pattern."""
        return cls(
            request_timeout=10,
            max_retries=1,
            verify_ssl=False,
            enable_monitoring=True,
        )

    @classmethod
    def create_for_production(cls) -> FlextOracleOicSettings:
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
    def create_for_testing(cls) -> FlextOracleOicSettings:
        """Create configuration optimized for testing using enhanced singleton pattern."""
        return cls(
            base_url="https://test.example.com",
            oauth_client_id="test_client",
            request_timeout=5,
            max_retries=1,
            verify_ssl=False,
            enable_monitoring=False,
        )

    @classmethod
    def get_global_instance(cls) -> FlextOracleOicSettings:
        """Get the global singleton instance using enhanced FlextSettings pattern."""
        return cls()

    # Note: FlextOracleOicSettings follows direct instantiation pattern
    # No global instance methods needed - use FlextOracleOicSettings() directly


__all__ = [
    "FlextOracleOicSettings",
]
