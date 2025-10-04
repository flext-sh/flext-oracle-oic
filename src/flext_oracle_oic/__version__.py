"""Version metadata for flext oracle oic ext."""

from __future__ import annotations

from typing import Final

# Temporarily disabled due to missing flext_core.metadata
# from flext_core.metadata import build_metadata_exports
# _metadata = build_metadata_exports(__file__)

__version__: Final[str] = "0.1.0"  # Temporary version
__version_info__: Final[tuple[int | str, ...]] = (0, 1, 0)

__all__ = ["__version__", "__version_info__"]
