"""Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from flext_core import FlextTypes

"""Oracle Integration Cloud extension implementation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""


class OracleOICExtension:
    """Oracle OIC Extension placeholder implementation."""

    def __init__(self) -> None:
        """Initialize OIC extension."""
        self.name = "Oracle OIC Extension"

    def get_info(self) -> str:
        """Get extension information."""
        return f"{self.name} - Implementation pending"


__all__: FlextTypes.Core.StringList = ["OracleOICExtension"]
