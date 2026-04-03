# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Services package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.constants import FlextConstants as c
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.models import FlextModels as m
    from flext_core.protocols import FlextProtocols as p
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_core.typings import FlextTypes as t
    from flext_core.utilities import FlextUtilities as u
    from flext_oracle_oic import (
        auth,
        base,
        integration_crud,
        integration_lifecycle,
        integration_patterns,
        monitoring,
        orchestration,
    )
    from flext_oracle_oic.auth import FlextOracleOicAuthMixin
    from flext_oracle_oic.base import FlextOracleOicServiceBase
    from flext_oracle_oic.integration_crud import FlextOracleOicIntegrationCrudMixin
    from flext_oracle_oic.integration_lifecycle import (
        FlextOracleOicIntegrationLifecycleMixin,
    )
    from flext_oracle_oic.integration_patterns import (
        FlextOracleOicIntegrationPatternsMixin,
    )
    from flext_oracle_oic.monitoring import FlextOracleOicMonitoringMixin
    from flext_oracle_oic.orchestration import FlextOracleOicOrchestrationMixin

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextOracleOicAuthMixin": "flext_oracle_oic.auth",
    "FlextOracleOicIntegrationCrudMixin": "flext_oracle_oic.integration_crud",
    "FlextOracleOicIntegrationLifecycleMixin": "flext_oracle_oic.integration_lifecycle",
    "FlextOracleOicIntegrationPatternsMixin": "flext_oracle_oic.integration_patterns",
    "FlextOracleOicMonitoringMixin": "flext_oracle_oic.monitoring",
    "FlextOracleOicOrchestrationMixin": "flext_oracle_oic.orchestration",
    "FlextOracleOicServiceBase": "flext_oracle_oic.base",
    "auth": "flext_oracle_oic.auth",
    "base": "flext_oracle_oic.base",
    "c": ("flext_core.constants", "FlextConstants"),
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "integration_crud": "flext_oracle_oic.integration_crud",
    "integration_lifecycle": "flext_oracle_oic.integration_lifecycle",
    "integration_patterns": "flext_oracle_oic.integration_patterns",
    "m": ("flext_core.models", "FlextModels"),
    "monitoring": "flext_oracle_oic.monitoring",
    "orchestration": "flext_oracle_oic.orchestration",
    "p": ("flext_core.protocols", "FlextProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "t": ("flext_core.typings", "FlextTypes"),
    "u": ("flext_core.utilities", "FlextUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
