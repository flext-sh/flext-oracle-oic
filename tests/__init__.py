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
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_oracle_oic import (
        constants,
        models,
        protocols,
        test_basic,
        test_cli,
        test_config,
        test_ext_client,
        test_ext_services,
        test_extension,
        test_import,
        test_main,
        test_models,
        test_typings,
        test_version,
        typings,
        unit,
        utilities,
    )
    from flext_oracle_oic.constants import (
        FlextOracleOicTestConstants,
        FlextOracleOicTestConstants as c,
    )
    from flext_oracle_oic.models import (
        FlextOracleOicTestModels,
        FlextOracleOicTestModels as m,
    )
    from flext_oracle_oic.protocols import (
        FlextOracleOicTestProtocols,
        FlextOracleOicTestProtocols as p,
    )
    from flext_oracle_oic.test_basic import TestBasicFunctionality
    from flext_oracle_oic.test_cli import TestCLI
    from flext_oracle_oic.test_config import TestFlextOracleOicSettings
    from flext_oracle_oic.test_extension import TestOracleOicExtension
    from flext_oracle_oic.test_import import test_basic_import
    from flext_oracle_oic.test_main import TestMainFunction
    from flext_oracle_oic.test_models import TestOICAuthConfig
    from flext_oracle_oic.test_typings import TestFlextTypes
    from flext_oracle_oic.typings import (
        FlextOracleOicTestTypes,
        FlextOracleOicTestTypes as t,
    )
    from flext_oracle_oic.unit import test_version_string
    from flext_oracle_oic.utilities import (
        FlextOracleOicTestUtilities,
        FlextOracleOicTestUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
    ("flext_oracle_oic.unit",),
    {
        "FlextOracleOicTestConstants": "flext_oracle_oic.constants",
        "FlextOracleOicTestModels": "flext_oracle_oic.models",
        "FlextOracleOicTestProtocols": "flext_oracle_oic.protocols",
        "FlextOracleOicTestTypes": "flext_oracle_oic.typings",
        "FlextOracleOicTestUtilities": "flext_oracle_oic.utilities",
        "TestBasicFunctionality": "flext_oracle_oic.test_basic",
        "TestCLI": "flext_oracle_oic.test_cli",
        "TestFlextOracleOicSettings": "flext_oracle_oic.test_config",
        "TestFlextTypes": "flext_oracle_oic.test_typings",
        "TestMainFunction": "flext_oracle_oic.test_main",
        "TestOICAuthConfig": "flext_oracle_oic.test_models",
        "TestOracleOicExtension": "flext_oracle_oic.test_extension",
        "c": ("flext_oracle_oic.constants", "FlextOracleOicTestConstants"),
        "constants": "flext_oracle_oic.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("flext_oracle_oic.models", "FlextOracleOicTestModels"),
        "models": "flext_oracle_oic.models",
        "p": ("flext_oracle_oic.protocols", "FlextOracleOicTestProtocols"),
        "protocols": "flext_oracle_oic.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "t": ("flext_oracle_oic.typings", "FlextOracleOicTestTypes"),
        "test_basic": "flext_oracle_oic.test_basic",
        "test_basic_import": "flext_oracle_oic.test_import",
        "test_cli": "flext_oracle_oic.test_cli",
        "test_config": "flext_oracle_oic.test_config",
        "test_ext_client": "flext_oracle_oic.test_ext_client",
        "test_ext_services": "flext_oracle_oic.test_ext_services",
        "test_extension": "flext_oracle_oic.test_extension",
        "test_import": "flext_oracle_oic.test_import",
        "test_main": "flext_oracle_oic.test_main",
        "test_models": "flext_oracle_oic.test_models",
        "test_typings": "flext_oracle_oic.test_typings",
        "test_version": "flext_oracle_oic.test_version",
        "typings": "flext_oracle_oic.typings",
        "u": ("flext_oracle_oic.utilities", "FlextOracleOicTestUtilities"),
        "unit": "flext_oracle_oic.unit",
        "utilities": "flext_oracle_oic.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
