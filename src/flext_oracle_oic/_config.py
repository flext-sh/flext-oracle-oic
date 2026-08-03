"""FlextOracleOicConfig — frozen config singleton for flext-oracle-oic (ADR-005 §7).

Model-less: business rules live in ``config/*.yaml`` under the ``OracleOic:`` key and
are exposed through the open ``config.OracleOic`` namespace (``extra="allow"``), with
no per-domain model. Access is ``config.OracleOic.<domain>[<key>...]``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_cli import FlextCliConfig, m


class _OracleOicNamespace(m.BaseModel):
    """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

    model_config = m.ConfigDict(extra="allow", frozen=True)


class FlextOracleOicConfig(FlextCliConfig):
    """OracleOic config auto-loaded model-less from ``config/*.yaml``."""

    OracleOic: _OracleOicNamespace = _OracleOicNamespace()


config: FlextOracleOicConfig = FlextOracleOicConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_oracle_oic import config``."""

__all__: list[str] = ["FlextOracleOicConfig", "config"]
