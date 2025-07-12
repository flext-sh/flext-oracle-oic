"""Pass-through invoker for Oracle OIC extension.

REFACTORED:
            Uses flext-core patterns.
Zero tolerance for code duplication.
"""

from __future__ import annotations

import sys

from meltano.edk.process import Invoker, log_subprocess_error

from flext_observability.logging import get_logger

logger = get_logger(__name__)


def pass_through_cli() -> None:
    """Pass-through CLI for oracle-oic-ext."""
    logger.debug("Running pass-through invoker", command=sys.argv[1:])

    # Pass through to actual command
    invoker = Invoker("oracle-oic-ext")

    try:
        invoker.run(*sys.argv[1:])
    except (OSError, RuntimeError, ValueError, ImportError) as e:
        log_subprocess_error(
            "oracle-oic-ext invocation failed",
            e,
            "oracle-oic-ext",
        )
        sys.exit(1)


if __name__ == "__main__":
    pass_through_cli()
