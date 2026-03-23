# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_tests import d, e, h, r, s, x

    from tests import unit
    from tests.constants import (
        FlextOracleOicTestConstants,
        FlextOracleOicTestConstants as c,
    )
    from tests.models import FlextOracleOicTestModels, FlextOracleOicTestModels as m
    from tests.protocols import (
        FlextOracleOicTestProtocols,
        FlextOracleOicTestProtocols as p,
    )
    from tests.test_basic import TestBasicFunctionality
    from tests.test_cli import TestCLI
    from tests.test_config import TestFlextOracleOicSettings
    from tests.test_extension import TestOracleOicExtension
    from tests.test_import import test_basic_import, test_config_import
    from tests.test_main import TestMainFunction, TestMainModule
    from tests.test_models import (
        TestOICAuthConfig,
        TestOICConnectionConfig,
        TestOICConnectionInfo,
        TestOICIntegrationInfo,
    )
    from tests.test_typings import TestFlextTypes
    from tests.typings import FlextOracleOicTestTypes, FlextOracleOicTestTypes as t
    from tests.unit.test_version import test_version_info_tuple, test_version_string
    from tests.utilities import (
        FlextOracleOicTestUtilities,
        FlextOracleOicTestUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, tuple[str, str]] = {
    "FlextOracleOicTestConstants": ("tests.constants", "FlextOracleOicTestConstants"),
    "FlextOracleOicTestModels": ("tests.models", "FlextOracleOicTestModels"),
    "FlextOracleOicTestProtocols": ("tests.protocols", "FlextOracleOicTestProtocols"),
    "FlextOracleOicTestTypes": ("tests.typings", "FlextOracleOicTestTypes"),
    "FlextOracleOicTestUtilities": ("tests.utilities", "FlextOracleOicTestUtilities"),
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
    "c": ("tests.constants", "FlextOracleOicTestConstants"),
    "d": ("flext_tests", "d"),
    "e": ("flext_tests", "e"),
    "h": ("flext_tests", "h"),
    "m": ("tests.models", "FlextOracleOicTestModels"),
    "p": ("tests.protocols", "FlextOracleOicTestProtocols"),
    "r": ("flext_tests", "r"),
    "s": ("flext_tests", "s"),
    "t": ("tests.typings", "FlextOracleOicTestTypes"),
    "test_basic_import": ("tests.test_import", "test_basic_import"),
    "test_config_import": ("tests.test_import", "test_config_import"),
    "test_version_info_tuple": ("tests.unit.test_version", "test_version_info_tuple"),
    "test_version_string": ("tests.unit.test_version", "test_version_string"),
    "u": ("tests.utilities", "FlextOracleOicTestUtilities"),
    "unit": ("tests.unit", ""),
    "x": ("flext_tests", "x"),
}

__all__ = [
    "FlextOracleOicTestConstants",
    "FlextOracleOicTestModels",
    "FlextOracleOicTestProtocols",
    "FlextOracleOicTestTypes",
    "FlextOracleOicTestUtilities",
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
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "test_basic_import",
    "test_config_import",
    "test_version_info_tuple",
    "test_version_string",
    "u",
    "unit",
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
