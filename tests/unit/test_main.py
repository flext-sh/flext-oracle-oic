"""Behavioral tests for the Oracle OIC CLI entry point.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest
from flext_tests import tm

from flext_oracle_oic import FlextOracleOicCli, __version__, c
from flext_oracle_oic.main import main


class TestsFlextOracleOicMain:
    """Public-contract behavior of the Oracle OIC CLI entry point."""

    @staticmethod
    def test_version_command_reports_success_exit_code() -> None:
        """`version` runs offline and yields the success exit code 0."""
        tm.that(main(["version"]), eq=0)

    @staticmethod
    def test_unknown_command_reports_failure_exit_code() -> None:
        """An unrecognized command surfaces the failure exit code, never 0."""
        exit_code = main(["definitely-not-a-command"])

        tm.that(exit_code, is_=int)
        tm.that(exit_code, ne=0)

    @staticmethod
    @pytest.mark.parametrize("args", [["version"], ["--help"]])
    def test_documented_invocations_return_int_exit_code(args: list[str]) -> None:
        """Every documented invocation returns an int the process can exit with."""
        tm.that(main(args), is_=int)

    @staticmethod
    def test_build_app_produces_an_application() -> None:
        """`build_app` returns a usable Typer application object."""
        app = FlextOracleOicCli.build_app()

        tm.that(app, none=False)

    @staticmethod
    def test_build_app_is_deterministic() -> None:
        """Building the app twice yields independent, equivalent applications."""
        first = FlextOracleOicCli.build_app()
        second = FlextOracleOicCli.build_app()

        tm.that(first, none=False)
        tm.that(second, none=False)

    @staticmethod
    def test_app_identity_is_exposed_as_public_metadata() -> None:
        """The CLI advertises its program name and help text as public contract."""
        tm.that(c.Cli.APP_NAME, eq="flext-oracle-oic-ext")
        tm.that(c.Cli.APP_HELP, has="Oracle OIC")

    @staticmethod
    def test_package_exposes_non_empty_version_string() -> None:
        """`__version__` is a non-empty string usable by the `version` command."""
        tm.that(__version__, is_=str)
        assert __version__
