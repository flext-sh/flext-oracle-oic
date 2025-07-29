"""Oracle OIC monitoring service using flext-core patterns.

CONSOLIDATED: Uses centralized monitoring from flext-meltano.
Zero tolerance for code duplication.
"""

from __future__ import annotations

# CONSOLIDATED: Import from centralized flext-meltano
from flext_meltano.extensions.oracle_oic.monitoring.monitor import (
    HealthCheckResult,
    MonitoringService,
    PerformanceMetrics,
)

# Re-export for backward compatibility
__all__ = [
    "HealthCheckResult",
    "MonitoringService",
    "PerformanceMetrics",
]
