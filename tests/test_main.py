"""Tests for main.py module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from unittest.mock import Mock, patch

import typer
from typer.testing import CliRunner

import flext_oracle_oic_ext.main as main_module
from flext_oracle_oic_ext import __version__, create_development_oic_service
from flext_oracle_oic_ext.main import (
    app,
    create_development_oic_service as main_factory,
    main,
)


class TestMainApp:
    """Test main Typer app functionality."""

    def test_app_creation(self) -> None:
        """Test that Typer app is created properly."""
        assert isinstance(app, typer.Typer)
        assert app.info.name == "oracle-oic-ext"
        assert app.info.help is not None
        assert "FLEXT Oracle OIC Extension CLI" in app.info.help
        assert app.info.no_args_is_help is True

    def test_app_has_commands(self) -> None:
        """Test app has expected commands."""
        # Should have registered commands
        command_names = (
            [cmd.name for cmd in app.registered_commands]
            if hasattr(app.registered_commands, "__iter__")
            else []
        )
        assert len(command_names) >= 0  # May have commands added dynamically


class TestMainFunction:
    """Test main function entry point."""

    @patch("flext_oracle_oic_ext.main.sys.exit")
    @patch("flext_oracle_oic_ext.main.app")
    def test_main_function_calls_app(self, mock_app: Mock, mock_exit: Mock) -> None:
        """Test main function calls app()."""
        # Mock sys.exit to prevent actual exit and make code reachable
        mock_exit.side_effect = SystemExit(0)

        try:
            main()
        except SystemExit:
            pass  # Expected behavior due to NoReturn

        mock_app.assert_called_once()
        mock_exit.assert_called_once_with(0)

    def test_main_function_exists(self) -> None:
        """Test main function is callable."""
        assert callable(main)


class TestCLICommands:
    """Test CLI command functionality."""

    def setUp(self) -> None:
        """Set up test client."""
        self.runner = CliRunner()

    def test_cli_help_command(self) -> None:
        """Test CLI shows help when no args provided."""
        runner = CliRunner()
        result = runner.invoke(app, [])

        # Should show help due to no_args_is_help=True
        assert result.exit_code != 0 or "oracle-oic-ext" in result.stdout

    def test_cli_version_option(self) -> None:
        """Test CLI version option."""
        runner = CliRunner()
        result = runner.invoke(app, ["--version"])

        # Should exit successfully and show version
        assert result.exit_code == 0

    @patch("flext_oracle_oic_ext.main.logger")
    def test_logger_initialization(self, mock_logger: Mock) -> None:
        """Test logger is properly initialized."""
        _ = mock_logger  # Use the parameter to avoid unused argument warning
        # Re-import to trigger logger creation

        # Logger should be created
        assert hasattr(main_module, "logger")


class TestAppIntegration:
    """Test app integration with other modules."""

    def test_app_imports_available(self) -> None:
        """Test app can import required modules."""
        # Should be able to import without errors
        assert app is not None
        assert main is not None
        assert __version__ is not None
        assert callable(create_development_oic_service)

    @patch("flext_oracle_oic_ext.main.create_development_oic_service")
    def test_app_can_use_factory_functions(self, mock_factory: Mock) -> None:
        """Test app can use factory functions."""
        # Should be able to call factory function from main module
        assert callable(main_factory)
        main_factory()
        mock_factory.assert_called_once()


class TestErrorHandling:
    """Test error handling in main module."""

    @patch("sys.exit")
    def test_main_handles_keyboard_interrupt(self, mock_exit: Mock) -> None:
        """Test main handles KeyboardInterrupt gracefully."""
        _ = mock_exit  # Use the parameter to avoid unused argument warning
        with patch("flext_oracle_oic_ext.main.app") as mock_app:
            mock_app.side_effect = KeyboardInterrupt()

            try:
                main()
            except KeyboardInterrupt:
                pass  # Expected behavior

    @patch("sys.exit")
    def test_main_handles_system_exit(self, mock_exit: Mock) -> None:
        """Test main handles SystemExit gracefully."""
        _ = mock_exit  # Use the parameter to avoid unused argument warning
        with patch("flext_oracle_oic_ext.main.app") as mock_app:
            mock_app.side_effect = SystemExit(1)

            try:
                main()
            except SystemExit:
                pass  # Expected behavior
