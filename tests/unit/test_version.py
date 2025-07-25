"""Unit tests for flext-oracle-oic-ext version module."""

from __future__ import annotations

from unittest.mock import patch

from flext_oracle_oic_ext import __version__


def test_version_import() -> None:
    """Test that version can be imported successfully."""
    assert __version__ is not None


def test_version_module_functions() -> None:
    """Test version module uses flext_core functions."""
    # Import the module to trigger function calls

    # Test that version functions are called from flext_core
    with (
        patch("flext_core.version.get_version") as mock_get_version,
        patch("flext_core.version.get_version_info") as mock_get_version_info,
    ):
        mock_get_version.return_value = "1.0.0"
        mock_get_version_info.return_value = (1, 0, 0)

        # Re-import to trigger the version calls
        import importlib
        import sys

        module_name = "flext_oracle_oic_ext.__version__"
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)

        # Verify the functions were called with correct package name
        mock_get_version.assert_called_with("flext-oracle-oic-ext")
        mock_get_version_info.assert_called_with("flext-oracle-oic-ext")


def test_version_attributes_exist() -> None:
    """Test that version attributes exist and have expected types."""
    import flext_oracle_oic_ext.__version__ as version_module

    # Test __version__ exists and is string
    assert hasattr(version_module, "__version__")
    assert isinstance(version_module.__version__, str)

    # Test __version_info__ exists and is tuple
    assert hasattr(version_module, "__version_info__")
    assert isinstance(version_module.__version_info__, tuple)


def test_version_centralized_management() -> None:
    """Test version uses centralized management comment."""
    import inspect

    import flext_oracle_oic_ext.__version__ as version_module

    # Get module source to check for centralized management comment
    source = inspect.getsource(version_module)
    assert "centralized version management" in source.lower()
    assert "flext_core.version" in source
