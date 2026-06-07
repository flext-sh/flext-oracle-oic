"""Oracle OIC Extension Constants - Unified Constants Pattern.

This module provides centralized constants for the flext-oracle-oic project,
inheriting from c and following FLEXT architectural standards.

FLEXT Unified Constants Pattern: Single FlextOracleOicConstants class
inheriting from c with flat structure and no duplication.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import re
from collections.abc import (
    Mapping,
)
from enum import StrEnum, unique
from types import MappingProxyType
from typing import TYPE_CHECKING, Final

from flext_auth import c

if TYPE_CHECKING:
    from flext_oracle_oic import t


class FlextOracleOicConstants(c):
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

    class OracleOic:
        """Oracle Integration Cloud specific constants."""

        DEFAULT_BASE_URL: Final[str] = (
            "https://localhost.integration.ocp.oraclecloud.com"
        )
        DEFAULT_API_VERSION: Final[str] = "v1"
        DEFAULT_PAGE_SIZE: Final[int] = 100
        MIN_PAGE_SIZE: Final[int] = 1
        MIN_REQUEST_TIMEOUT: Final[int] = 1
        DEFAULT_VERIFY_SSL: Final[bool] = True

    class Auth(c.Auth):
        """Oracle OIC Authentication constants extending base auth namespace."""

        DEFAULT_OAUTH_SCOPE: Final[str] = ""

    class Integration:
        """Oracle OIC Integration constants."""

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

        DEFAULT_VERSION: Final[str] = "01.00.0000"
        DEFAULT_VERSION_FALLBACK: Final[str] = "01.00.0000"

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

    class Monitoring:
        """Oracle OIC Monitoring constants."""

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

        COMPONENT_DATABASE: Final[str] = "database"
        COMPONENT_MESSAGING: Final[str] = "messaging"
        COMPONENT_INTEGRATION_ENGINE: Final[str] = "integration_engine"

    class API:
        """Oracle OIC API constants."""

        HTTP_ERROR_STATUS_THRESHOLD: Final[int] = 400

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

        HEADER_CONTENT_TYPE: Final[str] = "Content-Type"
        HEADER_AUTHORIZATION: Final[str] = "Authorization"
        HEADER_ACCEPT: Final[str] = "Accept"
        ENDPOINT_HEALTH: Final[str] = "/ic/api/integration/v1/health"
        HTTP_STATUS_OK: Final[int] = 200

    class OracleOicValidation:
        """Oracle OIC validation constants (named to avoid overriding c)."""

        # === Regex authority for the OracleOicValidation domain ===
        INTEGRATION_NAME_RE: Final[t.RegexPattern] = re.compile(r"^[a-zA-Z0-9_\-\s]+$")
        CLIENT_ID_RE: Final[t.RegexPattern] = re.compile(r"^[a-zA-Z0-9_\-\.]+$")

        MIN_INTEGRATION_NAME_LENGTH: Final[int] = 1
        MAX_INTEGRATION_NAME_LENGTH: Final[int] = 100
        VALID_INTEGRATION_STATUSES: Final[frozenset[str]] = frozenset({
            "ACTIVATED",
            "DEACTIVATED",
            "DRAFT",
            "PUBLISHED",
            "RUNNING",
            "STOPPED",
            "ERROR",
        })
        VERSION_PATTERN: Final[t.RegexPattern] = re.compile(
            r"^\\d{2}\\.\\d{2}\\.\\d{4}$",
        )
        VALID_CONNECTION_TYPES: Final[frozenset[str]] = frozenset({
            "REST",
            "SOAP",
            "DATABASE",
            "FILE",
            "FTP",
            "SFTP",
        })
        VALID_CONNECTION_STATUSES: Final[frozenset[str]] = frozenset({
            "ACTIVE",
            "INACTIVE",
            "ERROR",
            "unknown",
        })
        MIN_CLIENT_ID_LENGTH: Final[int] = 1
        MIN_CLIENT_SECRET_LENGTH: Final[int] = 8
        PERFORMANCE_THRESHOLDS: Final[Mapping[str, float]] = MappingProxyType({
            "response_time_ms": 5000.0,
            "success_rate": 0.95,
            "error_rate": 0.05,
        })

    @unique
    class ProjectType(StrEnum):
        """Project-type identifiers for Oracle OIC packages."""


c = FlextOracleOicConstants

__all__: list[str] = ["FlextOracleOicConstants", "c"]
