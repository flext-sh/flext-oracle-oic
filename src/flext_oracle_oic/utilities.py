"""Oracle OIC Extension utilities module.

This module provides domain-specific utilities for Oracle Integration Cloud (OIC)
operations, extending u with nested classes for complete
Oracle OIC integration functionality.

FLEXT COMPLIANCE: Follows [Project]Utilities pattern with:
- Single unified class extending u
- Nested classes composed via MRO from _utilities/ mixins
- Python 3.13+ features and Pydantic 2.11+
- Railway-oriented programming with r
- Type-safe operations with proper validation
- SOLID principles with clean separation of concerns
"""

from __future__ import annotations

from flext_core import FlextUtilities
from flext_oracle_oic import (
    FlextOracleOicUtilitiesAPIRequestBuilder,
    FlextOracleOicUtilitiesAuthenticationValidation,
    FlextOracleOicUtilitiesConnectionValidation,
    FlextOracleOicUtilitiesMonitoring,
    FlextOracleOicUtilitiesOracleOic,
    FlextOracleOicUtilitiesPatternAnalysis,
)


class FlextOracleOicUtilities(FlextUtilities):
    """Unified Oracle OIC Extension utilities.

    Extends u with Oracle Integration Cloud
    functionality organized in domain-specific nested classes composed via MRO.
    """

    class OracleOic(FlextOracleOicUtilitiesOracleOic):
        """Oracle OIC domain utilities namespace."""

    class ConnectionValidation(FlextOracleOicUtilitiesConnectionValidation):
        """Oracle OIC connection validation utilities namespace."""

    class AuthenticationValidation(FlextOracleOicUtilitiesAuthenticationValidation):
        """Oracle OIC authentication validation utilities namespace."""

    class APIRequestBuilder(FlextOracleOicUtilitiesAPIRequestBuilder):
        """Oracle OIC API request builder utilities namespace."""

    class PatternAnalysis(FlextOracleOicUtilitiesPatternAnalysis):
        """Oracle OIC pattern analysis utilities namespace."""

    class MonitoringUtilities(FlextOracleOicUtilitiesMonitoring):
        """Oracle OIC monitoring utilities namespace."""


u = FlextOracleOicUtilities
__all__ = ["FlextOracleOicUtilities", "u"]
