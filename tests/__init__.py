# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_tests import d, e, h, r, s, x

    from tests.constants import *
    from tests.models import *
    from tests.protocols import *
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
    from tests.typings import *
    from tests.unit import *
    from tests.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = merge_lazy_imports(
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
        "constants": "tests.constants",
        "d": "flext_tests",
        "e": "flext_tests",
        "h": "flext_tests",
        "m": ("tests.models", "FlextOracleOicTestModels"),
        "models": "tests.models",
        "p": ("tests.protocols", "FlextOracleOicTestProtocols"),
        "protocols": "tests.protocols",
        "r": "flext_tests",
        "s": "flext_tests",
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
        "x": "flext_tests",
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
