"""Base constants for flext-oracle-oic.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final


class FlextOracleOicConstantsBase:
    """Base constants for flext-oracle-oic.

    Foundational scalars the layer-0 settings module reads through this family
    base (a settings module may import its own family ``base.py``); every other
    scalar is owned by ``_constants.values``.
    """

    DEFAULT_BASE_URL: Final[str] = "https://localhost.integration.ocp.oraclecloud.com"
    DEFAULT_TOKEN_URL: Final[str] = f"{DEFAULT_BASE_URL}/oauth/token"


__all__: list[str] = ["FlextOracleOicConstantsBase"]
