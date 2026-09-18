# from flext-oracle-oic_docs/configuration.md:301
from flext_oracle_oic import FlextOracleOicSettings

# Create and inspect configuration
settings = FlextOracleOicSettings(
    OracleOic={
        "base_url": "https://your-instance.integration.ocp.oraclecloud.com",
        "oauth_client_id": "your_client_id",
        "oauth_client_secret": "your_client_secret",
        "oauth_token_url": "https://your-idcs.identity.oraclecloud.com/oauth2/v1/token",
    }
)

# Debug connection settings
print(f"Base URL: {settings.OracleOic.base_url}")
print(f"API Version: {settings.OracleOic.api_version}")
print(f"Timeout: {settings.OracleOic.request_timeout}")

# Debug auth settings (careful with secrets)
print(f"Client ID: {settings.OracleOic.oauth_client_id}")
print(f"Token URL: {settings.OracleOic.oauth_token_url}")
# oauth_client_secret is stored as a plain string in the current settings model
