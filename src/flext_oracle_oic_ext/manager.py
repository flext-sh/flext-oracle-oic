"""Integration lifecycle management for Oracle OIC using flext-core patterns.

CONSOLIDATED: Uses centralized lifecycle manager from flext-meltano.
Zero tolerance for code duplication.
"""

from __future__ import annotations

# CONSOLIDATED: Import from centralized flext-meltano
from flext_meltano.extensions.oracle_oic.lifecycle.manager import (
    IntegrationIdentifier,
    IntegrationStatus,
    LifecycleManager,
    LifecycleOperationResult,
)

# Re-export for backward compatibility
__all__ = [
    "IntegrationIdentifier",
    "IntegrationStatus",
    "LifecycleManager",
    "LifecycleOperationResult",
]
