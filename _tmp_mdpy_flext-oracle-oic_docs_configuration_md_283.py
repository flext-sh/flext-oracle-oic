# from flext-oracle-oic_docs/configuration.md:283
from flext_oracle_oic import FlextOracleOicSettings

# ❌ Wrong type for request_timeout
try:
    settings = FlextOracleOicSettings(
        base_url="https://example.com",
        request_timeout="invalid",  # Should be integer
    )
except ValueError as e:
    print(f"Type error: {e}")

# ✅ Correct type
settings = FlextOracleOicSettings(base_url="https://example.com", request_timeout=30)
