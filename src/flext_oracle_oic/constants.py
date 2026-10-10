"""Oracle OIC Extension Constants - Unified Constants Pattern.

This module provides centralized constants for the flext-oracle-oic project,
inheriting from c and following FLEXT architectural standards.

FLEXT Unified Constants Pattern: Single FlextOracleOicConstants class
inheriting from c with flat structure and no duplication.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from enum import StrEnum, unique

from flext_auth import FlextAuthConstants

from flext_oracle_oic._constants.base import FlextOracleOicConstantsBase
from flext_oracle_oic._constants.values import FlextOracleOicConstantsValues


class FlextOracleOicConstants(FlextAuthConstants):
    """Oracle OIC Extension constants inheriting from c.

    Provides centralized constants for Oracle OIC Extension operations,
    following FLEXT architectural standards with flat structure and no duplication.

    Usage:
    ```python
    from flext_oracle_oic import FlextOracleOicConstants
    from flext_oracle_oic import t

    # Access Oracle OIC specific constants
    api_version = FlextOracleOicConstants.OracleOic.DEFAULT_API_VERSION
    timeout = FlextOracleOicConstants.DEFAULT_TIMEOUT_SECONDS
    page_size = FlextOracleOicConstants.OracleOic.DEFAULT_PAGE_SIZE
    base_url = FlextOracleOicConstants.OracleOic.DEFAULT_BASE_URL
    ```

    IMPLEMENTATION NOTES:
    - Inherits all constants from c base class
    - Flat structure with nested namespaces for organization
    - Single source of truth for all Oracle OIC Extension constants
    - No duplication with c or other modules
    - Type-safe constants with Final annotations
    - Complete documentation and usage examples
    """

    class OracleOic(
        FlextOracleOicConstantsBase,
        FlextOracleOicConstantsValues.OracleOic,
        FlextOracleOicConstantsValues.OracleOicValidation,
    ):
        """Oracle Integration Cloud specific constants."""

        @unique
        class OICApiVersion(StrEnum):
            """OIC API version enumeration."""

            V1 = "v1"
            V2 = "v2"

        @unique
        class IntegrationStatus(StrEnum):
            """Integration status values.

            DRY Pattern: This StrEnum is the single source of truth for
            integration statuses. All integration status constants and Literal
            types MUST reference this enum.
            """

            ACTIVATED = "ACTIVATED"
            DEACTIVATED = "DEACTIVATED"
            DRAFT = "DRAFT"
            RUNNING = "RUNNING"
            STOPPED = "STOPPED"
            ERROR = "ERROR"

        @unique
        class ConnectionStatus(StrEnum):
            """Connection status values.

            DRY Pattern: This StrEnum is the single source of truth for
            connection statuses. All connection status constants and Literal
            types MUST reference this enum.
            """

            ACTIVE = "ACTIVE"
            INACTIVE = "INACTIVE"
            ERROR = "ERROR"
            UNKNOWN = "unknown"

        @unique
        class ConnectionType(StrEnum):
            """Connection type values.

            DRY Pattern: This StrEnum is the single source of truth for
            connection types. All connection type constants and Literal types
            MUST reference this enum.
            Note: ADAPTER_TYPE_* constants are aliases to these values.
            """

            REST = "REST"
            SOAP = "SOAP"
            DATABASE = "DATABASE"
            FILE = "FILE"
            FTP = "FTP"

        @unique
        class MonitoringHealthStatus(StrEnum):
            """Health status values.

            DRY Pattern: This StrEnum is the single source of truth for health statuses.
            All health status constants and Literal types MUST reference this
            enum.
            """

            HEALTHY = "healthy"
            UNHEALTHY = "unhealthy"
            ERROR = "error"
            UNKNOWN = "unknown"

        @unique
        class MonitoringComponentStatus(StrEnum):
            """Component status values.

            DRY Pattern: This StrEnum is the single source of truth for
            component statuses. All component status constants and Literal
            types MUST reference this enum.
            """

            HEALTHY = "healthy"
            UNHEALTHY = "unhealthy"
            UNKNOWN = "unknown"

        @unique
        class APIMethod(StrEnum):
            """HTTP method values.

            DRY Pattern: This StrEnum is the single source of truth for HTTP methods.
            All HTTP method constants and Literal types MUST reference this enum.
            """

            GET = "GET"
            POST = "POST"
            PUT = "PUT"
            DELETE = "DELETE"
            PATCH = "PATCH"

        @unique
        class ProjectType(StrEnum):
            """Project-type identifiers for Oracle OIC packages."""


c = FlextOracleOicConstants

__all__: list[str] = ["FlextOracleOicConstants", "c"]
