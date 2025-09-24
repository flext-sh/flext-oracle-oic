"""Models for Oracle OIC External operations.

This module provides data models for Oracle OIC External operations.
"""

from flext_core import FlextModels


class FlextOracleOicExtModels:
    """Models for Oracle OIC Extension operations."""

    Core = FlextModels

    OicRecord = dict[str, object]
    OicRecords = list[OicRecord]
