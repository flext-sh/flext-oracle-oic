# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

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
_LAZY_IMPORTS = merge_lazy_imports(
    ("tests.unit",),
    {
        "TestsFlextOracleOicConstants": (
            "tests.constants",
            "TestsFlextOracleOicConstants",
        ),
        "TestsFlextOracleOicModels": ("tests.models", "TestsFlextOracleOicModels"),
        "TestsFlextOracleOicProtocols": (
            "tests.protocols",
            "TestsFlextOracleOicProtocols",
        ),
        "TestsFlextOracleOicTypes": ("tests.typings", "TestsFlextOracleOicTypes"),
        "TestsFlextOracleOicUtilities": (
            "tests.utilities",
            "TestsFlextOracleOicUtilities",
        ),
        "c": ("tests.constants", "TestsFlextOracleOicConstants"),
        "conftest": "tests.conftest",
        "constants": "tests.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("tests.models", "TestsFlextOracleOicModels"),
        "models": "tests.models",
        "p": ("tests.protocols", "TestsFlextOracleOicProtocols"),
        "protocols": "tests.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "t": ("tests.typings", "TestsFlextOracleOicTypes"),
        "test_basic": "tests.test_basic",
        "test_cli": "tests.test_cli",
        "test_config": "tests.test_config",
        "test_ext_client": "tests.test_ext_client",
        "test_ext_services": "tests.test_ext_services",
        "test_extension": "tests.test_extension",
        "test_import": "tests.test_import",
        "test_main": "tests.test_main",
        "test_models": "tests.test_models",
        "test_typings": "tests.test_typings",
        "typings": "tests.typings",
        "u": ("tests.utilities", "TestsFlextOracleOicUtilities"),
        "unit": "tests.unit",
        "utilities": "tests.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)
_ = _LAZY_IMPORTS.pop("cleanup_submodule_namespace", None)
_ = _LAZY_IMPORTS.pop("install_lazy_exports", None)
_ = _LAZY_IMPORTS.pop("lazy_getattr", None)
_ = _LAZY_IMPORTS.pop("logger", None)
_ = _LAZY_IMPORTS.pop("merge_lazy_imports", None)
_ = _LAZY_IMPORTS.pop("output", None)
_ = _LAZY_IMPORTS.pop("output_reporting", None)

__all__ = [
    "TestsFlextOracleOicConstants",
    "TestsFlextOracleOicModels",
    "TestsFlextOracleOicProtocols",
    "TestsFlextOracleOicTypes",
    "TestsFlextOracleOicUtilities",
    "c",
    "conftest",
    "constants",
    "d",
    "e",
    "h",
    "m",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "t",
    "test_basic",
    "test_cli",
    "test_config",
    "test_ext_client",
    "test_ext_services",
    "test_extension",
    "test_import",
    "test_main",
    "test_models",
    "test_typings",
    "typings",
    "u",
    "unit",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
