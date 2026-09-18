# from flext-oracle-oic_docs/api-reference.md:153
from flext_oracle_oic import e

# Structured exception classes via the shared `e` facade
base_error = e.BaseError  # Base exception
auth_error = e.AuthenticationError  # Authentication failures
config_error = e.ConfigurationError  # Configuration issues
connection_error = e.ConnectionError  # Connection problems
