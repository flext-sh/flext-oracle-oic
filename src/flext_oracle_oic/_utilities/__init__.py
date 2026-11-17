# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Oracle Oic. Utilities package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_oic._utilities.authentication_validation import (
        FlextOracleOicUtilitiesAuthenticationValidation,
    )
    from flext_oracle_oic._utilities.connection_validation import (
        FlextOracleOicUtilitiesConnectionValidation,
    )
    from flext_oracle_oic._utilities.monitoring import FlextOracleOicUtilitiesMonitoring
    from flext_oracle_oic._utilities.oracle_oic import FlextOracleOicUtilitiesOracleOic


__all__: tuple[str, ...] = (
    "FlextOracleOicUtilitiesAuthenticationValidation",
    "FlextOracleOicUtilitiesConnectionValidation",
    "FlextOracleOicUtilitiesMonitoring",
    "FlextOracleOicUtilitiesOracleOic",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "FlextOracleOicUtilitiesAuthenticationValidation": ".authentication_validation",
        "FlextOracleOicUtilitiesConnectionValidation": ".connection_validation",
        "FlextOracleOicUtilitiesMonitoring": ".monitoring",
        "FlextOracleOicUtilitiesOracleOic": ".oracle_oic",
    },
    public_exports=__all__,
    deferred_members={
        "FlextOracleOicUtilitiesAuthenticationValidation": (
            "validate_oauth_client_id",
            "validate_oauth_client_secret",
        ),
        "FlextOracleOicUtilitiesConnectionValidation": (
            "_validate_closed_string",
            "validate_base_url",
            "validate_connection_status",
            "validate_connection_type",
        ),
        "FlextOracleOicUtilitiesMonitoring": (
            "_assess_metric",
            "_components_validation_error",
            "analyze_performance_metrics",
            "validate_health_status",
        ),
        "FlextOracleOicUtilitiesOracleOic": (
            "validate_integration_data",
            "validate_string_field",
            "validate_integration_name",
            "validate_integration_status",
            "validate_integration_version",
        ),
    },
)
