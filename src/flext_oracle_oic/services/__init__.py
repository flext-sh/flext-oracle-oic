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
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
