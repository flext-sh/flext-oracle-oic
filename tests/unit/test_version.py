"""Version tests for flext-oracle-oic."""

from __future__ import annotations

from flext_oracle_oic import __version__, __version_info__


class TestsFlextOracleOicVersion:
    """Behavior contract for test_version."""

    def test_version_string(self) -> None:
        """Ensure __version__ is a non-empty string."""
        assert isinstance(__version__, str)
        assert len(__version__) >= 1

    def test_version_info_tuple(self) -> None:
        """Ensure __version_info__ is a tuple of int or (int, int, int)."""
        assert isinstance(__version_info__, tuple)
        assert len(__version_info__) >= 1
        for part in __version_info__:
            assert isinstance(part, (int, str))
