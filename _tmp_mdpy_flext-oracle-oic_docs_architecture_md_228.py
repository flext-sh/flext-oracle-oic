# from flext-oracle-oic_docs/architecture.md:228
from __future__ import annotations

from flext_oracle_oic import s


# ❌ Current implementation
class OracleOicExtensionService:
    pass


# ✅ Required FLEXT pattern
class OracleOicIntegrationService(s):
    pass
