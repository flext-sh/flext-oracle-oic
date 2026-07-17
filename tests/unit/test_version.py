"""Behavioral contract tests for flext-oracle-oic package version metadata."""

from __future__ import annotations

from flext_tests import tm

from flext_oracle_oic import __version__, __version_info__


class TestsFlextOracleOicVersion:
    """Public contract of the package version metadata.

    Observable contract: the package exposes a human-readable ``__version__``
    string and a structured ``__version_info__`` tuple, and the two are
    consistent with one another (the tuple parts joined by ``.`` reproduce the
    string). Numeric prefix components are integers; any trailing pre-release
    segment is a string.
    """

    def test_version_is_non_empty_string(self) -> None:
        """__version__ is a non-empty string."""
        tm.that(__version__, is_=str)
        tm.that(__version__.strip(), eq=__version__)
        assert len(__version__) >= 1

    def test_version_info_is_non_empty_tuple(self) -> None:
        """__version_info__ is a non-empty tuple."""
        tm.that(__version_info__, is_=tuple)
        assert len(__version_info__) >= 1

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

    def test_version_info_trailing_components_are_strings(self) -> None:
        """Any component beyond the numeric triple is a pre-release string."""
        for part in __version_info__[3:]:
            tm.that(part, is_=str)
            tm.that(part, ne="")

    def test_version_string_matches_version_info(self) -> None:
        """__version__ equals the tuple components joined by dots (single SSOT)."""
        rebuilt = ".".join(str(part) for part in __version_info__)
        tm.that(__version__, eq=rebuilt)

    def test_version_string_numeric_prefix_matches_info(self) -> None:
        """The dotted numeric prefix of __version__ matches the integer triple."""
        numeric_prefix = __version__.split(".")[:3]
        tm.that(numeric_prefix, eq=[str(part) for part in __version_info__[:3]])
