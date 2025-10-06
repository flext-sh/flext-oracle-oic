"""Project metadata for flext oracle oic ext."""

from __future__ import annotations

from typing import Final


class FlextOracleOicVersion:
    """Temporary version class fallback."""

    def __init__(self) -> None:
        """Initialize version information."""
        self.version = "0.1.0"
        self.version_info = (0, 1, 0)

    @classmethod
    def current(cls) -> FlextOracleOicVersion:
        """Return current version."""
        return cls()


VERSION: Final[FlextOracleOicVersion] = FlextOracleOicVersion.current()
__version__: Final[str] = VERSION.version
__version_info__: Final[tuple[int | str, ...]] = VERSION.version_info

__all__ = ["VERSION", "FlextOracleOicVersion", "__version__", "__version_info__"]
