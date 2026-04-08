# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests.constants import (
        TestsFlextOracleOicConstants,
        TestsFlextOracleOicConstants as c,
    )
    from tests.models import TestsFlextOracleOicModels, TestsFlextOracleOicModels as m
    from tests.protocols import (
        TestsFlextOracleOicProtocols,
        TestsFlextOracleOicProtocols as p,
    )
    from tests.typings import TestsFlextOracleOicTypes, TestsFlextOracleOicTypes as t
    from tests.utilities import (
        TestsFlextOracleOicUtilities,
        TestsFlextOracleOicUtilities as u,
    )
_LAZY_IMPORTS = {
    "TestsFlextOracleOicConstants": ("tests.constants", "TestsFlextOracleOicConstants"),
    "TestsFlextOracleOicModels": ("tests.models", "TestsFlextOracleOicModels"),
    "TestsFlextOracleOicProtocols": ("tests.protocols", "TestsFlextOracleOicProtocols"),
    "TestsFlextOracleOicTypes": ("tests.typings", "TestsFlextOracleOicTypes"),
    "TestsFlextOracleOicUtilities": ("tests.utilities", "TestsFlextOracleOicUtilities"),
    "c": ("tests.constants", "TestsFlextOracleOicConstants"),
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("tests.models", "TestsFlextOracleOicModels"),
    "p": ("tests.protocols", "TestsFlextOracleOicProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "t": ("tests.typings", "TestsFlextOracleOicTypes"),
    "u": ("tests.utilities", "TestsFlextOracleOicUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "TestsFlextOracleOicConstants",
    "TestsFlextOracleOicModels",
    "TestsFlextOracleOicProtocols",
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
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
