# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_basic": ("test_basic",),
        ".test_cli": ("test_cli",),
        ".test_config": ("test_config",),
        ".test_ext_client": ("test_ext_client",),
        ".test_ext_services": ("test_ext_services",),
        ".test_extension": ("test_extension",),
        ".test_import": ("test_import",),
        ".test_main": ("test_main",),
        ".test_models": ("test_models",),
        ".test_typings": ("test_typings",),
        ".test_version": ("test_version",),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
