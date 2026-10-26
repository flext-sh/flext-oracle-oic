# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import (
        api,
        cli,
        config,
        d,
        e,
        h,
        install_local_packages,
        main,
        r,
        settings,
        td,
        tf,
        tk,
        tm,
        x,
    )

    from flext_oracle_oic import auth, oracle_oic, web
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
    "auth",
    "c",
    "cli",
    "config",
    "d",
    "e",
    "h",
    "install_local_packages",
    "m",
    "main",
    "oracle_oic",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "u",
    "web",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "TestsFlextOracleOicConstants": ".constants",
        "TestsFlextOracleOicModels": ".models",
        "TestsFlextOracleOicProtocols": ".protocols",
        "TestsFlextOracleOicServiceBase": ".base",
        "TestsFlextOracleOicSettings": ".settings",
        "TestsFlextOracleOicTypes": ".typings",
        "TestsFlextOracleOicUtilities": ".utilities",
        "api": "flext_tests",
        "auth": "flext_oracle_oic",
        "c": ".constants",
        "cli": "flext_tests",
        "config": "flext_tests",
        "d": "flext_tests",
        "e": "flext_tests",
        "h": "flext_tests",
        "install_local_packages": "flext_tests",
        "m": ".models",
        "main": "flext_tests",
        "oracle_oic": "flext_oracle_oic",
        "p": ".protocols",
        "r": "flext_tests",
        "s": ".base",
        "settings": "flext_tests",
        "t": ".typings",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "web": "flext_oracle_oic",
        "x": "flext_tests",
    }),
    public_exports=__all__,
)
