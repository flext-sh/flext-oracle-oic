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
    from flext_tests import td as td, tf as tf, tk as tk, tv as tv

    from flext_oracle_oic import d as d, e as e, h as h, r as r, x as x
    from tests.base import (
        TestsFlextOracleOicServiceBase as TestsFlextOracleOicServiceBase,
        s as s,
    )
    from tests.constants import (
        TestsFlextOracleOicConstants as TestsFlextOracleOicConstants,
        c as c,
    )
    from tests.models import (
        TestsFlextOracleOicModels as TestsFlextOracleOicModels,
        m as m,
    )
    from tests.protocols import (
        TestsFlextOracleOicProtocols as TestsFlextOracleOicProtocols,
        p as p,
    )
    from tests.settings import (
        TestsFlextOracleOicSettings as TestsFlextOracleOicSettings,
    )
    from tests.typings import (
        TestsFlextOracleOicTypes as TestsFlextOracleOicTypes,
        t as t,
    )
    from tests.unit.test_basic import (
        TestsFlextOracleOicBasic as TestsFlextOracleOicBasic,
    )
    from tests.unit.test_cli import TestsFlextOracleOicCli as TestsFlextOracleOicCli
    from tests.unit.test_config import (
        TestsFlextOracleOicConfig as TestsFlextOracleOicConfig,
    )
    from tests.unit.test_extension import (
        TestsFlextOracleOicExtension as TestsFlextOracleOicExtension,
    )
    from tests.unit.test_import import (
        TestsFlextOracleOicImport as TestsFlextOracleOicImport,
    )
    from tests.unit.test_main import TestsFlextOracleOicMain as TestsFlextOracleOicMain
    from tests.unit.test_models import (
        TestsFlextOracleOicModelsUnit as TestsFlextOracleOicModelsUnit,
    )
    from tests.unit.test_typings import (
        TestsFlextOracleOicTypingsUnit as TestsFlextOracleOicTypingsUnit,
    )
    from tests.unit.test_version import (
        TestsFlextOracleOicVersion as TestsFlextOracleOicVersion,
    )
    from tests.utilities import (
        TestsFlextOracleOicUtilities as TestsFlextOracleOicUtilities,
        u as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    (".unit",),
    build_lazy_import_map(
        {
            ".base": (
                "TestsFlextOracleOicServiceBase",
                "s",
            ),
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
            "flext_oracle_oic": (
                "d",
                "e",
                "h",
                "r",
                "x",
            ),
            "flext_tests": (
                "td",
                "tf",
                "tk",
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
    "TestsFlextOracleOicImport",
    "TestsFlextOracleOicMain",
    "TestsFlextOracleOicModels",
    "TestsFlextOracleOicModelsUnit",
    "TestsFlextOracleOicProtocols",
    "TestsFlextOracleOicServiceBase",
    "TestsFlextOracleOicSettings",
    "TestsFlextOracleOicTypes",
    "TestsFlextOracleOicTypingsUnit",
    "TestsFlextOracleOicUtilities",
    "TestsFlextOracleOicVersion",
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
    "tv",
    "u",
    "x",
]
