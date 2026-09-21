"""Scalar constants for flext-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final


class FlextOracleOicConstantsValues:
    """Scalar constants mixed into ``c.OracleOic`` and ``c.Auth``."""

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


__all__: list[str] = ["FlextOracleOicConstantsValues"]
