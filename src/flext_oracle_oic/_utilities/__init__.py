# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic. Utilities package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .authentication_validation import (
        FlextOracleOicUtilitiesAuthenticationValidation as FlextOracleOicUtilitiesAuthenticationValidation,
    )
    from .connection_validation import (
        FlextOracleOicUtilitiesConnectionValidation as FlextOracleOicUtilitiesConnectionValidation,
    )
    from .monitoring import (
        FlextOracleOicUtilitiesMonitoring as FlextOracleOicUtilitiesMonitoring,
    )
    from .oracle_oic import (
        FlextOracleOicUtilitiesOracleOic as FlextOracleOicUtilitiesOracleOic,
    )

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    ".authentication_validation": ("FlextOracleOicUtilitiesAuthenticationValidation",),
    ".connection_validation": ("FlextOracleOicUtilitiesConnectionValidation",),
    ".monitoring": ("FlextOracleOicUtilitiesMonitoring",),
    ".oracle_oic": ("FlextOracleOicUtilitiesOracleOic",),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
    "FlextOracleOicUtilitiesAuthenticationValidation",
    "FlextOracleOicUtilitiesConnectionValidation",
    "FlextOracleOicUtilitiesMonitoring",
    "FlextOracleOicUtilitiesOracleOic",
)

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
