# from flext-oracle-oic/docs/architecture.md:200
from __future__ import annotations


def validate_connection(settings: dict) -> p.Result[ConnectionInfo]:
    """Example of current r usage."""
    if not settings.get("base_url"):
        return r[ConnectionInfo].fail("Base URL required")
    return r[ConnectionInfo].ok(ConnectionInfo(**settings))
