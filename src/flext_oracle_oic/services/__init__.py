# AUTO-GENERATED FILE — Regenerate with: make gen
"""Services package."""

from __future__ import annotations

from flext_core.lazy import install_lazy_exports

_LAZY_IMPORTS = {
    "FlextOracleOicAuthMixin": ".auth",
    "FlextOracleOicIntegrationCrudMixin": ".integration_crud",
    "FlextOracleOicIntegrationLifecycleMixin": ".integration_lifecycle",
    "FlextOracleOicIntegrationPatternsMixin": ".integration_patterns",
    "FlextOracleOicMonitoringMixin": ".monitoring",
    "FlextOracleOicOrchestrationMixin": ".orchestration",
    "FlextOracleOicServiceBase": ".base",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
