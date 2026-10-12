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
from flext_cli import FlextCliConstants

from flext_oracle_oic._constants import FlextOracleOicConstantsValues
from flext_oracle_oic._constants.base import FlextOracleOicConstantsBase


class FlextOracleOicConstants(FlextAuthConstants):
    """Oracle OIC Extension constants inheriting from c.

    Provides centralized constants for Oracle OIC Extension operations,
    following FLEXT architectural standards with flat structure and no duplication.
    """

    class OracleOic(
        FlextOracleOicConstantsBase,
        FlextOracleOicConstantsValues.OracleOic,
    ):
        """Oracle Integration Cloud specific constants."""

    class OracleOicValidation(
        FlextOracleOicConstantsValues.OracleOicValidation,
    ):
        """Oracle OIC validation scalar constants."""

    class OICApiVersion:
        """OIC API version enumeration."""

        V1 = "v1"
        V2 = "v2"

    class Integration(
        FlextOracleOicConstantsValues.Integration,
    ):
        """Oracle OIC Integration scalar constants."""

        @unique
        class Status(StrEnum):
            """Integration status values."""

            ACTIVATED = "ACTIVATED"
            DEACTIVATED = "DEACTIVATED"
            DRAFT = "DRAFT"
            RUNNING = "RUNNING"
            STOPPED = "STOPPED"
            ERROR = "ERROR"

    class Connection(
        FlextOracleOicConstantsValues.Connection,
    ):
        """Oracle OIC Connection scalar constants."""

        @unique
        class Status(StrEnum):
            """Connection status values."""

            ACTIVE = "ACTIVE"
            INACTIVE = "INACTIVE"
            ERROR = "ERROR"
            UNKNOWN = "unknown"

    class Monitoring(
        FlextOracleOicConstantsValues.Monitoring,
    ):
        """Oracle OIC Monitoring scalar constants."""

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

    class API(
        FlextOracleOicConstantsValues.API,
    ):
        """Oracle OIC API scalar constants."""

        @unique
        class Method(StrEnum):
            """HTTP method values."""

            GET = "GET"
            POST = "POST"
            PUT = "PUT"
            DELETE = "DELETE"
            PATCH = "PATCH"

    class Cli(
        FlextOracleOicConstantsValues.Cli,
        FlextCliConstants.Cli,
    ):
        """Oracle OIC CLI scalar constants."""


c = FlextOracleOicConstants

__all__: list[str] = ["FlextOracleOicConstants", "c"]
