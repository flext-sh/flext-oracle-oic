"""Declarations for the Oracle OIC business configuration namespace.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Annotated, ClassVar

from flext_core import m, p, t


class FlextModelsOracleOicConfig:
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

    class FieldValidationPlan(m.Value):
        """Validated plan for one integration string field."""

        model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
            arbitrary_types_allowed=True,
            frozen=True,
        )

        field_name: Annotated[str, m.Field(description="Name of the field to validate")]
        label: Annotated[str, m.Field(description="Human-readable label for the field")]
        required: Annotated[
            bool,
            m.Field(description="Whether the field is required"),
        ] = False
        required_message: Annotated[
            str,
            m.Field(description="Error message when required field is missing"),
        ] = ""
        validator: Annotated[
            Callable[[str], p.Result[str]],
            m.Field(description="Validation function for the field value"),
        ]


__all__: list[str] = ["FlextModelsOracleOicConfig"]
