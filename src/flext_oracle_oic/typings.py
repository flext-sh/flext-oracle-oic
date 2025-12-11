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

    class Integration:
        """Oracle OIC integration complex types."""

        type IntegrationConfiguration = dict[str, str | int | bool | dict[str, object]]
        type IntegrationFlow = list[dict[str, str | dict[str, FlextTypes.JsonValue]]]
        type IntegrationMapping = dict[str, str | list[str] | dict[str, object]]
        type IntegrationMetadata = dict[
            str, str | int | dict[str, FlextTypes.JsonValue]
        ]
        type IntegrationMonitoring = dict[
            str, bool | int | dict[str, FlextTypes.JsonValue]
        ]
        type IntegrationSecurity = dict[str, str | bool | dict[str, object]]

    # =========================================================================
    # CONNECTION TYPES - Complex OIC connection types
    # =========================================================================

    class Connection:
        """Oracle OIC connection complex types."""

        type ConnectionConfiguration = dict[str, str | int | bool | dict[str, object]]
        type ConnectionPool = dict[str, int | bool | dict[str, object]]
        type ConnectionSecurity = dict[str, str | bool | dict[str, object]]
        type ConnectionMonitoring = dict[
            str, int | float | dict[str, FlextTypes.JsonValue]
        ]
        type ConnectionLifecycle = dict[str, str | bool | dict[str, object]]
        type ConnectionValidation = dict[str, bool | str | list[str]]

    # =========================================================================
    # ADAPTER TYPES - Complex OIC adapter types
    # =========================================================================

    class Adapter:
        """Oracle OIC adapter complex types."""

        type AdapterConfiguration = dict[str, str | bool | dict[str, object]]
        type AdapterCapabilities = list[dict[str, str | bool | dict[str, object]]]
        type AdapterMetadata = dict[
            str, str | list[str] | dict[str, FlextTypes.JsonValue]
        ]
        type AdapterBinding = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type AdapterTransformation = list[dict[str, str | dict[str, object]]]
        type AdapterValidation = dict[str, bool | list[str] | dict[str, object]]

    # =========================================================================
    # MESSAGE PROCESSING TYPES - Complex message handling types
    # =========================================================================

    class MessageProcessing:
        """Oracle OIC message processing complex types."""

        type MessageConfiguration = dict[str, str | int | dict[str, object]]
        type MessageFormat = dict[str, str | bool | dict[str, object]]
        type MessageTransformation = list[
            dict[str, str | dict[str, FlextTypes.JsonValue]]
        ]
        type MessageValidation = dict[str, bool | str | list[str] | dict[str, object]]
        type MessageRouting = dict[
            str, str | list[str] | dict[str, FlextTypes.JsonValue]
        ]
        type MessageTracking = dict[str, str | int | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # TRANSFORMATION TYPES - Complex data transformation types
    # =========================================================================

    class Transformation:
        """Oracle OIC transformation complex types."""

        type TransformationRule = dict[str, str | list[str] | dict[str, object]]
        type TransformationMapping = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type TransformationValidation = dict[str, bool | str | list[str]]
        type TransformationEngine = dict[str, str | bool | dict[str, object]]
        type TransformationResult = dict[
            str, bool | object | dict[str, FlextTypes.JsonValue]
        ]
        type TransformationMetrics = dict[
            str, int | float | dict[str, FlextTypes.JsonValue]
        ]

    # =========================================================================
    # MONITORING TYPES - Complex OIC monitoring types
    # =========================================================================

    class Monitoring:
        """Oracle OIC monitoring complex types."""

        type MonitoringConfiguration = dict[str, bool | str | int | dict[str, object]]
        type MonitoringMetrics = dict[
            str, int | float | dict[str, FlextTypes.JsonValue]
        ]
        type MonitoringAlerts = list[dict[str, str | int | bool | dict[str, object]]]
        type MonitoringDashboard = dict[
            str, str | list[dict[str, FlextTypes.JsonValue]]
        ]
        type MonitoringReports = dict[str, str | list[dict[str, object]]]
        type MonitoringThresholds = dict[str, int | float | bool]

    # =========================================================================
    # SECURITY TYPES - Complex OIC security types
    # =========================================================================

    class Security:
        """Oracle OIC security complex types."""

        type SecurityConfiguration = dict[str, str | bool | dict[str, object]]
        type SecurityPolicy = dict[str, str | bool | list[str] | dict[str, object]]
        type SecurityCredentials = dict[str, str | dict[str, object]]
        type SecurityValidation = dict[str, bool | str | list[str]]
        type SecurityAudit = list[
            dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        ]
        type SecurityCompliance = dict[str, bool | str | dict[str, object]]

    # =========================================================================
    # CORE TYPES - Essential Oracle OIC types extending t
    # =========================================================================

    class OicCore:
        """Core Oracle OIC extension types.

        Essential domain-specific types for Oracle OIC integration operations.
        Replaces generic dict[str, object] with semantic Oracle OIC types.
        """

        # Configuration and connection types
        type ConfigDict = dict[str, object]
        type ConnectionDict = dict[str, str | int | bool | dict[str, object]]
        type AuthDict = dict[str, str | dict[str, object]]
        type ContextDict = dict[str, object]

        # Integration and workflow types
        type IntegrationDict = dict[str, FlextTypes.JsonValue | dict[str, object]]
        type WorkflowDict = dict[str, bool | str | dict[str, object]]
        type AdapterDict = dict[str, object]
        type MessageDict = dict[str, str | bool | dict[str, object]]

        # Data processing types
        type DataDict = dict[str, object]
        type ResponseDict = dict[str, object]
        type RequestDict = dict[str, object]
        type ResultDict = dict[str, object]
        type MetricsDict = dict[str, object]
        type HealthDict = dict[str, object]

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
        type OicProjectConfig = dict[str, object]
        type IntegrationConfig = dict[str, str | int | bool | list[str]]
        type WorkflowConfig = dict[str, bool | str | dict[str, object]]
        type AdapterConfig = dict[str, object]

    class OracleOic:
        """OracleOic types namespace for cross-project access.

        Provides organized access to all OracleOic types for other FLEXT projects.
        Usage: Other projects can reference `t.OracleOic.Integration.*`, `t.OracleOic.Project.*`, etc.
        This enables consistent namespace patterns for cross-project type access.

        Examples:
            from flext_oracle_oic.typings import t
            config: t.OracleOic.Integration.IntegrationConfiguration = ...
            flow: t.OracleOic.Integration.IntegrationFlow = ...

        Note: Namespace composition via inheritance - no aliases needed.
        Access parent namespaces directly through inheritance.

        """


# Alias for simplified usage
t = FlextOracleOicTypes

# Namespace composition via class inheritance
# OracleOic namespace provides access to nested classes through inheritance
# Access patterns:
# - t.OracleOic.* for OracleOic-specific types
# - t.Project.* for project types
# - t.Core.* for core types (inherited from parent)

__all__ = ["FlextOracleOicTypes", "t"]
