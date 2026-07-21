# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
from flext_oracle_oic.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if TYPE_CHECKING:
    from flext_auth import d as d, e as e, h as h, r as r, x as x
    from flext_oracle_oic._config import (
        FlextOracleOicConfig as FlextOracleOicConfig,
        config as config,
    )
    from flext_oracle_oic._settings import (
        FlextOracleOicSettings as FlextOracleOicSettings,
        settings as settings,
    )
    from flext_oracle_oic.api import (
        FlextOracleOicApi as FlextOracleOicApi,
        oracle_oic as oracle_oic,
    )
    from flext_oracle_oic.constants import (
        FlextOracleOicConstants as FlextOracleOicConstants,
        c as c,
    )
    from flext_oracle_oic.main import (
        FlextOracleOicCli as FlextOracleOicCli,
        main as main,
    )
    from flext_oracle_oic.models import (
        FlextOracleOicModels as FlextOracleOicModels,
        m as m,
    )
    from flext_oracle_oic.protocols import (
        FlextOracleOicProtocols as FlextOracleOicProtocols,
        p,
    )
    from flext_oracle_oic.service import (
        FlextOracleOicService as FlextOracleOicService,
        s as s,
    )
    from flext_oracle_oic.services.auth import (
        FlextOracleOicAuthMixin as FlextOracleOicAuthMixin,
    )
    from flext_oracle_oic.services.base import (
        FlextOracleOicServiceBase as FlextOracleOicServiceBase,
    )
    from flext_oracle_oic.services.integration_crud import (
        FlextOracleOicIntegrationCrudMixin as FlextOracleOicIntegrationCrudMixin,
    )
    from flext_oracle_oic.services.integration_lifecycle import (
        FlextOracleOicIntegrationLifecycleMixin as FlextOracleOicIntegrationLifecycleMixin,
    )
    from flext_oracle_oic.services.monitoring import (
        FlextOracleOicMonitoringMixin as FlextOracleOicMonitoringMixin,
    )
    from flext_oracle_oic.services.orchestration import (
        FlextOracleOicOrchestrationMixin as FlextOracleOicOrchestrationMixin,
    )
    from flext_oracle_oic.typings import (
        FlextOracleOicTypes as FlextOracleOicTypes,
        t as t,
    )
    from flext_oracle_oic.utilities import (
        FlextOracleOicUtilities as FlextOracleOicUtilities,
        u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    (".services",),
    build_lazy_import_map(
        {
            "._config": ("FlextOracleOicConfig", "config"),
            "._settings": ("FlextOracleOicSettings", "settings"),
            ".api": (
                "FlextOracleOicApi",
                "oracle_oic",
            ),
            ".constants": (
                "FlextOracleOicConstants",
                "c",
            ),
            ".main": (
                "FlextOracleOicCli",
                "main",
            ),
            ".models": (
                "FlextOracleOicModels",
                "m",
            ),
            ".protocols": (
                "FlextOracleOicProtocols",
                "p",
            ),
            ".service": (
                "FlextOracleOicService",
                "s",
            ),
            ".services.auth": ("FlextOracleOicAuthMixin",),
            ".services.base": ("FlextOracleOicServiceBase",),
            ".services.integration_crud": ("FlextOracleOicIntegrationCrudMixin",),
            ".services.integration_lifecycle": (
                "FlextOracleOicIntegrationLifecycleMixin",
            ),
            ".services.monitoring": ("FlextOracleOicMonitoringMixin",),
            ".services.orchestration": ("FlextOracleOicOrchestrationMixin",),
            ".typings": (
                "FlextOracleOicTypes",
                "t",
            ),
            ".utilities": (
                "FlextOracleOicUtilities",
                "u",
            ),
            "flext_auth": (
                "d",
                "e",
                "h",
                "r",
                "x",
            ),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
        "pytest_addoption",
        "pytest_collect_file",
        "pytest_collection_modifyitems",
        "pytest_configure",
        "pytest_runtest_setup",
        "pytest_runtest_teardown",
        "pytest_sessionfinish",
        "pytest_sessionstart",
        "pytest_terminal_summary",
        "pytest_warning_recorded",
    ),
    module_name=__name__,
)


__all__: tuple[str, ...] = (
    "FlextOracleOicApi",
    "FlextOracleOicAuthMixin",
    "FlextOracleOicCli",
    "FlextOracleOicConfig",
    "FlextOracleOicConstants",
    "FlextOracleOicIntegrationCrudMixin",
    "FlextOracleOicIntegrationLifecycleMixin",
    "FlextOracleOicModels",
    "FlextOracleOicMonitoringMixin",
    "FlextOracleOicOrchestrationMixin",
    "FlextOracleOicProtocols",
    "FlextOracleOicService",
    "FlextOracleOicServiceBase",
    "FlextOracleOicSettings",
    "FlextOracleOicTypes",
    "FlextOracleOicUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "config",
    "d",
    "e",
    "h",
    "m",
    "main",
    "oracle_oic",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "u",
    "x",
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    public_exports=__all__,
)
