"""Scalar constants for flext-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import re
from types import MappingProxyType
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from collections.abc import Mapping

    from flext_oracle_oic import t


class FlextOracleOicConstantsValues:
    """Scalar constants.

    Mixed into ``c.OracleOic``, ``c.Auth``, ``c.Integration``,
    ``c.Monitoring``, ``c.API``, ``c.OracleOicValidation`` and ``c.Cli``.
    """

    class OracleOic:
        """Oracle Integration Cloud specific constants."""

        DEFAULT_BASE_URL: Final[str] = (
            "https://localhost.integration.ocp.oraclecloud.com"
        )
        DEFAULT_API_VERSION: Final[str] = "v1"
        DEFAULT_TOKEN_URL: Final[str] = f"{DEFAULT_BASE_URL}/oauth/token"
        DEFAULT_PAGE_SIZE: Final[int] = 100
        MIN_PAGE_SIZE: Final[int] = 1
        MIN_REQUEST_TIMEOUT: Final[int] = 1
        DEFAULT_VERIFY_SSL: Final[bool] = True

    class Auth:
        """Oracle OIC Authentication scalar constants."""

        DEFAULT_OAUTH_SCOPE: Final[str] = ""

    class Integration:
        """Oracle OIC Integration scalar constants."""

        DEFAULT_VERSION: Final[str] = "01.00.0000"
        DEFAULT_VERSION_FALLBACK: Final[str] = "01.00.0000"

    class Monitoring:
        """Oracle OIC Monitoring scalar constants."""

        COMPONENT_DATABASE: Final[str] = "database"
        COMPONENT_MESSAGING: Final[str] = "messaging"
        COMPONENT_INTEGRATION_ENGINE: Final[str] = "integration_engine"

    class API:
        """Oracle OIC API scalar constants."""

        HTTP_ERROR_STATUS_THRESHOLD: Final[int] = 400
        HEADER_CONTENT_TYPE: Final[str] = "Content-Type"
        HEADER_AUTHORIZATION: Final[str] = "Authorization"
        HEADER_ACCEPT: Final[str] = "Accept"
        ENDPOINT_HEALTH: Final[str] = "/ic/api/integration/v1/health"
        HTTP_STATUS_OK: Final[int] = 200

    class OracleOicValidation:
        """Oracle OIC validation scalar constants."""

        MIN_INTEGRATION_NAME_LENGTH: Final[int] = 1
        MAX_INTEGRATION_NAME_LENGTH: Final[int] = 100
        INTEGRATION_NAME_RE: Final[t.RegexPattern] = re.compile(r"^[a-zA-Z0-9_\-\s]+$")
        CLIENT_ID_RE: Final[t.RegexPattern] = re.compile(r"^[a-zA-Z0-9_\-\.]+$")
        VERSION_PATTERN: Final[t.RegexPattern] = re.compile(
            r"^\\d{2}\\.\\d{2}\\.\\d{4}$",
        )
        VALID_INTEGRATION_STATUSES: Final[frozenset[str]] = frozenset({
            "ACTIVATED",
            "DEACTIVATED",
            "DRAFT",
            "PUBLISHED",
            "RUNNING",
            "STOPPED",
            "ERROR",
        })
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

    class Cli:
        """Oracle OIC CLI scalar constants."""

        APP_NAME: Final[str] = "flext-oracle-oic-ext"
        APP_HELP: Final[str] = (
            "FLEXT Oracle OIC Extension CLI - Enterprise Oracle "
            "Integration Cloud operations"
        )


__all__: list[str] = ["FlextOracleOicConstantsValues"]
