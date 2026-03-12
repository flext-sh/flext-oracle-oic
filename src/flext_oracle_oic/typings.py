"""FLEXT Oracle OIC Extension Types - Domain-specific Oracle OIC type definitions.

This module provides Oracle OIC extension-specific type definitions extending t.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends t properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextTypes


class FlextOracleOicTypes(FlextTypes):
    """Oracle OIC extension-specific type definitions extending t.

    Domain-specific type system for Oracle OIC integration operations.
    Contains ONLY complex OIC-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class OracleOic:
        """Oracle OIC integration complex types."""

        type IntegrationConfiguration = dict[str, str | int | bool | Mapping[str, object]]
        type IntegrationFlow = list[dict[str, str | Mapping[str, object]]]
        type IntegrationMapping = dict[str, str | list[str] | Mapping[str, object]]
        type IntegrationMetadata = dict[str, str | int | Mapping[str, object]]
        type IntegrationMonitoring = dict[str, bool | int | Mapping[str, object]]
        type IntegrationSecurity = dict[str, str | bool | Mapping[str, object]]

    class Connection:
        """Oracle OIC connection complex types."""

        type ConnectionConfiguration = dict[str, str | int | bool | Mapping[str, object]]
        type ConnectionPool = dict[str, int | bool | Mapping[str, object]]
        type ConnectionSecurity = dict[str, str | bool | Mapping[str, object]]
        type ConnectionMonitoring = dict[str, int | float | Mapping[str, object]]
        type ConnectionLifecycle = dict[str, str | bool | Mapping[str, object]]
        type ConnectionValidation = dict[str, bool | str | list[str]]

    class Adapter:
        """Oracle OIC adapter complex types."""

        type AdapterConfiguration = dict[str, str | bool | Mapping[str, object]]
        type AdapterCapabilities = list[dict[str, str | bool | Mapping[str, object]]]
        type AdapterMetadata = dict[str, str | list[str] | Mapping[str, object]]
        type AdapterBinding = dict[str, str | Mapping[str, object]]
        type AdapterTransformation = list[dict[str, str | Mapping[str, object]]]
        type AdapterValidation = dict[str, bool | list[str] | Mapping[str, object]]

    class MessageProcessing:
        """Oracle OIC message processing complex types."""

        type MessageConfiguration = dict[str, str | int | Mapping[str, object]]
        type MessageFormat = dict[str, str | bool | Mapping[str, object]]
        type MessageTransformation = list[dict[str, str | Mapping[str, object]]]
        type MessageValidation = dict[str, bool | str | list[str] | Mapping[str, object]]
        type MessageRouting = dict[str, str | list[str] | Mapping[str, object]]
        type MessageTracking = dict[str, str | int | Mapping[str, object]]

    class Transformation:
        """Oracle OIC transformation complex types."""

        type TransformationRule = dict[str, str | list[str] | Mapping[str, object]]
        type TransformationMapping = dict[str, str | Mapping[str, object]]
        type TransformationValidation = dict[str, bool | str | list[str]]
        type TransformationEngine = dict[str, str | bool | Mapping[str, object]]
        type TransformationResult = dict[str, bool | object | Mapping[str, object]]
        type TransformationMetrics = dict[str, int | float | Mapping[str, object]]

    class Monitoring:
        """Oracle OIC monitoring complex types."""

        type MonitoringConfiguration = dict[str, bool | str | int | Mapping[str, object]]
        type MonitoringMetrics = dict[str, int | float | Mapping[str, object]]
        type MonitoringAlerts = list[dict[str, str | int | bool | Mapping[str, object]]]
        type MonitoringDashboard = dict[str, str | list[Mapping[str, object]]]
        type MonitoringReports = dict[str, str | list[Mapping[str, object]]]
        type MonitoringThresholds = dict[str, int | float | bool]

    class Security:
        """Oracle OIC security complex types."""

        type SecurityConfiguration = dict[str, str | bool | Mapping[str, object]]
        type SecurityPolicy = dict[str, str | bool | list[str] | Mapping[str, object]]
        type SecurityCredentials = dict[str, str | Mapping[str, object]]
        type SecurityValidation = dict[str, bool | str | list[str]]
        type SecurityAudit = list[dict[str, str | int | Mapping[str, object]]]
        type SecurityCompliance = dict[str, bool | str | Mapping[str, object]]

    class OicCore:
        """Core Oracle OIC extension types.

        Essential domain-specific types for Oracle OIC integration operations.
        Replaces generic dict[str, object] with semantic Oracle OIC types.
        """

        type ConfigDict = dict[str, object]
        type ConnectionDict = dict[str, str | int | bool | Mapping[str, object]]
        type AuthDict = dict[str, str | Mapping[str, object]]
        type ContextDict = dict[str, object]
        type IntegrationDict = dict[str, object | Mapping[str, object]]
        type WorkflowDict = dict[str, bool | str | Mapping[str, object]]
        type AdapterDict = dict[str, object]
        type MessageDict = dict[str, str | bool | Mapping[str, object]]
        type DataDict = dict[str, object]
        type ResponseDict = dict[str, object]
        type RequestDict = dict[str, object]
        type ResultDict = dict[str, object]
        type MetricsDict = dict[str, object]
        type HealthDict = dict[str, object]
        type DataList = list[dict[str, object]]
        type ConfigList = list[dict[str, object]]
        type StringList = list[str]

    class Project:
        """Oracle OIC extension-specific project types.

        Adds Oracle OIC integration-specific project types.
        Follows domain separation principle: Oracle OIC domain owns integration
        and workflow-specific types.
        """

        type ProjectType = Literal[
            "library",
            "application",
            "service",
            "oic-integration",
            "integration-flow",
            "oic-adapter",
            "message-processor",
            "transformation-service",
            "oic-connector",
            "workflow-engine",
            "integration-platform",
            "oic-monitor",
            "integration-gateway",
            "oic-security",
            "adapter-framework",
            "integration-api",
            "oic-extension",
            "workflow-designer",
            "integration-hub",
        ]
        type OicProjectConfig = dict[str, object]
        type IntegrationConfig = dict[str, str | int | bool | list[str]]
        type WorkflowConfig = dict[str, bool | str | Mapping[str, object]]
        type AdapterConfig = dict[str, object]


t = FlextOracleOicTypes
__all__ = ["FlextOracleOicTypes", "t"]
