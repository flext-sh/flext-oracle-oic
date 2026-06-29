# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

_LAZY_IMPORTS = merge_lazy_imports(
    (".unit",),
    build_lazy_import_map(
        {
            ".base": (
                "TestsFlextOracleOicServiceBase",
                "s",
            ),
            ".conftest": ("conftest",),
            ".constants": (
                "TestsFlextOracleOicConstants",
                "c",
            ),
            ".models": (
                "TestsFlextOracleOicModels",
                "m",
            ),
            ".protocols": (
                "TestsFlextOracleOicProtocols",
                "p",
            ),
            ".settings": ("TestsFlextOracleOicSettings",),
            ".typings": (
                "TestsFlextOracleOicTypes",
                "t",
            ),
            ".unit": ("unit",),
            ".unit.test_basic": ("TestsFlextOracleOicBasic",),
            ".unit.test_cli": ("TestsFlextOracleOicCli",),
            ".unit.test_config": ("TestsFlextOracleOicConfig",),
            ".unit.test_extension": ("TestsFlextOracleOicExtension",),
            ".unit.test_import": ("TestsFlextOracleOicImport",),
            ".unit.test_main": ("TestsFlextOracleOicMain",),
            ".unit.test_models": ("TestsFlextOracleOicModelsUnit",),
            ".unit.test_typings": ("TestsFlextOracleOicTypingsUnit",),
            ".unit.test_version": ("TestsFlextOracleOicVersion",),
            ".utilities": (
                "TestsFlextOracleOicUtilities",
                "u",
            ),
            "flext_tests": (
                "d",
                "e",
                "h",
                "r",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "x",
            ),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
        "pytest_addoption",
        "pytest_collect_file",
        "pytest_collection_modifyitems",
        "pytest_configure",
        "pytest_runtest_setup",
        "pytest_runtest_teardown",
        "pytest_sessionfinish",
        "pytest_sessionstart",
        "pytest_terminal_summary",
        "pytest_warning_recorded",
    ),
    module_name=__name__,
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
