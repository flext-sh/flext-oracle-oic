"""Declarations for the Oracle OIC business configuration namespace.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, ClassVar

from flext_core import m, t


class FlextOracleOicModelsConfig:
    """Config declarations composed into the Oracle OIC model facade."""

    class Config(m.ImmutableValueModel):
        """Required business domains with values supplied by the YAML owner."""

        model_config: ClassVar[m.ConfigDict] = m.ConfigDict(extra="allow")

        api: Annotated[
            t.JsonMapping,
            m.Field(description="Oracle OIC API business rules"),
        ]
        integration: Annotated[
            t.JsonMapping,
            m.Field(description="Oracle OIC integration business rules"),
        ]
        validation: Annotated[
            t.JsonMapping,
            m.Field(description="Oracle OIC validation business rules"),
        ]
        monitoring: Annotated[
            t.JsonMapping,
            m.Field(description="Oracle OIC monitoring business rules"),
        ]


__all__: list[str] = ["FlextOracleOicModelsConfig"]
