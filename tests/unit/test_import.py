"""Behavioral contract tests for the flext_oracle_oic public package surface.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest
from pydantic import ValidationError

import flext_oracle_oic
from flext_oracle_oic import FlextOracleOicSettings
from flext_oracle_oic.main import main as main_entrypoint

__all__ = ["TestsFlextOracleOicImport"]


class TestsFlextOracleOicImport:
    """Public-contract behavior for the flext_oracle_oic package facade."""

    @pytest.mark.parametrize(
        "export_name",
        [
            "FlextOracleOicApi",
            "FlextOracleOicConstants",
            "FlextOracleOicModels",
            "FlextOracleOicProtocols",
            "FlextOracleOicService",
            "FlextOracleOicSettings",
            "FlextOracleOicTypes",
            "FlextOracleOicUtilities",
            "main",
        ],
    )
    def test_package_publishes_documented_export(self, export_name: str) -> None:
        """Every advertised name in __all__ resolves to a real attribute."""
        assert export_name in flext_oracle_oic.__all__
        assert getattr(flext_oracle_oic, export_name) is not None

    def test_package_entrypoint_is_callable(self) -> None:
        """The published main entrypoint is invocable."""
        assert callable(main_entrypoint)

    def test_version_metadata_matches_version_info_tuple(self) -> None:
        """__version__ string is consistent with the __version_info__ tuple."""
        info = flext_oracle_oic.__version_info__
        assert isinstance(info, tuple)
        assert flext_oracle_oic.__version__.startswith(
            ".".join(str(part) for part in info[:3])
        )

    def test_settings_construct_with_defaults(self) -> None:
        """Default settings expose a stable public field contract."""
        settings = FlextOracleOicSettings()
        dumped = settings.model_dump()
        assert {
            "base_url",
            "api_version",
            "request_timeout",
            "max_retries",
            "verify_ssl",
        } <= dumped.keys()
        assert settings.request_timeout > 0
        assert settings.max_retries >= 0

    def test_settings_override_public_fields(self) -> None:
        """Explicit values override defaults and are readable via the public API."""
        settings = FlextOracleOicSettings(
            base_url="https://tenant.example.com",
            request_timeout=99,
            max_retries=7,
        )
        assert settings.base_url == "https://tenant.example.com"
        assert settings.request_timeout == 99
        assert settings.max_retries == 7

    def test_settings_round_trip_via_model_dump(self) -> None:
        """model_dump output re-validates into an equivalent settings instance."""
        original = FlextOracleOicSettings(request_timeout=45, max_retries=2)
        restored = FlextOracleOicSettings.model_validate(original.model_dump())
        assert restored.request_timeout == original.request_timeout
        assert restored.max_retries == original.max_retries

    @pytest.mark.parametrize("invalid_timeout", [-5, 0])
    def test_settings_reject_non_positive_timeout(self, invalid_timeout: int) -> None:
        """A non-positive request timeout fails validation with a field-scoped error."""
        with pytest.raises(ValidationError) as exc_info:
            FlextOracleOicSettings(request_timeout=invalid_timeout)
        assert "request_timeout" in str(exc_info.value)
