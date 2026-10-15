"""Oracle OIC Extension Constants - Unified Constants Pattern.

This module provides centralized constants for the flext-oracle-oic project,
inheriting from c and following FLEXT architectural standards.

FLEXT Unified Constants Pattern: single ``FlextOracleOicConstants`` facade that
composes the scalar namespace owned by ``_constants.values`` through one local
namespace (``c.OracleOic.*``).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_auth import FlextAuthConstants

from flext_oracle_oic._constants import FlextOracleOicConstantsValues
from flext_oracle_oic._constants.base import FlextOracleOicConstantsBase


class FlextOracleOicConstants(FlextAuthConstants):
    """Oracle OIC Extension constants inheriting from c.

    Provides centralized constants for Oracle OIC Extension operations,
    following FLEXT architectural standards with flat structure and no
    duplication.

    Every scalar, enum and nested namespace is owned by
    ``flext_oracle_oic._constants`` and inherited through the single
    ``OracleOic`` namespace composed here.
    """

    class OracleOic(
        FlextOracleOicConstantsBase,
        FlextOracleOicConstantsValues,
    ):
        """Oracle Integration Cloud constants namespace."""


c = FlextOracleOicConstants

__all__: list[str] = ["FlextOracleOicConstants", "c"]
