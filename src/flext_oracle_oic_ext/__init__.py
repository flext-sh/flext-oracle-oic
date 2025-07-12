"""FLEXT Oracle OIC Extension - Advanced Oracle Integration Cloud Extensions.

REFACTORED: Uses flext-core patterns.
Zero tolerance for code duplication.
"""

from __future__ import annotations

from flext_oracle_oic_ext.__version__ import __version__, __version_info__
from flext_oracle_oic_ext.extension import OracleOICExtension

__all__ = ["OracleOICExtension", "__version__", "__version_info__"]
