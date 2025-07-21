"""FLEXT Oracle OIC Extension - Advanced Oracle Integration Cloud Extensions.

REFACTORED: Uses flext-core patterns.
Zero tolerance for code duplication.
"""

from __future__ import annotations

import importlib.metadata

try:
    __version__ = importlib.metadata.version("flext-oracle-oic-ext")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0-dev"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())
from flext_oracle_oic_ext.extension import OracleOICExtension

__all__ = ["OracleOICExtension", "__version__", "__version_info__"]
