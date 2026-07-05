"""Main entry point for Oracle OIC Extension - FLEXT CLI Pattern.

FLEXT Unified Module Pattern: Single unified CLI class consolidating
all Oracle OIC CLI functionality. Implements complete s pattern
with railway-oriented error handling.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, ClassVar

from flext_cli import cli, m as cli_m
from flext_core import r
from flext_oracle_oic import c, p, t
from flext_oracle_oic.__version__ import __version__
from flext_oracle_oic.service import FlextOracleOicService
from flext_oracle_oic.settings import FlextOracleOicSettings

if TYPE_CHECKING:
    from flext_oracle_oic.models import FlextOracleOicModels


class _TestConnectionCommand(cli_m.BaseModel):
    """Test connection to Oracle OIC instance."""

    def execute(self) -> p.Result[bool]:
        """Test the Oracle OIC connection through the canonical service."""
        try:
            return self._execute_connection_test()
        except c.EXC_NETWORK_TYPE as exc:
            return r[bool].fail_op("Connection test", exc)

    @staticmethod
    def _execute_connection_test() -> p.Result[bool]:
        """Execute the Oracle OIC connection test."""
        FlextOracleOicSettings.create_for_development()
        service = FlextOracleOicService()
        with service:
            connection_result = service.test_connection()
            if connection_result.success:
                cli.print(
                    "Connection to Oracle OIC established successfully",
                )
                return r[bool].ok(value=True)
            return r[bool].fail_op("Connection", connection_result.error)


class _ListIntegrationsCommand(cli_m.BaseModel):
    """List Oracle OIC integrations."""

    def execute(self) -> p.Result[bool]:
        """List integrations through the canonical service."""
        try:
            return self._execute_list_integrations()
        except c.EXC_NETWORK_TYPE as exc:
            return r[bool].fail_op("List integrations", exc)

    @staticmethod
    def _execute_list_integrations() -> p.Result[bool]:
        """Execute Oracle OIC integration listing."""
        FlextOracleOicSettings.create_for_development()
        service = FlextOracleOicService()
        integrations_result = service.list_integrations()
        if integrations_result.failure:
            return r[bool].fail(
                f"Failed to list integrations: {integrations_result.error}",
            )
        integrations = integrations_result.value or []
        _print_integrations(integrations)
        return r[bool].ok(value=True)


class _ShowVersionCommand(cli_m.BaseModel):
    """Show Oracle OIC Extension version."""

    def execute(self) -> p.Result[bool]:
        """Print Oracle OIC Extension version through cli.print."""
        cli.print(f"Oracle OIC Extension v{__version__}")
        cli.print("FLEXT CLI Pattern: Enterprise Oracle Integration Cloud")
        return r[bool].ok(value=True)


def _print_integrations(
    integrations: t.SequenceOf[FlextOracleOicModels.OracleOic.OICIntegrationInfo],
) -> None:
    """Print integrations to CLI output via the canonical cli facade."""
    if not integrations:
        cli.print("📋 No integrations found")
        return
    cli.print("📋 Oracle OIC Integrations:")
    for integration in integrations:
        cli.print(
            f"  • {integration.name} (ID: {integration.integration_id})",
        )
        cli.print(
            f"    Status: {integration.status}, "
            f"Version: {integration.integration_version}",
        )
        if integration.description:
            cli.print(f"    Description: {integration.description}")


class FlextOracleOicCli:
    """Oracle OIC CLI dispatch via the canonical cli facade.

    Composes a Typer app with three Pydantic-driven commands:
    - test-connection: probe the configured Oracle OIC endpoint
    - list-integrations: enumerate published integrations
    - version: print the Oracle OIC Extension version
    """

    APP_NAME: ClassVar[str] = "flext-oracle-oic-ext"
    APP_HELP: ClassVar[str] = (
        "FLEXT Oracle OIC Extension CLI - Enterprise Oracle "
        "Integration Cloud operations"
    )

    @classmethod
    def build_app(cls) -> t.Cli.CliApp:
        """Build the Typer application with the registered commands."""
        app = cli.create_app_with_common_params(
            name=cls.APP_NAME,
            help_text=cls.APP_HELP,
        )
        cli.register_result_routes(
            app,
            [
                cli_m.Cli.ResultCommandRoute(
                    name="test-connection",
                    help_text="Test connection to Oracle OIC instance",
                    model_cls=_TestConnectionCommand,
                    handler=lambda params: params.execute(),
                ),
                cli_m.Cli.ResultCommandRoute(
                    name="list-integrations",
                    help_text="List Oracle OIC integrations",
                    model_cls=_ListIntegrationsCommand,
                    handler=lambda params: params.execute(),
                ),
                cli_m.Cli.ResultCommandRoute(
                    name="version",
                    help_text="Show Oracle OIC Extension version",
                    model_cls=_ShowVersionCommand,
                    handler=lambda params: params.execute(),
                ),
            ],
        )
        return app


def main(args: t.StrSequence | None = None) -> int:
    """Run main CLI entry point - FLEXT CLI Pattern."""
    app = FlextOracleOicCli.build_app()
    try:
        outcome = cli.execute_app(
            app,
            prog_name=FlextOracleOicCli.APP_NAME,
            args=list(args) if args is not None else sys.argv[1:],
        )
    except KeyboardInterrupt:
        return 130
    return 0 if outcome.success else 1


__all__: t.StrSequence = ("FlextOracleOicCli", "main")
