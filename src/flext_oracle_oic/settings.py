"""Oracle OIC Extension Settings - Unified Class Pattern.

FLEXT Unified Class Pattern: Single OracleOicExtensionConfig class
with nested configuration classes following FLEXT architectural standards.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated, ClassVar, Self

from flext_core import FlextSettings

from flext_oracle_oic import c, m, t, u


@FlextSettings.auto_register("oracle-oic")
class FlextOracleOicSettings(FlextSettings):
    """Runtime configuration for Oracle OIC integration."""

    OICApiVersion: ClassVar[type[c.OracleOic.OICApiVersion]] = c.OracleOic.OICApiVersion

    model_config: ClassVar[m.SettingsConfigDict] = m.SettingsConfigDict(
        env_prefix="FLEXT_ORACLE_OIC_", extra="ignore"
    )

    base_url: Annotated[t.NonEmptyStr, u.Field(default=c.OracleOic.DEFAULT_BASE_URL)]
    api_version: Annotated[
        c.OracleOic.OICApiVersion, u.Field(default=c.OracleOic.OICApiVersion.V1)
    ]
    request_timeout: Annotated[
        t.PositiveInt, u.Field(default=c.DEFAULT_TIMEOUT_SECONDS)
    ]
    max_retries: Annotated[t.RetryCount, u.Field(default=c.MAX_RETRY_ATTEMPTS)]
    verify_ssl: Annotated[bool, u.Field(default=True)]
    use_ssl: Annotated[bool, u.Field(default=True)]
    enable_monitoring: Annotated[bool, u.Field(default=True)]
    enable_enterprise_patterns: Annotated[bool, u.Field(default=True)]
    enable_orchestration: Annotated[bool, u.Field(default=True)]
    oauth_client_id: Annotated[str, u.Field(default="")]
    oauth_client_secret: Annotated[t.SecretStr, u.Field(default=t.SecretStr(""))]
    oauth_token_url: Annotated[
        t.NonEmptyStr,
        u.Field(default=f"{c.OracleOic.DEFAULT_BASE_URL}/oauth/token"),
    ]
    oauth_client_aud: Annotated[str, u.Field(default="")]
    oauth_scope: Annotated[str, u.Field(default="")]

    @classmethod
    def create_for_development(cls) -> Self:
        """Build deterministic development settings."""
        return cls.model_validate({
            "base_url": c.OracleOic.DEFAULT_BASE_URL,
            "api_version": c.OracleOic.OICApiVersion.V1.value,
        })


__all__: list[str] = ["FlextOracleOicSettings"]
