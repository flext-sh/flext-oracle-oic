# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT Oracle OIC utilities submodules."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes

    from flext_oracle_oic._utilities.api_request_builder import *
    from flext_oracle_oic._utilities.authentication_validation import *
    from flext_oracle_oic._utilities.connection_validation import *
    from flext_oracle_oic._utilities.monitoring import *
    from flext_oracle_oic._utilities.oracle_oic import *
    from flext_oracle_oic._utilities.pattern_analysis import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextOracleOicUtilitiesAPIRequestBuilder": "flext_oracle_oic._utilities.api_request_builder",
    "FlextOracleOicUtilitiesAuthenticationValidation": "flext_oracle_oic._utilities.authentication_validation",
    "FlextOracleOicUtilitiesConnectionValidation": "flext_oracle_oic._utilities.connection_validation",
    "FlextOracleOicUtilitiesMonitoring": "flext_oracle_oic._utilities.monitoring",
    "FlextOracleOicUtilitiesOracleOic": "flext_oracle_oic._utilities.oracle_oic",
    "FlextOracleOicUtilitiesPatternAnalysis": "flext_oracle_oic._utilities.pattern_analysis",
    "api_request_builder": "flext_oracle_oic._utilities.api_request_builder",
    "authentication_validation": "flext_oracle_oic._utilities.authentication_validation",
    "connection_validation": "flext_oracle_oic._utilities.connection_validation",
    "monitoring": "flext_oracle_oic._utilities.monitoring",
    "oracle_oic": "flext_oracle_oic._utilities.oracle_oic",
    "pattern_analysis": "flext_oracle_oic._utilities.pattern_analysis",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
