"""Oracle OIC Extension Configuration - EXTENSION Pattern.

This module establishes the EXTENSION PEP8 pattern for Oracle OIC extension
configuration. Serves as a template for future extensions.
"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextSettings

# Type definitions seguindo padrão EXTENSION
EnvironmentLiteral = Literal["development", "staging", "production"]
LogLevelLiteral = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
OICApiVersionLiteral = Literal["v1", "v2"]


class OICExtensionConnectionConfig(FlextSettings):
    """Oracle OIC Extension connection configuration.

    EXTENSION Pattern: Oracle OIC connection configuration with
    enterprise validation and best practices.
    """

    base_url: str = "https://localhost.integration.ocp.oraclecloud.com"
    api_version: OICApiVersionLiteral = "v1"
    request_timeout: int = 30
    max_retries: int = 3
    use_ssl: bool = True
    verify_ssl: bool = True


class OICExtensionAuthConfig(FlextSettings):
    """Oracle OIC Extension OAuth2 authentication configuration.

    Padrão EXTENSION: Configuração de autenticação IDCS OAuth2
    com segurança enterprise.
    """

    oauth_client_id: str = "default_client_id"
    oauth_client_secret: str = "default_client_" + "secret_value"
    oauth_token_url: str = (
        "https://idcs-tenant.identity.oraclecloud.com/" + "oauth2/v1/token"
    )
    oauth_client_aud: str | None = None
    oauth_scope: str = ""


class OracleOICExtensionSettings(FlextSettings):
    """Oracle OIC Extension main settings.

    Padrão EXTENSION: Configuração principal da extension Oracle OIC
    consolidando todas as configurações necessárias.
    """

    environment: EnvironmentLiteral = "development"
    log_level: LogLevelLiteral = "INFO"
    enable_monitoring: bool = True
    enable_enterprise_patterns: bool = True
    enable_orchestration: bool = True

    # Sub-configurations
    connection: OICExtensionConnectionConfig = OICExtensionConnectionConfig()
    auth: OICExtensionAuthConfig = OICExtensionAuthConfig()


# Exports seguindo padrão EXTENSION
__all__: list[str] = [
    # Type literals
    "EnvironmentLiteral",
    "LogLevelLiteral",
    "OICApiVersionLiteral",
    "OICExtensionAuthConfig",
    # Configuration classes
    "OICExtensionConnectionConfig",
    "OracleOICExtensionSettings",
]
