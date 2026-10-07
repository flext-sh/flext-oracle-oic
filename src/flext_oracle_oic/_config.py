"""FlextOracleOicConfig — frozen config singleton for flext-oracle-oic (ADR-005 §7).

Business rules live in ``config/*.yaml`` under the ``OracleOic:`` key and are
validated through the project's config declarations. Access remains
``config.OracleOic.<domain>[<key>...]``; values come from the YAML owner.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from flext_cli import FlextCliConfig

from flext_core import FlextSettings
from flext_oracle_oic import m

if TYPE_CHECKING:
    from flext_oracle_oic import p


class FlextOracleOicConfig(FlextSettings, FlextCliConfig):
    """Oracle OIC business config validated from the canonical YAML source."""

    @cached_property
    def OracleOic(self) -> p.OracleOic.Config:
        """Return the required business namespace without synthesized defaults."""
        if self.model_extra is None:
            msg = "Oracle OIC business configuration namespace is missing"
            raise ValueError(msg)
        return m.OracleOic.Config.model_validate(self.model_extra["OracleOic"])


config: FlextOracleOicConfig = FlextOracleOicConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_oracle_oic import config``."""

__all__: list[str] = ["FlextOracleOicConfig", "config"]
