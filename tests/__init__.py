# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_oic import FlextOracleOicConstants
    from flext_tests import FlextTestsConstants, d, e, h, r, td, tf, tk, tm, tv, x

    from . import unit as unit
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
    "FlextOracleOicConstants",
    "FlextTestsConstants",
    "TestsFlextOracleOicConstants",
    "TestsFlextOracleOicModels",
    "TestsFlextOracleOicProtocols",
    "TestsFlextOracleOicServiceBase",
    "TestsFlextOracleOicSettings",
    "TestsFlextOracleOicTypes",
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
    "unit",
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
            "flext_oracle_oic": ("FlextOracleOicConstants",),
            "flext_tests": (
                "FlextTestsConstants",
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
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
