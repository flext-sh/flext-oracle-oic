"""Oracle Integration Cloud extension implementation.

CONSOLIDATED: Uses centralized extension from flext-meltano.
Zero tolerance for code duplication.
"""

from __future__ import annotations

# CONSOLIDATED: Import from centralized flext-meltano
from flext_meltano.extensions.oracle_oic import OracleOICExtension

# Re-export for backward compatibility
__all__ = ["OracleOICExtension"]
