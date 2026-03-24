"""Oracle OIC Extension Configuration - Unified Class Pattern.

FLEXT Unified Class Pattern: Single OracleOicExtensionConfig class
with nested configuration classes following FLEXT architectural standards.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated, ClassVar, Literal

from flext_core import FlextSettings
from pydantic import Field, SecretStr
from pydantic_settings import SettingsConfigDict

from flext_oracle_oic.typings import t


class FlextOracleOicSettings(FlextSettings):
    """Runtime configuration for Oracle OIC integration."""

    type OICApiVersionLiteral = Literal["v1", "v2"]

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(extra="ignore")

    base_url: Annotated[t.NonEmptyStr, Field(default="https://localhost")]
    api_version: Annotated[OICApiVersionLiteral, Field(default="v1")]
    request_timeout: Annotated[t.PositiveInt, Field(default=30)]
    max_retries: Annotated[t.RetryCount, Field(default=3)]
    verify_ssl: Annotated[bool, Field(default=True)]
    use_ssl: Annotated[bool, Field(default=True)]
    enable_monitoring: Annotated[bool, Field(default=True)]
    enable_enterprise_patterns: Annotated[bool, Field(default=True)]
    enable_orchestration: Annotated[bool, Field(default=True)]
    oauth_client_id: Annotated[str, Field(default="")]
    oauth_client_secret: Annotated[SecretStr, Field(default=SecretStr(""))]
    oauth_token_url: Annotated[
        t.NonEmptyStr,
        Field(default="https://localhost/oauth/token"),
    ]
    oauth_client_aud: Annotated[str, Field(default="")]
    oauth_scope: Annotated[str, Field(default="")]

    @classmethod
    def create_for_development(cls) -> FlextOracleOicSettings:
        """Build deterministic development settings."""
        return cls.model_validate({
            "base_url": "https://localhost",
            "api_version": "v1",
        })


__all__ = ["FlextOracleOicSettings"]
