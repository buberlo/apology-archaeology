"""Entry point for running Apology Archaeology as a module.

This file makes ``python -m apoloarch`` work by delegating to the package's
command-line interface.
"""

from __future__ import annotations

import sys

from .cli import main


def _run() -> int:
    """Run the CLI and normalize the return value for ``sys.exit``."""
    try:
        result = main()
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        return 130

    if result is None:
        return 0
    return int(result)


if __name__ == "__main__":
    sys.exit(_run())