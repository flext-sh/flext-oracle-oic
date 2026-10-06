"""Read-only contracts for the Oracle OIC business configuration namespace.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
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


__all__: list[str] = ["FlextOracleOicProtocolsConfig"]
