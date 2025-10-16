"""FLEXT Oracle OIC Extension Types - Domain-specific Oracle OIC type definitions.

This module provides Oracle OIC extension-specific type definitions extending FlextTypes.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextTypes properly

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
    """Oracle OIC extension-specific type definitions extending FlextTypes.

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
            str, str | int | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type IntegrationFlow = list[dict[str, str | dict[str, FlextTypes.JsonValue]]]
        type IntegrationMapping = dict[
            str, str | FlextTypes.StringList | FlextTypes.Dict
        ]
        type IntegrationMetadata = dict[
            str, str | int | dict[str, FlextTypes.JsonValue]
        ]
        type IntegrationMonitoring = dict[
            str, bool | int | dict[str, FlextTypes.JsonValue]
        ]
        type IntegrationSecurity = dict[
            str, str | bool | dict[str, FlextTypes.ConfigValue]
        ]

    # =========================================================================
    # CONNECTION TYPES - Complex OIC connection types
    # =========================================================================

    class Connection:
        """Oracle OIC connection complex types."""

        type ConnectionConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type ConnectionPool = dict[str, int | bool | FlextTypes.Dict]
        type ConnectionSecurity = dict[
            str, str | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type ConnectionMonitoring = dict[
            str, int | float | dict[str, FlextTypes.JsonValue]
        ]
        type ConnectionLifecycle = dict[str, str | bool | FlextTypes.Dict]
        type ConnectionValidation = dict[str, bool | str | FlextTypes.StringList]

    # =========================================================================
    # ADAPTER TYPES - Complex OIC adapter types
    # =========================================================================

    class Adapter:
        """Oracle OIC adapter complex types."""

        type AdapterConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type AdapterCapabilities = list[dict[str, str | bool | FlextTypes.Dict]]
        type AdapterMetadata = dict[
            str, str | FlextTypes.StringList | dict[str, FlextTypes.JsonValue]
        ]
        type AdapterBinding = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type AdapterTransformation = list[dict[str, str | FlextTypes.Dict]]
        type AdapterValidation = dict[
            str, bool | FlextTypes.StringList | FlextTypes.Dict
        ]

    # =========================================================================
    # MESSAGE PROCESSING TYPES - Complex message handling types
    # =========================================================================

    class MessageProcessing:
        """Oracle OIC message processing complex types."""

        type MessageConfiguration = dict[
            str, str | int | dict[str, FlextTypes.ConfigValue]
        ]
        type MessageFormat = dict[str, str | bool | FlextTypes.Dict]
        type MessageTransformation = list[
            dict[str, str | dict[str, FlextTypes.JsonValue]]
        ]
        type MessageValidation = dict[
            str, bool | str | FlextTypes.StringList | FlextTypes.Dict
        ]
        type MessageRouting = dict[
            str, str | FlextTypes.StringList | dict[str, FlextTypes.JsonValue]
        ]
        type MessageTracking = dict[str, str | int | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # TRANSFORMATION TYPES - Complex data transformation types
    # =========================================================================

    class Transformation:
        """Oracle OIC transformation complex types."""

        type TransformationRule = dict[
            str, str | FlextTypes.StringList | FlextTypes.Dict
        ]
        type TransformationMapping = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type TransformationValidation = dict[str, bool | str | FlextTypes.StringList]
        type TransformationEngine = dict[
            str, str | bool | dict[str, FlextTypes.ConfigValue]
        ]
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

        type MonitoringConfiguration = dict[
            str, bool | str | int | dict[str, FlextTypes.ConfigValue]
        ]
        type MonitoringMetrics = dict[
            str, int | float | dict[str, FlextTypes.JsonValue]
        ]
        type MonitoringAlerts = list[dict[str, str | int | bool | FlextTypes.Dict]]
        type MonitoringDashboard = dict[
            str, str | list[dict[str, FlextTypes.JsonValue]]
        ]
        type MonitoringReports = dict[str, str | list[FlextTypes.Dict]]
        type MonitoringThresholds = dict[str, int | float | bool]

    # =========================================================================
    # SECURITY TYPES - Complex OIC security types
    # =========================================================================

    class Security:
        """Oracle OIC security complex types."""

        type SecurityConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type SecurityPolicy = dict[
            str, str | bool | FlextTypes.StringList | FlextTypes.Dict
        ]
        type SecurityCredentials = dict[str, str | dict[str, FlextTypes.ConfigValue]]
        type SecurityValidation = dict[str, bool | str | FlextTypes.StringList]
        type SecurityAudit = list[
            dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        ]
        type SecurityCompliance = dict[str, bool | str | FlextTypes.Dict]

    # =========================================================================
    # CORE TYPES - Essential Oracle OIC types extending FlextTypes
    # =========================================================================

    class OicCore:
        """Core Oracle OIC extension types.

        Essential domain-specific types for Oracle OIC integration operations.
        Replaces generic FlextTypes.Dict with semantic Oracle OIC types.
        """

        # Configuration and connection types
        type ConfigDict = dict[str, FlextTypes.ConfigValue | object]
        type ConnectionDict = dict[str, str | int | bool | FlextTypes.Dict]
        type AuthDict = dict[str, str | FlextTypes.Dict]
        type ContextDict = FlextTypes.Dict

        # Integration and workflow types
        type IntegrationDict = dict[str, FlextTypes.JsonValue | FlextTypes.Dict]
        type WorkflowDict = dict[str, bool | str | FlextTypes.Dict]
        type AdapterDict = dict[str, FlextTypes.ConfigValue | object]
        type MessageDict = dict[str, str | bool | FlextTypes.Dict]

        # Data processing types
        type DataDict = FlextTypes.Dict
        type ResponseDict = FlextTypes.Dict
        type RequestDict = FlextTypes.Dict
        type ResultDict = FlextTypes.Dict
        type MetricsDict = FlextTypes.Dict
        type HealthDict = FlextTypes.Dict

        # Collection types for Oracle OIC operations
        type DataList = list[DataDict]
        type ConfigList = list[ConfigDict]
        type StringList = FlextTypes.StringList

    # =========================================================================
    # ORACLE OIC PROJECT TYPES - Domain-specific project types extending FlextTypes
    # =========================================================================

    class OicProject:
        """Oracle OIC extension-specific project types.

        Adds Oracle OIC integration-specific project types.
        Follows domain separation principle: Oracle OIC domain owns integration
        and workflow-specific types.
        """

        # Oracle OIC-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextTypes.Project
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
        type OicProjectConfig = dict[str, FlextTypes.ConfigValue | object]
        type IntegrationConfig = dict[str, str | int | bool | FlextTypes.StringList]
        type WorkflowConfig = dict[str, bool | str | FlextTypes.Dict]
        type AdapterConfig = dict[str, FlextTypes.ConfigValue | object]


# =============================================================================
# PUBLIC API EXPORTS - Oracle OIC TypeVars and types
# =============================================================================

__all__: FlextTypes.StringList = [
    "FlextOracleOicTypes",
]
