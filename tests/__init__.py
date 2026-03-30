# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from tests import (
        constants as constants,
        models as models,
        protocols as protocols,
        test_basic as test_basic,
        test_cli as test_cli,
        test_config as test_config,
        test_ext_client as test_ext_client,
        test_ext_services as test_ext_services,
        test_extension as test_extension,
        test_import as test_import,
        test_main as test_main,
        test_models as test_models,
        test_typings as test_typings,
        typings as typings,
        unit as unit,
        utilities as utilities,
    )
    from tests.constants import (
        FlextOracleOicTestConstants as FlextOracleOicTestConstants,
        FlextOracleOicTestConstants as c,
    )
    from tests.models import (
        FlextOracleOicTestModels as FlextOracleOicTestModels,
        FlextOracleOicTestModels as m,
    )
    from tests.protocols import (
        FlextOracleOicTestProtocols as FlextOracleOicTestProtocols,
        FlextOracleOicTestProtocols as p,
    )
    from tests.test_basic import TestBasicFunctionality as TestBasicFunctionality
    from tests.test_cli import TestCLI as TestCLI
    from tests.test_config import (
        TestFlextOracleOicSettings as TestFlextOracleOicSettings,
    )
    from tests.test_extension import TestOracleOicExtension as TestOracleOicExtension
    from tests.test_import import (
        test_basic_import as test_basic_import,
        test_config_import as test_config_import,
    )
    from tests.test_main import (
        TestMainFunction as TestMainFunction,
        TestMainModule as TestMainModule,
    )
    from tests.test_models import (
        TestOICAuthConfig as TestOICAuthConfig,
        TestOICConnectionConfig as TestOICConnectionConfig,
        TestOICConnectionInfo as TestOICConnectionInfo,
        TestOICIntegrationInfo as TestOICIntegrationInfo,
    )
    from tests.test_typings import TestFlextTypes as TestFlextTypes
    from tests.typings import (
        FlextOracleOicTestTypes as FlextOracleOicTestTypes,
        FlextOracleOicTestTypes as t,
    )
    from tests.unit import test_version as test_version
    from tests.unit.test_version import (
        test_version_info_tuple as test_version_info_tuple,
        test_version_string as test_version_string,
    )
    from tests.utilities import (
        FlextOracleOicTestUtilities as FlextOracleOicTestUtilities,
        FlextOracleOicTestUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextOracleOicTestConstants": ["tests.constants", "FlextOracleOicTestConstants"],
    "FlextOracleOicTestModels": ["tests.models", "FlextOracleOicTestModels"],
    "FlextOracleOicTestProtocols": ["tests.protocols", "FlextOracleOicTestProtocols"],
    "FlextOracleOicTestTypes": ["tests.typings", "FlextOracleOicTestTypes"],
    "FlextOracleOicTestUtilities": ["tests.utilities", "FlextOracleOicTestUtilities"],
    "TestBasicFunctionality": ["tests.test_basic", "TestBasicFunctionality"],
    "TestCLI": ["tests.test_cli", "TestCLI"],
    "TestFlextOracleOicSettings": ["tests.test_config", "TestFlextOracleOicSettings"],
    "TestFlextTypes": ["tests.test_typings", "TestFlextTypes"],
    "TestMainFunction": ["tests.test_main", "TestMainFunction"],
    "TestMainModule": ["tests.test_main", "TestMainModule"],
    "TestOICAuthConfig": ["tests.test_models", "TestOICAuthConfig"],
    "TestOICConnectionConfig": ["tests.test_models", "TestOICConnectionConfig"],
    "TestOICConnectionInfo": ["tests.test_models", "TestOICConnectionInfo"],
    "TestOICIntegrationInfo": ["tests.test_models", "TestOICIntegrationInfo"],
    "TestOracleOicExtension": ["tests.test_extension", "TestOracleOicExtension"],
    "c": ["tests.constants", "FlextOracleOicTestConstants"],
    "constants": ["tests.constants", ""],
    "d": ["flext_tests", "d"],
    "e": ["flext_tests", "e"],
    "h": ["flext_tests", "h"],
    "m": ["tests.models", "FlextOracleOicTestModels"],
    "models": ["tests.models", ""],
    "p": ["tests.protocols", "FlextOracleOicTestProtocols"],
    "protocols": ["tests.protocols", ""],
    "r": ["flext_tests", "r"],
    "s": ["flext_tests", "s"],
    "t": ["tests.typings", "FlextOracleOicTestTypes"],
    "test_basic": ["tests.test_basic", ""],
    "test_basic_import": ["tests.test_import", "test_basic_import"],
    "test_cli": ["tests.test_cli", ""],
    "test_config": ["tests.test_config", ""],
    "test_config_import": ["tests.test_import", "test_config_import"],
    "test_ext_client": ["tests.test_ext_client", ""],
    "test_ext_services": ["tests.test_ext_services", ""],
    "test_extension": ["tests.test_extension", ""],
    "test_import": ["tests.test_import", ""],
    "test_main": ["tests.test_main", ""],
    "test_models": ["tests.test_models", ""],
    "test_typings": ["tests.test_typings", ""],
    "test_version": ["tests.unit.test_version", ""],
    "test_version_info_tuple": ["tests.unit.test_version", "test_version_info_tuple"],
    "test_version_string": ["tests.unit.test_version", "test_version_string"],
    "typings": ["tests.typings", ""],
    "u": ["tests.utilities", "FlextOracleOicTestUtilities"],
    "unit": ["tests.unit", ""],
    "utilities": ["tests.utilities", ""],
    "x": ["flext_tests", "x"],
}

_EXPORTS: Sequence[str] = [
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
    "test_basic_import",
    "test_cli",
    "test_config",
    "test_config_import",
    "test_ext_client",
    "test_ext_services",
    "test_extension",
    "test_import",
    "test_main",
    "test_models",
    "test_typings",
    "test_version",
    "test_version_info_tuple",
    "test_version_string",
    "typings",
    "u",
    "unit",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
