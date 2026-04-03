# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Services package."""

from __future__ import annotations

import typing as _t

from flext_core.constants import FlextConstants as c
from flext_core.decorators import FlextDecorators as d
from flext_core.exceptions import FlextExceptions as e
from flext_core.handlers import FlextHandlers as h
from flext_core.lazy import install_lazy_exports
from flext_core.mixins import FlextMixins as x
from flext_core.models import FlextModels as m
from flext_core.protocols import FlextProtocols as p
from flext_core.result import FlextResult as r
from flext_core.typings import FlextTypes as t
from flext_core.utilities import FlextUtilities as u

if _t.TYPE_CHECKING:
    import flext_oracle_oic.services.auth as _flext_oracle_oic_services_auth

    auth = _flext_oracle_oic_services_auth
    import flext_oracle_oic.services.base as _flext_oracle_oic_services_base

    base = _flext_oracle_oic_services_base
    import flext_oracle_oic.services.integration_crud as _flext_oracle_oic_services_integration_crud

    integration_crud = _flext_oracle_oic_services_integration_crud
    import flext_oracle_oic.services.integration_lifecycle as _flext_oracle_oic_services_integration_lifecycle

    integration_lifecycle = _flext_oracle_oic_services_integration_lifecycle
    import flext_oracle_oic.services.integration_patterns as _flext_oracle_oic_services_integration_patterns

    integration_patterns = _flext_oracle_oic_services_integration_patterns
    import flext_oracle_oic.services.monitoring as _flext_oracle_oic_services_monitoring

    monitoring = _flext_oracle_oic_services_monitoring
    import flext_oracle_oic.services.orchestration as _flext_oracle_oic_services_orchestration

    orchestration = _flext_oracle_oic_services_orchestration

    _ = (
        FlextOracleOicAuthMixin,
        FlextOracleOicIntegrationCrudMixin,
        FlextOracleOicIntegrationLifecycleMixin,
        FlextOracleOicIntegrationPatternsMixin,
        FlextOracleOicMonitoringMixin,
        FlextOracleOicOrchestrationMixin,
        FlextOracleOicServiceBase,
        auth,
        base,
        c,
        d,
        e,
        h,
        integration_crud,
        integration_lifecycle,
        integration_patterns,
        m,
        monitoring,
        orchestration,
        p,
        r,
        s,
        t,
        u,
        x,
    )
_LAZY_IMPORTS = {
    "FlextOracleOicAuthMixin": "flext_oracle_oic.services.auth",
    "FlextOracleOicIntegrationCrudMixin": "flext_oracle_oic.services.integration_crud",
    "FlextOracleOicIntegrationLifecycleMixin": "flext_oracle_oic.services.integration_lifecycle",
    "FlextOracleOicIntegrationPatternsMixin": "flext_oracle_oic.services.integration_patterns",
    "FlextOracleOicMonitoringMixin": "flext_oracle_oic.services.monitoring",
    "FlextOracleOicOrchestrationMixin": "flext_oracle_oic.services.orchestration",
    "FlextOracleOicServiceBase": "flext_oracle_oic.services.base",
    "auth": "flext_oracle_oic.services.auth",
    "base": "flext_oracle_oic.services.base",
    "c": ("flext_core.constants", "FlextConstants"),
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "integration_crud": "flext_oracle_oic.services.integration_crud",
    "integration_lifecycle": "flext_oracle_oic.services.integration_lifecycle",
    "integration_patterns": "flext_oracle_oic.services.integration_patterns",
    "m": ("flext_core.models", "FlextModels"),
    "monitoring": "flext_oracle_oic.services.monitoring",
    "orchestration": "flext_oracle_oic.services.orchestration",
    "p": ("flext_core.protocols", "FlextProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_oracle_oic.services.base", "FlextOracleOicServiceBase"),
    "t": ("flext_core.typings", "FlextTypes"),
    "u": ("flext_core.utilities", "FlextUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "FlextOracleOicAuthMixin",
    "FlextOracleOicIntegrationCrudMixin",
    "FlextOracleOicIntegrationLifecycleMixin",
    "FlextOracleOicIntegrationPatternsMixin",
    "FlextOracleOicMonitoringMixin",
    "FlextOracleOicOrchestrationMixin",
    "FlextOracleOicServiceBase",
    "auth",
    "base",
    "c",
    "d",
    "e",
    "h",
    "integration_crud",
    "integration_lifecycle",
    "integration_patterns",
    "m",
    "monitoring",
    "orchestration",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
