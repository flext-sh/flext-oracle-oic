"""Oracle OIC Extension Configuration - Unified Class Pattern.

FLEXT Unified Class Pattern: Single OracleOICExtensionConfig class
with nested configuration classes following FLEXT architectural standards.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Literal

from pydantic import Field, model_validator

from flext_core import FlextConfig, FlextTypes
from flext_oracle_oic_ext.constants import FlextOracleOicExtConstants

# Type definitions outside class to avoid Pydantic field errors
EnvironmentLiteral = Literal["development", "staging", "production"]
LogLevelLiteral = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
OICApiVersionLiteral = Literal["v1", "v2"]


class OracleOICExtensionConfig(FlextConfig):
    """Unified Oracle OIC Extension configuration following FLEXT patterns.

    Single responsibility class with nested configuration helpers
    following the unified class pattern from FLEXT architectural standards.
    """

    class ConnectionConfig(FlextConfig):
        """Oracle OIC Extension connection configuration.

        EXTENSION Pattern: Oracle OIC connection configuration with
        enterprise validation and best practices.
        """

        base_url: str = FlextOracleOicExtConstants.OIC.DEFAULT_BASE_URL
        api_version: str = FlextOracleOicExtConstants.OIC.DEFAULT_API_VERSION
        request_timeout: int = FlextOracleOicExtConstants.OIC.DEFAULT_REQUEST_TIMEOUT
        max_retries: int = FlextOracleOicExtConstants.OIC.DEFAULT_MAX_RETRIES
        use_ssl: bool = FlextOracleOicExtConstants.OIC.DEFAULT_USE_SSL
        verify_ssl: bool = FlextOracleOicExtConstants.OIC.DEFAULT_VERIFY_SSL

    class AuthConfig(FlextConfig):
        """Oracle OIC Extension OAuth2 authentication configuration.

        EXTENSION Pattern: IDCS OAuth2 authentication configuration
        with enterprise security.
        """

        oauth_client_id: str = FlextOracleOicExtConstants.Auth.DEFAULT_OAUTH_CLIENT_ID
        oauth_client_secret: str = (
            FlextOracleOicExtConstants.Auth.DEFAULT_OAUTH_CLIENT_SECRET
        )
        oauth_token_url: str = FlextOracleOicExtConstants.Auth.DEFAULT_OAUTH_TOKEN_URL
        oauth_client_aud: str | None = (
            FlextOracleOicExtConstants.Auth.DEFAULT_OAUTH_CLIENT_AUD
        )
        oauth_scope: str = FlextOracleOicExtConstants.Auth.DEFAULT_OAUTH_SCOPE

    class Settings(FlextConfig):
        """Oracle OIC Extension main settings.

        Padrão EXTENSION: Configuração principal da extension Oracle OIC
        consolidando todas as configurações necessárias.
        """

        # Use forward references for nested types
        connection: OracleOICExtensionConfig.ConnectionConfig | None = Field(
            default=None
        )
        auth: OracleOICExtensionConfig.AuthConfig | None = Field(default=None)

        @model_validator(mode="after")
        def _validate_settings(self: object) -> OracleOICExtensionConfig.Settings:
            """Validate configuration settings after initialization.

            With proper default factories, type safety is guaranteed by Pydantic.
            This validator can be used for additional business logic validation.
            """
            # Additional validation can be added here if needed
            # Type safety is already guaranteed by proper default factories
            return self

        # Use base types from FlextConfig to avoid type conflicts
        enable_monitoring: bool = True
        enable_enterprise_patterns: bool = True
        enable_orchestration: bool = True

    # Main configuration settings (for backward compatibility)
    enable_monitoring: bool = True
    enable_enterprise_patterns: bool = True
    enable_orchestration: bool = True


# Backward compatibility aliases
OICExtensionConnectionConfig = OracleOICExtensionConfig.ConnectionConfig
OICExtensionAuthConfig = OracleOICExtensionConfig.AuthConfig
OracleOICExtensionSettings = OracleOICExtensionConfig.Settings
# EnvironmentLiteral, LogLevelLiteral, OICApiVersionLiteral are defined at module level


# Exports following EXTENSION pattern
__all__: FlextTypes.Core.StringList = [
    "EnvironmentLiteral",
    "LogLevelLiteral",
    "OICApiVersionLiteral",
    "OICExtensionAuthConfig",
    "OICExtensionConnectionConfig",
    "OracleOICExtensionConfig",
    "OracleOICExtensionSettings",
]
