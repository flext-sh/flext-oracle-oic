"""FLEXT Oracle OIC Extension - EXTENSION Pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import (
        FlextDecorators as d,
        FlextExceptions as e,
        FlextHandlers as h,
        r,
        x,
    )

    from flext_oracle_oic.__version__ import __version__, __version_info__
    from flext_oracle_oic.api import FlextOracleOicApi
    from flext_oracle_oic.constants import (
        FlextOracleOicConstants,
        FlextOracleOicConstants as c,
    )
    from flext_oracle_oic.ext_client import FlextOracleOicClient
    from flext_oracle_oic.models import FlextOracleOicModels, m
    from flext_oracle_oic.protocols import (
        FlextOracleOicProtocols,
        FlextOracleOicProtocols as p,
    )
    from flext_oracle_oic.service import FlextOracleOicService
    from flext_oracle_oic.settings import (
        FlextOracleOicSettings,
        FlextOracleOicSettings as s,
    )
    from flext_oracle_oic.typings import FlextOracleOicTypes, t
    from flext_oracle_oic.utilities import (
        FlextOracleOicUtilities,
        FlextOracleOicUtilities as u,
    )

# Lazy import mapping: export_name -> (module_path, attr_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextOracleOicApi": ("flext_oracle_oic.api", "FlextOracleOicApi"),
    "FlextOracleOicClient": ("flext_oracle_oic.ext_client", "FlextOracleOicClient"),
    "FlextOracleOicConstants": (
        "flext_oracle_oic.constants",
        "FlextOracleOicConstants",
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
    "__version__": ("flext_oracle_oic.__version__", "__version__"),
    "__version_info__": ("flext_oracle_oic.__version__", "__version_info__"),
    "c": ("flext_oracle_oic.constants", "FlextOracleOicConstants"),
    "d": ("flext_core", "FlextDecorators"),
    "e": ("flext_core", "FlextExceptions"),
    "h": ("flext_core", "FlextHandlers"),
    "m": ("flext_oracle_oic.models", "m"),
    "p": ("flext_oracle_oic.protocols", "FlextOracleOicProtocols"),
    "r": ("flext_core", "r"),
    "s": ("flext_oracle_oic.settings", "FlextOracleOicSettings"),
    "t": ("flext_oracle_oic.typings", "t"),
    "u": ("flext_oracle_oic.utilities", "FlextOracleOicUtilities"),
    "x": ("flext_core", "x"),
}

__all__ = [
    "FlextOracleOicApi",
    "FlextOracleOicClient",
    "FlextOracleOicConstants",
    "FlextOracleOicModels",
    "FlextOracleOicProtocols",
    "FlextOracleOicService",
    "FlextOracleOicSettings",
    "FlextOracleOicTypes",
    "FlextOracleOicUtilities",
    "__version__",
    "__version_info__",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]


def __getattr__(
    name: str,
):  # JUSTIFIED: Ruff (any-type) with PEP 562 dynamic module exports — https://docs.astral.sh/ruff/rules/any-type/
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
