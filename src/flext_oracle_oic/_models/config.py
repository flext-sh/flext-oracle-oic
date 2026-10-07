"""Declarations for the Oracle OIC business configuration namespace.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_core import m, t


class FlextOracleOicModelsConfig:
    """Config declarations composed into the Oracle OIC model facade."""

    class Config(m.ImmutableValueModel):
        """Required business domains with values supplied by the YAML owner."""

        model_config: ClassVar[m.ConfigDict] = m.ConfigDict(extra="allow")

        __pydantic_extra__: dict[str, t.JsonValue] = m.Field(init=False)

        api: t.JsonMapping
        integration: t.JsonMapping
        validation: t.JsonMapping
        monitoring: t.JsonMapping


__all__: list[str] = ["FlextOracleOicModelsConfig"]
