"""FLEXT Oracle OIC Extension Types - Domain-specific Oracle OIC type definitions.

This module provides Oracle OIC extension-specific type definitions extending FlextCore.Types.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextCore.Types properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextCore

# =============================================================================
# ORACLE OIC-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for OIC operations
# =============================================================================


# Oracle OIC domain TypeVars
class FlextOracleOicTypes(FlextCore.Types):
    """Oracle OIC extension-specific type definitions extending FlextCore.Types.

    Domain-specific type system for Oracle OIC integration operations.
    Contains ONLY complex OIC-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # INTEGRATION TYPES - Complex OIC integration types
    # =========================================================================

    class Integration:
        """Oracle OIC integration complex types."""

        type IntegrationConfiguration = dict[
            str, str | int | bool | dict[str, FlextCore.Types.ConfigValue]
        ]
        type IntegrationFlow = list[
            dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        ]
        type IntegrationMapping = dict[
            str, str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type IntegrationMetadata = dict[
            str, str | int | dict[str, FlextCore.Types.JsonValue]
        ]
        type IntegrationMonitoring = dict[
            str, bool | int | dict[str, FlextCore.Types.JsonValue]
        ]
        type IntegrationSecurity = dict[
            str, str | bool | dict[str, FlextCore.Types.ConfigValue]
        ]

    # =========================================================================
    # CONNECTION TYPES - Complex OIC connection types
    # =========================================================================

    class Connection:
        """Oracle OIC connection complex types."""

        type ConnectionConfiguration = dict[
            str, str | int | bool | dict[str, FlextCore.Types.ConfigValue]
        ]
        type ConnectionPool = dict[str, int | bool | FlextCore.Types.Dict]
        type ConnectionSecurity = dict[
            str, str | bool | dict[str, FlextCore.Types.ConfigValue]
        ]
        type ConnectionMonitoring = dict[
            str, int | float | dict[str, FlextCore.Types.JsonValue]
        ]
        type ConnectionLifecycle = dict[str, str | bool | FlextCore.Types.Dict]
        type ConnectionValidation = dict[str, bool | str | FlextCore.Types.StringList]

    # =========================================================================
    # ADAPTER TYPES - Complex OIC adapter types
    # =========================================================================

    class Adapter:
        """Oracle OIC adapter complex types."""

        type AdapterConfiguration = dict[
            str, str | bool | dict[str, FlextCore.Types.ConfigValue]
        ]
        type AdapterCapabilities = list[dict[str, str | bool | FlextCore.Types.Dict]]
        type AdapterMetadata = dict[
            str, str | FlextCore.Types.StringList | dict[str, FlextCore.Types.JsonValue]
        ]
        type AdapterBinding = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type AdapterTransformation = list[dict[str, str | FlextCore.Types.Dict]]
        type AdapterValidation = dict[
            str, bool | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]

    # =========================================================================
    # MESSAGE PROCESSING TYPES - Complex message handling types
    # =========================================================================

    class MessageProcessing:
        """Oracle OIC message processing complex types."""

        type MessageConfiguration = dict[
            str, str | int | dict[str, FlextCore.Types.ConfigValue]
        ]
        type MessageFormat = dict[str, str | bool | FlextCore.Types.Dict]
        type MessageTransformation = list[
            dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        ]
        type MessageValidation = dict[
            str, bool | str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type MessageRouting = dict[
            str, str | FlextCore.Types.StringList | dict[str, FlextCore.Types.JsonValue]
        ]
        type MessageTracking = dict[
            str, str | int | dict[str, FlextCore.Types.JsonValue]
        ]

    # =========================================================================
    # TRANSFORMATION TYPES - Complex data transformation types
    # =========================================================================

    class Transformation:
        """Oracle OIC transformation complex types."""

        type TransformationRule = dict[
            str, str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type TransformationMapping = dict[
            str, str | dict[str, FlextCore.Types.JsonValue]
        ]
        type TransformationValidation = dict[
            str, bool | str | FlextCore.Types.StringList
        ]
        type TransformationEngine = dict[
            str, str | bool | dict[str, FlextCore.Types.ConfigValue]
        ]
        type TransformationResult = dict[
            str, bool | object | dict[str, FlextCore.Types.JsonValue]
        ]
        type TransformationMetrics = dict[
            str, int | float | dict[str, FlextCore.Types.JsonValue]
        ]

    # =========================================================================
    # MONITORING TYPES - Complex OIC monitoring types
    # =========================================================================

    class Monitoring:
        """Oracle OIC monitoring complex types."""

        type MonitoringConfiguration = dict[
            str, bool | str | int | dict[str, FlextCore.Types.ConfigValue]
        ]
        type MonitoringMetrics = dict[
            str, int | float | dict[str, FlextCore.Types.JsonValue]
        ]
        type MonitoringAlerts = list[dict[str, str | int | bool | FlextCore.Types.Dict]]
        type MonitoringDashboard = dict[
            str, str | list[dict[str, FlextCore.Types.JsonValue]]
        ]
        type MonitoringReports = dict[str, str | list[FlextCore.Types.Dict]]
        type MonitoringThresholds = dict[str, int | float | bool]

    # =========================================================================
    # SECURITY TYPES - Complex OIC security types
    # =========================================================================

    class Security:
        """Oracle OIC security complex types."""

        type SecurityConfiguration = dict[
            str, str | bool | dict[str, FlextCore.Types.ConfigValue]
        ]
        type SecurityPolicy = dict[
            str, str | bool | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type SecurityCredentials = dict[
            str, str | dict[str, FlextCore.Types.ConfigValue]
        ]
        type SecurityValidation = dict[str, bool | str | FlextCore.Types.StringList]
        type SecurityAudit = list[
            dict[str, str | int | dict[str, FlextCore.Types.JsonValue]]
        ]
        type SecurityCompliance = dict[str, bool | str | FlextCore.Types.Dict]

    # =========================================================================
    # CORE TYPES - Essential Oracle OIC types extending FlextCore.Types
    # =========================================================================

    class Core(FlextCore.Types):
        """Core Oracle OIC extension types extending FlextCore.Types.

        Essential domain-specific types for Oracle OIC integration operations.
        Replaces generic FlextCore.Types.Dict with semantic Oracle OIC types.
        """

        # Configuration and connection types
        type ConfigDict = dict[str, FlextCore.Types.ConfigValue | object]
        type ConnectionDict = dict[str, str | int | bool | FlextCore.Types.Dict]
        type AuthDict = dict[str, str | FlextCore.Types.Dict]
        type ContextDict = FlextCore.Types.Dict

        # Integration and workflow types
        type IntegrationDict = dict[
            str, FlextCore.Types.JsonValue | FlextCore.Types.Dict
        ]
        type WorkflowDict = dict[str, bool | str | FlextCore.Types.Dict]
        type AdapterDict = dict[str, FlextCore.Types.ConfigValue | object]
        type MessageDict = dict[str, str | bool | FlextCore.Types.Dict]

        # Data processing types
        type DataDict = FlextCore.Types.Dict
        type ResponseDict = FlextCore.Types.Dict
        type RequestDict = FlextCore.Types.Dict
        type ResultDict = FlextCore.Types.Dict
        type MetricsDict = FlextCore.Types.Dict
        type HealthDict = FlextCore.Types.Dict

        # Collection types for Oracle OIC operations
        type DataList = list[DataDict]
        type ConfigList = list[ConfigDict]
        type StringList = FlextCore.Types.StringList

    # =========================================================================
    # ORACLE OIC PROJECT TYPES - Domain-specific project types extending FlextCore.Types
    # =========================================================================

    class Project(FlextCore.Types.Project):
        """Oracle OIC extension-specific project types extending FlextCore.Types.Project.

        Adds Oracle OIC integration-specific project types while inheriting
        generic types from FlextCore.Types. Follows domain separation principle:
        Oracle OIC domain owns integration and workflow-specific types.
        """

        # Oracle OIC-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextCore.Types.Project
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
        type OicProjectConfig = dict[str, FlextCore.Types.ConfigValue | object]
        type IntegrationConfig = dict[
            str, str | int | bool | FlextCore.Types.StringList
        ]
        type WorkflowConfig = dict[str, bool | str | FlextCore.Types.Dict]
        type AdapterConfig = dict[str, FlextCore.Types.ConfigValue | object]


# =============================================================================
# PUBLIC API EXPORTS - Oracle OIC TypeVars and types
# =============================================================================

__all__: FlextCore.Types.StringList = [
    "FlextOracleOicTypes",
]
