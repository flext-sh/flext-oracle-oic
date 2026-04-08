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

    constants = _tests_constants
    import tests.models as _tests_models
    from tests.constants import (
        TestsFlextOracleOicConstants,
        TestsFlextOracleOicConstants as c,
    )

    models = _tests_models
    import tests.protocols as _tests_protocols
    from tests.models import TestsFlextOracleOicModels, TestsFlextOracleOicModels as m

    protocols = _tests_protocols
    import tests.test_basic as _tests_test_basic
    from tests.protocols import (
        TestsFlextOracleOicProtocols,
        TestsFlextOracleOicProtocols as p,
    )

    test_basic = _tests_test_basic
    import tests.test_cli as _tests_test_cli

    test_cli = _tests_test_cli
    import tests.test_config as _tests_test_config

    test_config = _tests_test_config
    import tests.test_ext_client as _tests_test_ext_client

    test_ext_client = _tests_test_ext_client
    import tests.test_ext_services as _tests_test_ext_services

    test_ext_services = _tests_test_ext_services
    import tests.test_extension as _tests_test_extension

    test_extension = _tests_test_extension
    import tests.test_import as _tests_test_import

    test_import = _tests_test_import
    import tests.test_main as _tests_test_main

    test_main = _tests_test_main
    import tests.test_models as _tests_test_models

    test_models = _tests_test_models
    import tests.test_typings as _tests_test_typings

    test_typings = _tests_test_typings
    import tests.typings as _tests_typings

    typings = _tests_typings
    import tests.unit as _tests_unit
    from tests.typings import TestsFlextOracleOicTypes, TestsFlextOracleOicTypes as t

    unit = _tests_unit
    import tests.utilities as _tests_utilities

    utilities = _tests_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
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
