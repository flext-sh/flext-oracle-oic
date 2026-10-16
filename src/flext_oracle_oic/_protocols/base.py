"""Base protocols for Oracle OIC integration points.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_oracle_oic/_protocols/base
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class FlextOracleOicProtocolsBase(Protocol):
    """Base Oracle OIC protocol part composed by the protocols facade."""


__all__: list[str] = ["FlextOracleOicProtocolsBase"]
