# AUTO-GENERATED FILE — Regenerate with: make gen
"""Utilities package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
