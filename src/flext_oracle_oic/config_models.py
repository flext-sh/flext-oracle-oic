"""Layer-zero schemas for YAML-owned Oracle OIC configuration.

Typed, frozen shapes for the ``config/*.yaml`` business-rule SSOT. This module
imports only Pydantic. ``FlextOracleOicConfig`` declares one typed field per
YAML domain and exposes the validated objects as ``config.<domain>``. Adding a
new config domain = add a nested model here and a typed field on
``FlextOracleOicConfig``.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping

from pydantic import BaseModel, ConfigDict, JsonValue


class FlextModelsOracleOicConfig:
    """Namespace of typed flext-oracle-oic config models (pure Pydantic)."""

    class Config(BaseModel):
        """Required business domains with values supplied by the YAML owner."""

        model_config = ConfigDict(extra="allow", frozen=True)

        api: Mapping[str, JsonValue]
        integration: Mapping[str, JsonValue]
        validation: Mapping[str, JsonValue]
        monitoring: Mapping[str, JsonValue]


__all__: list[str] = ["FlextModelsOracleOicConfig"]
