"""Basic test to verify flext-extensions.oracle.flext-oracle-oic-ext imports work."""

import flext_oracle_oic_ext
from flext_oracle_oic_ext import OracleOICExtensionSettings


def test_basic_import() -> None:
    """Test that we can import the module."""
    assert flext_oracle_oic_ext is not None


def test_config_import() -> None:
    """Test that we can import config."""
    assert OracleOICExtensionSettings is not None
