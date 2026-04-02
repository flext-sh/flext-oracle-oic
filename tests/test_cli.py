"""Tests for cli.py module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from unittest.mock import Mock, patch

from flext_oracle_oic import FlextOracleOicCli
from flext_oracle_oic.main import main


class TestCLI:
    """Test CLI module functionality."""

    def test_imports_available(self) -> None:
        """Test that CLI imports are available."""
        assert main is not None
        assert FlextOracleOicCli is not None
        assert callable(main)

    @patch("flext_oracle_oic.main.main")
    def test_cli_main_callable(self, mock_main: Mock) -> None:
        """Test CLI main is callable."""
        mock_main.return_value = None
        assert callable(main)
        assert main is not None
