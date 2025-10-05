"""FLEXT Oracle OIC CLI Module - Unified CLI Pattern.

FLEXT Unified Module Pattern: CLI module providing unified access
to Oracle OIC CLI functionality through FlextOracleOicCli class.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_oracle_oic.main import FlextOracleOicCli, main

# Backward compatibility - expose CLI instance as 'app'
app = FlextOracleOicCli()

__all__ = ["FlextOracleOicCli", "app", "main"]
