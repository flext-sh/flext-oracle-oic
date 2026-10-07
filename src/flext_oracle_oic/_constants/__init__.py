# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic. Constants package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_oic._constants.base import FlextOracleOicConstantsBase
    from flext_oracle_oic._constants.values import FlextOracleOicConstantsValues


__all__: tuple[str, ...] = (
    "FlextOracleOicConstantsBase",
    "FlextOracleOicConstantsValues",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextOracleOicConstantsBase": ".base",
        "FlextOracleOicConstantsValues": ".values",
    }),
    public_exports=__all__,
)
