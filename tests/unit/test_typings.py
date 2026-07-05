"""Behavioral tests for the Oracle OIC test-types facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest
from flext_tests import FlextTestsTypes

from flext_oracle_oic import FlextOracleOicTypes
from tests.typings import TestsFlextOracleOicTypes, t

__all__: list[str] = ["TestsFlextOracleOicTypingsUnit"]


class TestsFlextOracleOicTypingsUnit:
    """Contract of the composed test-types facade ``t``."""

    def test_facade_alias_is_the_composed_class(self) -> None:
        """``t`` is the public alias of the composed test-types class."""
        assert t is TestsFlextOracleOicTypes

    @pytest.mark.parametrize(
        "base",
        [FlextTestsTypes, FlextOracleOicTypes],
    )
    def test_facade_composes_both_type_domains(self, base: type[object]) -> None:
        """Facade inherits from both the shared and OIC-specific type roots."""
        assert issubclass(t, base)

    @pytest.mark.parametrize(
        "member",
        ["JsonValue", "JsonList", "JsonDict", "ConfigDict"],
    )
    def test_inherited_type_members_are_exposed(self, member: str) -> None:
        """Domain type members are reachable through the composed facade."""
        assert getattr(t, member, None) is not None

    @pytest.mark.parametrize(
        "member",
        ["JsonValue", "JsonList", "JsonDict", "ConfigDict"],
    )
    def test_members_resolve_to_the_root_definition(self, member: str) -> None:
        """MRO composition exposes each member without shadowing its root."""
        assert getattr(t, member) is getattr(FlextTestsTypes, member)

    def test_oic_domain_does_not_shadow_shared_json_value(self) -> None:
        """OIC extension reuses (not redefines) the shared ``JsonValue``."""
        assert t.JsonValue is FlextOracleOicTypes.JsonValue
