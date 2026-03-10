"""Oracle OIC Extension Configuration - Unified Class Pattern.

FLEXT Unified Class Pattern: Single OracleOicExtensionConfig class
with nested configuration classes following FLEXT architectural standards.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextSettings
from pydantic import ConfigDict, Field, SecretStr

EnvironmentLiteral = Literal["development", "staging", "production"]
LogLevelLiteral = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
OICApiVersionLiteral = Literal["v1", "v2"]


class FlextOracleOicSettings(FlextSettings):
    """Runtime configuration for Oracle OIC integration."""

    model_config = ConfigDict(extra="ignore")

    base_url: str = Field(default="https://localhost")
    api_version: OICApiVersionLiteral = Field(default="v1")
    request_timeout: int = Field(default=30, ge=1, le=300)
    verify_ssl: bool = Field(default=True)
    use_ssl: bool = Field(default=True)
    enable_monitoring: bool = Field(default=True)
    oauth_client_id: str = Field(default="")
    oauth_client_secret: SecretStr = Field(default=SecretStr(""))
    oauth_token_url: str = Field(default="https://localhost/oauth/token")
    oauth_client_aud: str = Field(default="")
    oauth_scope: str = Field(default="")

    @classmethod
    def create_for_development(cls) -> FlextOracleOicSettings:
        """Build deterministic development settings."""
        return cls(base_url="https://localhost", api_version="v1")


__all__ = ["FlextOracleOicSettings"]
