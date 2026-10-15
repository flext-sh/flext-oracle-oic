# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

from flext_oracle_oic.__version__ import __version__

if TYPE_CHECKING:
    from flext_auth import d, e, h, r, x

    from flext_oracle_oic import _constants, _models, _protocols, _utilities, services
    from flext_oracle_oic.__version__ import (
        FlextOracleOicVersion,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version_info__,
    )
    from flext_oracle_oic._config import FlextOracleOicConfig, config
    from flext_oracle_oic._settings import FlextOracleOicSettings, settings
    from flext_oracle_oic.api import FlextOracleOicApi, oracle_oic
    from flext_oracle_oic.base import FlextOracleOicServiceBase, s
    from flext_oracle_oic.cli import FlextOracleOicCli, main
    from flext_oracle_oic.constants import FlextOracleOicConstants, c
    from flext_oracle_oic.ext_client import FlextOracleOicClient
    from flext_oracle_oic.models import FlextOracleOicModels, m
    from flext_oracle_oic.protocols import FlextOracleOicProtocols, p
    from flext_oracle_oic.typings import FlextOracleOicTypes, t
    from flext_oracle_oic.utilities import FlextOracleOicUtilities, u


__all__: tuple[str, ...] = (
    "FlextOracleOicApi",
    "FlextOracleOicCli",
    "FlextOracleOicClient",
    "FlextOracleOicConfig",
    "FlextOracleOicConstants",
    "FlextOracleOicModels",
    "FlextOracleOicProtocols",
    "FlextOracleOicServiceBase",
    "FlextOracleOicSettings",
    "FlextOracleOicTypes",
    "FlextOracleOicUtilities",
    "FlextOracleOicVersion",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "_constants",
    "_models",
    "_protocols",
    "_utilities",
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
    "services",
    "settings",
    "t",
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextOracleOicApi": ".api",
        "FlextOracleOicCli": ".cli",
        "FlextOracleOicClient": ".ext_client",
        "FlextOracleOicConfig": "._config",
        "FlextOracleOicConstants": ".constants",
        "FlextOracleOicModels": ".models",
        "FlextOracleOicProtocols": ".protocols",
        "FlextOracleOicServiceBase": ".base",
        "FlextOracleOicSettings": "._settings",
        "FlextOracleOicTypes": ".typings",
        "FlextOracleOicUtilities": ".utilities",
        "FlextOracleOicVersion": ".__version__",
        "__author__": ".__version__",
        "__author_email__": ".__version__",
        "__description__": ".__version__",
        "__license__": ".__version__",
        "__title__": ".__version__",
        "__url__": ".__version__",
        "__version_info__": ".__version__",
        "_constants": "._constants",
        "_models": "._models",
        "_protocols": "._protocols",
        "_utilities": "._utilities",
        "c": ".constants",
        "config": "._config",
        "d": "flext_auth",
        "e": "flext_auth",
        "h": "flext_auth",
        "m": ".models",
        "main": ".cli",
        "oracle_oic": ".api",
        "p": ".protocols",
        "r": "flext_auth",
        "s": ".base",
        "services": ".services",
        "settings": "._settings",
        "t": ".typings",
        "u": ".utilities",
        "x": "flext_auth",
    }),
    public_exports=__all__,
)
