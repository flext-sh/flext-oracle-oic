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

from collections.abc import Mapping, Sequence

from flext_core import FlextTypes

from flext_oracle_oic.constants import c


class FlextOracleOicTypes(FlextTypes):
    """Oracle OIC extension-specific type definitions extending t.

    Domain-specific type system for Oracle OIC integration operations.
    Contains ONLY complex OIC-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class OracleOic:
        """Oracle OIC integration complex types."""

        type IntegrationConfiguration = Mapping[
            str,
            str | int | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type IntegrationFlow = Sequence[
            Mapping[str, str | Mapping[str, FlextTypes.NormalizedValue]]
        ]
        type IntegrationMapping = Mapping[
            str,
            str | Sequence[str] | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type IntegrationMetadata = Mapping[
            str,
            str | int | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type IntegrationMonitoring = Mapping[
            str,
            bool | int | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type IntegrationSecurity = Mapping[
            str,
            str | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]

    class Connection:
        """Oracle OIC connection complex types."""

        type ConnectionConfiguration = Mapping[
            str,
            str | int | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type ConnectionPool = Mapping[
            str,
            int | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type ConnectionSecurity = Mapping[
            str,
            str | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type ConnectionMonitoring = Mapping[
            str,
            int | float | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type ConnectionLifecycle = Mapping[
            str,
            str | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type ConnectionValidation = Mapping[str, bool | str | Sequence[str]]

    class Adapter:
        """Oracle OIC adapter complex types."""

        type AdapterConfiguration = Mapping[
            str,
            str | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type AdapterCapabilities = Sequence[
            Mapping[str, str | bool | Mapping[str, FlextTypes.NormalizedValue]]
        ]
        type AdapterMetadata = Mapping[
            str,
            str | Sequence[str] | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type AdapterBinding = Mapping[
            str, str | Mapping[str, FlextTypes.NormalizedValue]
        ]
        type AdapterTransformation = Sequence[
            Mapping[str, str | Mapping[str, FlextTypes.NormalizedValue]]
        ]
        type AdapterValidation = Mapping[
            str,
            bool | Sequence[str] | Mapping[str, FlextTypes.NormalizedValue],
        ]

    class MessageProcessing:
        """Oracle OIC message processing complex types."""

        type MessageConfiguration = Mapping[
            str,
            str | int | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type MessageFormat = Mapping[
            str,
            str | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type MessageTransformation = Sequence[
            Mapping[str, str | Mapping[str, FlextTypes.NormalizedValue]]
        ]
        type MessageValidation = Mapping[
            str,
            bool | str | Sequence[str] | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type MessageRouting = Mapping[
            str,
            str | Sequence[str] | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type MessageTracking = Mapping[
            str,
            str | int | Mapping[str, FlextTypes.NormalizedValue],
        ]

    class Transformation:
        """Oracle OIC transformation complex types."""

        type TransformationRule = Mapping[
            str,
            str | Sequence[str] | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type TransformationMapping = Mapping[
            str,
            str | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type TransformationValidation = Mapping[str, bool | str | Sequence[str]]
        type TransformationEngine = Mapping[
            str,
            str | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type TransformationResult = Mapping[
            str,
            bool
            | FlextTypes.NormalizedValue
            | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type TransformationMetrics = Mapping[
            str,
            int | float | Mapping[str, FlextTypes.NormalizedValue],
        ]

    class Monitoring:
        """Oracle OIC monitoring complex types."""

        type MonitoringConfiguration = Mapping[
            str,
            bool | str | int | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type MonitoringMetrics = Mapping[
            str,
            int | float | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type MonitoringAlerts = Sequence[
            Mapping[str, str | int | bool | Mapping[str, FlextTypes.NormalizedValue]]
        ]
        type MonitoringDashboard = Mapping[
            str,
            str | Sequence[Mapping[str, FlextTypes.NormalizedValue]],
        ]
        type MonitoringReports = Mapping[
            str,
            str | Sequence[Mapping[str, FlextTypes.NormalizedValue]],
        ]
        type MonitoringThresholds = Mapping[str, int | float | bool]

    class Security:
        """Oracle OIC security complex types."""

        type SecurityConfiguration = Mapping[
            str,
            str | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type SecurityPolicy = Mapping[
            str,
            str | bool | Sequence[str] | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type SecurityCredentials = Mapping[
            str,
            str | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type SecurityValidation = Mapping[str, bool | str | Sequence[str]]
        type SecurityAudit = Sequence[
            Mapping[str, str | int | Mapping[str, FlextTypes.NormalizedValue]]
        ]
        type SecurityCompliance = Mapping[
            str,
            bool | str | Mapping[str, FlextTypes.NormalizedValue],
        ]

    class OicCore:
        """Core Oracle OIC extension types.

        Essential domain-specific types for Oracle OIC integration operations.
        Replaces generic Mapping[str, FlextTypes.NormalizedValue] with semantic Oracle OIC types.
        """

        type ConfigDict = Mapping[str, FlextTypes.NormalizedValue]
        type ConnectionDict = Mapping[
            str,
            str | int | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type AuthDict = Mapping[str, str | Mapping[str, FlextTypes.NormalizedValue]]
        type ContextDict = Mapping[str, FlextTypes.NormalizedValue]
        type IntegrationDict = Mapping[
            str,
            FlextTypes.NormalizedValue | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type WorkflowDict = Mapping[
            str,
            bool | str | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type AdapterDict = Mapping[str, FlextTypes.NormalizedValue]
        type MessageDict = Mapping[
            str,
            str | bool | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type DataDict = Mapping[str, FlextTypes.NormalizedValue]
        type ResponseDict = Mapping[str, FlextTypes.NormalizedValue]
        type RequestDict = Mapping[str, FlextTypes.NormalizedValue]
        type ResultDict = Mapping[str, FlextTypes.NormalizedValue]
        type MetricsDict = Mapping[str, FlextTypes.NormalizedValue]
        type HealthDict = Mapping[str, FlextTypes.NormalizedValue]
        type DataList = Sequence[Mapping[str, FlextTypes.NormalizedValue]]
        type ConfigList = Sequence[Mapping[str, FlextTypes.NormalizedValue]]
        type StringList = Sequence[str]

    class Project:
        """Oracle OIC extension-specific project types.

        Adds Oracle OIC integration-specific project types.
        Follows domain separation principle: Oracle OIC domain owns integration
        and workflow-specific types.
        """

        type ProjectType = c.ProjectType
        type OicProjectConfig = Mapping[str, FlextTypes.NormalizedValue]
        type IntegrationConfig = Mapping[str, str | int | bool | Sequence[str]]
        type WorkflowConfig = Mapping[
            str,
            bool | str | Mapping[str, FlextTypes.NormalizedValue],
        ]
        type AdapterConfig = Mapping[str, FlextTypes.NormalizedValue]


t = FlextOracleOicTypes
__all__ = ["FlextOracleOicTypes", "t"]
