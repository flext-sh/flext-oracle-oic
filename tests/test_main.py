"""Tests for main.py module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import flext_oracle_oic.main as main_module
from flext_oracle_oic import __version__
from flext_oracle_oic.main import FlextOracleOicCli, main


class TestMainFunction:
    """Test main function entry point."""

    def test_main_function_exists(self) -> None:
        """Test main function is callable."""
        assert callable(main)

    @patch("flext_oracle_oic.main.sys.exit")
    def test_main_exits(self, mock_exit: MagicMock) -> None:
        """Test main eventually calls sys.exit (no Typer app)."""
        mock_exit.side_effect = SystemExit(0)
        try:
            main()
        except SystemExit:
            pass
        mock_exit.assert_called()


class TestMainModule:
    """Test main module exports."""

    def test_cli_class_available(self) -> None:
        """Test FlextOracleOicCli is available from main."""
        assert hasattr(main_module, "FlextOracleOicCli")
        assert main_module.FlextOracleOicCli is FlextOracleOicCli

    def test_version_available(self) -> None:
        """Test __version__ is available from package."""
        assert __version__ is not None
        assert isinstance(__version__, str)
