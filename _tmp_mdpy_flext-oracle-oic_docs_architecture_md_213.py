# from flext-oracle-oic_docs/architecture.md:213
from __future__ import annotations

from flext_cli import u


class ServiceClass:
    def __init__(self):
        self.logger = u.fetch_logger(__name__)
