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
from collections.abc import Sequence
from typing import override

from flext_infra import __version__

from flext_core import FlextService, r
from flext_oracle_oic import (
    FlextOracleOicModels,
    FlextOracleOicService,
    FlextOracleOicSettings,
    t,
)


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

    @staticmethod
    def create_parser() -> argparse.ArgumentParser:
        """Create the argument parser for CLI."""
        parser = argparse.ArgumentParser(
            prog="flext-oracle-oic-ext",
            description="FLEXT Oracle OIC Extension CLI - Enterprise Oracle Integration Cloud operations",
        )
        _ = parser.add_argument(
            "--version",
            action="store_true",
            help="Show version information",
        )
        subparsers = parser.add_subparsers(
            dest="command",
            help="Available commands",
            metavar="COMMAND",
        )
        subparsers.add_parser(
            "test-connection",
            help="Test connection to Oracle OIC instance",
        )
        subparsers.add_parser("list-integrations", help="List Oracle OIC integrations")
        subparsers.add_parser("version", help="Show Oracle OIC Extension version")
        return parser

    @override
    def execute(self) -> r[None]:
        """Execute main CLI operation - run with default arguments."""
        exit_code = self.run_cli()
        if exit_code == 0:
            return r[None].ok(None)
        return r[None].fail(f"CLI execution failed with exit code {exit_code}")

    def list_integrations(self) -> r[bool]:
        """List Oracle OIC integrations.

        Returns:
        r indicating success or failure.

        """
        try:
            if self.logger:
                self.logger.info("Listing Oracle OIC integrations...")
            FlextOracleOicSettings.create_for_development()
            service = FlextOracleOicService()
            return self._list_integrations_with_service(service)
        except (ConnectionError, TimeoutError, ValueError) as exc:
            if self.logger:
                self.logger.exception("List integrations failed")
            return r[bool].fail(f"List integrations failed: {exc!s}")

    def run_cli(self, args: t.StrSequence | None = None) -> int:
        """Run the CLI with the given arguments.

        Args:
        args: Command line arguments (defaults to sys.argv[1:]).

        Returns:
        Exit code (0 for success, non-zero for failure).

        """
        parser = self.create_parser()
        parsed_args = parser.parse_args(args)
        if parsed_args.version or parsed_args.command == "version":
            result = self.show_version()
            return 0 if result.is_success else 1
        if parsed_args.command:
            result = self.run_command(parsed_args.command)
            return 0 if result.is_success else 1
        parser.print_help()
        return 1

    def run_command(self, command: str) -> r[bool]:
        """Run the specified CLI command.

        Args:
        command: The command to run ('test-connection', 'list-integrations', 'version').

        Returns:
        r indicating success or failure.

        """
        commands = {
            "test-connection": self.test_connection,
            "list-integrations": self.list_integrations,
            "version": self.show_version,
        }
        if command not in commands:
            return r[bool].fail(f"Unknown command: {command}")
        return commands[command]()

    def show_version(self) -> r[bool]:
        """Show Oracle OIC Extension version.

        Returns:
        r indicating success or failure.

        """
        try:
            _ = sys.stdout.write(f"Oracle OIC Extension v{__version__}\n")
            _ = sys.stdout.write(
                "FLEXT CLI Pattern: Enterprise Oracle Integration Cloud\n",
            )
            return r[bool].ok(value=True)
        except (ConnectionError, TimeoutError, ValueError) as exc:
            if self.logger:
                self.logger.exception("Version display failed")
            return r[bool].fail(f"Version display failed: {exc!s}")

    def test_connection(self) -> r[bool]:
        """Test connection to Oracle OIC instance.

        Returns:
        r indicating success or failure.

        """
        try:
            if self.logger:
                self.logger.info("Testing Oracle OIC connection...")
            FlextOracleOicSettings.create_for_development()
            service = FlextOracleOicService()
            with service:
                connection_result = service.test_connection()
                if connection_result.is_success:
                    if self.logger:
                        self.logger.info("Oracle OIC connection successful!")
                    _ = sys.stdout.write(
                        "Connection to Oracle OIC established successfully\n",
                    )
                    return r[bool].ok(value=True)
                return r[bool].fail(f"Connection failed: {connection_result.error}")
        except (ConnectionError, TimeoutError, ValueError) as exc:
            if self.logger:
                self.logger.exception("Connection test failed")
            return r[bool].fail(f"Connection test failed: {exc!s}")

    def _list_integrations_with_service(
        self,
        service: FlextOracleOicService,
    ) -> r[bool]:
        """List integrations using the provided service.

        Args:
            service: Oracle OIC service instance

        Returns:
            r[bool]: Success or failure result

        """
        integrations_result = service.list_integrations()
        if integrations_result.is_failure:
            return r[bool].fail(
                f"Failed to list integrations: {integrations_result.error}",
            )
        integrations = integrations_result.value or []
        if self.logger:
            self.logger.info(f"Found {len(integrations)} integrations")
        self._print_integrations(integrations)
        return r[bool].ok(value=True)

    def _print_integrations(
        self,
        integrations: Sequence[FlextOracleOicModels.OracleOic.OICIntegrationInfo],
    ) -> None:
        """Print integrations to CLI output.

        Args:
            integrations: List of integration objects

        """
        if not integrations:
            _ = sys.stdout.write("📋 No integrations found\n")
            return
        _ = sys.stdout.write("📋 Oracle OIC Integrations:\n")
        for integration in integrations:
            _ = sys.stdout.write(
                f"  • {integration.name} (ID: {integration.integration_id})\n",
            )
            _ = sys.stdout.write(
                f"    Status: {integration.status}, Version: {integration.integration_version}\n",
            )
            if integration.description:
                _ = sys.stdout.write(f"    Description: {integration.description}\n")
            _ = sys.stdout.write("\n")


def main() -> int:
    """Run main CLI entry point - FLEXT CLI Pattern.

    FLEXT CLI Pattern: Main entry point for Oracle OIC Extension CLI
    with enterprise commands and structured logging.
    """
    cli_instance = FlextOracleOicCli()
    try:
        return cli_instance.run_cli()
    except KeyboardInterrupt:
        cli_instance.logger.info("Oracle OIC Extension CLI interrupted by user")
        return 130
    except (ConnectionError, TimeoutError, ValueError):
        cli_instance.logger.exception("Oracle OIC Extension CLI error")
        return 1


__all__: t.StrSequence = ["FlextOracleOicCli", "main"]
