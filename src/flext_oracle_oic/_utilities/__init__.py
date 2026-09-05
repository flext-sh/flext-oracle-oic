# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic. Utilities package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .authentication_validation import (
        FlextOracleOicUtilitiesAuthenticationValidation,
    )
    from .connection_validation import FlextOracleOicUtilitiesConnectionValidation
    from .monitoring import FlextOracleOicUtilitiesMonitoring
    from .oracle_oic import FlextOracleOicUtilitiesOracleOic
__all__: tuple[str, ...] = (
    "FlextOracleOicUtilitiesAuthenticationValidation",
    "FlextOracleOicUtilitiesConnectionValidation",
    "FlextOracleOicUtilitiesMonitoring",
    "FlextOracleOicUtilitiesOracleOic",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".authentication_validation": (
                "FlextOracleOicUtilitiesAuthenticationValidation",
            ),
            ".connection_validation": ("FlextOracleOicUtilitiesConnectionValidation",),
            ".monitoring": ("FlextOracleOicUtilitiesMonitoring",),
            ".oracle_oic": ("FlextOracleOicUtilitiesOracleOic",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
