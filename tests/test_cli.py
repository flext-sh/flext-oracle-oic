"""Tests for cli.py module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from unittest.mock import Mock, patch

from flext_oracle_oic_ext import app, main


class TestCLI:
    """Test CLI module functionality."""

    def test_imports_available(self) -> None:
        """Test that CLI imports are available."""
        # Should be able to import app and main
        assert app is not None
        assert main is not None

    @patch("flext_oracle_oic_ext.main.app")
    @patch("flext_oracle_oic_ext.main.main")
    def test_self(self, mock_main: Mock, mock_app: Mock) -> None:
        """Test CLI exports main app and main function."""
        # Mock the main module components
        mock_app.return_value = Mock()
        mock_main.return_value = Mock()

        # Verify imports work without error
        assert app is not None
        assert main is not None
        assert hasattr(app, "__name__") or callable(app)
        assert hasattr(main, "__name__") or callable(main)
