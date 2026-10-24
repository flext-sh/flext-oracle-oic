"""FlextOracleOicConfig — frozen config singleton for flext-oracle-oic (ADR-005 §7).

Business rules live in ``config/*.yaml`` under the ``OracleOic:`` key and are
validated through the project's config declarations. Access remains
``config.OracleOic.<domain>[<key>...]``; values come from the YAML owner.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated

from flext_cli import FlextCliConfig, m

from flext_oracle_oic._models.config import FlextOracleOicModelsConfig


class FlextOracleOicConfig(FlextCliConfig):
    """Oracle OIC business config validated from the canonical YAML source.

    The fleet-converged config inherits only the declared frozen config
    capability base (``config_bases`` precedence: meltano -> cli -> core); the
    adjustable runtime settings keep their own independent lifecycle.
    """

    OracleOic: Annotated[
        FlextOracleOicModelsConfig.Config,
        m.Field(description="Oracle OIC business domains from ``config/*.yaml``."),
    ]


config: FlextOracleOicConfig = FlextOracleOicConfig.fetch_global()
"""Pre-instantiated frozen config singleton.

Exposed as ``from flext_oracle_oic import config``.
"""

__all__: list[str] = ["FlextOracleOicConfig", "config"]
