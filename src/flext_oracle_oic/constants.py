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

from ._constants.base import FlextOracleOicConstantsBase
from ._constants.values import FlextOracleOicConstantsValues


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

    @unique
    class OICApiVersion(StrEnum):
        """OIC API version enumeration."""

        V1 = "v1"
        V2 = "v2"

    class OracleOic(
        FlextOracleOicConstantsBase, FlextOracleOicConstantsValues.OracleOic
    ):
        """Oracle Integration Cloud specific constants."""

    class Auth(FlextAuthConstants.Auth, FlextOracleOicConstantsValues.Auth):
        """Oracle OIC Authentication constants extending base auth namespace."""

    class Cli(FlextOracleOicConstantsValues.Cli, FlextAuthConstants.Cli):
        """Oracle OIC CLI constants extending the shared CLI namespace.

        OIC-owned scalars are re-exported from ``_constants``.
        """

    class Integration(FlextOracleOicConstantsValues.Integration):
        """Oracle OIC Integration constants.

        ``DEFAULT_VERSION`` is owned by ``flext_oracle_oic._constants`` and
        inherited through this facade subclass.
        """

        @unique
        class Status(StrEnum):
            """Integration status values.

            DRY Pattern: This StrEnum is the single source of truth for integration statuses.
            All integration status-related constants and Literal types MUST reference this enum.
            """

            ACTIVATED = "ACTIVATED"
            DEACTIVATED = "DEACTIVATED"
            DRAFT = "DRAFT"
            RUNNING = "RUNNING"
            STOPPED = "STOPPED"
            ERROR = "ERROR"

    class Connection:
        """Oracle OIC Connection constants."""

        @unique
        class Status(StrEnum):
            """Connection status values.

            DRY Pattern: This StrEnum is the single source of truth for connection statuses.
            All connection status-related constants and Literal types MUST reference this enum.
            """

            ACTIVE = "ACTIVE"
            INACTIVE = "INACTIVE"
            ERROR = "ERROR"
            UNKNOWN = "unknown"

        @unique
        class Type(StrEnum):
            """Connection type values.

            DRY Pattern: This StrEnum is the single source of truth for connection types.
            All connection type-related constants and Literal types MUST reference this enum.
            Note: ADAPTER_TYPE_* constants are aliases to these values.
            """

            REST = "REST"
            SOAP = "SOAP"
            DATABASE = "DATABASE"
            FILE = "FILE"
            FTP = "FTP"

    class Monitoring(FlextOracleOicConstantsValues.Monitoring):
        """Oracle OIC Monitoring constants.

        ``COMPONENT_DATABASE`` is owned by ``flext_oracle_oic._constants`` and
        inherited through this facade subclass.
        """

        @unique
        class HealthStatus(StrEnum):
            """Health status values.

            DRY Pattern: This StrEnum is the single source of truth for health statuses.
            All health status-related constants and Literal types MUST reference this enum.
            """

            HEALTHY = "healthy"
            UNHEALTHY = "unhealthy"
            ERROR = "error"
            UNKNOWN = "unknown"

        @unique
        class ComponentStatus(StrEnum):
            """Component status values.

            DRY Pattern: This StrEnum is the single source of truth for component statuses.
            All component status-related constants and Literal types MUST reference this enum.
            """

            HEALTHY = "healthy"
            UNHEALTHY = "unhealthy"
            UNKNOWN = "unknown"

    class API(FlextOracleOicConstantsValues.API):
        """Oracle OIC API constants.

        ``HTTP_ERROR_STATUS_THRESHOLD`` is owned by
        ``flext_oracle_oic._constants`` and inherited through this facade
        subclass.
        """

        @unique
        class Method(StrEnum):
            """HTTP method values.

            DRY Pattern: This StrEnum is the single source of truth for HTTP methods.
            All HTTP method-related constants and Literal types MUST reference this enum.
            """

            GET = "GET"
            POST = "POST"
            PUT = "PUT"
            DELETE = "DELETE"
            PATCH = "PATCH"

    class OracleOicValidation(FlextOracleOicConstantsValues.OracleOicValidation):
        """Oracle OIC validation constants (named to avoid overriding c).

        All scalars, patterns and whitelists are owned by
        ``flext_oracle_oic._constants`` and inherited through this facade
        subclass.
        """

    @unique
    class ProjectType(StrEnum):
        """Project-type identifiers for Oracle OIC packages."""


c = FlextOracleOicConstants

__all__: list[str] = ["FlextOracleOicConstants", "c"]
