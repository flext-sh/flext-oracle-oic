# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

    from . import unit as unit
    from .constants import TestsFlextOracleOicConstants, c
    from .models import TestsFlextOracleOicModels, m, tm
    from .protocols import TestsFlextOracleOicProtocols, p
    from .test_basic import TestBasicFunctionality
    from .test_cli import TestCLI
    from .test_config import TestFlextOracleOicSettings
    from .test_extension import TestOracleOicExtension
    from .test_import import test_basic_import, test_config_import
    from .test_main import TestMainFunction, TestMainModule
    from .test_models import (
        TestOICAuthConfig,
        TestOICConnectionConfig,
        TestOICConnectionInfo,
        TestOICIntegrationInfo,
    )
    from .test_typings import TestFlextTypes
    from .typings import TestsFlextOracleOicTypes, t
    from .unit.test_version import test_version_info_tuple, test_version_string
    from .utilities import TestsFlextOracleOicUtilities, u

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "TestBasicFunctionality": ("tests.test_basic", "TestBasicFunctionality"),
    "TestCLI": ("tests.test_cli", "TestCLI"),
    "TestFlextOracleOicSettings": ("tests.test_config", "TestFlextOracleOicSettings"),
    "TestFlextTypes": ("tests.test_typings", "TestFlextTypes"),
    "TestMainFunction": ("tests.test_main", "TestMainFunction"),
    "TestMainModule": ("tests.test_main", "TestMainModule"),
    "TestOICAuthConfig": ("tests.test_models", "TestOICAuthConfig"),
    "TestOICConnectionConfig": ("tests.test_models", "TestOICConnectionConfig"),
    "TestOICConnectionInfo": ("tests.test_models", "TestOICConnectionInfo"),
    "TestOICIntegrationInfo": ("tests.test_models", "TestOICIntegrationInfo"),
    "TestOracleOicExtension": ("tests.test_extension", "TestOracleOicExtension"),
    "TestsFlextOracleOicConstants": ("tests.constants", "TestsFlextOracleOicConstants"),
    "TestsFlextOracleOicModels": ("tests.models", "TestsFlextOracleOicModels"),
    "TestsFlextOracleOicProtocols": ("tests.protocols", "TestsFlextOracleOicProtocols"),
    "TestsFlextOracleOicTypes": ("tests.typings", "TestsFlextOracleOicTypes"),
    "TestsFlextOracleOicUtilities": ("tests.utilities", "TestsFlextOracleOicUtilities"),
    "c": ("tests.constants", "c"),
    "m": ("tests.models", "m"),
    "p": ("tests.protocols", "p"),
    "t": ("tests.typings", "t"),
    "test_basic_import": ("tests.test_import", "test_basic_import"),
    "test_config_import": ("tests.test_import", "test_config_import"),
    "test_version_info_tuple": ("tests.unit.test_version", "test_version_info_tuple"),
    "test_version_string": ("tests.unit.test_version", "test_version_string"),
    "tm": ("tests.models", "tm"),
    "u": ("tests.utilities", "u"),
    "unit": ("tests.unit", ""),
}

__all__ = [
    "TestBasicFunctionality",
    "TestCLI",
    "TestFlextOracleOicSettings",
    "TestFlextTypes",
    "TestMainFunction",
    "TestMainModule",
    "TestOICAuthConfig",
    "TestOICConnectionConfig",
    "TestOICConnectionInfo",
    "TestOICIntegrationInfo",
    "TestOracleOicExtension",
    "TestsFlextOracleOicConstants",
    "TestsFlextOracleOicModels",
    "TestsFlextOracleOicProtocols",
    "TestsFlextOracleOicTypes",
    "TestsFlextOracleOicUtilities",
    "c",
    "m",
    "p",
    "t",
    "test_basic_import",
    "test_config_import",
    "test_version_info_tuple",
    "test_version_string",
    "tm",
    "u",
    "unit",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
