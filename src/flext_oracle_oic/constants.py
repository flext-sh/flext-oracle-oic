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
from enum import StrEnum
from typing import Final, Literal

from flext_core import FlextConstants


class FlextOracleOicConstants(FlextConstants):
    """Oracle OIC Extension constants inheriting from FlextConstants.

    Provides centralized constants for Oracle OIC Extension operations,
    following FLEXT architectural standards with flat structure and no duplication.

    Usage:
    ```python
    from flext_oracle_oic.constants import FlextOracleOicConstants

    # Access Oracle OIC specific constants
    api_version = FlextOracleOicConstants.OIC.DEFAULT_API_VERSION
    timeout = FlextOracleOicConstants.OIC.DEFAULT_TIMEOUT
    page_size = FlextOracleOicConstants.OIC.DEFAULT_PAGE_SIZE

    # Access inherited FlextConstants
    http_ok = FlextOracleOicConstants.Platform.HTTP_STATUS_OK
    default_timeout = FlextOracleOicConstants.Defaults.TIMEOUT
    ```

    IMPLEMENTATION NOTES:
    - Inherits all constants from FlextConstants base class
    - Flat structure with nested namespaces for organization
    - Single source of truth for all Oracle OIC Extension constants
    - No duplication with FlextConstants or other modules
    - Type-safe constants with Final annotations
    - Complete documentation and usage examples
    """

    class OracleOic:
        """Oracle Integration Cloud specific constants."""

        # API Configuration
        DEFAULT_API_VERSION: Final[str] = "v1"
        SUPPORTED_API_VERSIONS: Final[list[str]] = ["v1", "v2"]

        # Connection Configuration
        DEFAULT_BASE_URL: Final[str] = (
            "https://localhost.integration.ocp.oraclecloud.com"
        )
        DEFAULT_TIMEOUT: Final[int] = 30
        DEFAULT_MAX_RETRIES: Final[int] = 3
        DEFAULT_VERIFY_SSL: Final[bool] = True
        DEFAULT_USE_SSL: Final[bool] = True

        # Pagination
        DEFAULT_PAGE_SIZE: Final[int] = 100
        MAX_PAGE_SIZE: Final[int] = 1000
        MIN_PAGE_SIZE: Final[int] = 1

        # Request Configuration
        DEFAULT_REQUEST_TIMEOUT: Final[int] = 30
        MIN_REQUEST_TIMEOUT: Final[int] = 1
        MAX_REQUEST_TIMEOUT: Final[int] = 300

        # Retry Configuration
        MIN_MAX_RETRIES: Final[int] = 0
        MAX_MAX_RETRIES: Final[int] = 10
        DEFAULT_BACKOFF_MULTIPLIER: Final[float] = 2.0
        DEFAULT_MAX_DELAY_SECONDS: Final[float] = 60.0

    OIC = OracleOic  # alias for backward compatibility

    class Auth:
        """Oracle OIC Authentication constants."""

        # OAuth2 Configuration
        DEFAULT_OAUTH_CLIENT_ID: Final[str] = "default_client_id"
        DEFAULT_OAUTH_CLIENT_SECRET: Final[str] = "default_client_secret_value"
        DEFAULT_OAUTH_TOKEN_URL: Final[str] = (
            "https://idcs-tenant.identity.oraclecloud.com/oauth2/v1/token"
        )
        DEFAULT_OAUTH_CLIENT_AUD: Final[str | None] = None
        DEFAULT_OAUTH_SCOPE: Final[str] = ""

        # Token Configuration
        DEFAULT_TOKEN_EXPIRY_SECONDS: Final[int] = 3600  # 1 hour
        MIN_TOKEN_EXPIRY_SECONDS: Final[int] = 300  # 5 minutes
        MAX_TOKEN_EXPIRY_SECONDS: Final[int] = 86400  # 24 hours

        class AuthType(StrEnum):
            """Authentication types.

            DRY Pattern: This StrEnum is the single source of truth for authentication types.
            All authentication type-related constants and Literal types MUST reference this enum.
            """

            OAUTH2 = "oauth2"
            BASIC = "basic"
            BEARER = "bearer"

        # Backward compatibility aliases
        AUTH_TYPE_OAUTH2: Final[str] = AuthType.OAUTH2
        AUTH_TYPE_BASIC: Final[str] = AuthType.BASIC
        AUTH_TYPE_BEARER: Final[str] = AuthType.BEARER

        # PEP 695 Literal type referencing StrEnum members
        type AuthTypeLiteral = Literal["oauth2", "basic", "bearer"]

    class Integration:
        """Oracle OIC Integration constants."""

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

        # Backward compatibility aliases
        STATUS_ACTIVATED: Final[str] = Status.ACTIVATED
        STATUS_DEACTIVATED: Final[str] = Status.DEACTIVATED
        STATUS_DRAFT: Final[str] = Status.DRAFT
        STATUS_PUBLISHED: Final[str] = Status.PUBLISHED
        STATUS_RUNNING: Final[str] = Status.RUNNING
        STATUS_STOPPED: Final[str] = Status.STOPPED
        STATUS_ERROR: Final[str] = Status.ERROR

        # PEP 695 Literal type referencing StrEnum members
        type StatusLiteral = Literal[
            "ACTIVATED",
            "DEACTIVATED",
            "DRAFT",
            "PUBLISHED",
            "RUNNING",
            "STOPPED",
            "ERROR",
        ]

        # Integration Versions
        DEFAULT_VERSION: Final[str] = "01.00.0000"
        MIN_VERSION_LENGTH: Final[int] = 1
        MAX_VERSION_LENGTH: Final[int] = 50

        # Integration Lifecycle
        DEFAULT_ACTIVATED_BY: Final[str] = "system"
        DEFAULT_CREATED_BY: Final[str] = "unknown"
        DEFAULT_LAST_UPDATED: Final[str] = ""

        # Integration Patterns
        PATTERN_MESSAGE_ROUTER: Final[str] = "message_router"
        PATTERN_SCATTER_GATHER: Final[str] = "scatter_gather"
        PATTERN_PUBLISH_SUBSCRIBE: Final[str] = "publish_subscribe"
        PATTERN_REQUEST_REPLY: Final[str] = "request_reply"

    class Connection:
        """Oracle OIC Connection constants."""

        class Status(StrEnum):
            """Connection status values.

            DRY Pattern: This StrEnum is the single source of truth for connection statuses.
            All connection status-related constants and Literal types MUST reference this enum.
            """

            ACTIVE = "ACTIVE"
            INACTIVE = "INACTIVE"
            ERROR = "ERROR"
            UNKNOWN = "unknown"

        # Backward compatibility aliases
        STATUS_ACTIVE: Final[str] = Status.ACTIVE
        STATUS_INACTIVE: Final[str] = Status.INACTIVE
        STATUS_ERROR: Final[str] = Status.ERROR
        STATUS_UNKNOWN: Final[str] = Status.UNKNOWN

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

        # Backward compatibility aliases
        TYPE_REST: Final[str] = Type.REST
        TYPE_SOAP: Final[str] = Type.SOAP
        TYPE_DATABASE: Final[str] = Type.DATABASE
        TYPE_FILE: Final[str] = Type.FILE
        TYPE_FTP: Final[str] = Type.FTP
        TYPE_SFTP: Final[str] = Type.SFTP

        # Adapter Types (aliases to Type enum)
        ADAPTER_TYPE_REST: Final[str] = Type.REST
        ADAPTER_TYPE_SOAP: Final[str] = Type.SOAP
        ADAPTER_TYPE_DATABASE: Final[str] = Type.DATABASE
        ADAPTER_TYPE_FILE: Final[str] = Type.FILE
        ADAPTER_TYPE_FTP: Final[str] = Type.FTP
        ADAPTER_TYPE_SFTP: Final[str] = Type.SFTP

        # PEP 695 Literal types referencing StrEnum members
        type StatusLiteral = Literal["ACTIVE", "INACTIVE", "ERROR", "unknown"]

        type TypeLiteral = Literal["REST", "SOAP", "DATABASE", "FILE", "FTP", "SFTP"]

    class Monitoring:
        """Oracle OIC Monitoring constants."""

        class HealthStatus(StrEnum):
            """Health status values.

            DRY Pattern: This StrEnum is the single source of truth for health statuses.
            All health status-related constants and Literal types MUST reference this enum.
            """

            HEALTHY = "healthy"
            UNHEALTHY = "unhealthy"
            ERROR = "error"
            UNKNOWN = "unknown"

        # Backward compatibility aliases
        HEALTH_STATUS_HEALTHY: Final[str] = HealthStatus.HEALTHY
        HEALTH_STATUS_UNHEALTHY: Final[str] = HealthStatus.UNHEALTHY
        HEALTH_STATUS_ERROR: Final[str] = HealthStatus.ERROR
        HEALTH_STATUS_UNKNOWN: Final[str] = HealthStatus.UNKNOWN

        class ComponentStatus(StrEnum):
            """Component status values.

            DRY Pattern: This StrEnum is the single source of truth for component statuses.
            All component status-related constants and Literal types MUST reference this enum.
            """

            HEALTHY = "healthy"
            UNHEALTHY = "unhealthy"
            UNKNOWN = "unknown"

        # Backward compatibility aliases
        COMPONENT_STATUS_HEALTHY: Final[str] = ComponentStatus.HEALTHY
        COMPONENT_STATUS_UNHEALTHY: Final[str] = ComponentStatus.UNHEALTHY
        COMPONENT_STATUS_UNKNOWN: Final[str] = ComponentStatus.UNKNOWN

        # PEP 695 Literal types referencing StrEnum members
        type HealthStatusLiteral = Literal["healthy", "unhealthy", "error", "unknown"]
        type ComponentStatusLiteral = Literal["healthy", "unhealthy", "unknown"]

        # Component Types
        COMPONENT_DATABASE: Final[str] = "database"
        COMPONENT_MESSAGING: Final[str] = "messaging"
        COMPONENT_INTEGRATION_ENGINE: Final[str] = "integration_engine"

        # Performance Metrics
        DEFAULT_SUCCESS_RATE: Final[float] = 0.0
        DEFAULT_AVERAGE_RESPONSE_TIME: Final[float] = 0.0
        DEFAULT_ACTIVE_INTEGRATIONS: Final[int] = 0
        DEFAULT_TOTAL_EXECUTIONS: Final[int] = 0

    class API:
        """Oracle OIC API constants."""

        # HTTP Status Codes
        HTTP_STATUS_OK: Final[int] = 200
        HTTP_ERROR_STATUS_THRESHOLD: Final[int] = 400

        # API Endpoints
        ENDPOINT_HEALTH: Final[str] = "/ic/api/integration/v1/health"
        ENDPOINT_METRICS: Final[str] = "/ic/api/integration/v1/metrics"
        ENDPOINT_INTEGRATIONS: Final[str] = "/ic/api/integration/v1/integrations"
        ENDPOINT_CONNECTIONS: Final[str] = "/ic/api/integration/v1/connections"

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

        # Backward compatibility aliases
        METHOD_GET: Final[str] = Method.GET
        METHOD_POST: Final[str] = Method.POST
        METHOD_PUT: Final[str] = Method.PUT
        METHOD_DELETE: Final[str] = Method.DELETE
        METHOD_PATCH: Final[str] = Method.PATCH

        # PEP 695 Literal type referencing StrEnum members
        type MethodLiteral = Literal["GET", "POST", "PUT", "DELETE", "PATCH"]

        # API Headers
        HEADER_CONTENT_TYPE: Final[str] = "Content-Type"
        HEADER_AUTHORIZATION: Final[str] = "Authorization"
        HEADER_ACCEPT: Final[str] = "Accept"
        HEADER_USER_AGENT: Final[str] = "User-Agent"

        # Content Types
        CONTENT_TYPE_JSON: Final[str] = "application/json"
        CONTENT_TYPE_XML: Final[str] = "application/xml"
        CONTENT_TYPE_FORM: Final[str] = "application/x-www-form-urlencoded"

    OIC = OracleOic

    class OICPatterns:
        """Oracle OIC Integration Pattern constants."""

        class PatternStatus(StrEnum):
            """Pattern status values.

            DRY Pattern: This StrEnum is the single source of truth for pattern statuses.
            All pattern status-related constants and Literal types MUST reference this enum.
            """

            PROCESSED = "processed"
            FAILED = "failed"
            PENDING = "pending"

        # Backward compatibility aliases
        PATTERN_STATUS_PROCESSED: Final[str] = PatternStatus.PROCESSED
        PATTERN_STATUS_FAILED: Final[str] = PatternStatus.FAILED
        PATTERN_STATUS_PENDING: Final[str] = PatternStatus.PENDING

        # PEP 695 Literal type referencing StrEnum members
        type PatternStatusLiteral = Literal["processed", "failed", "pending"]

        # Pattern Identifiers
        PATTERN_ID_UNKNOWN: Final[str] = "unknown"
        PATTERN_MESSAGE_ID_UNKNOWN: Final[str] = "unknown"
        PATTERN_REQUEST_ID_UNKNOWN: Final[str] = "unknown"

        # Pattern Configuration
        DEFAULT_APPLIED_RULES: Final[int] = 0
        DEFAULT_TARGET_COUNT: Final[int] = 0

        # Pattern identifiers (aliases for Integration.PATTERN_*)
        PATTERN_MESSAGE_ROUTER: Final[str] = "message_router"
        PATTERN_SCATTER_GATHER: Final[str] = "scatter_gather"

    class OICErrors:
        """Oracle OIC Extension specific error constants."""

        # Connection Errors
        ERROR_CONNECTION_FAILED: Final[str] = "CONNECTION_FAILED"
        ERROR_AUTHENTICATION_FAILED: Final[str] = "AUTHENTICATION_FAILED"
        ERROR_CLIENT_CREATION_FAILED: Final[str] = "CLIENT_CREATION_FAILED"
        ERROR_NO_CLIENT_AVAILABLE: Final[str] = "NO_CLIENT_AVAILABLE"

        # Integration Errors
        ERROR_INTEGRATION_NOT_FOUND: Final[str] = "INTEGRATION_NOT_FOUND"
        ERROR_INTEGRATION_ACTIVATION_FAILED: Final[str] = (
            "INTEGRATION_ACTIVATION_FAILED"
        )
        ERROR_INTEGRATION_DEACTIVATION_FAILED: Final[str] = (
            "INTEGRATION_DEACTIVATION_FAILED"
        )
        ERROR_INTEGRATION_DEPLOYMENT_FAILED: Final[str] = (
            "INTEGRATION_DEPLOYMENT_FAILED"
        )

        # API Errors
        ERROR_API_REQUEST_FAILED: Final[str] = "API_REQUEST_FAILED"
        ERROR_API_RESPONSE_INVALID: Final[str] = "API_RESPONSE_INVALID"
        ERROR_API_TIMEOUT: Final[str] = "API_TIMEOUT"

        # Configuration Errors
        ERROR_CONFIG_VALIDATION_FAILED: Final[str] = "CONFIG_VALIDATION_FAILED"
        ERROR_SETTINGS_REQUIRED: Final[str] = "SETTINGS_REQUIRED"
        ERROR_BASE_URL_REQUIRED: Final[str] = "BASE_URL_REQUIRED"
        ERROR_OAUTH_CLIENT_ID_REQUIRED: Final[str] = "OAUTH_CLIENT_ID_REQUIRED"
        ERROR_OAUTH_CLIENT_SECRET_REQUIRED: Final[str] = "OAUTH_CLIENT_SECRET_REQUIRED"
        ERROR_OAUTH_TOKEN_URL_REQUIRED: Final[str] = "OAUTH_TOKEN_URL_REQUIRED"

    class OICMessages:
        """Oracle OIC Extension specific message constants."""

        # Success Messages
        MESSAGE_CONNECTION_SUCCESSFUL: Final[str] = "OIC connection test successful"
        MESSAGE_INTEGRATION_ACTIVATED: Final[str] = (
            "Integration {integration_id} activated successfully"
        )
        MESSAGE_INTEGRATION_DEACTIVATED: Final[str] = (
            "Integration {integration_id} deactivated successfully"
        )
        MESSAGE_INTEGRATION_DEPLOYED: Final[str] = (
            "Integration deployed successfully: {integration_id}"
        )

        # Error Messages
        MESSAGE_CONNECTION_FAILED: Final[str] = "OIC connection test failed: {error}"
        MESSAGE_INTEGRATION_ACTIVATION_FAILED: Final[str] = (
            "Failed to activate integration {integration_id}: {error}"
        )
        MESSAGE_INTEGRATION_DEACTIVATION_FAILED: Final[str] = (
            "Failed to deactivate integration {integration_id}: {error}"
        )
        MESSAGE_INTEGRATION_DEPLOYMENT_FAILED: Final[str] = (
            "Failed to deploy integration: {error}"
        )

        # Info Messages
        MESSAGE_INTEGRATIONS_RETRIEVED: Final[str] = "Retrieved {count} integrations"
        MESSAGE_CONNECTIONS_RETRIEVED: Final[str] = "Retrieved {count} connections"
        MESSAGE_APPLYING_MESSAGE_ROUTER: Final[str] = "Applying message router pattern"
        MESSAGE_APPLYING_SCATTER_GATHER: Final[str] = "Applying scatter-gather pattern"

        # Warning Messages
        MESSAGE_INTEGRATION_PARSE_FAILED: Final[str] = (
            "Failed to parse integration: {error}"
        )
        MESSAGE_CONNECTION_PARSE_FAILED: Final[str] = (
            "Failed to parse connection: {error}"
        )

    class OracleOicValidation:
        """Oracle OIC validation constants (named to avoid overriding FlextConstants.Validation)."""

        # Integration validation
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
        VERSION_PATTERN: Final[re.Pattern[str]] = re.compile(r"^\d{2}\.\d{2}\.\d{4}$")

        # Connection validation
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
            "UNKNOWN",
        })

        # Authentication validation
        MIN_CLIENT_ID_LENGTH: Final[int] = 1
        MIN_TOKEN_URL_LENGTH: Final[int] = 10
        MIN_CLIENT_SECRET_LENGTH: Final[int] = 8
        VALID_AUTH_TYPES: Final[frozenset[str]] = frozenset({
            "oauth2",
            "basic",
            "bearer",
        })

        # API request configuration
        DEFAULT_TIMEOUT: Final[int] = 30
        MAX_TIMEOUT: Final[int] = 300
        VALID_HTTP_METHODS: Final[frozenset[str]] = frozenset({
            "GET",
            "POST",
            "PUT",
            "DELETE",
            "PATCH",
            "HEAD",
            "OPTIONS",
        })

        # Pattern analysis
        SUPPORTED_PATTERNS: Final[frozenset[str]] = frozenset({
            "message_router",
            "scatter_gather",
            "publish_subscribe",
            "request_reply",
        })
        MIN_ENDPOINTS_FOR_ROUTER: Final[int] = 2

        # Monitoring
        HEALTH_CHECK_TIMEOUT: Final[int] = 10
        PERFORMANCE_THRESHOLDS: Final[dict[str, float]] = {
            "response_time_ms": 5000.0,
            "success_rate": 0.95,
            "error_rate": 0.05,
        }


# Exports following EXTENSION pattern
c = FlextOracleOicConstants

__all__: list[str] = [
    "FlextOracleOicConstants",
    "c",
]
