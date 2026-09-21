"""FlextOracleOicConfig — frozen config singleton for flext-oracle-oic (ADR-005 §7).

Model-less: business rules live in ``config/*.yaml`` under the ``OracleOic:`` key and
are exposed through the open ``config.OracleOic`` namespace (``extra="allow"``), with
no per-domain model. Access is ``config.OracleOic.<domain>[<key>...]``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated

from flext_cli import FlextCliConfig, m

from flext_core import FlextSettings


class _OracleOicNamespace(m.BaseModel):
    """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

    model_config = m.ConfigDict(extra="allow", frozen=True)


class FlextOracleOicConfig(FlextSettings, FlextCliConfig):
    """OracleOic config auto-loaded model-less from ``config/*.yaml``.

    MRO carries ``FlextSettings`` FIRST (ENFORCE-042); unlike never-instantiated
    namespace holders, this class IS instantiated by ``fetch_global``, so the
    instance-inert holder contract does not apply and pydantic settings
    construction machinery stays intact.
    """

    OracleOic: Annotated[
        _OracleOicNamespace,
        m.Field(description="Open namespace exposing ``config/*.yaml`` under ``OracleOic``."),
    ] = _OracleOicNamespace()


config: FlextOracleOicConfig = FlextOracleOicConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_oracle_oic import config``."""

__all__: list[str] = ["FlextOracleOicConfig", "config"]
