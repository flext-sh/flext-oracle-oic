# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if _t.TYPE_CHECKING:
    from flext_oracle_oic.test_basic import TestBasicFunctionality
    from flext_oracle_oic.test_cli import TestCLI
    from flext_oracle_oic.test_config import TestFlextOracleOicSettings
    from flext_oracle_oic.test_extension import TestOracleOicExtension
    from flext_oracle_oic.test_import import test_basic_import, test_config_import
    from flext_oracle_oic.test_main import TestMainFunction, TestMainModule
    from flext_oracle_oic.test_models import (
        TestOICAuthConfig,
        TestOICConnectionConfig,
        TestOICConnectionInfo,
        TestOICIntegrationInfo,
    )
    from flext_oracle_oic.test_typings import TestFlextTypes
    from flext_oracle_oic.test_version import (
        test_version_info_tuple,
        test_version_string,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_basic": ("TestBasicFunctionality",),
        ".test_cli": ("TestCLI",),
        ".test_config": ("TestFlextOracleOicSettings",),
        ".test_extension": ("TestOracleOicExtension",),
        ".test_import": (
            "test_basic_import",
            "test_config_import",
        ),
        ".test_main": (
            "TestMainFunction",
            "TestMainModule",
        ),
        ".test_models": (
            "TestOICAuthConfig",
            "TestOICConnectionConfig",
            "TestOICConnectionInfo",
            "TestOICIntegrationInfo",
        ),
        ".test_typings": ("TestFlextTypes",),
        ".test_version": (
            "test_version_info_tuple",
            "test_version_string",
        ),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

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
    "test_basic_import",
    "test_config_import",
    "test_version_info_tuple",
    "test_version_string",
]
