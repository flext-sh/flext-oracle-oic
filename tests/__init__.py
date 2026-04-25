# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if _t.TYPE_CHECKING:
    from flext_tests import td, tf, tk, tm, tv

    from flext_oracle_oic import d, e, h, r, s, x
    from tests.constants import TestsFlextOracleOicConstants, c
    from tests.models import TestsFlextOracleOicModels, m
    from tests.protocols import TestsFlextOracleOicProtocols, p
    from tests.typings import TestsFlextOracleOicTypes, t
    from tests.unit.test_basic import TestsFlextOracleOicBasic
    from tests.unit.test_cli import TestsFlextOracleOicCli
    from tests.unit.test_config import TestsFlextOracleOicConfig
    from tests.unit.test_extension import TestsFlextOracleOicExtension
    from tests.unit.test_main import TestsFlextOracleOicMain
    from tests.unit.test_models import TestsFlextOracleOicModelsUnit
    from tests.unit.test_typings import TestsFlextOracleOicTypingsUnit
    from tests.utilities import TestsFlextOracleOicUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    (".unit",),
    build_lazy_import_map(
        {
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
            ".typings": (
                "TestsFlextOracleOicTypes",
                "t",
            ),
            ".unit.test_basic": ("TestsFlextOracleOicBasic",),
            ".unit.test_cli": ("TestsFlextOracleOicCli",),
            ".unit.test_config": ("TestsFlextOracleOicConfig",),
            ".unit.test_extension": ("TestsFlextOracleOicExtension",),
            ".unit.test_main": ("TestsFlextOracleOicMain",),
            ".unit.test_models": ("TestsFlextOracleOicModelsUnit",),
            ".unit.test_typings": ("TestsFlextOracleOicTypingsUnit",),
            ".utilities": (
                "TestsFlextOracleOicUtilities",
                "u",
            ),
            "flext_oracle_oic": (
                "d",
                "e",
                "h",
                "r",
                "s",
                "x",
            ),
            "flext_tests": (
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "TestsFlextOracleOicBasic",
    "TestsFlextOracleOicCli",
    "TestsFlextOracleOicConfig",
    "TestsFlextOracleOicConstants",
    "TestsFlextOracleOicExtension",
    "TestsFlextOracleOicMain",
    "TestsFlextOracleOicModels",
    "TestsFlextOracleOicModelsUnit",
    "TestsFlextOracleOicProtocols",
    "TestsFlextOracleOicTypes",
    "TestsFlextOracleOicTypingsUnit",
    "TestsFlextOracleOicUtilities",
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
]
