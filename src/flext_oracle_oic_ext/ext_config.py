"""Oracle OIC Extension Configuration Classes.

Legacy configuration classes for backward compatibility.
These classes provide the expected API for existing tests and integrations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import Field, SecretStr
from pydantic_settings import SettingsConfigDict

from flext_core import FlextConfig
from flext_oracle_oic_ext.models import FlextOracleOicExtModels


class OICExtensionAuthConfig(FlextOracleOicExtModels.OICAuthConfig):
    """Legacy alias for OICAuthConfig for backward compatibility.

    Provides backward compatibility with default values for required fields.
    """

    oauth_client_id: str = Field(
        default="default_client_id", description="IDCS OAuth2 client ID"
    )
    oauth_client_secret: SecretStr = Field(
        default_factory=lambda: SecretStr("default_secret"),
        description="IDCS OAuth2 client secret",
    )
    oauth_token_url: str = Field(
        default="https://example.com/oauth2/token",
        description="IDCS OAuth2 token endpoint",
    )
    oauth_client_aud: str | None = Field(None, description="OAuth2 audience")
    oauth_scope: str = Field("", description="OAuth2 scope")


class OICExtensionConnectionConfig(FlextOracleOicExtModels.OICConnectionConfig):
    """Legacy alias for OICConnectionConfig for backward compatibility.

    Provides backward compatibility with default values for required fields.
    """

    base_url: str = Field(
        default="https://example.com", description="Oracle OIC instance base URL"
    )


class OracleOICExtensionSettings(FlextConfig):
    """Oracle OIC Extension settings with nested connection and auth configs.

    This class provides the expected API for existing tests and integrations.
    """

    model_config = SettingsConfigDict(extra="forbid")

    # Nested configurations
    connection: OICExtensionConnectionConfig = Field(
        default_factory=OICExtensionConnectionConfig,
        description="Oracle OIC connection configuration",
    )

    auth: OICExtensionAuthConfig = Field(
        default_factory=OICExtensionAuthConfig,
        description="Oracle OIC authentication configuration",
    )

    # Feature flags
    enable_monitoring: bool = Field(
        default=True, description="Enable monitoring features"
    )

    enable_enterprise_patterns: bool = Field(
        default=True, description="Enable enterprise patterns"
    )

    enable_orchestration: bool = Field(
        default=True, description="Enable orchestration features"
    )
