"""CLI entrypoint for python -m flext_oracle_oic.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_cli import cli

from flext_oracle_oic import main

if __name__ == "__main__":
    cli.exit(main())
