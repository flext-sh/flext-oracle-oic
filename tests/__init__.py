# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import api, d, e, h, r, td, tf, tk, tm, x

    from tests import unit
    from tests.base import TestsFlextOracleOicServiceBase, s
    from tests.constants import TestsFlextOracleOicConstants, c
    from tests.models import TestsFlextOracleOicModels, m
    from tests.protocols import TestsFlextOracleOicProtocols, p
    from tests.settings import TestsFlextOracleOicSettings
    from tests.typings import TestsFlextOracleOicTypes, t
    from tests.utilities import TestsFlextOracleOicUtilities, u


__all__: tuple[str, ...] = (
    "TestsFlextOracleOicConstants",
    "TestsFlextOracleOicModels",
    "TestsFlextOracleOicProtocols",
    "TestsFlextOracleOicServiceBase",
    "TestsFlextOracleOicSettings",
    "TestsFlextOracleOicTypes",
    "TestsFlextOracleOicUtilities",
    "api",
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
            "flext_tests": ("api", "d", "e", "h", "r", "td", "tf", "tk", "tm", "x"),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    ),
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
