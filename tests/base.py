"""Service base for flext-oracle-oic tests."""

from __future__ import annotations

from typing import override

from flext_tests import s as tests_s

from flext_oracle_oic import m
from tests.settings import TestsFlextOracleOicSettings


class TestsFlextOracleOicServiceBase(tests_s):
    """Oracle OIC test service base with source and test settings namespaces."""

    @classmethod
    @override
    def fetch_settings(cls) -> TestsFlextOracleOicSettings:
        """Return the typed Oracle OIC+Tests settings singleton."""

    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(settings_type=TestsFlextOracleOicSettings)


s = TestsFlextOracleOicServiceBase

__all__: list[str] = ["TestsFlextOracleOicServiceBase", "s"]
