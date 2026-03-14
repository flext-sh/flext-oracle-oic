# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""FLEXT Oracle OIC Extension - EXTENSION Pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_oracle_oic.__version__ import __all__
    from flext_oracle_oic.api import FlextOracleOicApi
    from flext_oracle_oic.constants import FlextOracleOicConstants, c
    from flext_oracle_oic.ext_client import FlextOracleOicClient
    from flext_oracle_oic.ext_services import FlextOracleOicExtServices, logger
    from flext_oracle_oic.main import FlextOracleOicCli, main
    from flext_oracle_oic.models import FlextOracleOicModels, m
    from flext_oracle_oic.protocols import FlextOracleOicProtocols, p
    from flext_oracle_oic.service import (
        FlextOracleOicService,
        FlextOracleOicService as s,
    )
    from flext_oracle_oic.settings import FlextOracleOicSettings
    from flext_oracle_oic.typings import FlextOracleOicTypes, t
    from flext_oracle_oic.utilities import FlextOracleOicUtilities, u

# Lazy import mapping: export_name -> (module_path, attr_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextOracleOicApi": ("flext_oracle_oic.api", "FlextOracleOicApi"),
    "FlextOracleOicCli": ("flext_oracle_oic.main", "FlextOracleOicCli"),
    "FlextOracleOicClient": ("flext_oracle_oic.ext_client", "FlextOracleOicClient"),
    "FlextOracleOicConstants": (
        "flext_oracle_oic.constants",
        "FlextOracleOicConstants",
    ),
    "FlextOracleOicExtServices": (
        "flext_oracle_oic.ext_services",
        "FlextOracleOicExtServices",
    ),
    "FlextOracleOicModels": ("flext_oracle_oic.models", "FlextOracleOicModels"),
    "FlextOracleOicProtocols": (
        "flext_oracle_oic.protocols",
        "FlextOracleOicProtocols",
    ),
    "FlextOracleOicService": ("flext_oracle_oic.service", "FlextOracleOicService"),
    "FlextOracleOicSettings": ("flext_oracle_oic.settings", "FlextOracleOicSettings"),
    "FlextOracleOicTypes": ("flext_oracle_oic.typings", "FlextOracleOicTypes"),
    "FlextOracleOicUtilities": (
        "flext_oracle_oic.utilities",
        "FlextOracleOicUtilities",
    ),
    "__all__": ("flext_oracle_oic.__version__", "__all__"),
    "c": ("flext_oracle_oic.constants", "c"),
    "logger": ("flext_oracle_oic.ext_services", "logger"),
    "m": ("flext_oracle_oic.models", "m"),
    "main": ("flext_oracle_oic.main", "main"),
    "p": ("flext_oracle_oic.protocols", "p"),
    "s": ("flext_oracle_oic.service", "FlextOracleOicService"),
    "t": ("flext_oracle_oic.typings", "t"),
    "u": ("flext_oracle_oic.utilities", "u"),
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
    "logger",
    "m",
    "main",
    "p",
    "s",
    "t",
    "u",
]


def __getattr__(name: str) -> t.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
