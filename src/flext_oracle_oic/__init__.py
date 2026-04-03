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

    _utilities = _flext_oracle_oic__utilities
    import flext_oracle_oic._utilities.api_request_builder as _flext_oracle_oic__utilities_api_request_builder

    api_request_builder = _flext_oracle_oic__utilities_api_request_builder
    import flext_oracle_oic._utilities.authentication_validation as _flext_oracle_oic__utilities_authentication_validation
    from flext_oracle_oic._utilities.api_request_builder import (
        FlextOracleOicUtilitiesAPIRequestBuilder,
    )

    authentication_validation = _flext_oracle_oic__utilities_authentication_validation
    import flext_oracle_oic._utilities.connection_validation as _flext_oracle_oic__utilities_connection_validation
    from flext_oracle_oic._utilities.authentication_validation import (
        FlextOracleOicUtilitiesAuthenticationValidation,
    )

    connection_validation = _flext_oracle_oic__utilities_connection_validation
    import flext_oracle_oic._utilities.monitoring as _flext_oracle_oic__utilities_monitoring
    from flext_oracle_oic._utilities.connection_validation import (
        FlextOracleOicUtilitiesConnectionValidation,
    )

    monitoring = _flext_oracle_oic__utilities_monitoring
    import flext_oracle_oic._utilities.oracle_oic as _flext_oracle_oic__utilities_oracle_oic
    from flext_oracle_oic._utilities.monitoring import FlextOracleOicUtilitiesMonitoring

    oracle_oic = _flext_oracle_oic__utilities_oracle_oic
    import flext_oracle_oic._utilities.pattern_analysis as _flext_oracle_oic__utilities_pattern_analysis
    from flext_oracle_oic._utilities.oracle_oic import FlextOracleOicUtilitiesOracleOic

    pattern_analysis = _flext_oracle_oic__utilities_pattern_analysis
    import flext_oracle_oic.api as _flext_oracle_oic_api
    from flext_oracle_oic._utilities.pattern_analysis import (
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
    import flext_oracle_oic.main as _flext_oracle_oic_main
    from flext_oracle_oic.ext_client import FlextOracleOicClient

    main = _flext_oracle_oic_main
    import flext_oracle_oic.models as _flext_oracle_oic_models
    from flext_oracle_oic.main import FlextOracleOicCli

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
    import flext_oracle_oic.services as _flext_oracle_oic_services
    from flext_oracle_oic.service import FlextOracleOicService

    services = _flext_oracle_oic_services
    import flext_oracle_oic.services.auth as _flext_oracle_oic_services_auth

    auth = _flext_oracle_oic_services_auth
    import flext_oracle_oic.services.base as _flext_oracle_oic_services_base
    from flext_oracle_oic.services.auth import FlextOracleOicAuthMixin

    base = _flext_oracle_oic_services_base
    import flext_oracle_oic.services.integration_crud as _flext_oracle_oic_services_integration_crud
    from flext_oracle_oic.services.base import (
        FlextOracleOicServiceBase,
        FlextOracleOicServiceBase as s,
    )

    integration_crud = _flext_oracle_oic_services_integration_crud
    import flext_oracle_oic.services.integration_lifecycle as _flext_oracle_oic_services_integration_lifecycle
    from flext_oracle_oic.services.integration_crud import (
        FlextOracleOicIntegrationCrudMixin,
    )

    integration_lifecycle = _flext_oracle_oic_services_integration_lifecycle
    import flext_oracle_oic.services.integration_patterns as _flext_oracle_oic_services_integration_patterns
    from flext_oracle_oic.services.integration_lifecycle import (
        FlextOracleOicIntegrationLifecycleMixin,
    )

    integration_patterns = _flext_oracle_oic_services_integration_patterns
    import flext_oracle_oic.services.orchestration as _flext_oracle_oic_services_orchestration
    from flext_oracle_oic.services.integration_patterns import (
        FlextOracleOicIntegrationPatternsMixin,
    )
    from flext_oracle_oic.services.monitoring import FlextOracleOicMonitoringMixin

    orchestration = _flext_oracle_oic_services_orchestration
    import flext_oracle_oic.settings as _flext_oracle_oic_settings
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
        "__author__": "flext_oracle_oic.__version__",
        "__author_email__": "flext_oracle_oic.__version__",
        "__description__": "flext_oracle_oic.__version__",
        "__license__": "flext_oracle_oic.__version__",
        "__title__": "flext_oracle_oic.__version__",
        "__url__": "flext_oracle_oic.__version__",
        "__version__": "flext_oracle_oic.__version__",
        "__version_info__": "flext_oracle_oic.__version__",
        "_utilities": "flext_oracle_oic._utilities",
        "api": "flext_oracle_oic.api",
        "c": ("flext_oracle_oic.constants", "FlextOracleOicConstants"),
        "constants": "flext_oracle_oic.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "ext_client": "flext_oracle_oic.ext_client",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("flext_oracle_oic.models", "FlextOracleOicModels"),
        "main": "flext_oracle_oic.main",
        "models": "flext_oracle_oic.models",
        "p": ("flext_oracle_oic.protocols", "FlextOracleOicProtocols"),
        "protocols": "flext_oracle_oic.protocols",
        "r": ("flext_core.result", "FlextResult"),
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
    "api_request_builder",
    "auth",
    "authentication_validation",
    "base",
    "c",
    "connection_validation",
    "constants",
    "d",
    "e",
    "ext_client",
    "h",
    "integration_crud",
    "integration_lifecycle",
    "integration_patterns",
    "m",
    "main",
    "models",
    "monitoring",
    "oracle_oic",
    "orchestration",
    "p",
    "pattern_analysis",
    "protocols",
    "r",
    "s",
    "service",
    "services",
    "settings",
    "t",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
