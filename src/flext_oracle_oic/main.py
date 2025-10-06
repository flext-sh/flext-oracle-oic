"""Main entry point for Oracle OIC Extension - FLEXT CLI Pattern.

FLEXT Unified Module Pattern: Single unified CLI class consolidating
all Oracle OIC CLI functionality. Implements complete FlextService pattern
with railway-oriented error handling.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import argparse
import sys
from typing import NoReturn

from flext_core import (
    FlextBus,
    FlextContainer,
    FlextContext,
    FlextDispatcher,
    FlextLogger,
    FlextRegistry,
    FlextResult,
    FlextService,
    FlextTypes,
)

from flext_oracle_oic import __version__
from flext_oracle_oic.factory import create_development_oic_service

# CLI output helper moved into FlextOracleOicCli class


class FlextOracleOicCli(FlextService[None]):
    """Unified Oracle OIC CLI Service - Single Class Pattern.

    Consolidates all Oracle OIC CLI functionality into a single unified service class:
    - Connection testing
    - Integration listing
    - Version display

    Implements complete FlextService pattern with railway-oriented error handling.
    """

    def __init__(self) -> None:
        """Initialize unified Oracle OIC CLI service."""
        super().__init__()
        self._logger = FlextLogger(f"{__name__}.{self.__class__.__name__}")

        # Complete FLEXT ecosystem integration for CLI
        self._container = FlextContainer.get_global()
        self._context = FlextContext()
        self._bus = FlextBus()
        self._dispatcher = FlextDispatcher()
        self._registry = FlextRegistry(dispatcher=self._dispatcher)

    def execute(self) -> FlextResult[None]:
        """Execute main CLI operation - run with default arguments."""
        exit_code = self.run_cli()
        if exit_code == 0:
            return FlextResult[None].ok(None)
        return FlextResult[None].fail(
            f"CLI execution failed with exit code {exit_code}"
        )

    # Nested Helper Classes

    class CliOutputHelper:
        """CLI output helper - nested within main class per unified pattern."""

        @staticmethod
        def print(text: str) -> None:
            """Print to CLI stdout."""
            sys.stdout.write(text + "\n")
            sys.stdout.flush()

    class BackwardCompatibilityHelper:
        """Backward compatibility functions - nested within main class."""

        def __init__(self, cli_instance: FlextOracleOicCli) -> None:
            """Initialize backward compatibility helper with CLI instance."""
            self._cli_instance = cli_instance

        def test_connection(self) -> None:
            """Test connection to Oracle OIC instance (backward compatibility)."""
            result = self._cli_instance.test_connection()
            if result.is_failure:
                self._cli_instance.CliOutputHelper.print(f"❌ {result.error}")
                sys.exit(1)

        def list_integrations(self) -> None:
            """List Oracle OIC integrations (backward compatibility)."""
            result = self._cli_instance.list_integrations()
            if result.is_failure:
                self._cli_instance.CliOutputHelper.print(f"❌ {result.error}")
                sys.exit(1)

        def show_version(self) -> None:
            """Show Oracle OIC Extension version (backward compatibility)."""
            result = self._cli_instance.show_version()
            if result.is_failure:
                self._cli_instance.CliOutputHelper.print(f"❌ {result.error}")
                sys.exit(1)

    # CLI Command Methods

    def test_connection(self) -> FlextResult[None]:
        """Test connection to Oracle OIC instance.

        Returns:
            FlextResult indicating success or failure.

        """
        try:
            if self._logger:
                self._logger.info("Testing Oracle OIC connection...")

            # Create development service for testing
            service_result = create_development_oic_service()
            if service_result.is_failure:
                return FlextResult[None].fail(
                    f"Failed to create service: {service_result.error}"
                )

            service = service_result.unwrap()
            if service is None:
                return FlextResult[None].fail("Service is None")

            # Test connection
            with service:
                connection_result = service.test_connection()
                if connection_result.is_success:
                    if self._logger:
                        self._logger.info("✅ Oracle OIC connection successful!")
                    self.CliOutputHelper.print(
                        "✅ Connection to Oracle OIC established successfully"
                    )
                    return FlextResult[None].ok(None)
                return FlextResult[None].fail(
                    f"Connection failed: {connection_result.error}"
                )

        except Exception as e:
            if self._logger:
                self._logger.exception("Connection test failed")
            return FlextResult[None].fail(f"Connection test failed: {e!s}")

    def list_integrations(self) -> FlextResult[None]:
        """List Oracle OIC integrations.

        Returns:
            FlextResult indicating success or failure.

        """
        try:
            if self._logger:
                self._logger.info("Listing Oracle OIC integrations...")

            # Create development service
            service_result = create_development_oic_service()
            if service_result.is_failure:
                return FlextResult[None].fail(
                    f"Failed to create service: {service_result.error}"
                )

            service = service_result.unwrap()
            if service is None:
                return FlextResult[None].fail("Service is None")

            # List integrations
            with service:
                integrations_result = service.list_integrations()
                if integrations_result.is_success:
                    integrations = integrations_result.unwrap() or []
                    if self._logger:
                        self._logger.info(f"Found {len(integrations)} integrations")

                    if integrations:
                        self.CliOutputHelper.print("📋 Oracle OIC Integrations:")
                        for integration in integrations:
                            self.CliOutputHelper.print(
                                f"  • {integration.name} (ID: {integration.integration_id})"
                            )
                            self.CliOutputHelper.print(
                                f"    Status: {integration.status}, Version: {integration.integration_version}"
                            )
                            if integration.description:
                                self.CliOutputHelper.print(
                                    f"    Description: {integration.description}"
                                )
                            self.CliOutputHelper.print("")
                    else:
                        self.CliOutputHelper.print("📋 No integrations found")
                    return FlextResult[None].ok(None)
                return FlextResult[None].fail(
                    f"Failed to list integrations: {integrations_result.error}"
                )

        except Exception as e:
            if self._logger:
                self._logger.exception("List integrations failed")
            return FlextResult[None].fail(f"List integrations failed: {e!s}")

    def show_version(self) -> FlextResult[None]:
        """Show Oracle OIC Extension version.

        Returns:
            FlextResult indicating success or failure.

        """
        try:
            self.CliOutputHelper.print(f"Oracle OIC Extension v{__version__}")
            self.CliOutputHelper.print(
                "FLEXT CLI Pattern: Enterprise Oracle Integration Cloud"
            )
            return FlextResult[None].ok(None)
        except Exception as e:
            if self._logger:
                self._logger.exception("Version display failed")
            return FlextResult[None].fail(f"Version display failed: {e!s}")

    def run_command(self, command: str) -> FlextResult[None]:
        """Run the specified CLI command.

        Args:
            command: The command to run ('test-connection', 'list-integrations', 'version').

        Returns:
            FlextResult indicating success or failure.

        """
        commands = {
            "test-connection": self.test_connection,
            "list-integrations": self.list_integrations,
            "version": self.show_version,
        }

        if command not in commands:
            return FlextResult[None].fail(f"Unknown command: {command}")

        return commands[command]()

    @staticmethod
    def create_parser() -> argparse.ArgumentParser:
        """Create the argument parser for CLI."""
        parser = argparse.ArgumentParser(
            prog="flext-oracle-oic-ext",
            description="FLEXT Oracle OIC Extension CLI - Enterprise Oracle Integration Cloud operations",
        )

        parser.add_argument(
            "--version",
            action="store_true",
            help="Show version information",
        )

        subparsers = parser.add_subparsers(
            dest="command",
            help="Available commands",
            metavar="COMMAND",
        )

        # test-connection command
        subparsers.add_parser(
            "test-connection",
            help="Test connection to Oracle OIC instance",
        )

        # list-integrations command
        subparsers.add_parser(
            "list-integrations",
            help="List Oracle OIC integrations",
        )

        # version command
        subparsers.add_parser(
            "version",
            help="Show Oracle OIC Extension version",
        )

        return parser

    def run_cli(self, args: list[str] | None = None) -> int:
        """Run the CLI with the given arguments.

        Args:
            args: Command line arguments (defaults to sys.argv[1:]).

        Returns:
            Exit code (0 for success, non-zero for failure).

        """
        parser = self.create_parser()
        parsed_args = parser.parse_args(args)

        # Handle --version flag
        if parsed_args.version or parsed_args.command == "version":
            result = self.show_version()
            return 0 if result.is_success else 1

        # Handle commands
        if parsed_args.command:
            result = self.run_command(parsed_args.command)
            return 0 if result.is_success else 1

        # No command provided
        parser.print_help()
        return 1

    @property
    def logger(self) -> FlextLogger:
        """Get the logger instance (public access for backward compatibility)."""
        if self._logger is None:
            self._logger = FlextLogger(f"{__name__}.{self.__class__.__name__}")
        return self._logger


# Global CLI instance for backward compatibility
_cli_instance = FlextOracleOicCli()
_backward_compat = _cli_instance.BackwardCompatibilityHelper(_cli_instance)


def main() -> NoReturn:
    """Run main CLI entry point - FLEXT CLI Pattern.

    FLEXT CLI Pattern: Main entry point for Oracle OIC Extension CLI
    with enterprise commands and structured logging.
    """
    try:
        exit_code = _cli_instance.run_cli()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        _cli_instance.logger.info("Oracle OIC Extension CLI interrupted by user")
        sys.exit(130)
    except Exception:
        _cli_instance.logger.exception("Oracle OIC Extension CLI error")
        sys.exit(1)


# Backward compatibility functions (using nested helper)
def test_connection() -> None:
    """Test connection to Oracle OIC instance (backward compatibility)."""
    _backward_compat.test_connection()


def list_integrations() -> None:
    """List Oracle OIC integrations (backward compatibility)."""
    _backward_compat.list_integrations()


def show_version() -> None:
    """Show Oracle OIC Extension version (backward compatibility)."""
    _backward_compat.show_version()


__all__: FlextTypes.StringList = [
    "FlextOracleOicCli",
    "list_integrations",
    "main",
    "show_version",
    "test_connection",
]

if __name__ == "__main__":
    main()
