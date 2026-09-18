# from flext-oracle-oic/docs/getting-started.md:98
from flext_oracle_oic import FlextOracleOicSettings

# Create configuration following FLEXT patterns
settings = FlextOracleOicSettings(
    OracleOic={
        "base_url": "https://your-oic-instance.integration.ocp.oraclecloud.com",
        "api_version": "v1",
        "request_timeout": 30,
        "oauth_client_id": "your_client_id",
        "oauth_client_secret": "your_client_secret",
        "oauth_token_url": "https://your-idcs.identity.oraclecloud.com/oauth2/v1/token",
    }
)

print(f"Configuration created: {settings.OracleOic.base_url}")
