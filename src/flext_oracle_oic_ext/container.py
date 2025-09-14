"""Container module for flext-oracle-oic-ext.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextContainer

# Create all module-specific utilities using DRY pattern
_utilities = FlextContainer.create_module_utilities("flext_oracle_oic_ext")

# Extract utilities with proper names for backward compatibility
get_flext_oracle_oic_ext_container = _utilities["get_container"]
configure_flext_oracle_oic_ext_dependencies = _utilities["configure_dependencies"]
get_flext_oracle_oic_ext_service = _utilities["get_service"]

# Initialize flext_oracle_oic_ext dependencies on module import
if callable(configure_flext_oracle_oic_ext_dependencies):
    configure_flext_oracle_oic_ext_dependencies()
# Skip if not callable - may be a placeholder object
