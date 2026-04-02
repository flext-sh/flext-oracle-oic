# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from tests.unit import test_version
    from tests.unit.test_version import test_version_info_tuple, test_version_string

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "test_version": "tests.unit.test_version",
    "test_version_info_tuple": "tests.unit.test_version",
    "test_version_string": "tests.unit.test_version",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
