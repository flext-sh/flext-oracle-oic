# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext oracle oic package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
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
    from flext_oracle_oic.main import FlextOracleOicCli
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
        "flext_oracle_oic._utilities",
        "flext_oracle_oic.services",
    ),
    {
        "FlextOracleOicApi": ("flext_oracle_oic.api", "FlextOracleOicApi"),
        "FlextOracleOicCli": ("flext_oracle_oic.main", "FlextOracleOicCli"),
        "FlextOracleOicClient": ("flext_oracle_oic.ext_client", "FlextOracleOicClient"),
        "FlextOracleOicConstants": (
            "flext_oracle_oic.constants",
            "FlextOracleOicConstants",
        ),
        "FlextOracleOicModels": ("flext_oracle_oic.models", "FlextOracleOicModels"),
        "FlextOracleOicProtocols": (
            "flext_oracle_oic.protocols",
            "FlextOracleOicProtocols",
        ),
        "FlextOracleOicService": ("flext_oracle_oic.service", "FlextOracleOicService"),
        "FlextOracleOicSettings": (
            "flext_oracle_oic.settings",
            "FlextOracleOicSettings",
        ),
        "FlextOracleOicTypes": ("flext_oracle_oic.typings", "FlextOracleOicTypes"),
        "FlextOracleOicUtilities": (
            "flext_oracle_oic.utilities",
            "FlextOracleOicUtilities",
        ),
        "__author__": ("flext_oracle_oic.__version__", "__author__"),
        "__author_email__": ("flext_oracle_oic.__version__", "__author_email__"),
        "__description__": ("flext_oracle_oic.__version__", "__description__"),
        "__license__": ("flext_oracle_oic.__version__", "__license__"),
        "__title__": ("flext_oracle_oic.__version__", "__title__"),
        "__url__": ("flext_oracle_oic.__version__", "__url__"),
        "__version__": ("flext_oracle_oic.__version__", "__version__"),
        "__version_info__": ("flext_oracle_oic.__version__", "__version_info__"),
        "c": ("flext_oracle_oic.constants", "FlextOracleOicConstants"),
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("flext_oracle_oic.models", "FlextOracleOicModels"),
        "p": ("flext_oracle_oic.protocols", "FlextOracleOicProtocols"),
        "r": ("flext_core.result", "FlextResult"),
        "t": ("flext_oracle_oic.typings", "FlextOracleOicTypes"),
        "u": ("flext_oracle_oic.utilities", "FlextOracleOicUtilities"),
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
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
