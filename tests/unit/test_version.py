"""Unit tests for flext-oracle-oic-ext version module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import inspect

import flext_oracle_oic_ext as version_module
from flext_oracle_oic_ext import __version__


def test_version_import() -> None:
    """Test that version can be imported successfully."""
    assert __version__ is not None


def test_version_module_functions() -> None:
    """Test version module has expected functions."""
    # Test that version module has the expected attributes
    assert hasattr(version_module, "__version__")
    assert hasattr(version_module, "__version_info__")

    # Test that version values are correct
    assert version_module.__version__ == "0.9.0"
    assert version_module.__version_info__ == (0, 9, 0)


def test_version_attributes_exist() -> None:
    """Test that version attributes exist and have expected types."""
    # Test __version__ exists and is string
    assert hasattr(version_module, "__version__")
    assert isinstance(version_module.__version__, str)

    # Test __version_info__ exists and is tuple
    assert hasattr(version_module, "__version_info__")
    assert isinstance(version_module.__version_info__, tuple)


def test_version_centralized_management() -> None:
    """Test version module structure."""
    # Get module source to check for proper structure
    source = inspect.getsource(version_module)

    # Test that version module has proper structure
    assert "__version__" in source
    assert "__version_info__" in source
    assert "0.9.0" in source
