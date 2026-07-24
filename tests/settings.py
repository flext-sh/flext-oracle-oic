"""Runtime settings for flext-oracle-oic tests."""

from __future__ import annotations

from flext_oracle_oic import FlextOracleOicSettings
from flext_tests import FlextTestsSettings


class TestsFlextOracleOicSettings(FlextOracleOicSettings, FlextTestsSettings):
    """Oracle OIC settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextOracleOicSettings"]
