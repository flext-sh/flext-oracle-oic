# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_auth import auth
    from flext_cli import cli, main
    from flext_tests import (
        active_rules,
        api,
        config,
        discover_repository_root,
        install_local_packages,
        load_infra_report,
        settings,
        split_csv,
        td,
        tf,
        tk,
        tm,
        tv,
    )
    from flext_web import web

    from flext_core import core, d, e, h, lazy_attribute, r, x
    from flext_oracle_oic import oracle_oic

    from . import unit
    from .base import (
        TestsFlextOracleOicServiceBase,
        TestsFlextOracleOicServiceBase as s,
    )
    from .constants import (
        TestsFlextOracleOicConstants,
        TestsFlextOracleOicConstants as c,
    )
    from .models import TestsFlextOracleOicModels, TestsFlextOracleOicModels as m
    from .protocols import (
        TestsFlextOracleOicProtocols,
        TestsFlextOracleOicProtocols as p,
    )
    from .settings import TestsFlextOracleOicSettings
    from .typings import TestsFlextOracleOicTypes, TestsFlextOracleOicTypes as t
    from .utilities import (
        TestsFlextOracleOicUtilities,
        TestsFlextOracleOicUtilities as u,
    )
__all__: tuple[str, ...] = (
    "TestsFlextOracleOicConstants",
    "TestsFlextOracleOicModels",
    "TestsFlextOracleOicProtocols",
    "TestsFlextOracleOicServiceBase",
    "TestsFlextOracleOicSettings",
    "TestsFlextOracleOicTypes",
    "TestsFlextOracleOicUtilities",
    "active_rules",
    "api",
    "auth",
    "c",
    "cli",
    "config",
    "core",
    "d",
    "discover_repository_root",
    "e",
    "h",
    "install_local_packages",
    "lazy_attribute",
    "load_infra_report",
    "m",
    "main",
    "oracle_oic",
    "p",
    "r",
    "s",
    "settings",
    "split_csv",
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "unit",
    "web",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("TestsFlextOracleOicServiceBase", "s"),
            ".constants": ("TestsFlextOracleOicConstants", "c"),
            ".models": ("TestsFlextOracleOicModels", "m"),
            ".protocols": ("TestsFlextOracleOicProtocols", "p"),
            ".settings": ("TestsFlextOracleOicSettings",),
            ".typings": ("TestsFlextOracleOicTypes", "t"),
            ".unit": ("unit",),
            ".utilities": ("TestsFlextOracleOicUtilities", "u"),
            "flext_auth": ("auth",),
            "flext_cli": ("cli", "main"),
            "flext_core": ("core", "d", "e", "h", "lazy_attribute", "r", "x"),
            "flext_oracle_oic": ("oracle_oic",),
            "flext_tests": (
                "active_rules",
                "api",
                "config",
                "discover_repository_root",
                "install_local_packages",
                "load_infra_report",
                "settings",
                "split_csv",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
            ),
            "flext_web": ("web",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
