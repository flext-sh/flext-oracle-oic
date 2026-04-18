# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_basic": ("TestBasicFunctionality",),
        ".test_cli": ("TestCLI",),
        ".test_config": ("TestFlextOracleOicSettings",),
        ".test_ext_client": ("test_ext_client",),
        ".test_ext_services": ("test_ext_services",),
        ".test_extension": ("TestOracleOicExtension",),
        ".test_import": ("test_import",),
        ".test_main": (
            "TestMainFunction",
            "TestMainModule",
        ),
        ".test_models": (
            "TestOICAuthConfig",
            "TestOICConnectionConfig",
            "TestOICConnectionInfo",
            "TestOICIntegrationInfo",
        ),
        ".test_typings": ("TestFlextTypes",),
        ".test_version": ("test_version",),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
