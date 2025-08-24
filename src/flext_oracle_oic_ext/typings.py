"""Centralized typings facade for flext-oracle-oic-ext.

- Extends flext-core types
- Add Oracle OIC Ext-specific type aliases and Protocols here
"""

from __future__ import annotations

from flext_core import E, F, FlextTypes as CoreFlextTypes, P, R, T, U, V


class FlextTypes(CoreFlextTypes):
    """Oracle OIC Ext domain-specific types can extend here."""


__all__ = [
    "E",
    "F",
    "FlextTypes",
    "P",
    "R",
    "T",
    "U",
    "V",
]
