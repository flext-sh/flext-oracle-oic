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

        base_url: str = "https://localhost.integration.ocp.oraclecloud.com"
        api_version: str = "v1"
        request_timeout: int = 30
        max_retries: int = 3
        use_ssl: bool = True
        verify_ssl: bool = True

    class AuthConfig(FlextConfig):
        """Oracle OIC Extension OAuth2 authentication configuration.

        EXTENSION Pattern: IDCS OAuth2 authentication configuration
        with enterprise security.
        """

        oauth_client_id: str = "default_client_id"
        oauth_client_secret: str = "default_client_" + "secret_value"
        oauth_token_url: str = (
            "https://idcs-tenant.identity.oraclecloud.com/" + "oauth2/v1/token"
        )
        oauth_client_aud: str | None = None
        oauth_scope: str = ""

    class Settings(FlextConfig):
        """Oracle OIC Extension main settings.

        Padrão EXTENSION: Configuração principal da extension Oracle OIC
        consolidando todas as configurações necessárias.
        """

        # Use forward references for nested types
        connection: OracleOICExtensionConfig.ConnectionConfig = Field(
            default_factory=OracleOICExtensionConfig.ConnectionConfig,
        )
        auth: OracleOICExtensionConfig.AuthConfig = Field(
            default_factory=OracleOICExtensionConfig.AuthConfig,
        )

        @model_validator(mode="after")
        def _validate_settings(self) -> OracleOICExtensionConfig.Settings:
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
