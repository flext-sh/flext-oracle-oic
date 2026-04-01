# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT Oracle OIC utilities submodules."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_oracle_oic.ext_client import FlextOracleOicClient
    from flext_oracle_oic.ext_services import FlextOracleOicExtServices, logger
    from flext_oracle_oic.main import FlextOracleOicCli, main
    from flext_oracle_oic.service import FlextOracleOicService

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextOracleOicCli": ["flext_oracle_oic.main", "FlextOracleOicCli"],
    "FlextOracleOicClient": [
        "flext_oracle_oic.ext_client",
        "FlextOracleOicClient",
    ],
    "FlextOracleOicExtServices": [
        "flext_oracle_oic.ext_services",
        "FlextOracleOicExtServices",
    ],
    "FlextOracleOicService": [
        "flext_oracle_oic.service",
        "FlextOracleOicService",
    ],
    "logger": ["flext_oracle_oic.ext_services", "logger"],
    "main": ["flext_oracle_oic.main", "main"],
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
