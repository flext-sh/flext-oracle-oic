"""Main entry point for Oracle OIC Extension - FLEXT CLI Pattern.

FLEXT Unified Module Pattern: Single unified CLI class consolidating
all Oracle OIC CLI functionality. Implements complete s pattern
with railway-oriented error handling.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import sys

from flext_cli import cli, m as cli_m

from flext_core import r
from flext_oracle_oic import c, p, t
from flext_oracle_oic.__version__ import __version__
from flext_oracle_oic.service import FlextOracleOicService


class FlextOracleOicCli:
    """Oracle OIC CLI dispatch via the canonical cli facade.

    Composes a Typer app with three Pydantic-driven commands:
    - test-connection: probe the configured Oracle OIC endpoint
    - list-integrations: enumerate published integrations
    - version: print the Oracle OIC Extension version
    """

    @staticmethod
    def probe_connection(_params: t.Cli.ModelLike) -> p.Result[bool]:
        """Probe the configured connection for a validated empty CLI request.

        Returns:
            The resulting ``p.Result[bool]``.
        """
        try:
            service = FlextOracleOicService()
            with service:
                connection_result = service.test_connection()
                if connection_result.success:
                    cli.print("Connection to Oracle OIC established successfully")
                    return r[bool].ok(value=True)
                return r[bool].fail_op("Connection", connection_result.error)
        except c.EXC_NETWORK_TYPE as exc:
            return r[bool].fail_op("Connection test", exc)

    @staticmethod
    def list_integrations(_params: t.Cli.ModelLike) -> p.Result[bool]:
        """List integrations for a validated empty CLI request.

        Returns:
            The resulting ``p.Result[bool]``.
        """
        try:
            service = FlextOracleOicService()
            integrations_result = service.list_integrations()
        except c.EXC_NETWORK_TYPE as exc:
            return r[bool].fail_op("List integrations", exc)
        if integrations_result.failure:
            return r[bool].fail(
                f"Failed to list integrations: {integrations_result.error}",
            )
        integrations = integrations_result.unwrap()
        if not integrations:
            cli.print("📋 No integrations found")
            return r[bool].ok(value=True)
        cli.print("📋 Oracle OIC Integrations:")
        for integration in integrations:
            cli.print(f"  • {integration.name} (ID: {integration.integration_id})")
            cli.print(
                f"    Status: {integration.status}, "
                f"Version: {integration.integration_version}",
            )
            if integration.description:
                cli.print(f"    Description: {integration.description}")
        return r[bool].ok(value=True)

    @staticmethod
    def show_version(_params: t.Cli.ModelLike) -> p.Result[bool]:
        """Print the package version for a validated empty CLI request.

        Returns:
            The resulting ``p.Result[bool]``.
        """
        cli.print(f"Oracle OIC Extension v{__version__}")
        cli.print("FLEXT CLI Pattern: Enterprise Oracle Integration Cloud")
        return r[bool].ok(value=True)

    @classmethod
    def build_app(cls) -> p.Cli.Application:
        """Build the Typer application with the registered commands.

        Returns:
            The resulting ``p.Cli.Application``.
        """
        app = cli.create_app_with_common_params(
            name=c.Cli.APP_NAME,
            help_text=c.Cli.APP_HELP,
        )
        cli.register_result_routes(
            app,
            [
                cli_m.Cli.ResultCommandRoute(
                    name="test-connection",
                    help_text="Test connection to Oracle OIC instance",
                    model_cls=cli_m.Cli.EmptyRequest,
                    handler=cls.probe_connection,
                ),
                cli_m.Cli.ResultCommandRoute(
                    name="list-integrations",
                    help_text="List Oracle OIC integrations",
                    model_cls=cli_m.Cli.EmptyRequest,
                    handler=cls.list_integrations,
                ),
                cli_m.Cli.ResultCommandRoute(
                    name="version",
                    help_text="Show Oracle OIC Extension version",
                    model_cls=cli_m.Cli.EmptyRequest,
                    handler=cls.show_version,
                ),
            ],
        )
        return app


def main(args: t.StrSequence | None = None) -> int:
    """Run main CLI entry point - FLEXT CLI Pattern.

    Returns:
        The resulting ``int``.
    """
    app = FlextOracleOicCli.build_app()
    try:
        outcome = cli.execute_app(
            app,
            prog_name=c.Cli.APP_NAME,
            args=list(args) if args is not None else sys.argv[1:],
        )
    except KeyboardInterrupt:
        return 130
    return 0 if outcome.success else 1


__all__: t.StrSequence = ("FlextOracleOicCli", "main")
