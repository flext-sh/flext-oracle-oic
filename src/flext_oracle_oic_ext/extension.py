"""Oracle Integration Cloud extension implementation.

REFACTORED: Uses flext-core patterns.
Zero tolerance for code duplication.
"""

from __future__ import annotations

import subprocess
import sys
from typing import Any

from meltano.edk import models
from meltano.edk.extension import ExtensionBase

from flext_observability.logging import get_logger
from flext_oracle_oic_ext.config import OracleOICExtensionSettings
from flext_oracle_oic_ext.lifecycle import LifecycleManager
from flext_oracle_oic_ext.monitoring import MonitoringService

logger = get_logger(__name__)


class OracleOICExtension(ExtensionBase):
    """Extension for Oracle Integration Cloud operations."""

    def __init__(self) -> None:
        self.oracle_oic_bin = "oracle-oic-ext"
        self.lifecycle_manager: LifecycleManager | None = None
        self.monitoring_service: MonitoringService | None = None
        self.config: dict[str, Any] = {}

    def invoke(self, command_name: str | None, *command_args: Any) -> None:
        """Invoke a command within the Oracle OIC extension.

        Routes commands to appropriate handlers based on command prefix.
        Supports lifecycle:, monitor:, and extraction: command namespaces.

        Args:
            command_name: Command to execute (e.g., 'lifecycle:activate').
            *command_args: Arguments to pass to the command handler.

        """
        if not command_name:
            # Show help if no command provided:
            self._show_help()
            return

        # Initialize services with config
        self._initialize_services()

        # Route to appropriate handler
        if command_name.startswith("lifecycle:"):
            self._handle_lifecycle_command(command_name, *command_args)
        elif command_name.startswith("monitor:"):
            self._handle_monitoring_command(command_name, *command_args)
        elif command_name.startswith("extract:"):
            self._handle_extraction_command(command_name, *command_args)
        elif command_name.startswith("transform:"):
            self._handle_transformation_command(command_name, *command_args)
        else:
            logger.error("Unknown command: %s", command_name)
            sys.exit(1)

    def describe(self) -> models.Describe:
        """Describe available commands and capabilities.

        Returns:
            Describe model containing command information and metadata.

        """
        return models.Describe(
            commands=[
                # Lifecycle Management Commands
                models.ExtensionCommand(
                    name="lifecycle:activate",
                    description="Activate an integration",
                ),
                models.ExtensionCommand(
                    name="lifecycle:deactivate",
                    description="Deactivate an integration",
                ),
                models.ExtensionCommand(
                    name="lifecycle:bulk-activate",
                    description="Activate multiple integrations",
                ),
                models.ExtensionCommand(
                    name="lifecycle:bulk-deactivate",
                    description="Deactivate multiple integrations",
                ),
                models.ExtensionCommand(
                    name="lifecycle:status",
                    description="Check integration status",
                ),
                # Monitoring Commands
                models.ExtensionCommand(
                    name="monitor:health",
                    description="Check OIC instance health",
                ),
                models.ExtensionCommand(
                    name="monitor:performance",
                    description="Get performance metrics",
                ),
                models.ExtensionCommand(
                    name="monitor:errors",
                    description="Analyze error patterns",
                ),
                models.ExtensionCommand(
                    name="monitor:usage",
                    description="Get usage analytics",
                ),
                # Advanced Extraction Commands
                models.ExtensionCommand(
                    name="extract:artifacts",
                    description="Extract integration artifacts (.iar files)",
                ),
                models.ExtensionCommand(
                    name="extract:logs",
                    description="Extract execution logs",
                ),
                models.ExtensionCommand(
                    name="extract:metadata",
                    description="Extract comprehensive metadata",
                ),
                # Transformation Commands
                models.ExtensionCommand(
                    name="transform:flatten",
                    description="Flatten nested data structures",
                ),
                models.ExtensionCommand(
                    name="transform:mask",
                    description="Mask sensitive data",
                ),
            ],
        )

    def _initialize_services(self) -> None:
        config = self.config

        # Create settings object from config dict
        settings = OracleOICExtensionSettings.from_dict(config)

        # Initialize lifecycle manager with settings
        self.lifecycle_manager = LifecycleManager(settings)

        # Initialize monitoring service - needs a session object
        # For now we'll create a basic session
        import requests
        session = requests.Session()
        self.monitoring_service = MonitoringService(session)

    def _handle_lifecycle_command(self, command: str, *args) -> None:
        cmd = command.split(":", 1)[1]

        if cmd == "activate":
            if len(args) < 1:
                logger.error("Integration ID required")
                sys.exit(1)
            integration_id = args[0]
            version = args[1] if len(args) > 1 else "01.00.0000"
            if self.lifecycle_manager:
                self.lifecycle_manager.activate_integration(integration_id, version)
            else:
                logger.error("Lifecycle manager not initialized")
                sys.exit(1)

        elif cmd == "deactivate":
            if len(args) < 1:
                logger.error("Integration ID required")
                sys.exit(1)
            integration_id = args[0]
            version = args[1] if len(args) > 1 else "01.00.0000"
            if self.lifecycle_manager:
                self.lifecycle_manager.deactivate_integration(integration_id, version)

        elif cmd == "status":
            if len(args) < 1:
                logger.error("Integration ID required")
                sys.exit(1)
            integration_id = args[0]
            version = args[1] if len(args) > 1 else "01.00.0000"
            if self.lifecycle_manager is None:
                logger.error("Lifecycle manager not initialized")
                sys.exit(1)
            status = self.lifecycle_manager.get_integration_status(
                integration_id,
                version,
            )
            logger.info("Integration %s|%s status: %s", integration_id, version, status)
        else:
            logger.error("Unknown lifecycle command: %s", cmd)
            sys.exit(1)

    def _handle_monitoring_command(self, command: str, *args) -> None:
        cmd = command.split(":", 1)[1]

        if cmd == "health":
            detailed = "--detailed" in args
            if self.monitoring_service:
                health = self.monitoring_service.check_health(detailed=detailed)
                logger.info("OIC Health Status", **health)

        elif cmd == "performance":
            window_hours = 24
            for i, arg in enumerate(args):
                if arg == "--window" and i + 1 < len(args):
                    window_hours = int(args[i + 1])
            if self.monitoring_service:
                metrics = self.monitoring_service.get_performance_metrics(window_hours)
                logger.info("Performance Metrics", **metrics)

        elif cmd == "errors":
            window_hours = 24
            integration_id = None
            for i, arg in enumerate(args):
                if arg == "--window" and i + 1 < len(args):
                    window_hours = int(args[i + 1])
                elif arg == "--integration" and i + 1 < len(args):
                    integration_id = args[i + 1]
            if self.monitoring_service:
                errors = self.monitoring_service.analyze_errors(
                    window_hours,
                    integration_id,
                )
                logger.info("Error Analysis", **errors)
        else:
            logger.error("Unknown monitoring command: %s", cmd)
            sys.exit(1)

    def _handle_extraction_command(self, command: str, *args) -> None:
        cmd = command.split(":", 1)[1]

        if cmd == "artifacts":
            # Parse arguments
            output_dir = None
            integration_id = None
            for i, arg in enumerate(args):
                if arg == "--output-dir" and i + 1 < len(args):
                    output_dir = args[i + 1]
                elif arg == "--integration" and i + 1 < len(args):
                    integration_id = args[i + 1]

            if not output_dir:
                logger.error("--output-dir required")
                sys.exit(1)

            # Use tap-oracle-oic with specific configuration
            tap_config = {
                **self.config,
                "extract_artifacts": True,
                "artifact_directory": output_dir,
            }
            if integration_id:
                tap_config["integration_filter"] = integration_id

            # Run tap-oracle-oic in artifact extraction mode
            self._run_tap_extraction(tap_config)
        else:
            logger.error("Unknown extraction command: %s", cmd)
            sys.exit(1)

    def _handle_transformation_command(self, command: str, *args) -> None:
        cmd = command.split(":", 1)[1]

        logger.info("Transformation command '%s' not yet implemented", cmd)
        sys.exit(1)

    def _run_tap_extraction(self, config: dict) -> None:
        try:
            # Run tap-oracle-oic with specific config
            cmd = ["tap-oracle-oic", "--config", "-"]
            proc = subprocess.run(
                cmd,
                input=str(config).encode(),
                capture_output=True,
                text=True,
                check=False,
            )
            if proc.returncode != 0:
                logger.error("Extraction failed", stderr=proc.stderr)
                sys.exit(1)
            logger.info("Extraction completed successfully")
        except Exception as e:
            logger.exception("Failed to run extraction", error=str(e))
            sys.exit(1)

    def _show_help(self) -> None:
        logger.info("Oracle OIC Extension Commands:")
        for cmd in self.describe().commands:
            logger.info("  %s: %s", cmd.name, cmd.description)
            if hasattr(cmd, "args") and cmd.args:
                logger.info("    Args: %s", cmd.args)
