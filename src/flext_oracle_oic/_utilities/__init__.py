# AUTO-GENERATED FILE — Regenerate with: make gen
"""Utilities package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_oic._utilities.authentication_validation import (
        FlextOracleOicUtilitiesAuthenticationValidation,
    )
    from flext_oracle_oic._utilities.connection_validation import (
        FlextOracleOicUtilitiesConnectionValidation,
    )
    from flext_oracle_oic._utilities.monitoring import FlextOracleOicUtilitiesMonitoring
    from flext_oracle_oic._utilities.oracle_oic import FlextOracleOicUtilitiesOracleOic
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".authentication_validation": (
            "FlextOracleOicUtilitiesAuthenticationValidation",
        ),
        ".connection_validation": ("FlextOracleOicUtilitiesConnectionValidation",),
        ".monitoring": ("FlextOracleOicUtilitiesMonitoring",),
        ".oracle_oic": ("FlextOracleOicUtilitiesOracleOic",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
