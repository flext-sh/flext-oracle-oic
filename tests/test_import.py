"""Basic test to verify flext-extensions.oracle.flext-oracle-oic imports work.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

import flext_oracle_oic
from flext_oracle_oic import OracleOicExtensionSettings


def test_basic_import() -> None:
    """Test that we can import the module."""
    assert flext_oracle_oic is not None


def test_config_import() -> None:
    """Test that we can import config."""
    assert OracleOicExtensionSettings is not None
