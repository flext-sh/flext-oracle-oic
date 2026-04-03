# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext oracle oic package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_oracle_oic.__version__ import __all__, __version_info__

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_oracle_oic import (
        _utilities,
        api,
        api_request_builder,
        auth,
        authentication_validation,
        base,
        connection_validation,
        constants,
        ext_client,
        integration_crud,
        integration_lifecycle,
        integration_patterns,
        main,
        models,
        monitoring,
        oracle_oic,
        orchestration,
        pattern_analysis,
        protocols,
        service,
        services,
        settings,
        typings,
        utilities,
    )
    from flext_oracle_oic._utilities import (
        FlextOracleOicUtilitiesAPIRequestBuilder,
        FlextOracleOicUtilitiesAuthenticationValidation,
        FlextOracleOicUtilitiesConnectionValidation,
        FlextOracleOicUtilitiesMonitoring,
        FlextOracleOicUtilitiesOracleOic,
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
    from flext_oracle_oic.services import (
        FlextOracleOicAuthMixin,
        FlextOracleOicIntegrationCrudMixin,
        FlextOracleOicIntegrationLifecycleMixin,
        FlextOracleOicIntegrationPatternsMixin,
        FlextOracleOicMonitoringMixin,
        FlextOracleOicOrchestrationMixin,
        FlextOracleOicServiceBase,
    )
    from flext_oracle_oic.settings import FlextOracleOicSettings
    from flext_oracle_oic.typings import FlextOracleOicTypes, FlextOracleOicTypes as t
    from flext_oracle_oic.utilities import (
        FlextOracleOicUtilities,
        FlextOracleOicUtilities as u,
    )

__author__ = "FLEXT Team"
__author_email__ = ""
__description__ = "Oracle OIC Extension for FLEXT ecosystem"
__license__ = "MIT"
__title__ = "flext-oracle-oic"
__url__ = ""
__version__ = "0.9.9"


_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
    (
        "flext_oracle_oic._utilities",
        "flext_oracle_oic.services",
    ),
    {
        "FlextOracleOicApi": "flext_oracle_oic.api",
        "FlextOracleOicCli": "flext_oracle_oic.main",
        "FlextOracleOicClient": "flext_oracle_oic.ext_client",
        "FlextOracleOicConstants": "flext_oracle_oic.constants",
        "FlextOracleOicModels": "flext_oracle_oic.models",
        "FlextOracleOicProtocols": "flext_oracle_oic.protocols",
        "FlextOracleOicService": "flext_oracle_oic.service",
        "FlextOracleOicSettings": "flext_oracle_oic.settings",
        "FlextOracleOicTypes": "flext_oracle_oic.typings",
        "FlextOracleOicUtilities": "flext_oracle_oic.utilities",
        "_utilities": "flext_oracle_oic._utilities",
        "api": "flext_oracle_oic.api",
        "api_request_builder": "flext_oracle_oic.api_request_builder",
        "auth": "flext_oracle_oic.auth",
        "authentication_validation": "flext_oracle_oic.authentication_validation",
        "base": "flext_oracle_oic.base",
        "c": ("flext_oracle_oic.constants", "FlextOracleOicConstants"),
        "connection_validation": "flext_oracle_oic.connection_validation",
        "constants": "flext_oracle_oic.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "ext_client": "flext_oracle_oic.ext_client",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "integration_crud": "flext_oracle_oic.integration_crud",
        "integration_lifecycle": "flext_oracle_oic.integration_lifecycle",
        "integration_patterns": "flext_oracle_oic.integration_patterns",
        "m": ("flext_oracle_oic.models", "FlextOracleOicModels"),
        "main": "flext_oracle_oic.main",
        "models": "flext_oracle_oic.models",
        "monitoring": "flext_oracle_oic.monitoring",
        "oracle_oic": "flext_oracle_oic.oracle_oic",
        "orchestration": "flext_oracle_oic.orchestration",
        "p": ("flext_oracle_oic.protocols", "FlextOracleOicProtocols"),
        "pattern_analysis": "flext_oracle_oic.pattern_analysis",
        "protocols": "flext_oracle_oic.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "service": "flext_oracle_oic.service",
        "services": "flext_oracle_oic.services",
        "settings": "flext_oracle_oic.settings",
        "t": ("flext_oracle_oic.typings", "FlextOracleOicTypes"),
        "typings": "flext_oracle_oic.typings",
        "u": ("flext_oracle_oic.utilities", "FlextOracleOicUtilities"),
        "utilities": "flext_oracle_oic.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__all__",
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
        "__version__",
        "__version_info__",
    ],
)
