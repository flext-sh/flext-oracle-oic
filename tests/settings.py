"""Runtime settings for flext-oracle-oic tests."""

from __future__ import annotations

from flext_tests.settings import FlextTestsSettings

from flext_oracle_oic import FlextOracleOicSettings


class TestsFlextOracleOicSettings(FlextOracleOicSettings, FlextTestsSettings):
    """Oracle OIC settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextOracleOicSettings"]
