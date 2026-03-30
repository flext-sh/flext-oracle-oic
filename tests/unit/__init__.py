# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from tests.unit import test_version as test_version
    from tests.unit.test_version import (
        test_version_info_tuple as test_version_info_tuple,
        test_version_string as test_version_string,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "test_version": ["tests.unit.test_version", ""],
    "test_version_info_tuple": ["tests.unit.test_version", "test_version_info_tuple"],
    "test_version_string": ["tests.unit.test_version", "test_version_string"],
}

_EXPORTS: Sequence[str] = [
    "test_version",
    "test_version_info_tuple",
    "test_version_string",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
