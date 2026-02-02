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

# =============================================================================
# ORACLE OIC-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for OIC operations
# =============================================================================


# Oracle OIC domain TypeVars
class FlextOracleOicTypes(FlextTypes):
    """Oracle OIC extension-specific type definitions extending t.

    Domain-specific type system for Oracle OIC integration operations.
    Contains ONLY complex OIC-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # INTEGRATION TYPES - Complex OIC integration types
    # =========================================================================

    class OracleOic:
        """Oracle OIC integration complex types."""

        type IntegrationConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.GeneralValueType]
        ]
        type IntegrationFlow = list[dict[str, str | dict[str, FlextTypes.JsonValue]]]
        type IntegrationMapping = dict[
            str, str | list[str] | dict[str, FlextTypes.GeneralValueType]
        ]
        type IntegrationMetadata = dict[
            str,
            str | int | dict[str, FlextTypes.JsonValue],
        ]
        type IntegrationMonitoring = dict[
            str,
            bool | int | dict[str, FlextTypes.JsonValue],
        ]
        type IntegrationSecurity = dict[
            str, str | bool | dict[str, FlextTypes.GeneralValueType]
        ]

    # =========================================================================
    # CONNECTION TYPES - Complex OIC connection types
    # =========================================================================

    class Connection:
        """Oracle OIC connection complex types."""

        type ConnectionConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.GeneralValueType]
        ]
        type ConnectionPool = dict[
            str, int | bool | dict[str, FlextTypes.GeneralValueType]
        ]
        type ConnectionSecurity = dict[
            str, str | bool | dict[str, FlextTypes.GeneralValueType]
        ]
        type ConnectionMonitoring = dict[
            str,
            int | float | dict[str, FlextTypes.JsonValue],
        ]
        type ConnectionLifecycle = dict[
            str, str | bool | dict[str, FlextTypes.GeneralValueType]
        ]
        type ConnectionValidation = dict[str, bool | str | list[str]]

    # =========================================================================
    # ADAPTER TYPES - Complex OIC adapter types
    # =========================================================================

    class Adapter:
        """Oracle OIC adapter complex types."""

        type AdapterConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.GeneralValueType]
        ]
        type AdapterCapabilities = list[
            dict[str, str | bool | dict[str, FlextTypes.GeneralValueType]]
        ]
        type AdapterMetadata = dict[
            str,
            str | list[str] | dict[str, FlextTypes.JsonValue],
        ]
        type AdapterBinding = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type AdapterTransformation = list[
            dict[str, str | dict[str, FlextTypes.GeneralValueType]]
        ]
        type AdapterValidation = dict[
            str, bool | list[str] | dict[str, FlextTypes.GeneralValueType]
        ]

    # =========================================================================
    # MESSAGE PROCESSING TYPES - Complex message handling types
    # =========================================================================

    class MessageProcessing:
        """Oracle OIC message processing complex types."""

        type MessageConfiguration = dict[
            str, str | int | dict[str, FlextTypes.GeneralValueType]
        ]
        type MessageFormat = dict[
            str, str | bool | dict[str, FlextTypes.GeneralValueType]
        ]
        type MessageTransformation = list[
            dict[str, str | dict[str, FlextTypes.JsonValue]]
        ]
        type MessageValidation = dict[
            str, bool | str | list[str] | dict[str, FlextTypes.GeneralValueType]
        ]
        type MessageRouting = dict[
            str,
            str | list[str] | dict[str, FlextTypes.JsonValue],
        ]
        type MessageTracking = dict[str, str | int | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # TRANSFORMATION TYPES - Complex data transformation types
    # =========================================================================

    class Transformation:
        """Oracle OIC transformation complex types."""

        type TransformationRule = dict[
            str, str | list[str] | dict[str, FlextTypes.GeneralValueType]
        ]
        type TransformationMapping = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type TransformationValidation = dict[str, bool | str | list[str]]
        type TransformationEngine = dict[
            str, str | bool | dict[str, FlextTypes.GeneralValueType]
        ]
        type TransformationResult = dict[
            str,
            bool | object | dict[str, FlextTypes.JsonValue],
        ]
        type TransformationMetrics = dict[
            str,
            int | float | dict[str, FlextTypes.JsonValue],
        ]

    # =========================================================================
    # MONITORING TYPES - Complex OIC monitoring types
    # =========================================================================

    class Monitoring:
        """Oracle OIC monitoring complex types."""

        type MonitoringConfiguration = dict[
            str, bool | str | int | dict[str, FlextTypes.GeneralValueType]
        ]
        type MonitoringMetrics = dict[
            str,
            int | float | dict[str, FlextTypes.JsonValue],
        ]
        type MonitoringAlerts = list[
            dict[str, str | int | bool | dict[str, FlextTypes.GeneralValueType]]
        ]
        type MonitoringDashboard = dict[
            str,
            str | list[dict[str, FlextTypes.JsonValue]],
        ]
        type MonitoringReports = dict[
            str, str | list[dict[str, FlextTypes.GeneralValueType]]
        ]
        type MonitoringThresholds = dict[str, int | float | bool]

    # =========================================================================
    # SECURITY TYPES - Complex OIC security types
    # =========================================================================

    class Security:
        """Oracle OIC security complex types."""

        type SecurityConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.GeneralValueType]
        ]
        type SecurityPolicy = dict[
            str, str | bool | list[str] | dict[str, FlextTypes.GeneralValueType]
        ]
        type SecurityCredentials = dict[
            str, str | dict[str, FlextTypes.GeneralValueType]
        ]
        type SecurityValidation = dict[str, bool | str | list[str]]
        type SecurityAudit = list[
            dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        ]
        type SecurityCompliance = dict[
            str, bool | str | dict[str, FlextTypes.GeneralValueType]
        ]

    # =========================================================================
    # CORE TYPES - Essential Oracle OIC types extending t
    # =========================================================================

    class OicCore:
        """Core Oracle OIC extension types.

        Essential domain-specific types for Oracle OIC integration operations.
        Replaces generic dict[str, t.GeneralValueType] with semantic Oracle OIC types.
        """

        # Configuration and connection types
        type ConfigDict = dict[str, FlextTypes.GeneralValueType]
        type ConnectionDict = dict[
            str, str | int | bool | dict[str, FlextTypes.GeneralValueType]
        ]
        type AuthDict = dict[str, str | dict[str, FlextTypes.GeneralValueType]]
        type ContextDict = dict[str, FlextTypes.GeneralValueType]

        # Integration and workflow types
        type IntegrationDict = dict[
            str, FlextTypes.JsonValue | dict[str, FlextTypes.GeneralValueType]
        ]
        type WorkflowDict = dict[
            str, bool | str | dict[str, FlextTypes.GeneralValueType]
        ]
        type AdapterDict = dict[str, FlextTypes.GeneralValueType]
        type MessageDict = dict[
            str, str | bool | dict[str, FlextTypes.GeneralValueType]
        ]

        # Data processing types
        type DataDict = dict[str, FlextTypes.GeneralValueType]
        type ResponseDict = dict[str, FlextTypes.GeneralValueType]
        type RequestDict = dict[str, FlextTypes.GeneralValueType]
        type ResultDict = dict[str, FlextTypes.GeneralValueType]
        type MetricsDict = dict[str, FlextTypes.GeneralValueType]
        type HealthDict = dict[str, FlextTypes.GeneralValueType]

        # Collection types for Oracle OIC operations
        type DataList = list[DataDict]
        type ConfigList = list[ConfigDict]
        type StringList = list[str]

    # =========================================================================
    # ORACLE OIC PROJECT TYPES - Domain-specific project types extending t
    # =========================================================================

    class Project:
        """Oracle OIC extension-specific project types.

        Adds Oracle OIC integration-specific project types.
        Follows domain separation principle: Oracle OIC domain owns integration
        and workflow-specific types.
        """

        # Oracle OIC-specific project types
        type ProjectType = Literal[
            # Generic types inherited from t
            "library",
            "application",
            "service",
            # Oracle OIC-specific types
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

        # Oracle OIC-specific project configurations
        type OicProjectConfig = dict[str, FlextTypes.GeneralValueType]
        type IntegrationConfig = dict[str, str | int | bool | list[str]]
        type WorkflowConfig = dict[
            str, bool | str | dict[str, FlextTypes.GeneralValueType]
        ]
        type AdapterConfig = dict[str, FlextTypes.GeneralValueType]


# Alias for simplified usage
t = FlextOracleOicTypes

# Namespace composition via class inheritance
# OracleOic namespace provides access to nested classes through inheritance
# Access patterns:
# - t.OracleOic.* for OracleOic-specific types
# - t.Project.* for project types
# - t.Core.* for core types (inherited from parent)

__all__ = ["FlextOracleOicTypes", "t"]
