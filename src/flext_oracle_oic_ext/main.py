"""Main entry point for Oracle OIC extension.

CONSOLIDATED: Uses centralized main from flext-meltano.
Zero tolerance for code duplication.
"""

from __future__ import annotations

# CONSOLIDATED: Import from centralized flext-meltano
from flext_meltano.extensions.oracle_oic.main import app, main

# Re-export for backward compatibility
__all__ = ["app", "main"]

if __name__ == "__main__":
    app()
