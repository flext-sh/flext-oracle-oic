"""Scalar constants for flext-oracle-oic.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from enum import StrEnum, unique
from types import MappingProxyType
from typing import ClassVar

from flext_core import t


class FlextOracleOicConstantsValues:
    """Scalar constants composed into the Oracle OIC constants facade.

    Every scalar, compiled pattern, enum and nested namespace of the Oracle OIC
    domain is owned here and inherited through the facade namespace
    (``c.OracleOic``).
    """

    DEFAULT_API_VERSION: ClassVar[str] = "v1"
    DEFAULT_PAGE_SIZE: ClassVar[int] = 100
    MIN_PAGE_SIZE: ClassVar[int] = 1
    MIN_REQUEST_TIMEOUT: ClassVar[int] = 1
    DEFAULT_VERIFY_SSL: ClassVar[bool] = True

    class Auth:
        """Oracle OIC Authentication scalar constants."""

        DEFAULT_OAUTH_SCOPE: ClassVar[str] = ""

    class OICApiVersion:
        """OIC API version enumeration."""

        V1: ClassVar[str] = "v1"
        V2: ClassVar[str] = "v2"

    class Integration:
        """Oracle OIC Integration scalar constants."""

        DEFAULT_VERSION: ClassVar[str] = "01.00.0000"
        DEFAULT_VERSION_FALLBACK: ClassVar[str] = "01.00.0000"

        @unique
        class Status(StrEnum):
            """Integration status values."""

            ACTIVATED = "ACTIVATED"
            DEACTIVATED = "DEACTIVATED"
            DRAFT = "DRAFT"
            RUNNING = "RUNNING"
            STOPPED = "STOPPED"
            ERROR = "ERROR"

    class Connection:
        """Oracle OIC Connection scalar constants."""

        DEFAULT_TIMEOUT_SECONDS: ClassVar[int] = 30
        DEFAULT_MAX_RETRIES: ClassVar[int] = 3

        @unique
        class Status(StrEnum):
            """Connection status values."""

            ACTIVE = "ACTIVE"
            INACTIVE = "INACTIVE"
            ERROR = "ERROR"
            UNKNOWN = "unknown"

    class Monitoring:
        """Oracle OIC Monitoring scalar constants."""

        COMPONENT_DATABASE: ClassVar[str] = "database"
        COMPONENT_MESSAGING: ClassVar[str] = "messaging"
        COMPONENT_INTEGRATION_ENGINE: ClassVar[str] = "integration_engine"

        @unique
        class HealthStatus(StrEnum):
            """Health status values."""

            HEALTHY = "healthy"
            UNHEALTHY = "unhealthy"
            ERROR = "error"
            UNKNOWN = "unknown"

        @unique
        class ComponentStatus(StrEnum):
            """Component status values."""

            HEALTHY = "healthy"
            UNHEALTHY = "unhealthy"
            UNKNOWN = "unknown"

    class API:
        """Oracle OIC API scalar constants."""

        HTTP_ERROR_STATUS_THRESHOLD: ClassVar[int] = 400
        HEADER_CONTENT_TYPE: ClassVar[str] = "Content-Type"
        HEADER_AUTHORIZATION: ClassVar[str] = "Authorization"
        HEADER_ACCEPT: ClassVar[str] = "Accept"
        ENDPOINT_HEALTH: ClassVar[str] = "/ic/api/integration/v1/health"
        HTTP_STATUS_OK: ClassVar[int] = 200

        @unique
        class Method(StrEnum):
            """HTTP method values."""

            GET = "GET"
            POST = "POST"
            PUT = "PUT"
            DELETE = "DELETE"
            PATCH = "PATCH"

    class OracleOicValidation:
        """Oracle OIC validation scalar constants."""

        MIN_INTEGRATION_NAME_LENGTH: ClassVar[int] = 1
        MAX_INTEGRATION_NAME_LENGTH: ClassVar[int] = 100
        INTEGRATION_NAME_RE: ClassVar[t.RegexPattern] = re.compile(
            r"^[a-zA-Z0-9_\-\s]+$"
        )
        CLIENT_ID_RE: ClassVar[t.RegexPattern] = re.compile(r"^[a-zA-Z0-9_\-\.]+$")
        VERSION_PATTERN: ClassVar[t.RegexPattern] = re.compile(
            r"^\\d{2}\\.\\d{2}\\.\\d{4}$",
        )
        VALID_INTEGRATION_STATUSES: ClassVar[frozenset[str]] = frozenset({
            "ACTIVATED",
            "DEACTIVATED",
            "DRAFT",
            "PUBLISHED",
            "RUNNING",
            "STOPPED",
            "ERROR",
        })
        VALID_CONNECTION_TYPES: ClassVar[frozenset[str]] = frozenset({
            "REST",
            "SOAP",
            "DATABASE",
            "FILE",
            "FTP",
            "SFTP",
        })
        VALID_CONNECTION_STATUSES: ClassVar[frozenset[str]] = frozenset({
            "ACTIVE",
            "INACTIVE",
            "ERROR",
            "unknown",
        })
        MIN_CLIENT_ID_LENGTH: ClassVar[int] = 1
        MIN_CLIENT_SECRET_LENGTH: ClassVar[int] = 8
        PERFORMANCE_THRESHOLDS: ClassVar[Mapping[str, float]] = MappingProxyType({
            "response_time_ms": 5000.0,
            "success_rate": 0.95,
            "error_rate": 0.05,
        })

    class Cli:
        """Oracle OIC CLI scalar constants."""

        APP_NAME: ClassVar[str] = "flext-oracle-oic-ext"
        APP_HELP: ClassVar[str] = (
            "FLEXT Oracle OIC Extension CLI - Enterprise Oracle "
            "Integration Cloud operations"
        )


__all__: list[str] = ["FlextOracleOicConstantsValues"]
