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

from flext_auth import u

from flext_oracle_oic._utilities.authentication_validation import (
    FlextOracleOicUtilitiesAuthenticationValidation,
)
from flext_oracle_oic._utilities.connection_validation import (
    FlextOracleOicUtilitiesConnectionValidation,
)
from flext_oracle_oic._utilities.monitoring import (
    FlextOracleOicUtilitiesMonitoring,
)
from flext_oracle_oic._utilities.oracle_oic import (
    FlextOracleOicUtilitiesOracleOic,
)


class FlextOracleOicUtilities(
    u,
    FlextOracleOicUtilitiesOracleOic,
    FlextOracleOicUtilitiesConnectionValidation,
    FlextOracleOicUtilitiesAuthenticationValidation,
    FlextOracleOicUtilitiesMonitoring,
):
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

    class MonitoringUtilities(FlextOracleOicUtilitiesMonitoring):
        """Oracle OIC monitoring utilities namespace."""


u = FlextOracleOicUtilities
__all__: list[str] = ["FlextOracleOicUtilities", "u"]
