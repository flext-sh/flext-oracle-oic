# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_oic.tests.unit.test_basic import (
        TestsFlextOracleOicBasic as TestsFlextOracleOicBasic,
    )
    from flext_oracle_oic.tests.unit.test_cli import (
        TestsFlextOracleOicCli as TestsFlextOracleOicCli,
    )
    from flext_oracle_oic.tests.unit.test_config import (
        TestsFlextOracleOicConfig as TestsFlextOracleOicConfig,
    )
    from flext_oracle_oic.tests.unit.test_extension import (
        TestsFlextOracleOicExtension as TestsFlextOracleOicExtension,
    )
    from flext_oracle_oic.tests.unit.test_import import (
        TestsFlextOracleOicImport as TestsFlextOracleOicImport,
    )
    from flext_oracle_oic.tests.unit.test_main import (
        TestsFlextOracleOicMain as TestsFlextOracleOicMain,
    )
    from flext_oracle_oic.tests.unit.test_models import (
        TestsFlextOracleOicModelsUnit as TestsFlextOracleOicModelsUnit,
    )
    from flext_oracle_oic.tests.unit.test_typings import (
        TestsFlextOracleOicTypingsUnit as TestsFlextOracleOicTypingsUnit,
    )
    from flext_oracle_oic.tests.unit.test_version import (
        TestsFlextOracleOicVersion as TestsFlextOracleOicVersion,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_basic": ("TestsFlextOracleOicBasic",),
        ".test_cli": ("TestsFlextOracleOicCli",),
        ".test_config": ("TestsFlextOracleOicConfig",),
        ".test_ext_client": ("test_ext_client",),
        ".test_ext_services": ("test_ext_services",),
        ".test_extension": ("TestsFlextOracleOicExtension",),
        ".test_import": ("TestsFlextOracleOicImport",),
        ".test_main": ("TestsFlextOracleOicMain",),
        ".test_models": ("TestsFlextOracleOicModelsUnit",),
        ".test_typings": ("TestsFlextOracleOicTypingsUnit",),
        ".test_version": ("TestsFlextOracleOicVersion",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
