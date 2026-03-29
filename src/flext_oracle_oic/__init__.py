# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT Oracle OIC Extension - EXTENSION Pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes, d, e, h, r, x

    from flext_oracle_oic.__version__ import __all__
    from flext_oracle_oic.api import FlextOracleOicApi
    from flext_oracle_oic.constants import (
        FlextOracleOicConstants,
        FlextOracleOicConstants as c,
    )
    from flext_oracle_oic.ext_client import FlextOracleOicClient
    from flext_oracle_oic.ext_services import FlextOracleOicExtServices, logger
    from flext_oracle_oic.main import FlextOracleOicCli, main
    from flext_oracle_oic.models import FlextOracleOicModels, FlextOracleOicModels as m
    from flext_oracle_oic.protocols import (
        FlextOracleOicProtocols,
        FlextOracleOicProtocols as p,
    )
    from flext_oracle_oic.service import (
        FlextOracleOicService,
        FlextOracleOicService as s,
    )
    from flext_oracle_oic.settings import FlextOracleOicSettings
    from flext_oracle_oic.typings import FlextOracleOicTypes, FlextOracleOicTypes as t
    from flext_oracle_oic.utilities import (
        FlextOracleOicUtilities,
        FlextOracleOicUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextOracleOicApi": ["flext_oracle_oic.api", "FlextOracleOicApi"],
    "FlextOracleOicCli": ["flext_oracle_oic.main", "FlextOracleOicCli"],
    "FlextOracleOicClient": ["flext_oracle_oic.ext_client", "FlextOracleOicClient"],
    "FlextOracleOicConstants": ["flext_oracle_oic.constants", "FlextOracleOicConstants"],
    "FlextOracleOicExtServices": ["flext_oracle_oic.ext_services", "FlextOracleOicExtServices"],
    "FlextOracleOicModels": ["flext_oracle_oic.models", "FlextOracleOicModels"],
    "FlextOracleOicProtocols": ["flext_oracle_oic.protocols", "FlextOracleOicProtocols"],
    "FlextOracleOicService": ["flext_oracle_oic.service", "FlextOracleOicService"],
    "FlextOracleOicSettings": ["flext_oracle_oic.settings", "FlextOracleOicSettings"],
    "FlextOracleOicTypes": ["flext_oracle_oic.typings", "FlextOracleOicTypes"],
    "FlextOracleOicUtilities": ["flext_oracle_oic.utilities", "FlextOracleOicUtilities"],
    "__all__": ["flext_oracle_oic.__version__", "__all__"],
    "c": ["flext_oracle_oic.constants", "FlextOracleOicConstants"],
    "d": ["flext_core", "d"],
    "e": ["flext_core", "e"],
    "h": ["flext_core", "h"],
    "logger": ["flext_oracle_oic.ext_services", "logger"],
    "m": ["flext_oracle_oic.models", "FlextOracleOicModels"],
    "main": ["flext_oracle_oic.main", "main"],
    "p": ["flext_oracle_oic.protocols", "FlextOracleOicProtocols"],
    "r": ["flext_core", "r"],
    "s": ["flext_oracle_oic.service", "FlextOracleOicService"],
    "t": ["flext_oracle_oic.typings", "FlextOracleOicTypes"],
    "u": ["flext_oracle_oic.utilities", "FlextOracleOicUtilities"],
    "x": ["flext_core", "x"],
}

__all__ = [
    "FlextOracleOicApi",
    "FlextOracleOicCli",
    "FlextOracleOicClient",
    "FlextOracleOicConstants",
    "FlextOracleOicExtServices",
    "FlextOracleOicModels",
    "FlextOracleOicProtocols",
    "FlextOracleOicService",
    "FlextOracleOicSettings",
    "FlextOracleOicTypes",
    "FlextOracleOicUtilities",
    "__all__",
    "c",
    "d",
    "e",
    "h",
    "logger",
    "m",
    "main",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
