"""Container module for flext-oracle-oic-ext.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextContainer, FlextResult

# Create all module-specific utilities using DRY pattern
_utilities_result: FlextResult[object] = FlextContainer.create_module_utilities(
    "flext_oracle_oic_ext"
)

# Extract utilities with proper names for backward compatibility
if _utilities_result.is_success:
    _utilities = _utilities_result.unwrap()
    # Type annotation: _utilities should be a dict-like object
    if hasattr(_utilities, "get"):
        get_flext_oracle_oic_ext_container = _utilities.get("get_container")
        configure_flext_oracle_oic_ext_dependencies = _utilities.get(
            "configure_dependencies"
        )
        get_flext_oracle_oic_ext_service = _utilities.get("get_service")
    else:
        # Fallback if utilities doesn't have expected interface
        get_flext_oracle_oic_ext_container = None
        configure_flext_oracle_oic_ext_dependencies = None
        get_flext_oracle_oic_ext_service = None
else:
    # Fallback to None if utilities creation fails
    get_flext_oracle_oic_ext_container = None
    configure_flext_oracle_oic_ext_dependencies = None
    get_flext_oracle_oic_ext_service = None

# Initialize flext_oracle_oic_ext dependencies on module import
if callable(configure_flext_oracle_oic_ext_dependencies):
    configure_flext_oracle_oic_ext_dependencies()
# Skip if not callable - may be a placeholder object
