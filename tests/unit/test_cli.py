"""Behavioral tests for the Oracle OIC CLI public contract.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest
from flext_tests import tm

from flext_oracle_oic import FlextOracleOicCli, c
from flext_oracle_oic.main import main


class TestsFlextOracleOicCli:
    """Observable behavior of the ``main`` entry point and CLI app builder."""

    @staticmethod
    def test_version_command_returns_success_exit_code() -> None:
        """The ``version`` command completes and reports success (exit code 0)."""
        tm.that(main(["version"]), eq=0)

    @staticmethod
    def test_version_command_prints_version_banner(
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        """The ``version`` command emits the Oracle OIC banner to stdout."""
        exit_code = main(["version"])
        out = capsys.readouterr().out

        tm.that(exit_code, eq=0)
        tm.that(out, has="Oracle OIC Extension v")
        tm.that(out, has="FLEXT CLI Pattern")

    @staticmethod
    @pytest.mark.parametrize(
        "argv",
        [
            pytest.param([], id="no-command"),
            pytest.param(["does-not-exist"], id="unknown-command"),
        ],
    )
    def test_invalid_invocation_returns_failure_exit_code(
        argv: list[str],
    ) -> None:
        """Missing or unknown commands yield a non-zero exit code, never raise."""
        tm.that(main(argv), eq=1)

    @staticmethod
    @pytest.mark.parametrize(
        "command",
        [
            pytest.param("test-connection", id="test-connection"),
            pytest.param("list-integrations", id="list-integrations"),
        ],
    )
    def test_network_commands_fail_gracefully_without_backend(
        command: str,
    ) -> None:
        """Network commands return an int failure code instead of propagating errors.

        Without a reachable Oracle OIC backend these commands must degrade to a
        failure exit code (1) rather than raising, honoring the railway contract.
        """
        tm.that(main([command]), eq=1)

    @staticmethod
    def test_main_returns_integer_exit_code() -> None:
        """The entry point always returns an ``int`` exit status."""
        tm.that(main(["version"]), is_=int)

    @staticmethod
    def test_build_app_produces_a_runnable_application() -> None:
        """``build_app`` returns a non-null application object on every call."""
        tm.that(FlextOracleOicCli.build_app(), none=False)

    @staticmethod
    def test_build_app_is_idempotent_across_calls() -> None:
        """Repeated ``build_app`` calls each yield an independent, usable app."""
        first = FlextOracleOicCli.build_app()
        second = FlextOracleOicCli.build_app()

        tm.that(first, none=False)
        tm.that(second, none=False)
        assert first is not second

    @staticmethod
    def test_app_identity_constants_are_populated() -> None:
        """The CLI exposes a stable application name and help text."""
        tm.that(c.Cli.APP_NAME, eq="flext-oracle-oic-ext")
        tm.that(c.Cli.APP_HELP, has="Oracle OIC")
