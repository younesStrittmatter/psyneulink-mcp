"""Thin shim around :mod:`psyneulink_mcp.generator.orchestrator`.

Kept so ``uv run python scripts/generate_tools.py ...`` keeps working
alongside the ``psyneulink-mcp-generate`` console script. All real logic
lives in the orchestrator and the surrounding ``generator`` modules.

Feedback helpers (``read_pending``, ``group_by_tool``, ``gather_feedback``,
``consumed_issue_numbers``, ``archive_pending``) are re-exported from
:mod:`psyneulink_mcp.generator.feedback_loop` so any caller that imported
them from here continues to work.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Make the package importable when run as `python scripts/generate_tools.py`
# (uv run does this for us, but bare python doesn't).
_REPO_ROOT = Path(__file__).resolve().parent.parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from psyneulink_mcp.generator.feedback_loop import (  # noqa: E402  (path setup)
    archive_pending,
    consumed_issue_numbers,
    gather_feedback,
    group_by_tool,
    read_pending,
)
from psyneulink_mcp.generator.orchestrator import main  # noqa: E402

__all__ = [
    "archive_pending",
    "consumed_issue_numbers",
    "gather_feedback",
    "group_by_tool",
    "main",
    "read_pending",
]


if __name__ == "__main__":
    raise SystemExit(main())
