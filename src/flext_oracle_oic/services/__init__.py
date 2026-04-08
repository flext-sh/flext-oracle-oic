# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Services package."""

from __future__ import annotations

from flext_core.lazy import install_lazy_exports

_LAZY_IMPORTS = {
    "FlextOracleOicAuthMixin": (
        "flext_oracle_oic.services.auth",
        "FlextOracleOicAuthMixin",
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
    "FlextOracleOicMonitoringMixin": (
        "flext_oracle_oic.services.monitoring",
        "FlextOracleOicMonitoringMixin",
    ),
    "FlextOracleOicOrchestrationMixin": (
        "flext_oracle_oic.services.orchestration",
        "FlextOracleOicOrchestrationMixin",
    ),
    "FlextOracleOicServiceBase": (
        "flext_oracle_oic.services.base",
        "FlextOracleOicServiceBase",
    ),
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
