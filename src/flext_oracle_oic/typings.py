"""FLEXT Oracle OIC Extension Types - Domain-specific Oracle OIC type definitions.

This module provides Oracle OIC extension-specific type definitions extending t.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends t properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pydantic import TypeAdapter

from flext_core import FlextTypes
from flext_oracle_oic import m


class FlextOracleOicTypes(FlextTypes):
    """Oracle OIC extension-specific type definitions extending t.

    Domain-specific type system for Oracle OIC integration operations.
    Contains ONLY complex OIC-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    CONTAINER_MAPPING_ADAPTER: m.TypeAdapter[FlextTypes.ContainerMapping] = TypeAdapter(
        FlextTypes.ContainerMapping,
    )


t = FlextOracleOicTypes
__all__: list[str] = ["FlextOracleOicTypes", "t"]
