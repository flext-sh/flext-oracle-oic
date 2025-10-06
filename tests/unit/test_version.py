"""Version tests for flext-oracle-oic."""

from __future__ import annotations

from flext_oracle_oic import __version__, __version_info__
from flext_oracle_oic.version import VERSION, FlextOracleOicVersion


def test_dunder_alignment() -> None:
    """Ensure dunder exports are aligned with VERSION."""
    assert __version__ == VERSION.version
    assert __version_info__ == VERSION.version_info


def test_version_object() -> None:
    """Validate that the VERSION object is properly initialized."""
    assert isinstance(VERSION, FlextOracleOicVersion)
    assert VERSION.version == "0.1.0"
    assert VERSION.version_info == (0, 1, 0)
