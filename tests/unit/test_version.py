"""Version metadata tests for flext-oracle-oic."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core.metadata import FlextProjectMetadata, FlextProjectPerson

from flext_oracle_oic import __version__, __version_info__
from flext_oracle_oic.version import VERSION, FlextOracleOicExtVersion


def test_dunder_alignment() -> None:
    """Ensure dunder exports are aligned with VERSION."""
    assert __version__ == VERSION.version
    assert __version_info__ == VERSION.version_info


def test_version_metadata_shape() -> None:
    """Validate that the VERSION object exposes normalized metadata."""
    assert isinstance(VERSION, FlextOracleOicExtVersion)
    assert isinstance(VERSION.metadata, FlextProjectMetadata)
    assert isinstance(VERSION.urls, Mapping)
    assert VERSION.version_tuple == VERSION.version_info


def test_contacts() -> None:
    """Primary contacts reflect the pyproject declarations."""
    assert isinstance(VERSION.author, FlextProjectPerson)
    assert isinstance(VERSION.maintainer, FlextProjectPerson)
    assert VERSION.author_name
    assert VERSION.maintainer_name


def test_metadata_passthrough() -> None:
    """VERSION forwards author and maintainer collections."""
    assert VERSION.authors == VERSION.metadata.authors
    assert VERSION.maintainers == VERSION.metadata.maintainers
