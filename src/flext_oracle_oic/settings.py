"""Oracle OIC Extension Configuration - Unified Class Pattern.

FLEXT Unified Class Pattern: Single OracleOicExtensionConfig class
with nested configuration classes following FLEXT architectural standards.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated, ClassVar, Self

from pydantic import Field, SecretStr
from pydantic_settings import SettingsConfigDict

from flext_core import FlextSettings
from flext_oracle_oic import c, t


@FlextSettings.auto_register("oracle-oic")
class FlextOracleOicSettings(FlextSettings):
    """Runtime configuration for Oracle OIC integration."""

    OICApiVersion: ClassVar[type[c.OICApiVersion]] = c.OICApiVersion

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_prefix="FLEXT_ORACLE_OIC_",
        extra="ignore",
    )

    base_url: Annotated[t.NonEmptyStr, Field(default=c.OracleOic.DEFAULT_BASE_URL)]
    api_version: Annotated[c.OICApiVersion, Field(default=c.OICApiVersion.V1)]
    request_timeout: Annotated[t.PositiveInt, Field(default=c.DEFAULT_TIMEOUT_SECONDS)]
    max_retries: Annotated[t.RetryCount, Field(default=c.MAX_RETRY_ATTEMPTS)]
    verify_ssl: Annotated[bool, Field(default=True)]
    use_ssl: Annotated[bool, Field(default=True)]
    enable_monitoring: Annotated[bool, Field(default=True)]
    enable_enterprise_patterns: Annotated[bool, Field(default=True)]
    enable_orchestration: Annotated[bool, Field(default=True)]
    oauth_client_id: Annotated[str, Field(default="")]
    oauth_client_secret: Annotated[SecretStr, Field(default=SecretStr(""))]
    oauth_token_url: Annotated[
        t.NonEmptyStr,
        Field(default=f"{c.OracleOic.DEFAULT_BASE_URL}/oauth/token"),
    ]
    oauth_client_aud: Annotated[str, Field(default="")]
    oauth_scope: Annotated[str, Field(default="")]

    @classmethod
    def create_for_development(cls) -> Self:
        """Build deterministic development settings."""
        return cls.model_validate({
            "base_url": c.OracleOic.DEFAULT_BASE_URL,
            "api_version": c.OICApiVersion.V1.value,
        })


__all__ = ["FlextOracleOicSettings"]
