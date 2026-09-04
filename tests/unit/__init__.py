# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests.unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import c, d, e, h, m, p, r, s, t, td, tf, tk, tm, tv, u, x

    from .test_basic import TestsFlextOracleOicBasic
    from .test_cli import TestsFlextOracleOicCli
    from .test_config import TestsFlextOracleOicConfig
    from .test_ext_client import TestsFlextOracleOicExtClient, test_ext_client
    from .test_ext_services import TestsFlextOracleOicExtServices
    from .test_extension import TestsFlextOracleOicExtension
    from .test_import import TestsFlextOracleOicImport
    from .test_main import TestsFlextOracleOicMain
    from .test_models import TestsFlextOracleOicModelsUnit
    from .test_typings import TestsFlextOracleOicTypingsUnit
    from .test_version import TestsFlextOracleOicVersion
__all__: tuple[str, ...] = (
    "TestsFlextOracleOicBasic",
    "TestsFlextOracleOicCli",
    "TestsFlextOracleOicConfig",
    "TestsFlextOracleOicExtClient",
    "TestsFlextOracleOicExtServices",
    "TestsFlextOracleOicExtension",
    "TestsFlextOracleOicImport",
    "TestsFlextOracleOicMain",
    "TestsFlextOracleOicModelsUnit",
    "TestsFlextOracleOicTypingsUnit",
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
    "test_ext_client",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".test_basic": ("TestsFlextOracleOicBasic",),
            ".test_cli": ("TestsFlextOracleOicCli",),
            ".test_config": ("TestsFlextOracleOicConfig",),
            ".test_ext_client": ("TestsFlextOracleOicExtClient", "test_ext_client"),
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
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
