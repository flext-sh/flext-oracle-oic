"""Main entry point for Oracle OIC Extension - FLEXT CLI Pattern.

FLEXT Unified Module Pattern: Single unified CLI class consolidating
all Oracle OIC CLI functionality. Implements complete FlextService pattern
with railway-oriented error handling.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import argparse
import json
import sys
from typing import NoReturn, override

from flext_core import (
    FlextContainer,
    FlextContext,
    FlextRegistry,
    FlextResult,
    FlextService,
)
from flext_oracle_oic import __version__
from flext_oracle_oic.factory import FlextOracleOicFactory
from flext_oracle_oic.models import FlextOracleOicModels
from flext_oracle_oic.service import FlextOracleOicService

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
        # Logger is inherited from parent class

        # Complete FLEXT ecosystem integration for CLI
        self._container = FlextContainer.get_global()
        self._context = FlextContext()
        self._dispatcher: object | None = None  # CommandBus not required for CLI
        self._registry = FlextRegistry(dispatcher=None)
        self._factory = FlextOracleOicFactory()

    @override
    def execute(self) -> FlextResult[None]:
        """Execute main CLI operation - run with default arguments."""
        exit_code = self.run_cli()
        if exit_code == 0:
            return FlextResult[None].ok(None)
        return FlextResult[None].fail(
            f"CLI execution failed with exit code {exit_code}",
        )

    # Nested Helper Classes

    class CliOutputHelper:
        """CLI output helper - nested within main class per unified pattern."""

        @staticmethod
        def print(text: str) -> None:
            """Print to CLI stdout."""
            sys.stdout.write(text + "\n")
            sys.stdout.flush()

    # CLI Command Methods

    def test_connection(self) -> FlextResult[bool]:
        """Test connection to Oracle OIC instance.

        Returns:
        FlextResult indicating success or failure.

        """
        try:
            if self.logger:
                self.logger.info("Testing Oracle OIC connection...")

            # Create development service for testing
            service_result = self._factory.create_development_oic_service()
            if service_result.is_failure:
                return FlextResult[bool].fail(
                    f"Failed to create service: {service_result.error}",
                )

            service = service_result.value
            if service is None:
                return FlextResult[bool].fail("Service is None")

            # Test connection
            with service:
                connection_result = service.test_connection()
                if connection_result.is_success:
                    if self.logger:
                        self.logger.info("Oracle OIC connection successful!")
                    self.CliOutputHelper.print(
                        "Connection to Oracle OIC established successfully",
                    )
                    return FlextResult[bool].ok(value=True)
                return FlextResult[bool].fail(
                    f"Connection failed: {connection_result.error}",
                )

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            if self.logger:
                self.logger.exception("Connection test failed")
            return FlextResult[bool].fail(f"Connection test failed: {e!s}")

    def list_integrations(self) -> FlextResult[bool]:
        """List Oracle OIC integrations.

        Returns:
        FlextResult indicating success or failure.

        """
        try:
            if self.logger:
                self.logger.info("Listing Oracle OIC integrations...")

            # Create development service
            service_result = self._factory.create_development_oic_service()
            if service_result.is_failure:
                return FlextResult[bool].fail(
                    f"Failed to create service: {service_result.error}",
                )

            raw_service = service_result.value
            if raw_service is None:
                return FlextResult[bool].fail("Service is None")
            service: FlextOracleOicService = raw_service
            # List integrations
            return self._list_integrations_with_service(service)

        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            if self.logger:
                self.logger.exception("List integrations failed")
            return FlextResult[bool].fail(f"List integrations failed: {e!s}")

    def _list_integrations_with_service(
        self,
        service: FlextOracleOicService,
    ) -> FlextResult[bool]:
        """List integrations using the provided service.

        Args:
            service: Oracle OIC service instance

        Returns:
            FlextResult[bool]: Success or failure result

        """
        integrations_result = service.list_integrations()
        if integrations_result.is_failure:
            return FlextResult[bool].fail(
                f"Failed to list integrations: {integrations_result.error}",
            )

        integrations = integrations_result.value or []
        if self.logger:
            self.logger.info(f"Found {len(integrations)} integrations")

        self._print_integrations(integrations)
        return FlextResult[bool].ok(value=True)

    def _print_integrations(
        self,
        integrations: list[FlextOracleOicModels.OracleOic.OICIntegrationInfo],
    ) -> None:
        """Print integrations to CLI output.

        Args:
            integrations: List of integration objects

        """
        if not integrations:
            self.CliOutputHelper.print("📋 No integrations found")
            return

        self.CliOutputHelper.print("📋 Oracle OIC Integrations:")
        for integration in integrations:
            self.CliOutputHelper.print(
                f"  • {integration.name} (ID: {integration.integration_id})",
            )
            self.CliOutputHelper.print(
                f"    Status: {integration.status}, Version: {integration.integration_version}",
            )
            if integration.description:
                self.CliOutputHelper.print(
                    f"    Description: {integration.description}",
                )
            self.CliOutputHelper.print("")

    def show_version(self) -> FlextResult[bool]:
        """Show Oracle OIC Extension version.

        Returns:
        FlextResult indicating success or failure.

        """
        try:
            self.CliOutputHelper.print(f"Oracle OIC Extension v{__version__}")
            self.CliOutputHelper.print(
                "FLEXT CLI Pattern: Enterprise Oracle Integration Cloud",
            )
            return FlextResult[bool].ok(value=True)
        except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError) as e:
            if self.logger:
                self.logger.exception("Version display failed")
            return FlextResult[bool].fail(f"Version display failed: {e!s}")

    def run_command(self, command: str) -> FlextResult[bool]:
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
            return FlextResult[bool].fail(f"Unknown command: {command}")

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


def main() -> NoReturn:
    """Run main CLI entry point - FLEXT CLI Pattern.

    FLEXT CLI Pattern: Main entry point for Oracle OIC Extension CLI
    with enterprise commands and structured logging.
    """
    cli_instance = FlextOracleOicCli()
    try:
        exit_code = cli_instance.run_cli()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        cli_instance.logger.info("Oracle OIC Extension CLI interrupted by user")
        sys.exit(130)
    except (ConnectionError, TimeoutError, ValueError, json.JSONDecodeError):
        cli_instance.logger.exception("Oracle OIC Extension CLI error")
        sys.exit(1)


__all__: list[str] = [
    "FlextOracleOicCli",
    "main",
]

if __name__ == "__main__":
    main()
