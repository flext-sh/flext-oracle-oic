# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

    from .test_version import test_version_info_tuple, test_version_string

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "test_version_info_tuple": ("tests.unit.test_version", "test_version_info_tuple"),
    "test_version_string": ("tests.unit.test_version", "test_version_string"),
}

__all__ = [
    "test_version_info_tuple",
    "test_version_string",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
