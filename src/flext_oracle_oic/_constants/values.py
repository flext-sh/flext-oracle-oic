"""Scalar constants for flext-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final


class FlextOracleOicConstantsValues:
    """Scalar constants.

    Mixed into ``c.OracleOic``, ``c.Auth``, ``c.Integration``,
    ``c.Monitoring``, ``c.API`` and ``c.OracleOicValidation``.
    """

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

    class Auth:
        """Oracle OIC Authentication scalar constants."""

        DEFAULT_OAUTH_SCOPE: Final[str] = ""

    class Integration:
        """Oracle OIC Integration scalar constants."""

        DEFAULT_VERSION: Final[str] = "01.00.0000"

    class Monitoring:
        """Oracle OIC Monitoring scalar constants."""

        COMPONENT_DATABASE: Final[str] = "database"

    class API:
        """Oracle OIC API scalar constants."""

        HTTP_ERROR_STATUS_THRESHOLD: Final[int] = 400

    class OracleOicValidation:
        """Oracle OIC validation scalar constants."""

        MIN_INTEGRATION_NAME_LENGTH: Final[int] = 1


__all__: list[str] = ["FlextOracleOicConstantsValues"]
