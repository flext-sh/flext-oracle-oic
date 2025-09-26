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
class FlextOracleOicExtTypes(FlextTypes):
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
            str, str | int | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type IntegrationFlow = list[
            dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        ]
        type IntegrationMapping = dict[str, str | list[str] | dict[str, object]]
        type IntegrationMetadata = dict[
            str, str | int | dict[str, FlextTypes.Core.JsonValue]
        ]
        type IntegrationMonitoring = dict[
            str, bool | int | dict[str, FlextTypes.Core.JsonValue]
        ]
        type IntegrationSecurity = dict[
            str, str | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]

    # =========================================================================
    # CONNECTION TYPES - Complex OIC connection types
    # =========================================================================

    class Connection:
        """Oracle OIC connection complex types."""

        type ConnectionConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type ConnectionPool = dict[str, int | bool | dict[str, object]]
        type ConnectionSecurity = dict[
            str, str | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type ConnectionMonitoring = dict[
            str, int | float | dict[str, FlextTypes.Core.JsonValue]
        ]
        type ConnectionLifecycle = dict[str, str | bool | dict[str, object]]
        type ConnectionValidation = dict[str, bool | str | list[str]]

    # =========================================================================
    # ADAPTER TYPES - Complex OIC adapter types
    # =========================================================================

    class Adapter:
        """Oracle OIC adapter complex types."""

        type AdapterConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type AdapterCapabilities = list[dict[str, str | bool | dict[str, object]]]
        type AdapterMetadata = dict[
            str, str | list[str] | dict[str, FlextTypes.Core.JsonValue]
        ]
        type AdapterBinding = dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        type AdapterTransformation = list[dict[str, str | dict[str, object]]]
        type AdapterValidation = dict[str, bool | list[str] | dict[str, object]]

    # =========================================================================
    # MESSAGE PROCESSING TYPES - Complex message handling types
    # =========================================================================

    class MessageProcessing:
        """Oracle OIC message processing complex types."""

        type MessageConfiguration = dict[
            str, str | int | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type MessageFormat = dict[str, str | bool | dict[str, object]]
        type MessageTransformation = list[
            dict[str, str | dict[str, FlextTypes.Core.JsonValue]]
        ]
        type MessageValidation = dict[str, bool | str | list[str] | dict[str, object]]
        type MessageRouting = dict[
            str, str | list[str] | dict[str, FlextTypes.Core.JsonValue]
        ]
        type MessageTracking = dict[
            str, str | int | dict[str, FlextTypes.Core.JsonValue]
        ]

    # =========================================================================
    # TRANSFORMATION TYPES - Complex data transformation types
    # =========================================================================

    class Transformation:
        """Oracle OIC transformation complex types."""

        type TransformationRule = dict[str, str | list[str] | dict[str, object]]
        type TransformationMapping = dict[
            str, str | dict[str, FlextTypes.Core.JsonValue]
        ]
        type TransformationValidation = dict[str, bool | str | list[str]]
        type TransformationEngine = dict[
            str, str | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type TransformationResult = dict[
            str, bool | object | dict[str, FlextTypes.Core.JsonValue]
        ]
        type TransformationMetrics = dict[
            str, int | float | dict[str, FlextTypes.Core.JsonValue]
        ]

    # =========================================================================
    # MONITORING TYPES - Complex OIC monitoring types
    # =========================================================================

    class Monitoring:
        """Oracle OIC monitoring complex types."""

        type MonitoringConfiguration = dict[
            str, bool | str | int | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type MonitoringMetrics = dict[
            str, int | float | dict[str, FlextTypes.Core.JsonValue]
        ]
        type MonitoringAlerts = list[dict[str, str | int | bool | dict[str, object]]]
        type MonitoringDashboard = dict[
            str, str | list[dict[str, FlextTypes.Core.JsonValue]]
        ]
        type MonitoringReports = dict[str, str | list[dict[str, object]]]
        type MonitoringThresholds = dict[str, int | float | bool]

    # =========================================================================
    # SECURITY TYPES - Complex OIC security types
    # =========================================================================

    class Security:
        """Oracle OIC security complex types."""

        type SecurityConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type SecurityPolicy = dict[str, str | bool | list[str] | dict[str, object]]
        type SecurityCredentials = dict[
            str, str | dict[str, FlextTypes.Core.ConfigValue]
        ]
        type SecurityValidation = dict[str, bool | str | list[str]]
        type SecurityAudit = list[
            dict[str, str | int | dict[str, FlextTypes.Core.JsonValue]]
        ]
        type SecurityCompliance = dict[str, bool | str | dict[str, object]]

    # =========================================================================
    # ORACLE OIC PROJECT TYPES - Domain-specific project types extending FlextTypes
    # =========================================================================

    class Project(FlextTypes.Project):
        """Oracle OIC extension-specific project types extending FlextTypes.Project.

        Adds Oracle OIC integration-specific project types while inheriting
        generic types from FlextTypes. Follows domain separation principle:
        Oracle OIC domain owns integration and workflow-specific types.
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
        type OicProjectConfig = dict[str, FlextTypes.Core.ConfigValue | object]
        type IntegrationConfig = dict[str, str | int | bool | list[str]]
        type WorkflowConfig = dict[str, bool | str | dict[str, object]]
        type AdapterConfig = dict[str, FlextTypes.Core.ConfigValue | object]


# =============================================================================
# PUBLIC API EXPORTS - Oracle OIC TypeVars and types
# =============================================================================

__all__: list[str] = [
    "FlextOracleOicExtTypes",
]
