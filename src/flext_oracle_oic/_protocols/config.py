"""Read-only contracts for the Oracle OIC business configuration namespace.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_auth import FlextAuthProtocols

if TYPE_CHECKING:
    from collections.abc import Callable

    from flext_auth import p
    from flext_core import t


class FlextOracleOicProtocolsConfig:
    """Config contracts composed into the Oracle OIC protocol facade."""

    @runtime_checkable
    class Config(Protocol):
        """The business domains consumed through the config namespace."""

        @property
        def api(self) -> t.JsonMapping:
            """The configured API rules."""
            ...

        @property
        def integration(self) -> t.JsonMapping:
            """The configured integration rules."""
            ...

        @property
        def validation(self) -> t.JsonMapping:
            """The configured validation rules."""
            ...

        @property
        def monitoring(self) -> t.JsonMapping:
            """The configured monitoring rules."""
            ...

    @runtime_checkable
    class FieldValidationPlan(FlextAuthProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def field_name(self) -> str:
            """Name of the field to validate."""
            ...

        @property
        def label(self) -> str:
            """Human-readable label for the field."""
            ...

        @property
        def required(self) -> bool:
            """Whether the field is required."""
            ...

        @property
        def required_message(self) -> str:
            """Error message when required field is missing."""
            ...

        @property
        def validator(self) -> Callable[[str], p.Result[str]]:
            """Validation function for the field value."""
            ...


__all__: list[str] = ["FlextOracleOicProtocolsConfig"]
