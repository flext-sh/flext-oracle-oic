# AUTO-GENERATED FILE — Regenerate with: make gen
"""Lazy export map part."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map

FLEXT_ORACLE_OIC_LAZY_IMPORTS_PART_01 = build_lazy_import_map(
    {
        "._utilities": ("_utilities",),
        ".api": (
            "FlextOracleOicApi",
            "oracle_oic",
        ),
        ".constants": (
            "FlextOracleOicConstants",
            "c",
        ),
        ".main": (
            "FlextOracleOicCli",
            "main",
        ),
        ".models": (
            "FlextOracleOicModels",
            "m",
        ),
        ".protocols": (
            "FlextOracleOicProtocols",
            "p",
        ),
        ".service": (
            "FlextOracleOicService",
            "s",
        ),
        ".services": ("services",),
        ".services.auth": ("FlextOracleOicAuthMixin",),
        ".services.base": ("FlextOracleOicServiceBase",),
        ".services.integration_crud": ("FlextOracleOicIntegrationCrudMixin",),
        ".services.integration_lifecycle": ("FlextOracleOicIntegrationLifecycleMixin",),
        ".services.monitoring": ("FlextOracleOicMonitoringMixin",),
        ".services.orchestration": ("FlextOracleOicOrchestrationMixin",),
        ".settings": ("FlextOracleOicSettings",),
        ".typings": (
            "FlextOracleOicTypes",
            "t",
        ),
        ".utilities": (
            "FlextOracleOicUtilities",
            "u",
        ),
    },
)

__all__: list[str] = ["FLEXT_ORACLE_OIC_LAZY_IMPORTS_PART_01"]
