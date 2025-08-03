"""Copyright (c) 2025 Flext. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from flext_core import create_module_container_utilities

# Create all module-specific utilities using DRY pattern
_utilities = create_module_container_utilities("flext_oracle_oic_ext")

# Extract utilities with proper names for backward compatibility
get_flext_oracle_oic_ext_container = _utilities["get_container"]
configure_flext_oracle_oic_ext_dependencies = _utilities["configure_dependencies"]
get_flext_oracle_oic_ext_service = _utilities["get_service"]

# Initialize flext_oracle_oic_ext dependencies on module import
if callable(configure_flext_oracle_oic_ext_dependencies):
    configure_flext_oracle_oic_ext_dependencies()
else:
    # Skip if not callable - may be a placeholder object
    pass
