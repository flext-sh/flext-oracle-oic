"""Oracle OIC Extension Constants - Unified Constants Pattern.

This module provides centralized constants for the flext-oracle-oic project,
inheriting from FlextCore.Constants and following FLEXT architectural standards.

FLEXT Unified Constants Pattern: Single FlextOracleOicConstants class
inheriting from FlextCore.Constants with flat structure and no duplication.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final

from flext_core import FlextCore


class FlextOracleOicConstants(FlextCore.Constants):
    """Oracle OIC Extension constants inheriting from FlextCore.Constants.

    Provides centralized constants for Oracle OIC Extension operations,
    following FLEXT architectural standards with flat structure and no duplication.

    Usage:
        ```python
        from flext_oracle_oic.constants import FlextOracleOicConstants

        # Access Oracle OIC specific constants
        api_version = FlextOracleOicConstants.OIC.DEFAULT_API_VERSION
        timeout = FlextOracleOicConstants.OIC.DEFAULT_TIMEOUT
        page_size = FlextOracleOicConstants.OIC.DEFAULT_PAGE_SIZE

        # Access inherited FlextCore.Constants
        http_ok = FlextOracleOicConstants.Platform.HTTP_STATUS_OK
        default_timeout = FlextOracleOicConstants.Defaults.TIMEOUT
        ```

    **IMPLEMENTATION NOTES**:
    - Inherits all constants from FlextCore.Constants base class
    - Flat structure with nested namespaces for organization
    - Single source of truth for all Oracle OIC Extension constants
    - No duplication with FlextCore.Constants or other modules
    - Type-safe constants with Final annotations
    - Comprehensive documentation and usage examples
    """

    class OIC:
        """Oracle Integration Cloud specific constants."""

        # API Configuration
        DEFAULT_API_VERSION: Final[str] = "v1"
        SUPPORTED_API_VERSIONS: Final[FlextCore.Types.StringList] = ["v1", "v2"]

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

        # Authentication Types
        AUTH_TYPE_OAUTH2: Final[str] = "oauth2"
        AUTH_TYPE_BASIC: Final[str] = "basic"
        AUTH_TYPE_BEARER: Final[str] = "bearer"

    class Integration:
        """Oracle OIC Integration constants."""

        # Integration Status
        STATUS_ACTIVATED: Final[str] = "ACTIVATED"
        STATUS_DEACTIVATED: Final[str] = "DEACTIVATED"
        STATUS_DRAFT: Final[str] = "DRAFT"
        STATUS_PUBLISHED: Final[str] = "PUBLISHED"
        STATUS_RUNNING: Final[str] = "RUNNING"
        STATUS_STOPPED: Final[str] = "STOPPED"
        STATUS_ERROR: Final[str] = "ERROR"

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

        # Connection Status
        STATUS_ACTIVE: Final[str] = "ACTIVE"
        STATUS_INACTIVE: Final[str] = "INACTIVE"
        STATUS_ERROR: Final[str] = "ERROR"
        STATUS_UNKNOWN: Final[str] = "unknown"

        # Connection Types
        TYPE_REST: Final[str] = "REST"
        TYPE_SOAP: Final[str] = "SOAP"
        TYPE_DATABASE: Final[str] = "DATABASE"
        TYPE_FILE: Final[str] = "FILE"
        TYPE_FTP: Final[str] = "FTP"
        TYPE_SFTP: Final[str] = "SFTP"

        # Adapter Types
        ADAPTER_TYPE_REST: Final[str] = "REST"
        ADAPTER_TYPE_SOAP: Final[str] = "SOAP"
        ADAPTER_TYPE_DATABASE: Final[str] = "DATABASE"
        ADAPTER_TYPE_FILE: Final[str] = "FILE"
        ADAPTER_TYPE_FTP: Final[str] = "FTP"
        ADAPTER_TYPE_SFTP: Final[str] = "SFTP"

    class Monitoring:
        """Oracle OIC Monitoring constants."""

        # Health Status
        HEALTH_STATUS_HEALTHY: Final[str] = "healthy"
        HEALTH_STATUS_UNHEALTHY: Final[str] = "unhealthy"
        HEALTH_STATUS_ERROR: Final[str] = "error"
        HEALTH_STATUS_UNKNOWN: Final[str] = "unknown"

        # Component Status
        COMPONENT_STATUS_HEALTHY: Final[str] = "healthy"
        COMPONENT_STATUS_UNHEALTHY: Final[str] = "unhealthy"
        COMPONENT_STATUS_UNKNOWN: Final[str] = "unknown"

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
        HTTP_ERROR_STATUS_THRESHOLD: Final[int] = 400

        # API Endpoints
        ENDPOINT_HEALTH: Final[str] = "/ic/api/integration/v1/health"
        ENDPOINT_METRICS: Final[str] = "/ic/api/integration/v1/metrics"
        ENDPOINT_INTEGRATIONS: Final[str] = "/ic/api/integration/v1/integrations"
        ENDPOINT_CONNECTIONS: Final[str] = "/ic/api/integration/v1/connections"

        # API Methods
        METHOD_GET: Final[str] = "GET"
        METHOD_POST: Final[str] = "POST"
        METHOD_PUT: Final[str] = "PUT"
        METHOD_DELETE: Final[str] = "DELETE"
        METHOD_PATCH: Final[str] = "PATCH"

        # API Headers
        HEADER_CONTENT_TYPE: Final[str] = "Content-Type"
        HEADER_AUTHORIZATION: Final[str] = "Authorization"
        HEADER_ACCEPT: Final[str] = "Accept"
        HEADER_USER_AGENT: Final[str] = "User-Agent"

        # Content Types
        CONTENT_TYPE_JSON: Final[str] = "application/json"
        CONTENT_TYPE_XML: Final[str] = "application/xml"
        CONTENT_TYPE_FORM: Final[str] = "application/x-www-form-urlencoded"

    class OICPatterns:
        """Oracle OIC Integration Pattern constants."""

        # Pattern Status
        PATTERN_STATUS_PROCESSED: Final[str] = "processed"
        PATTERN_STATUS_FAILED: Final[str] = "failed"
        PATTERN_STATUS_PENDING: Final[str] = "pending"

        # Pattern Identifiers
        PATTERN_ID_UNKNOWN: Final[str] = "unknown"
        PATTERN_MESSAGE_ID_UNKNOWN: Final[str] = "unknown"
        PATTERN_REQUEST_ID_UNKNOWN: Final[str] = "unknown"

        # Pattern Configuration
        DEFAULT_APPLIED_RULES: Final[int] = 0
        DEFAULT_TARGET_COUNT: Final[int] = 0

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


# Exports following EXTENSION pattern
__all__: FlextCore.Types.StringList = [
    "FlextOracleOicConstants",
]
