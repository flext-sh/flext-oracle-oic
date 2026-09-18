# from flext-oracle-oic/docs/configuration.md:210
from flext_oracle_oic import FlextOracleOicModels as m

# OICAuthConfig stores OAuth credentials as a SecretStr
auth_config = m.OracleOic.OICAuthConfig(
    oauth_client_id="public_client_id",
    oauth_client_secret="secret_value",
    oauth_token_url="https://idcs.example.com/oauth2/v1/token",
)

# Secret is protected from accidental exposure
print(auth_config.oauth_client_secret)  # Shows SecretStr('**********')
