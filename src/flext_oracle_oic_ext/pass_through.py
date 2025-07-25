"""Pass-through invoker for Oracle OIC extension.

CONSOLIDATED: Uses centralized pass-through from flext-meltano.
Zero tolerance for code duplication.
"""

from __future__ import annotations

# CONSOLIDATED: Import from centralized flext-meltano
from flext_meltano.extensions.oracle_oic.pass_through import pass_through_cli

# Re-export for backward compatibility
__all__ = ["pass_through_cli"]

if __name__ == "__main__":
    pass_through_cli()
