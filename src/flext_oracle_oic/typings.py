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

from collections.abc import Mapping

from flext_core import FlextTypes

from flext_oracle_oic import c


class FlextOracleOicTypes(FlextTypes):
    """Oracle OIC extension-specific type definitions extending t.

    Domain-specific type system for Oracle OIC integration operations.
    Contains ONLY complex OIC-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class OracleOic:
        """Oracle OIC integration complex types."""

        type IntegrationConfiguration = dict[
            str,
            str | int | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type IntegrationFlow = list[
            dict[str, str | Mapping[str, FlextTypes.NormalizedValue]]
        ]
        type IntegrationMapping = dict[
            str,
            str | list[str] | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type IntegrationMetadata = dict[
            str,
            str | int | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type IntegrationMonitoring = dict[
            str,
            bool | int | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type IntegrationSecurity = dict[
            str,
            str | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]

    class Connection:
        """Oracle OIC connection complex types."""

        type ConnectionConfiguration = dict[
            str,
            str | int | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type ConnectionPool = dict[
            str,
            int | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type ConnectionSecurity = dict[
            str,
            str | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type ConnectionMonitoring = dict[
            str,
            int | float | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type ConnectionLifecycle = dict[
            str,
            str | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type ConnectionValidation = dict[str, bool | str | list[str]]

    class Adapter:
        """Oracle OIC adapter complex types."""

        type AdapterConfiguration = dict[
            str,
            str | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type AdapterCapabilities = list[
            dict[str, str | bool | Mapping[str, FlextTypes.NormalizedValue]]
        ]
        type AdapterMetadata = dict[
            str,
            str | list[str] | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type AdapterBinding = dict[str, str | Mapping[str, FlextTypes.NormalizedValue]]
        type AdapterTransformation = list[
            dict[str, str | Mapping[str, FlextTypes.NormalizedValue]]
        ]
        type AdapterValidation = dict[
            str,
            bool | list[str] | Mapping[str, FlextTypes.NormalizedValue],
        ]

    class MessageProcessing:
        """Oracle OIC message processing complex types."""

        type MessageConfiguration = dict[
            str,
            str | int | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type MessageFormat = dict[
            str,
            str | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type MessageTransformation = list[
            dict[str, str | Mapping[str, FlextTypes.NormalizedValue]]
        ]
        type MessageValidation = dict[
            str,
            bool | str | list[str] | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type MessageRouting = dict[
            str,
            str | list[str] | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type MessageTracking = dict[
            str,
            str | int | Mapping[str, FlextTypes.NormalizedValue],
        ]

    class Transformation:
        """Oracle OIC transformation complex types."""

        type TransformationRule = dict[
            str,
            str | list[str] | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type TransformationMapping = dict[
            str,
            str | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type TransformationValidation = dict[str, bool | str | list[str]]
        type TransformationEngine = dict[
            str,
            str | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type TransformationResult = dict[
            str,
            bool
            | FlextTypes.NormalizedValue
            | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type TransformationMetrics = dict[
            str,
            int | float | Mapping[str, FlextTypes.NormalizedValue],
        ]

    class Monitoring:
        """Oracle OIC monitoring complex types."""

        type MonitoringConfiguration = dict[
            str,
            bool | str | int | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type MonitoringMetrics = dict[
            str,
            int | float | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type MonitoringAlerts = list[
            dict[str, str | int | bool | Mapping[str, FlextTypes.NormalizedValue]]
        ]
        type MonitoringDashboard = dict[
            str,
            str | list[Mapping[str, FlextTypes.NormalizedValue]],
        ]
        type MonitoringReports = dict[
            str,
            str | list[Mapping[str, FlextTypes.NormalizedValue]],
        ]
        type MonitoringThresholds = dict[str, int | float | bool]

    class Security:
        """Oracle OIC security complex types."""

        type SecurityConfiguration = dict[
            str,
            str | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type SecurityPolicy = dict[
            str,
            str | bool | list[str] | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type SecurityCredentials = dict[
            str,
            str | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type SecurityValidation = dict[str, bool | str | list[str]]
        type SecurityAudit = list[
            dict[str, str | int | Mapping[str, FlextTypes.NormalizedValue]]
        ]
        type SecurityCompliance = dict[
            str,
            bool | str | Mapping[str, FlextTypes.NormalizedValue],
        ]

    class OicCore:
        """Core Oracle OIC extension types.

        Essential domain-specific types for Oracle OIC integration operations.
        Replaces generic dict[str, FlextTypes.NormalizedValue] with semantic Oracle OIC types.
        """

        type ConfigDict = dict[str, FlextTypes.NormalizedValue]
        type ConnectionDict = dict[
            str,
            str | int | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type AuthDict = dict[str, str | Mapping[str, FlextTypes.NormalizedValue]]
        type ContextDict = dict[str, FlextTypes.NormalizedValue]
        type IntegrationDict = dict[
            str,
            FlextTypes.NormalizedValue | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type WorkflowDict = dict[
            str,
            bool | str | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type AdapterDict = dict[str, FlextTypes.NormalizedValue]
        type MessageDict = dict[
            str,
            str | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type DataDict = dict[str, FlextTypes.NormalizedValue]
        type ResponseDict = dict[str, FlextTypes.NormalizedValue]
        type RequestDict = dict[str, FlextTypes.NormalizedValue]
        type ResultDict = dict[str, FlextTypes.NormalizedValue]
        type MetricsDict = dict[str, FlextTypes.NormalizedValue]
        type HealthDict = dict[str, FlextTypes.NormalizedValue]
        type DataList = list[dict[str, FlextTypes.NormalizedValue]]
        type ConfigList = list[dict[str, FlextTypes.NormalizedValue]]
        type StringList = list[str]

    class Project:
        """Oracle OIC extension-specific project types.

        Adds Oracle OIC integration-specific project types.
        Follows domain separation principle: Oracle OIC domain owns integration
        and workflow-specific types.
        """

        type ProjectType = c.ProjectType
        type OicProjectConfig = dict[str, FlextTypes.NormalizedValue]
        type IntegrationConfig = dict[str, str | int | bool | list[str]]
        type WorkflowConfig = dict[
            str,
            bool | str | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type AdapterConfig = dict[str, FlextTypes.NormalizedValue]


t = FlextOracleOicTypes
__all__ = ["FlextOracleOicTypes", "t"]
