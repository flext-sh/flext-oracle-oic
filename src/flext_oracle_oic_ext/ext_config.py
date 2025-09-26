"""Oracle OIC Extension Configuration - Unified Class Pattern.

FLEXT Unified Class Pattern: Single OracleOICExtensionConfig class
with nested configuration classes following FLEXT architectural standards.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import threading
from typing import ClassVar, Literal

from pydantic import Field, SecretStr, field_validator, model_validator

from flext_core import FlextConfig, FlextTypes
from flext_oracle_oic_ext.constants import FlextOracleOicExtConstants

# Type definitions outside class to avoid Pydantic field errors
EnvironmentLiteral = Literal["development", "staging", "production"]
LogLevelLiteral = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
OICApiVersionLiteral = Literal["v1", "v2"]


class FlextOracleOicExtConfig(FlextConfig):
    """Single flat Pydantic 2 Settings class for flext-oracle-oic-ext extending FlextConfig.

    Follows standardized pattern:
    - Extends FlextConfig from flext-core
    - Flat class structure (no nested classes)
    - All defaults from FlextOracleOicExtConstants
    - SecretStr for sensitive data
    - Singleton pattern with shared dependency injection
    """

    # Singleton pattern override
    _global_instance: ClassVar[FlextOracleOicExtConfig | None] = None
    _lock: ClassVar[threading.Lock] = threading.Lock()

    # Connection Configuration (flattened from ConnectionConfig)
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

    # Authentication Configuration (flattened from AuthConfig)
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

    # General Settings (flattened from Settings)
    enable_monitoring: bool = Field(
        default=True, description="Enable monitoring features"
    )

    enable_enterprise_patterns: bool = Field(
        default=True, description="Enable enterprise patterns"
    )

    enable_orchestration: bool = Field(
        default=True, description="Enable orchestration features"
    )

    # Field validators
    @field_validator("base_url")
    @classmethod
    def validate_base_url(cls, v: str) -> str:
        """Validate base URL format."""
        if not v.startswith(("http://", "https://")):
            msg = f"Invalid base URL format: {v}. Must start with http:// or https://"
            raise ValueError(msg)
        return v.rstrip("/")

    @field_validator("oauth_token_url")
    @classmethod
    def validate_oauth_token_url(cls, v: str) -> str:
        """Validate OAuth token URL format."""
        if not v.startswith(("http://", "https://")):
            msg = f"Invalid OAuth token URL format: {v}. Must start with http:// or https://"
            raise ValueError(msg)
        return v

    @model_validator(mode="after")
    def validate_oauth_config(self) -> FlextOracleOicExtConfig:
        """Validate OAuth configuration consistency."""
        if self.oauth_client_id and not self.oauth_client_secret:
            msg = "OAuth client secret is required when client ID is provided"
            raise ValueError(msg)
        return self

    # Configuration context methods
    def get_connection_context(self) -> dict[str, object]:
        """Get connection configuration context."""
        return {
            "base_url": self.base_url,
            "api_version": self.api_version,
            "timeout": self.request_timeout,
            "max_retries": self.max_retries,
            "use_ssl": self.use_ssl,
            "verify_ssl": self.verify_ssl,
        }

    def get_auth_context(self) -> dict[str, object]:
        """Get authentication configuration context (without secrets)."""
        return {
            "client_id": self.oauth_client_id,
            "token_url": self.oauth_token_url,
            "audience": self.oauth_client_aud,
            "scope": self.oauth_scope,
            "has_secret": self.oauth_client_secret is not None,
        }

    def get_features_context(self) -> dict[str, object]:
        """Get feature configuration context."""
        return {
            "monitoring": self.enable_monitoring,
            "enterprise_patterns": self.enable_enterprise_patterns,
            "orchestration": self.enable_orchestration,
        }

    # Backward compatibility methods
    @property
    def connection(self) -> dict[str, object]:
        """Backward compatibility: return connection config as dict."""
        return self.get_connection_context()

    @property
    def auth(self) -> dict[str, object]:
        """Backward compatibility: return auth config as dict."""
        return self.get_auth_context()

    # Singleton pattern override for proper typing
    @classmethod
    def get_global_instance(cls) -> FlextOracleOicExtConfig:
        """Get the global singleton instance of FlextOracleOicExtConfig."""
        if cls._global_instance is None:
            with cls._lock:
                if cls._global_instance is None:
                    cls._global_instance = cls()
        return cls._global_instance

    @classmethod
    def reset_global_instance(cls) -> None:
        """Reset the global instance (mainly for testing)."""
        cls._global_instance = None


# Backward compatibility aliases
OracleOICExtensionConfig = (
    FlextOracleOicExtConfig  # Old name for backward compatibility
)
OracleOICExtensionSettings = (
    FlextOracleOicExtConfig  # Settings alias now points to main config
)
OICExtensionConnectionConfig = (
    FlextOracleOicExtConfig  # Connection config is now part of main config
)
OICExtensionAuthConfig = (
    FlextOracleOicExtConfig  # Auth config is now part of main config
)

# EnvironmentLiteral, LogLevelLiteral, OICApiVersionLiteral are defined at module level


# Exports following FLEXT standardized pattern
__all__: FlextTypes.Core.StringList = [
    "EnvironmentLiteral",
    "FlextOracleOicExtConfig",  # Primary standardized config
    "LogLevelLiteral",
    "OICApiVersionLiteral",
    "OICExtensionAuthConfig",  # Backward compatibility
    "OICExtensionConnectionConfig",  # Backward compatibility
    "OracleOICExtensionConfig",  # Backward compatibility
    "OracleOICExtensionSettings",  # Backward compatibility
]
