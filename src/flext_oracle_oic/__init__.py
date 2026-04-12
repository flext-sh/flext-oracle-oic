# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if _t.TYPE_CHECKING:
    from flext_core import d, e, h, r, x
    from flext_oracle_oic._utilities.api_request_builder import (
        FlextOracleOicUtilitiesAPIRequestBuilder,
    )
    from flext_oracle_oic._utilities.authentication_validation import (
        FlextOracleOicUtilitiesAuthenticationValidation,
    )
    from flext_oracle_oic._utilities.connection_validation import (
        FlextOracleOicUtilitiesConnectionValidation,
    )
    from flext_oracle_oic._utilities.monitoring import FlextOracleOicUtilitiesMonitoring
    from flext_oracle_oic._utilities.oracle_oic import FlextOracleOicUtilitiesOracleOic
    from flext_oracle_oic._utilities.pattern_analysis import (
        FlextOracleOicUtilitiesPatternAnalysis,
    )
    from flext_oracle_oic.api import FlextOracleOicApi, oracle_oic
    from flext_oracle_oic.constants import FlextOracleOicConstants, c
    from flext_oracle_oic.ext_client import FlextOracleOicClient
    from flext_oracle_oic.main import FlextOracleOicCli, main
    from flext_oracle_oic.models import FlextOracleOicModels, m
    from flext_oracle_oic.protocols import FlextOracleOicProtocols, p
    from flext_oracle_oic.service import FlextOracleOicService, s
    from flext_oracle_oic.services.auth import FlextOracleOicAuthMixin
    from flext_oracle_oic.services.base import FlextOracleOicServiceBase
    from flext_oracle_oic.services.integration_crud import (
        FlextOracleOicIntegrationCrudMixin,
    )
    from flext_oracle_oic.services.integration_lifecycle import (
        FlextOracleOicIntegrationLifecycleMixin,
    )
    from flext_oracle_oic.services.integration_patterns import (
        FlextOracleOicIntegrationPatternsMixin,
    )
    from flext_oracle_oic.services.monitoring import FlextOracleOicMonitoringMixin
    from flext_oracle_oic.services.orchestration import FlextOracleOicOrchestrationMixin
    from flext_oracle_oic.settings import FlextOracleOicSettings
    from flext_oracle_oic.typings import FlextOracleOicTypes, t
    from flext_oracle_oic.utilities import FlextOracleOicUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    (
        "._utilities",
        ".services",
    ),
    build_lazy_import_map(
        {
            ".api": (
                "FlextOracleOicApi",
                "oracle_oic",
            ),
            ".constants": (
                "FlextOracleOicConstants",
                "c",
            ),
            ".ext_client": ("FlextOracleOicClient",),
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
            ".settings": ("FlextOracleOicSettings",),
            ".typings": (
                "FlextOracleOicTypes",
                "t",
            ),
            ".utilities": (
                "FlextOracleOicUtilities",
                "u",
            ),
            "flext_core": (
                "d",
                "e",
                "h",
                "r",
                "x",
            ),
        },
    ),
    exclude_names=(
        "FlextDispatcher",
        "FlextLogger",
        "FlextRegistry",
        "FlextRuntime",
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
    ),
    module_name=__name__,
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "FlextOracleOicApi",
    "FlextOracleOicAuthMixin",
    "FlextOracleOicCli",
    "FlextOracleOicClient",
    "FlextOracleOicConstants",
    "FlextOracleOicIntegrationCrudMixin",
    "FlextOracleOicIntegrationLifecycleMixin",
    "FlextOracleOicIntegrationPatternsMixin",
    "FlextOracleOicModels",
    "FlextOracleOicMonitoringMixin",
    "FlextOracleOicOrchestrationMixin",
    "FlextOracleOicProtocols",
    "FlextOracleOicService",
    "FlextOracleOicServiceBase",
    "FlextOracleOicSettings",
    "FlextOracleOicTypes",
    "FlextOracleOicUtilities",
    "FlextOracleOicUtilitiesAPIRequestBuilder",
    "FlextOracleOicUtilitiesAuthenticationValidation",
    "FlextOracleOicUtilitiesConnectionValidation",
    "FlextOracleOicUtilitiesMonitoring",
    "FlextOracleOicUtilitiesOracleOic",
    "FlextOracleOicUtilitiesPatternAnalysis",
    "c",
    "d",
    "e",
    "h",
    "m",
    "main",
    "oracle_oic",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]
