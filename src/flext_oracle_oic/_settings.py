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

from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, Field
from pydantic_settings import SettingsConfigDict

from flext_core import FlextSettings


class FlextOracleOicSettings(FlextSettings):
    """Oracle OIC settings; all project fields under ``settings.OracleOic.*``."""

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_ORACLE_OIC_",
        env_nested_delimiter="__",
        extra="ignore",
    )

    class _OracleOic(BaseModel):
        """Namespaced Oracle OIC connection + OAuth + feature-flag scalars."""

        base_url: str = "https://localhost.integration.ocp.oraclecloud.com"
        api_version: str = "v1"
        request_timeout: int = 30
        max_retries: int = 3
        verify_ssl: bool = True
        use_ssl: bool = True
        enable_monitoring: bool = True
        enable_enterprise_patterns: bool = True
        enable_orchestration: bool = True
        oauth_client_id: str = ""
        oauth_client_secret: str = ""
        # NOTE (S105): a public OAuth endpoint URL is configuration, not a
        # secret; Field(default=...) matches the flext-auth layer-0 settings
        # pattern for non-secret URL defaults.
        oauth_token_url: Annotated[
            str,
            Field(
                default="https://localhost.integration.ocp.oraclecloud.com/oauth/token",
                description="IDCS OAuth2 token endpoint URL",
            ),
        ]
        oauth_client_aud: str = ""
        oauth_scope: str = ""

    if TYPE_CHECKING:
        OracleOic: _OracleOic
    else:
        OracleOic: _OracleOic = Field(default_factory=_OracleOic)


settings: FlextOracleOicSettings = FlextOracleOicSettings.fetch_global()
"""Pre-instantiated project settings singleton — ``from flext_oracle_oic import settings``."""

__all__ = ["FlextOracleOicSettings", "settings"]
