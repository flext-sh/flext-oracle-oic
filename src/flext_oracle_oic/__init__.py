# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext oracle oic package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_oracle_oic.__version__ import *

if _t.TYPE_CHECKING:
    import flext_oracle_oic._utilities as _flext_oracle_oic__utilities

    _utilities = _flext_oracle_oic__utilities
    import flext_oracle_oic.api as _flext_oracle_oic_api
    from flext_oracle_oic._utilities import (
        FlextOracleOicUtilitiesAPIRequestBuilder,
        FlextOracleOicUtilitiesAuthenticationValidation,
        FlextOracleOicUtilitiesConnectionValidation,
        FlextOracleOicUtilitiesMonitoring,
        FlextOracleOicUtilitiesOracleOic,
        FlextOracleOicUtilitiesPatternAnalysis,
    )

    api = _flext_oracle_oic_api
    import flext_oracle_oic.constants as _flext_oracle_oic_constants
    from flext_oracle_oic.api import FlextOracleOicApi

    constants = _flext_oracle_oic_constants
    import flext_oracle_oic.ext_client as _flext_oracle_oic_ext_client
    from flext_oracle_oic.constants import (
        FlextOracleOicConstants,
        FlextOracleOicConstants as c,
    )

    ext_client = _flext_oracle_oic_ext_client
    import flext_oracle_oic.models as _flext_oracle_oic_models
    from flext_oracle_oic.ext_client import FlextOracleOicClient
    from flext_oracle_oic.main import FlextOracleOicCli, main

    models = _flext_oracle_oic_models
    import flext_oracle_oic.protocols as _flext_oracle_oic_protocols
    from flext_oracle_oic.models import FlextOracleOicModels, FlextOracleOicModels as m

    protocols = _flext_oracle_oic_protocols
    import flext_oracle_oic.service as _flext_oracle_oic_service
    from flext_oracle_oic.protocols import (
        FlextOracleOicProtocols,
        FlextOracleOicProtocols as p,
    )

    service = _flext_oracle_oic_service
    import flext_oracle_oic.settings as _flext_oracle_oic_settings
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

    settings = _flext_oracle_oic_settings
    import flext_oracle_oic.typings as _flext_oracle_oic_typings
    from flext_oracle_oic.settings import FlextOracleOicSettings

    typings = _flext_oracle_oic_typings
    import flext_oracle_oic.utilities as _flext_oracle_oic_utilities
    from flext_oracle_oic.typings import FlextOracleOicTypes, FlextOracleOicTypes as t

    utilities = _flext_oracle_oic_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_oracle_oic.utilities import (
        FlextOracleOicUtilities,
        FlextOracleOicUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("flext_oracle_oic._utilities",),
    {
        "FlextOracleOicApi": ("flext_oracle_oic.api", "FlextOracleOicApi"),
        "FlextOracleOicAuthMixin": (
            "flext_oracle_oic.services.auth",
            "FlextOracleOicAuthMixin",
        ),
        "FlextOracleOicCli": ("flext_oracle_oic.main", "FlextOracleOicCli"),
        "FlextOracleOicClient": ("flext_oracle_oic.ext_client", "FlextOracleOicClient"),
        "FlextOracleOicConstants": (
            "flext_oracle_oic.constants",
            "FlextOracleOicConstants",
        ),
        "FlextOracleOicIntegrationCrudMixin": (
            "flext_oracle_oic.services.integration_crud",
            "FlextOracleOicIntegrationCrudMixin",
        ),
        "FlextOracleOicIntegrationLifecycleMixin": (
            "flext_oracle_oic.services.integration_lifecycle",
            "FlextOracleOicIntegrationLifecycleMixin",
        ),
        "FlextOracleOicIntegrationPatternsMixin": (
            "flext_oracle_oic.services.integration_patterns",
            "FlextOracleOicIntegrationPatternsMixin",
        ),
        "FlextOracleOicModels": ("flext_oracle_oic.models", "FlextOracleOicModels"),
        "FlextOracleOicMonitoringMixin": (
            "flext_oracle_oic.services.monitoring",
            "FlextOracleOicMonitoringMixin",
        ),
        "FlextOracleOicOrchestrationMixin": (
            "flext_oracle_oic.services.orchestration",
            "FlextOracleOicOrchestrationMixin",
        ),
        "FlextOracleOicProtocols": (
            "flext_oracle_oic.protocols",
            "FlextOracleOicProtocols",
        ),
        "FlextOracleOicService": ("flext_oracle_oic.service", "FlextOracleOicService"),
        "FlextOracleOicServiceBase": (
            "flext_oracle_oic.services.base",
            "FlextOracleOicServiceBase",
        ),
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
        "_utilities": "flext_oracle_oic._utilities",
        "api": "flext_oracle_oic.api",
        "c": ("flext_oracle_oic.constants", "FlextOracleOicConstants"),
        "constants": "flext_oracle_oic.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "ext_client": "flext_oracle_oic.ext_client",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("flext_oracle_oic.models", "FlextOracleOicModels"),
        "main": ("flext_oracle_oic.main", "main"),
        "models": "flext_oracle_oic.models",
        "p": ("flext_oracle_oic.protocols", "FlextOracleOicProtocols"),
        "protocols": "flext_oracle_oic.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_oracle_oic.services.base", "FlextOracleOicServiceBase"),
        "service": "flext_oracle_oic.service",
        "settings": "flext_oracle_oic.settings",
        "t": ("flext_oracle_oic.typings", "FlextOracleOicTypes"),
        "typings": "flext_oracle_oic.typings",
        "u": ("flext_oracle_oic.utilities", "FlextOracleOicUtilities"),
        "utilities": "flext_oracle_oic.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)
_ = _LAZY_IMPORTS.pop("cleanup_submodule_namespace", None)
_ = _LAZY_IMPORTS.pop("install_lazy_exports", None)
_ = _LAZY_IMPORTS.pop("lazy_getattr", None)
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
    "_utilities",
    "api",
    "c",
    "constants",
    "d",
    "e",
    "ext_client",
    "h",
    "m",
    "main",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "service",
    "settings",
    "t",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
