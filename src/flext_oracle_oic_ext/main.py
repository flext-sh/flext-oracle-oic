"""Main entry point for Oracle OIC Extension - EXTENSION Pattern.

This module implements the EXTENSION PEP8 pattern for CLI Oracle OIC Extension.


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import sys
from typing import NoReturn

import typer

from flext_core import FlextLogger, FlextTypes
from flext_oracle_oic_ext import (
    __version__,
    create_development_oic_service,
)


def version_callback(*, value: bool) -> None:
    """Version callback for --version option."""
    if value:
        typer.echo(f"Oracle OIC Extension v{__version__}")
        typer.echo("EXTENSION Pattern: Enterprise Oracle Integration Cloud")
        raise typer.Exit


logger = FlextLogger(__name__)
app = typer.Typer(
    name="oracle-oic-ext",
    help="FLEXT Oracle OIC Extension CLI - Enterprise Oracle Integration Cloud operations",
    no_args_is_help=True,
)


@app.callback()
def main_callback(
    *,
    version: bool = typer.Option(
        default=False,
        flag_value=True,
        callback=version_callback,
        is_eager=True,
        help="Show version",
    ),
) -> None:
    """Oracle OIC Extension CLI main callback."""
    # This callback is needed for the --version option to work


def _handle_service_error(message: str) -> NoReturn:
    """Handle service creation error by logging and raising typer.Exit."""
    logger.error(message)
    raise typer.Exit(code=1) from None


def _handle_connection_error(message: str) -> NoReturn:
    """Handle connection error by logging and raising typer.Exit."""
    logger.error(message)
    raise typer.Exit(code=1) from None


def _handle_general_error(message: str, error: Exception) -> NoReturn:
    """Handle general error by logging and raising typer.Exit."""
    logger.error(f"Error: {message}")
    typer.echo(f"❌ {message}: {error}")
    raise typer.Exit(code=1) from error


@app.command("test-connection")
async def test_connection() -> None:
    """Test connection to Oracle OIC instance.

    EXTENSION Pattern: Command to test Oracle OIC connectivity
    with authentication and configuration validation.
    """
    try:
        logger.info("Testing Oracle OIC connection...")

        # Create development service for testing
        service_result = create_development_oic_service()
        if not service_result.success:
            _handle_service_error(f"Failed to create service: {service_result.error}")

        service = service_result.data
        if service is None:
            _handle_service_error("Service is None")

        # Test connection
        with service:
            connection_result = await service.test_connection()
            if connection_result.success:
                logger.info("✅ Oracle OIC connection successful!")
                typer.echo("✅ Connection to Oracle OIC established successfully")
            else:
                _handle_connection_error(
                    f"❌ Connection failed: {connection_result.error}",
                )

    except Exception as e:
        _handle_general_error("Connection test failed", e)


@app.command("list-integrations")
async def list_integrations() -> None:
    """List Oracle OIC integrations.

    EXTENSION Pattern: Command to list Oracle OIC integrations
    with detailed information and status.

    Returns:
            object: Description of return value.

    """
    try:
        logger.info("Listing Oracle OIC integrations...")

        # Create development service
        service_result = create_development_oic_service()
        if not service_result.success:
            _handle_service_error(f"Failed to create service: {service_result.error}")

        service = service_result.data
        if service is None:
            _handle_service_error("Service is None")

        # List integrations
        with service:
            integrations_result = await service.list_integrations()
            if integrations_result.success:
                integrations = integrations_result.data or []
                logger.info(f"Found {len(integrations)} integrations")

                if integrations:
                    typer.echo("📋 Oracle OIC Integrations:")
                    for integration in integrations:
                        typer.echo(
                            f"  • {integration.name} (ID: {integration.integration_id})",
                        )
                        typer.echo(
                            f"    Status: {integration.status}, Version: {integration.version}",
                        )
                        if integration.description:
                            typer.echo(f"    Description: {integration.description}")
                        typer.echo("")
                else:
                    typer.echo("📋 No integrations found")
            else:
                _handle_connection_error(
                    f"❌ Failed to list integrations: {integrations_result.error}",
                )

    except Exception as e:
        _handle_general_error("List integrations failed", e)


@app.command("version")
def show_version() -> None:
    """Show Oracle OIC Extension version."""
    typer.echo(f"Oracle OIC Extension v{__version__}")
    typer.echo("EXTENSION Pattern: Enterprise Oracle Integration Cloud")


def main() -> NoReturn:
    """Run main CLI entry point - EXTENSION Pattern.

    EXTENSION Pattern: Main entry point for Oracle OIC Extension CLI
    with enterprise commands and structured logging.
    """
    try:
        app()
        sys.exit(0)  # Explicit exit for NoReturn
    except KeyboardInterrupt:
        logger.info("Oracle OIC Extension CLI interrupted by user")
        sys.exit(130)
    except Exception:
        logger.exception("Oracle OIC Extension CLI error")
        sys.exit(1)


__all__: FlextTypes.Core.StringList = ["app", "create_development_oic_service", "main"]

if __name__ == "__main__":
    main()
