# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_basic": ("TestsFlextOracleOicBasic",),
        ".test_cli": ("TestsFlextOracleOicCli",),
        ".test_config": ("TestsFlextOracleOicConfig",),
        ".test_ext_client": (
            "TestsFlextOracleOicExtClient",
            "test_ext_client",
        ),
        ".test_ext_services": ("TestsFlextOracleOicExtServices",),
        ".test_extension": ("TestsFlextOracleOicExtension",),
        ".test_import": ("TestsFlextOracleOicImport",),
        ".test_main": ("TestsFlextOracleOicMain",),
        ".test_models": ("TestsFlextOracleOicModelsUnit",),
        ".test_typings": ("TestsFlextOracleOicTypingsUnit",),
        ".test_version": ("TestsFlextOracleOicVersion",),
        "flext_tests": (
            "c",
            "d",
            "e",
            "h",
            "m",
            "p",
            "r",
            "s",
            "t",
            "td",
            "tf",
            "tk",
            "tm",
            "tv",
            "u",
            "x",
        ),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
