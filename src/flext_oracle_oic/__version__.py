"""Version and package metadata using importlib.metadata.

Single source of truth pattern following flext-core standards.
All metadata comes from pyproject.toml via importlib.metadata.

Copyright (c) 2025 client-a Telecom. Todos os direitos reservados.
SPDX-License-Identifier: Proprietary
"""

from __future__ import annotations

try:
    from importlib.metadata import metadata

    _metadata = metadata("flext_oracle_oic")
    __version__ = _metadata["Version"]
    __version_info__ = tuple(
        int(part) if part.isdigit() else part for part in __version__.split(".")
    )
    __title__ = _metadata["Name"]
    __description__ = _metadata["Summary"]
    __author__ = _metadata["Author"]
    __author_email__ = _metadata["Author-Email"]
    __license__ = _metadata["License"]
    __url__ = _metadata["Home-Page"]
except Exception:
    # Fallback for development when package is not installed
    __version__ = "0.9.9"
    __version_info__ = (0, 9, 9)
    __title__ = "flext-oracle-oic"
    __description__ = "Oracle OIC Extension for FLEXT ecosystem"
    __author__ = "FLEXT Team"
    __author_email__ = None
    __license__ = "MIT"
    __url__ = None

__all__ = [
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
]
