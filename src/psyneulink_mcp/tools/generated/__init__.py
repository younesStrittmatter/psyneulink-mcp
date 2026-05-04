"""Auto-generated tool registry. Do not edit by hand.

`scripts/generate_tools.py` rewrites this file on every successful run.
On a fresh clone (no regen yet) ``ALL`` is empty and :func:`register_all`
is a safe no-op, so the server starts cleanly even without any
generated tools.
"""

from __future__ import annotations

from typing import Any

ALL: tuple[Any, ...] = ()


def register_all(mcp: Any) -> None:
    """Register every generated tool module with ``mcp``."""
    for module in ALL:
        module.register(mcp)
