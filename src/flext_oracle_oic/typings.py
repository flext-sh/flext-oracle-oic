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

        type IntegrationConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.ContainerValue]
        ]
        type IntegrationFlow = list[dict[str, str | dict[str, FlextTypes.JsonValue]]]
        type IntegrationMapping = dict[
            str, str | list[str] | dict[str, FlextTypes.ContainerValue]
        ]
        type IntegrationMetadata = dict[
            str, str | int | dict[str, FlextTypes.JsonValue]
        ]
        type IntegrationMonitoring = dict[
            str, bool | int | dict[str, FlextTypes.JsonValue]
        ]
        type IntegrationSecurity = dict[
            str, str | bool | dict[str, FlextTypes.ContainerValue]
        ]

    class Connection:
        """Oracle OIC connection complex types."""

        type ConnectionConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.ContainerValue]
        ]
        type ConnectionPool = dict[
            str, int | bool | dict[str, FlextTypes.ContainerValue]
        ]
        type ConnectionSecurity = dict[
            str, str | bool | dict[str, FlextTypes.ContainerValue]
        ]
        type ConnectionMonitoring = dict[
            str, int | float | dict[str, FlextTypes.JsonValue]
        ]
        type ConnectionLifecycle = dict[
            str, str | bool | dict[str, FlextTypes.ContainerValue]
        ]
        type ConnectionValidation = dict[str, bool | str | list[str]]

    class Adapter:
        """Oracle OIC adapter complex types."""

        type AdapterConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.ContainerValue]
        ]
        type AdapterCapabilities = list[
            dict[str, str | bool | dict[str, FlextTypes.ContainerValue]]
        ]
        type AdapterMetadata = dict[
            str, str | list[str] | dict[str, FlextTypes.JsonValue]
        ]
        type AdapterBinding = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type AdapterTransformation = list[
            dict[str, str | dict[str, FlextTypes.ContainerValue]]
        ]
        type AdapterValidation = dict[
            str, bool | list[str] | dict[str, FlextTypes.ContainerValue]
        ]

    class MessageProcessing:
        """Oracle OIC message processing complex types."""

        type MessageConfiguration = dict[
            str, str | int | dict[str, FlextTypes.ContainerValue]
        ]
        type MessageFormat = dict[
            str, str | bool | dict[str, FlextTypes.ContainerValue]
        ]
        type MessageTransformation = list[
            dict[str, str | dict[str, FlextTypes.JsonValue]]
        ]
        type MessageValidation = dict[
            str, bool | str | list[str] | dict[str, FlextTypes.ContainerValue]
        ]
        type MessageRouting = dict[
            str, str | list[str] | dict[str, FlextTypes.JsonValue]
        ]
        type MessageTracking = dict[str, str | int | dict[str, FlextTypes.JsonValue]]

    class Transformation:
        """Oracle OIC transformation complex types."""

        type TransformationRule = dict[
            str, str | list[str] | dict[str, FlextTypes.ContainerValue]
        ]
        type TransformationMapping = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type TransformationValidation = dict[str, bool | str | list[str]]
        type TransformationEngine = dict[
            str, str | bool | dict[str, FlextTypes.ContainerValue]
        ]
        type TransformationResult = dict[
            str, bool | t.ContainerValue | dict[str, FlextTypes.JsonValue]
        ]
        type TransformationMetrics = dict[
            str, int | float | dict[str, FlextTypes.JsonValue]
        ]

    class Monitoring:
        """Oracle OIC monitoring complex types."""

        type MonitoringConfiguration = dict[
            str, bool | str | int | dict[str, FlextTypes.ContainerValue]
        ]
        type MonitoringMetrics = dict[
            str, int | float | dict[str, FlextTypes.JsonValue]
        ]
        type MonitoringAlerts = list[
            dict[str, str | int | bool | dict[str, FlextTypes.ContainerValue]]
        ]
        type MonitoringDashboard = dict[
            str, str | list[dict[str, FlextTypes.JsonValue]]
        ]
        type MonitoringReports = dict[
            str, str | list[dict[str, FlextTypes.ContainerValue]]
        ]
        type MonitoringThresholds = dict[str, int | float | bool]

    class Security:
        """Oracle OIC security complex types."""

        type SecurityConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.ContainerValue]
        ]
        type SecurityPolicy = dict[
            str, str | bool | list[str] | dict[str, FlextTypes.ContainerValue]
        ]
        type SecurityCredentials = dict[str, str | dict[str, FlextTypes.ContainerValue]]
        type SecurityValidation = dict[str, bool | str | list[str]]
        type SecurityAudit = list[
            dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        ]
        type SecurityCompliance = dict[
            str, bool | str | dict[str, FlextTypes.ContainerValue]
        ]

    class OicCore:
        """Core Oracle OIC extension types.

        Essential domain-specific types for Oracle OIC integration operations.
        Replaces generic dict[str, t.ContainerValue] with semantic Oracle OIC types.
        """

        type ConfigDict = dict[str, FlextTypes.ContainerValue]
        type ConnectionDict = dict[
            str, str | int | bool | dict[str, FlextTypes.ContainerValue]
        ]
        type AuthDict = dict[str, str | dict[str, FlextTypes.ContainerValue]]
        type ContextDict = dict[str, FlextTypes.ContainerValue]
        type IntegrationDict = dict[
            str, FlextTypes.JsonValue | dict[str, FlextTypes.ContainerValue]
        ]
        type WorkflowDict = dict[str, bool | str | dict[str, FlextTypes.ContainerValue]]
        type AdapterDict = dict[str, FlextTypes.ContainerValue]
        type MessageDict = dict[str, str | bool | dict[str, FlextTypes.ContainerValue]]
        type DataDict = dict[str, FlextTypes.ContainerValue]
        type ResponseDict = dict[str, FlextTypes.ContainerValue]
        type RequestDict = dict[str, FlextTypes.ContainerValue]
        type ResultDict = dict[str, FlextTypes.ContainerValue]
        type MetricsDict = dict[str, FlextTypes.ContainerValue]
        type HealthDict = dict[str, FlextTypes.ContainerValue]
        type DataList = list[dict[str, FlextTypes.ContainerValue]]
        type ConfigList = list[dict[str, FlextTypes.ContainerValue]]
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
        type OicProjectConfig = dict[str, FlextTypes.ContainerValue]
        type IntegrationConfig = dict[str, str | int | bool | list[str]]
        type WorkflowConfig = dict[
            str, bool | str | dict[str, FlextTypes.ContainerValue]
        ]
        type AdapterConfig = dict[str, FlextTypes.ContainerValue]


t = FlextOracleOicTypes
__all__ = ["FlextOracleOicTypes", "t"]
