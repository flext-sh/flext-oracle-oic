"""Oracle OIC Extension Constants - Unified Constants Pattern.

This module provides centralized constants for the flext-oracle-oic project,
inheriting from FlextConstants and following FLEXT architectural standards.

FLEXT Unified Constants Pattern: Single FlextOracleOicConstants class
inheriting from FlextConstants with flat structure and no duplication.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import re
from collections.abc import Mapping
from enum import StrEnum, unique
from types import MappingProxyType
from typing import Final

from flext_core import FlextConstants


class FlextOracleOicConstants(FlextConstants):
    """Oracle OIC Extension constants inheriting from FlextConstants.

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

    # Access inherited FlextConstants
    http_ok = FlextOracleOicConstants.Platform.HTTP_STATUS_OK
    default_timeout = FlextOracleOicConstants.TIMEOUT
    ```

    IMPLEMENTATION NOTES:
    - Inherits all constants from FlextConstants base class
    - Flat structure with nested namespaces for organization
    - Single source of truth for all Oracle OIC Extension constants
    - No duplication with FlextConstants or other modules
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
        DEFAULT_MAX_DELAY_SECONDS: Final[float] = 60.0
        MIN_REQUEST_TIMEOUT: Final[int] = 1
        MIN_MAX_RETRIES: Final[int] = 0
        DEFAULT_VERIFY_SSL: Final[bool] = True

    class Auth:
        """Oracle OIC Authentication constants."""

        DEFAULT_OAUTH_SCOPE: Final[str] = ""

        @unique
        class AuthType(StrEnum):
            """Authentication types.

            DRY Pattern: This StrEnum is the single source of truth for authentication types.
            All authentication type-related constants and Literal types MUST reference this enum.
            """

            OAUTH2 = "oauth2"
            BASIC = "basic"
            BEARER = "bearer"

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
            PUBLISHED = "PUBLISHED"
            RUNNING = "RUNNING"
            STOPPED = "STOPPED"
            ERROR = "ERROR"

        DEFAULT_VERSION: Final[str] = "01.00.0000"
        DEFAULT_VERSION_FALLBACK: Final[str] = "01.00.0000"
        DEFAULT_LAST_UPDATED: Final[str] = ""
        DEFAULT_ACTIVATED_BY: Final[str] = ""
        PATTERN_MESSAGE_ROUTER: Final[str] = "message_router"
        PATTERN_SCATTER_GATHER: Final[str] = "scatter_gather"

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
            SFTP = "SFTP"

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
        CONTENT_TYPE_JSON: Final[str] = "application/json"
        ENDPOINT_HEALTH: Final[str] = "/ic/api/integration/v1/health"
        HTTP_STATUS_OK: Final[int] = 200

    class OICPatterns:
        """Oracle OIC Integration Pattern constants."""

        @unique
        class PatternStatus(StrEnum):
            """Pattern status values.

            DRY Pattern: This StrEnum is the single source of truth for pattern statuses.
            All pattern status-related constants and Literal types MUST reference this enum.
            """

            PROCESSED = "processed"
            FAILED = "failed"
            PENDING = "pending"

        PATTERN_MESSAGE_ROUTER: Final[str] = "message_router"
        PATTERN_SCATTER_GATHER: Final[str] = "scatter_gather"
        PATTERN_MESSAGE_ID_UNKNOWN: Final[str] = "unknown"
        PATTERN_REQUEST_ID_UNKNOWN: Final[str] = "unknown"

    class OICErrors:
        """Oracle OIC Extension specific error constants."""

    class OICMessages:
        """Oracle OIC Extension specific message constants."""

    class OracleOicValidation:
        """Oracle OIC validation constants (named to avoid overriding FlextConstants)."""

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
        VERSION_PATTERN: Final[re.Pattern[str]] = re.compile(
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
        SUPPORTED_PATTERNS: Final[frozenset[str]] = frozenset({
            "message_router",
            "scatter_gather",
            "publish_subscribe",
            "request_reply",
        })
        MIN_ENDPOINTS_FOR_ROUTER: Final[int] = 2
        PERFORMANCE_THRESHOLDS: Final[Mapping[str, float]] = MappingProxyType({
            "response_time_ms": 5000.0,
            "success_rate": 0.95,
            "error_rate": 0.05,
        })

    @unique
    class ProjectType(StrEnum):
        """Project-type identifiers for Oracle OIC packages."""

        OIC_INTEGRATION = "oic-integration"
        INTEGRATION_FLOW = "integration-flow"
        OIC_ADAPTER = "oic-adapter"
        MESSAGE_PROCESSOR = "message-processor"
        TRANSFORMATION_SERVICE = "transformation-service"
        OIC_CONNECTOR = "oic-connector"
        WORKFLOW_ENGINE = "workflow-engine"
        INTEGRATION_PLATFORM = "integration-platform"
        OIC_MONITOR = "oic-monitor"
        INTEGRATION_GATEWAY = "integration-gateway"
        OIC_SECURITY = "oic-security"
        ADAPTER_FRAMEWORK = "adapter-framework"
        INTEGRATION_API = "integration-api"
        OIC_EXTENSION = "oic-extension"
        WORKFLOW_DESIGNER = "workflow-designer"
        INTEGRATION_HUB = "integration-hub"


c = FlextOracleOicConstants

__all__: list[str] = ["FlextOracleOicConstants", "c"]
