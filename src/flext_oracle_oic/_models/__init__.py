# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic. Models package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_oic._models.config import FlextOracleOicModelsConfig


__all__: tuple[str, ...] = ("FlextOracleOicModelsConfig",)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({"FlextOracleOicModelsConfig": ".config"}),
    public_exports=__all__,
)
