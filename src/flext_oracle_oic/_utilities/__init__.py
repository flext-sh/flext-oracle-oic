# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Utilities package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_oracle_oic import (
        api_request_builder,
        authentication_validation,
        connection_validation,
        monitoring,
        oracle_oic,
        pattern_analysis,
    )
    from flext_oracle_oic.api_request_builder import (
        FlextOracleOicUtilitiesAPIRequestBuilder,
    )
    from flext_oracle_oic.authentication_validation import (
        FlextOracleOicUtilitiesAuthenticationValidation,
    )
    from flext_oracle_oic.connection_validation import (
        FlextOracleOicUtilitiesConnectionValidation,
    )
    from flext_oracle_oic.monitoring import FlextOracleOicUtilitiesMonitoring
    from flext_oracle_oic.oracle_oic import FlextOracleOicUtilitiesOracleOic
    from flext_oracle_oic.pattern_analysis import FlextOracleOicUtilitiesPatternAnalysis

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextOracleOicUtilitiesAPIRequestBuilder": "flext_oracle_oic.api_request_builder",
    "FlextOracleOicUtilitiesAuthenticationValidation": "flext_oracle_oic.authentication_validation",
    "FlextOracleOicUtilitiesConnectionValidation": "flext_oracle_oic.connection_validation",
    "FlextOracleOicUtilitiesMonitoring": "flext_oracle_oic.monitoring",
    "FlextOracleOicUtilitiesOracleOic": "flext_oracle_oic.oracle_oic",
    "FlextOracleOicUtilitiesPatternAnalysis": "flext_oracle_oic.pattern_analysis",
    "api_request_builder": "flext_oracle_oic.api_request_builder",
    "authentication_validation": "flext_oracle_oic.authentication_validation",
    "connection_validation": "flext_oracle_oic.connection_validation",
    "monitoring": "flext_oracle_oic.monitoring",
    "oracle_oic": "flext_oracle_oic.oracle_oic",
    "pattern_analysis": "flext_oracle_oic.pattern_analysis",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
