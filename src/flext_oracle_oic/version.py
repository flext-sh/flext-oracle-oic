"""Project metadata for flext oracle oic ext."""

from __future__ import annotations

from typing import Final

# Temporarily disabled due to missing flext_core.metadata
# from flext_core.metadata import (
#     FlextProjectVersion,
#     build_metadata_exports,
# )

# _metadata = build_metadata_exports(__file__)
# globals().update(_metadata)
# _metadata_obj = cast("FlextProjectMetadata", _metadata["__flext_metadata__"])


# Temporary fallback implementation
class FlextOracleOicExtVersion:
    """Temporary version class fallback."""

    def __init__(self) -> None:
        """Initialize version information."""
        self.version = "0.1.0"
        self.version_info = (0, 1, 0)

    @classmethod
    def current(cls) -> FlextOracleOicExtVersion:
        """Return current version."""
        return cls()


VERSION: Final[FlextOracleOicExtVersion] = FlextOracleOicExtVersion.current()
__version__: Final[str] = VERSION.version
__version_info__: Final[tuple[int | str, ...]] = VERSION.version_info

__all__ = ["VERSION", "FlextOracleOicExtVersion", "__version__", "__version_info__"]
