"""Settings for flext-oracle-oic — namespaced under ``settings.OracleOic``.

Layer-0: imports only stdlib + pydantic + ``FlextSettings``. The universal
runtime fields (``debug``/``trace``/``log_level``/``timezone``/``async_logging``)
come from ``FlextSettings`` by MRO and are NOT redeclared here. Every project
field lives inside the ``OracleOic`` namespace group with simple scalar types so
each is settable via ``.env`` / env vars / params
(``FLEXT_ORACLE_OIC_ORACLEOIC__BASE_URL`` …). Connection/auth defaults are
inlined from ``flext_oracle_oic._constants`` (SSOT); OAuth credentials are
env-provided plain ``str`` (empty default) per the strict pattern. Range/enum
validation lives at the domain-model boundary
(``m.OracleOic.OICConnectionConfig`` / ``OICAuthConfig``), not here.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated

from flext_core import FlextSettings
from flext_oracle_oic import c, m


class FlextOracleOicSettings(FlextSettings):
    """Oracle OIC settings; all project fields under ``settings.OracleOic.*``."""

    model_config = m.SettingsConfigDict(
        env_prefix="FLEXT_ORACLE_OIC_",
        env_nested_delimiter="__",
        extra="ignore",
    )

    class OracleOicSettings(m.BaseModel):
        """Namespaced Oracle OIC connection + OAuth + feature-flag scalars.

        Defaults live on the assignment side (checker-visible optional
        constructor parameters).
        """

        base_url: Annotated[
            str,
            m.Field(description="Oracle OIC instance base URL"),
        ] = "https://localhost.integration.ocp.oraclecloud.com"
        api_version: Annotated[str, m.Field(description="OIC REST API version")] = "v1"
        request_timeout: Annotated[
            int,
            m.Field(description="Request timeout in seconds"),
        ] = 30
        max_retries: Annotated[int, m.Field(description="Maximum retry attempts")] = 3
        verify_ssl: Annotated[bool, m.Field(description="Verify TLS certificates")] = (
            True
        )
        use_ssl: Annotated[bool, m.Field(description="Use TLS transport")] = True
        enable_monitoring: Annotated[
            bool,
            m.Field(description="Enable monitoring client"),
        ] = True
        enable_enterprise_patterns: Annotated[
            bool,
            m.Field(description="Enable enterprise patterns"),
        ] = True
        enable_orchestration: Annotated[
            bool,
            m.Field(description="Enable orchestration operations"),
        ] = True
        oauth_client_id: Annotated[
            str,
            m.Field(description="IDCS OAuth2 client ID"),
        ] = ""
        oauth_client_secret: Annotated[
            str,
            m.Field(description="IDCS OAuth2 client secret"),
        ] = ""
        # NOTE: a public OAuth endpoint URL is configuration, not a secret;
        # the default is inlined from the constants SSOT (``c.OracleOic``),
        # matching the flext-auth layer-0 settings pattern for non-secret
        # URL defaults.
        oauth_token_url: Annotated[
            str,
            m.Field(description="IDCS OAuth2 token endpoint URL"),
        ] = c.OracleOic.DEFAULT_TOKEN_URL
        oauth_client_aud: Annotated[str, m.Field(description="OAuth2 audience")] = ""
        oauth_scope: Annotated[str, m.Field(description="OAuth2 scope")] = ""

    OracleOic: OracleOicSettings = m.Field(
        default_factory=OracleOicSettings,
        description="Namespaced Oracle OIC settings branch.",
    )


settings: FlextOracleOicSettings = FlextOracleOicSettings.fetch_global()
"""Pre-instantiated project settings singleton.

Exposed as ``from flext_oracle_oic import settings``.
"""

__all__ = ["FlextOracleOicSettings", "settings"]
