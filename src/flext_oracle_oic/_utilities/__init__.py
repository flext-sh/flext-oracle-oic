# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Utilities package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import flext_oracle_oic._utilities.api_request_builder as _flext_oracle_oic__utilities_api_request_builder

    api_request_builder = _flext_oracle_oic__utilities_api_request_builder
    import flext_oracle_oic._utilities.authentication_validation as _flext_oracle_oic__utilities_authentication_validation
    from flext_oracle_oic._utilities.api_request_builder import (
        FlextOracleOicUtilitiesAPIRequestBuilder,
    )

    authentication_validation = _flext_oracle_oic__utilities_authentication_validation
    import flext_oracle_oic._utilities.connection_validation as _flext_oracle_oic__utilities_connection_validation
    from flext_oracle_oic._utilities.authentication_validation import (
        FlextOracleOicUtilitiesAuthenticationValidation,
    )

    connection_validation = _flext_oracle_oic__utilities_connection_validation
    import flext_oracle_oic._utilities.monitoring as _flext_oracle_oic__utilities_monitoring
    from flext_oracle_oic._utilities.connection_validation import (
        FlextOracleOicUtilitiesConnectionValidation,
    )

    monitoring = _flext_oracle_oic__utilities_monitoring
    import flext_oracle_oic._utilities.oracle_oic as _flext_oracle_oic__utilities_oracle_oic
    from flext_oracle_oic._utilities.monitoring import FlextOracleOicUtilitiesMonitoring

    oracle_oic = _flext_oracle_oic__utilities_oracle_oic
    import flext_oracle_oic._utilities.pattern_analysis as _flext_oracle_oic__utilities_pattern_analysis
    from flext_oracle_oic._utilities.oracle_oic import FlextOracleOicUtilitiesOracleOic

    pattern_analysis = _flext_oracle_oic__utilities_pattern_analysis
    from flext_oracle_oic._utilities.pattern_analysis import (
        FlextOracleOicUtilitiesPatternAnalysis,
    )
_LAZY_IMPORTS = {
    "FlextOracleOicUtilitiesAPIRequestBuilder": (
        "flext_oracle_oic._utilities.api_request_builder",
        "FlextOracleOicUtilitiesAPIRequestBuilder",
    ),
    "FlextOracleOicUtilitiesAuthenticationValidation": (
        "flext_oracle_oic._utilities.authentication_validation",
        "FlextOracleOicUtilitiesAuthenticationValidation",
    ),
    "FlextOracleOicUtilitiesConnectionValidation": (
        "flext_oracle_oic._utilities.connection_validation",
        "FlextOracleOicUtilitiesConnectionValidation",
    ),
    "FlextOracleOicUtilitiesMonitoring": (
        "flext_oracle_oic._utilities.monitoring",
        "FlextOracleOicUtilitiesMonitoring",
    ),
    "FlextOracleOicUtilitiesOracleOic": (
        "flext_oracle_oic._utilities.oracle_oic",
        "FlextOracleOicUtilitiesOracleOic",
    ),
    "FlextOracleOicUtilitiesPatternAnalysis": (
        "flext_oracle_oic._utilities.pattern_analysis",
        "FlextOracleOicUtilitiesPatternAnalysis",
    ),
    "api_request_builder": "flext_oracle_oic._utilities.api_request_builder",
    "authentication_validation": "flext_oracle_oic._utilities.authentication_validation",
    "connection_validation": "flext_oracle_oic._utilities.connection_validation",
    "monitoring": "flext_oracle_oic._utilities.monitoring",
    "oracle_oic": "flext_oracle_oic._utilities.oracle_oic",
    "pattern_analysis": "flext_oracle_oic._utilities.pattern_analysis",
}

__all__ = [
    "FlextOracleOicUtilitiesAPIRequestBuilder",
    "FlextOracleOicUtilitiesAuthenticationValidation",
    "FlextOracleOicUtilitiesConnectionValidation",
    "FlextOracleOicUtilitiesMonitoring",
    "FlextOracleOicUtilitiesOracleOic",
    "FlextOracleOicUtilitiesPatternAnalysis",
    "api_request_builder",
    "authentication_validation",
    "connection_validation",
    "monitoring",
    "oracle_oic",
    "pattern_analysis",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
