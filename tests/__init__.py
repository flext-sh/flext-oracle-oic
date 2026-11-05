# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import api, d, e, h, r, td, tf, tk, tm, x

    from flext_oracle_oic import (
        FlextOracleOicApi,
        FlextOracleOicCli,
        FlextOracleOicClient,
        FlextOracleOicConfig,
        FlextOracleOicConstants,
        FlextOracleOicModels,
        FlextOracleOicModelsConfig,
        FlextOracleOicProtocols,
        FlextOracleOicServiceBase,
        FlextOracleOicSettings,
        FlextOracleOicTypes,
        FlextOracleOicUtilities,
        FlextOracleOicVersion,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
        config,
        main,
        oracle_oic,
        settings,
    )
    from tests.base import TestsFlextOracleOicServiceBase, s
    from tests.constants import TestsFlextOracleOicConstants, c
    from tests.models import TestsFlextOracleOicModels, m
    from tests.protocols import TestsFlextOracleOicProtocols, p
    from tests.settings import TestsFlextOracleOicSettings
    from tests.typings import TestsFlextOracleOicTypes, t
    from tests.utilities import TestsFlextOracleOicUtilities, u


__all__: tuple[str, ...] = (
    "FlextOracleOicApi",
    "FlextOracleOicCli",
    "FlextOracleOicClient",
    "FlextOracleOicConfig",
    "FlextOracleOicConstants",
    "FlextOracleOicModels",
    "FlextOracleOicModelsConfig",
    "FlextOracleOicProtocols",
    "FlextOracleOicServiceBase",
    "FlextOracleOicSettings",
    "FlextOracleOicTypes",
    "FlextOracleOicUtilities",
    "FlextOracleOicVersion",
    "TestsFlextOracleOicConstants",
    "TestsFlextOracleOicModels",
    "TestsFlextOracleOicProtocols",
    "TestsFlextOracleOicServiceBase",
    "TestsFlextOracleOicSettings",
    "TestsFlextOracleOicTypes",
    "TestsFlextOracleOicUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "api",
    "c",
    "config",
    "d",
    "e",
    "h",
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
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "FlextOracleOicApi": "flext_oracle_oic",
        "FlextOracleOicCli": "flext_oracle_oic",
        "FlextOracleOicClient": "flext_oracle_oic",
        "FlextOracleOicConfig": "flext_oracle_oic",
        "FlextOracleOicConstants": "flext_oracle_oic",
        "FlextOracleOicModels": "flext_oracle_oic",
        "FlextOracleOicModelsConfig": "flext_oracle_oic",
        "FlextOracleOicProtocols": "flext_oracle_oic",
        "FlextOracleOicServiceBase": "flext_oracle_oic",
        "FlextOracleOicSettings": "flext_oracle_oic",
        "FlextOracleOicTypes": "flext_oracle_oic",
        "FlextOracleOicUtilities": "flext_oracle_oic",
        "FlextOracleOicVersion": "flext_oracle_oic",
        "TestsFlextOracleOicConstants": ".constants",
        "TestsFlextOracleOicModels": ".models",
        "TestsFlextOracleOicProtocols": ".protocols",
        "TestsFlextOracleOicServiceBase": ".base",
        "TestsFlextOracleOicSettings": ".settings",
        "TestsFlextOracleOicTypes": ".typings",
        "TestsFlextOracleOicUtilities": ".utilities",
        "__author__": "flext_oracle_oic",
        "__author_email__": "flext_oracle_oic",
        "__description__": "flext_oracle_oic",
        "__license__": "flext_oracle_oic",
        "__title__": "flext_oracle_oic",
        "__url__": "flext_oracle_oic",
        "__version__": "flext_oracle_oic",
        "__version_info__": "flext_oracle_oic",
        "api": "flext_tests",
        "c": ".constants",
        "config": "flext_oracle_oic",
        "d": "flext_tests",
        "e": "flext_tests",
        "h": "flext_tests",
        "m": ".models",
        "main": "flext_oracle_oic",
        "oracle_oic": "flext_oracle_oic",
        "p": ".protocols",
        "r": "flext_tests",
        "s": ".base",
        "settings": "flext_oracle_oic",
        "t": ".typings",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "x": "flext_tests",
    },
    public_exports=__all__,
)
