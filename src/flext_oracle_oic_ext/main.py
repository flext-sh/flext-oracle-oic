"""Main entry point for Oracle OIC Extension - EXTENSION Pattern.

Este módulo implementa o padrão EXTENSION PEP8 para CLI Oracle OIC Extension.
"""

from __future__ import annotations

import sys
from typing import NoReturn

import typer
from flext_core import get_logger

from flext_oracle_oic_ext import (
    create_development_oic_service,
)

logger = get_logger(__name__)
app = typer.Typer(
    name="oracle-oic-ext",
    help="FLEXT Oracle OIC Extension CLI - Enterprise Oracle Integration Cloud operations",
    no_args_is_help=True,
)


@app.command("test-connection")
def test_connection() -> None:
    """Test connection to Oracle OIC instance.

    Padrão EXTENSION: Comando para testar conectividade Oracle OIC
    com validação de autenticação e configuração.
    """
    try:
        logger.info("Testing Oracle OIC connection...")

        # Create development service for testing
        service_result = create_development_oic_service()
        if not service_result.success:
            logger.error(f"Failed to create service: {service_result.error}")
            raise typer.Exit(code=1)

        service = service_result.data
        if service is None:
            logger.error("Service is None")
            raise typer.Exit(code=1)

        # Test connection
        with service:
            connection_result = service.test_connection()
            if connection_result.success:
                logger.info("✅ Oracle OIC connection successful!")
                typer.echo("✅ Connection to Oracle OIC established successfully")
            else:
                logger.error(f"❌ Connection failed: {connection_result.error}")
                typer.echo(f"❌ Connection failed: {connection_result.error}")
                raise typer.Exit(code=1)

    except Exception as e:
        logger.exception(f"Connection test error: {e}")
        typer.echo(f"❌ Connection test failed: {e}")
        raise typer.Exit(code=1)


@app.command("list-integrations")
def list_integrations() -> None:
    """List Oracle OIC integrations.

    Padrão EXTENSION: Comando para listar integrações Oracle OIC
    com informações detalhadas e status.
    """
    try:
        logger.info("Listing Oracle OIC integrations...")

        # Create development service
        service_result = create_development_oic_service()
        if not service_result.success:
            logger.error(f"Failed to create service: {service_result.error}")
            raise typer.Exit(code=1)

        service = service_result.data
        if service is None:
            logger.error("Service is None")
            raise typer.Exit(code=1)

        # List integrations
        with service:
            integrations_result = service.list_integrations()
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
                logger.error(
                    f"❌ Failed to list integrations: {integrations_result.error}",
                )
                typer.echo(
                    f"❌ Failed to list integrations: {integrations_result.error}",
                )
                raise typer.Exit(code=1)

    except Exception as e:
        logger.exception(f"List integrations error: {e}")
        typer.echo(f"❌ List integrations failed: {e}")
        raise typer.Exit(code=1)


@app.command("version")
def show_version() -> None:
    """Show Oracle OIC Extension version."""
    from flext_oracle_oic_ext import __version__

    typer.echo(f"Oracle OIC Extension v{__version__}")
    typer.echo("EXTENSION Pattern: Enterprise Oracle Integration Cloud")


def main() -> NoReturn:
    """Main CLI entry point - EXTENSION Pattern.

    Padrão EXTENSION: Entry point principal para CLI Oracle OIC Extension
    com comandos enterprise e logging estruturado.
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


__all__: list[str] = ["app", "main"]

if __name__ == "__main__":
    main()
