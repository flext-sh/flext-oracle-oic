"""Behavioral contract tests for flext-oracle-oic package version metadata."""

from __future__ import annotations

from flext_tests import tm
from packaging.version import Version

from flext_oracle_oic import __version__, __version_info__


class TestsFlextOracleOicVersion:
    """Public contract of the package version metadata.

    Observable contract: the package exposes a human-readable ``__version__``
    string and a three-integer ``__version_info__`` PEP 440 release tuple.
    Qualifiers remain represented only in the version string.
    """

    def test_version_is_non_empty_string(self) -> None:
        """__version__ is a non-empty string."""
        tm.that(__version__, is_=str)
        tm.that(__version__.strip(), eq=__version__)
        assert len(__version__) >= 1

    def test_version_info_is_release_triple(self) -> None:
        """__version_info__ is an exact three-integer release tuple."""
        tm.that(__version_info__, is_=tuple)
        tm.that(len(__version_info__), eq=3)
        assert all(isinstance(part, int) for part in __version_info__)

    def test_version_info_starts_with_three_integer_components(self) -> None:
        """The first three components form a major.minor.patch integer triple."""
        assert len(__version_info__) >= 3
        major, minor, patch = __version_info__[:3]
        assert isinstance(major, int)
        assert isinstance(minor, int)
        assert isinstance(patch, int)
        assert major >= 0
        assert minor >= 0
        assert patch >= 0

    def test_version_string_matches_version_info(self) -> None:
        """__version_info__ equals the exact PEP 440 release triple."""
        tm.that(__version_info__, eq=Version(__version__).release)
