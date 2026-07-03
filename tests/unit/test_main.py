"""Tests for main.py module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import flext_oracle_oic.main as main_module
from flext_oracle_oic import FlextOracleOicCli, __version__
from flext_oracle_oic.main import main


class TestsFlextOracleOicMain:
    """Test main function entry point."""

    def test_main_function_exists(self) -> None:
        """Test main function is callable."""
        assert callable(main)

    def test_main_returns_exit_code(self) -> None:
        """main() returns an int exit code; the __main__ entry wraps it in sys.exit()."""
        result = main([])
        assert isinstance(result, int)

    def test_cli_class_available(self) -> None:
        """Test FlextOracleOicCli is available from main."""
        assert main_module.FlextOracleOicCli is FlextOracleOicCli

    def test_version_available(self) -> None:
        """Test __version__ is available from package."""
        assert __version__ is not None
        assert isinstance(__version__, str)
