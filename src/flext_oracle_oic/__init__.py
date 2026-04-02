# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT Oracle OIC Extension - EXTENSION Pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
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

if _TYPE_CHECKING:
    from flext_core import FlextTypes, d, e, h, r, x
    from flext_oracle_oic import (
        _utilities,
        api,
        constants,
        ext_client,
        models,
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
        api_request_builder,
        authentication_validation,
        connection_validation,
        monitoring,
        oracle_oic,
        pattern_analysis,
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
    from flext_oracle_oic.service import (
        FlextOracleOicService,
        FlextOracleOicService as s,
    )
    from flext_oracle_oic.services import (
        FlextOracleOicAuthMixin,
        FlextOracleOicIntegrationCrudMixin,
        FlextOracleOicIntegrationLifecycleMixin,
        FlextOracleOicIntegrationPatternsMixin,
        FlextOracleOicMonitoringMixin,
        FlextOracleOicOrchestrationMixin,
        FlextOracleOicServiceBase,
        auth,
        base,
        integration_crud,
        integration_lifecycle,
        integration_patterns,
        orchestration,
    )
    from flext_oracle_oic.settings import FlextOracleOicSettings
    from flext_oracle_oic.typings import FlextOracleOicTypes, FlextOracleOicTypes as t
    from flext_oracle_oic.utilities import (
        FlextOracleOicUtilities,
        FlextOracleOicUtilities as u,
    )

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
        "c": ("flext_oracle_oic.constants", "FlextOracleOicConstants"),
        "constants": "flext_oracle_oic.constants",
        "d": "flext_core",
        "e": "flext_core",
        "ext_client": "flext_oracle_oic.ext_client",
        "h": "flext_core",
        "m": ("flext_oracle_oic.models", "FlextOracleOicModels"),
        "main": "flext_oracle_oic.main",
        "models": "flext_oracle_oic.models",
        "p": ("flext_oracle_oic.protocols", "FlextOracleOicProtocols"),
        "protocols": "flext_oracle_oic.protocols",
        "r": "flext_core",
        "s": ("flext_oracle_oic.service", "FlextOracleOicService"),
        "service": "flext_oracle_oic.service",
        "services": "flext_oracle_oic.services",
        "settings": "flext_oracle_oic.settings",
        "t": ("flext_oracle_oic.typings", "FlextOracleOicTypes"),
        "typings": "flext_oracle_oic.typings",
        "u": ("flext_oracle_oic.utilities", "FlextOracleOicUtilities"),
        "utilities": "flext_oracle_oic.utilities",
        "x": "flext_core",
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
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
