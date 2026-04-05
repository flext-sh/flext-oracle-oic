# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

if _t.TYPE_CHECKING:
    import tests.conftest as _tests_conftest

    conftest = _tests_conftest
    import tests.constants as _tests_constants
    from tests.conftest import pytest_plugins

    constants = _tests_constants
    import tests.models as _tests_models
    from tests.constants import (
        FlextOracleOicTestConstants,
        FlextOracleOicTestConstants as c,
    )

    models = _tests_models
    import tests.protocols as _tests_protocols
    from tests.models import FlextOracleOicTestModels, FlextOracleOicTestModels as m

    protocols = _tests_protocols
    import tests.test_basic as _tests_test_basic
    from tests.protocols import (
        FlextOracleOicTestProtocols,
        FlextOracleOicTestProtocols as p,
    )

    test_basic = _tests_test_basic
    import tests.test_cli as _tests_test_cli
    from tests.test_basic import TestBasicFunctionality

    test_cli = _tests_test_cli
    import tests.test_config as _tests_test_config
    from tests.test_cli import TestCLI

    test_config = _tests_test_config
    import tests.test_ext_client as _tests_test_ext_client
    from tests.test_config import TestFlextOracleOicSettings

    test_ext_client = _tests_test_ext_client
    import tests.test_ext_services as _tests_test_ext_services

    test_ext_services = _tests_test_ext_services
    import tests.test_extension as _tests_test_extension

    test_extension = _tests_test_extension
    import tests.test_import as _tests_test_import
    from tests.test_extension import TestOracleOicExtension

    test_import = _tests_test_import
    import tests.test_main as _tests_test_main
    from tests.test_import import test_basic_import, test_config_import

    test_main = _tests_test_main
    import tests.test_models as _tests_test_models
    from tests.test_main import TestMainFunction, TestMainModule

    test_models = _tests_test_models
    import tests.test_typings as _tests_test_typings
    from tests.test_models import (
        TestOICAuthConfig,
        TestOICConnectionConfig,
        TestOICConnectionInfo,
        TestOICIntegrationInfo,
    )

    test_typings = _tests_test_typings
    import tests.typings as _tests_typings
    from tests.test_typings import TestFlextTypes

    typings = _tests_typings
    import tests.unit as _tests_unit
    from tests.typings import FlextOracleOicTestTypes, FlextOracleOicTestTypes as t

    unit = _tests_unit
    import tests.utilities as _tests_utilities
    from tests.unit import test_version, test_version_info_tuple, test_version_string

    utilities = _tests_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests.utilities import (
        FlextOracleOicTestUtilities,
        FlextOracleOicTestUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("tests.unit",),
    {
        "FlextOracleOicTestConstants": "tests.constants",
        "FlextOracleOicTestModels": "tests.models",
        "FlextOracleOicTestProtocols": "tests.protocols",
        "FlextOracleOicTestTypes": "tests.typings",
        "FlextOracleOicTestUtilities": "tests.utilities",
        "TestBasicFunctionality": "tests.test_basic",
        "TestCLI": "tests.test_cli",
        "TestFlextOracleOicSettings": "tests.test_config",
        "TestFlextTypes": "tests.test_typings",
        "TestMainFunction": "tests.test_main",
        "TestMainModule": "tests.test_main",
        "TestOICAuthConfig": "tests.test_models",
        "TestOICConnectionConfig": "tests.test_models",
        "TestOICConnectionInfo": "tests.test_models",
        "TestOICIntegrationInfo": "tests.test_models",
        "TestOracleOicExtension": "tests.test_extension",
        "c": ("tests.constants", "FlextOracleOicTestConstants"),
        "conftest": "tests.conftest",
        "constants": "tests.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("tests.models", "FlextOracleOicTestModels"),
        "models": "tests.models",
        "p": ("tests.protocols", "FlextOracleOicTestProtocols"),
        "protocols": "tests.protocols",
        "pytest_plugins": "tests.conftest",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "t": ("tests.typings", "FlextOracleOicTestTypes"),
        "test_basic": "tests.test_basic",
        "test_basic_import": "tests.test_import",
        "test_cli": "tests.test_cli",
        "test_config": "tests.test_config",
        "test_config_import": "tests.test_import",
        "test_ext_client": "tests.test_ext_client",
        "test_ext_services": "tests.test_ext_services",
        "test_extension": "tests.test_extension",
        "test_import": "tests.test_import",
        "test_main": "tests.test_main",
        "test_models": "tests.test_models",
        "test_typings": "tests.test_typings",
        "typings": "tests.typings",
        "u": ("tests.utilities", "FlextOracleOicTestUtilities"),
        "unit": "tests.unit",
        "utilities": "tests.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)

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
    "conftest",
    "constants",
    "d",
    "e",
    "h",
    "m",
    "models",
    "p",
    "protocols",
    "pytest_plugins",
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
