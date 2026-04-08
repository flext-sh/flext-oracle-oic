# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
from flext_oracle_oic.__version__ import *

if _t.TYPE_CHECKING:
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
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
    from flext_oracle_oic.api import FlextOracleOicApi
    from flext_oracle_oic.constants import (
        FlextOracleOicConstants,
        FlextOracleOicConstants as c,
    )
    from flext_oracle_oic.ext_client import FlextOracleOicClient
    from flext_oracle_oic.main import FlextOracleOicCli, main
    from flext_oracle_oic.models import FlextOracleOicModels, FlextOracleOicModels as m
    from flext_oracle_oic.protocols import (
        FlextOracleOicProtocols,
        FlextOracleOicProtocols as p,
    )
    from flext_oracle_oic.service import FlextOracleOicService
    from flext_oracle_oic.services.auth import FlextOracleOicAuthMixin
    from flext_oracle_oic.services.base import (
        FlextOracleOicServiceBase,
        FlextOracleOicServiceBase as s,
    )
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
    from flext_oracle_oic.typings import FlextOracleOicTypes, FlextOracleOicTypes as t
    from flext_oracle_oic.utilities import (
        FlextOracleOicUtilities,
        FlextOracleOicUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    (
        "._utilities",
        ".services",
    ),
    build_lazy_import_map(
        {
            ".__version__": (
                "__author__",
                "__author_email__",
                "__description__",
                "__license__",
                "__title__",
                "__url__",
                "__version__",
                "__version_info__",
            ),
            ".api": ("FlextOracleOicApi",),
            ".constants": ("FlextOracleOicConstants",),
            ".ext_client": ("FlextOracleOicClient",),
            ".main": (
                "FlextOracleOicCli",
                "main",
            ),
            ".models": ("FlextOracleOicModels",),
            ".protocols": ("FlextOracleOicProtocols",),
            ".service": ("FlextOracleOicService",),
            ".settings": ("FlextOracleOicSettings",),
            ".typings": ("FlextOracleOicTypes",),
            ".utilities": ("FlextOracleOicUtilities",),
        },
        alias_groups={
            ".constants": (("c", "FlextOracleOicConstants"),),
            ".models": (("m", "FlextOracleOicModels"),),
            ".protocols": (("p", "FlextOracleOicProtocols"),),
            ".typings": (("t", "FlextOracleOicTypes"),),
            ".utilities": (("u", "FlextOracleOicUtilities"),),
            "flext_core.decorators": (("d", "FlextDecorators"),),
            "flext_core.exceptions": (("e", "FlextExceptions"),),
            "flext_core.handlers": (("h", "FlextHandlers"),),
            "flext_core.mixins": (("x", "FlextMixins"),),
            "flext_core.result": (("r", "FlextResult"),),
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
    ),
    module_name=__name__,
)

__all__ = [
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
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "d",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
