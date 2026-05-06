"""Look up canonical PsyNeuLink usage examples for a given symbol.

When the regen LLM writes a tool description for ``TransferMechanism``
or ``Composition.add_projection``, it benefits from seeing how PNL's
own canonical model implementations actually use that symbol. The
``psyneulink/library/models/`` directory ships a curated set of fully-
worked papers (Cohen_Huston1994, Botvinick_conflict_monitoring_model,
Giallanza2024_ego_study2, GilzenratModel, Kalanthroff_PCTC_2018,
MontagueDayanSejnowski96, Nieuwenhuis2005Model, …) — these are the
authoritative answer to "what does the right call shape look like
for this thing?"

We pull *snippets* (the relevant function or surrounding ~40 lines)
rather than whole files so the regen prompt stays compact. Snippets
are filtered by simple substring match on the symbol's short name —
good enough to surface real usages without pulling in introspection
machinery, and resilient to PNL renames because a renamed symbol
just stops appearing in the lookup until canonical models adopt the
new name.

PNL's ``tests/`` directory is NOT shipped with the installed package
(only the runtime modules), so test files are not yet a source. A
future commit can extend this module to walk a separate PNL devel
checkout when one is configured.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path

ENV_PNL_EXAMPLES_DIR = "PSYNEULINK_MCP_EXAMPLES_DIR"

# Cap how many example snippets we include in one regen prompt. 2 is
# enough to anchor a description; more would bloat the prompt without
# much marginal signal.
DEFAULT_MAX_EXAMPLES = 2

# Cap each snippet's character count so a single canonical model file
# (which can be hundreds of lines) doesn't blow out the prompt budget.
DEFAULT_MAX_CHARS_PER_SNIPPET = 2000

# Window of lines around a symbol mention to include as context.
_CONTEXT_LINES_BEFORE = 3
_CONTEXT_LINES_AFTER = 35


@dataclass(frozen=True)
class ExampleSnippet:
    """One canonical usage of a symbol from a PNL library/model file.

    ``file_label`` is the path relative to the PsyNeuLink package root
    (e.g. ``library/models/Cohen_Huston1994.py``) — descriptive enough
    for the LLM to anchor against without exposing a full venv path.
    ``line`` is the 1-based line number of the first match in the file.
    """

    file_label: str
    line: int
    body: str


def _pnl_install_root() -> Path | None:
    """Return the installed PNL package directory, or ``None`` if missing.

    Override with ``$PSYNEULINK_MCP_EXAMPLES_DIR`` to point at a separate
    PNL devel checkout (e.g. one cloned for access to ``tests/`` and
    ``Scripts/`` which the installed wheel doesn't ship).
    """
    override = os.environ.get(ENV_PNL_EXAMPLES_DIR)
    if override:
        path = Path(override).expanduser()
        return path if path.is_dir() else None
    try:
        import psyneulink  # local import — pure pkg lookup
    except ImportError:
        return None
    init = getattr(psyneulink, "__file__", None)
    if not init:
        return None
    return Path(init).resolve().parent


def _candidate_dirs(root: Path) -> list[Path]:
    """Return directories worth grepping for canonical examples.

    ``library/models`` is the highest-signal one — these files are
    full reproductions of published cognitive models. We also check
    a couple of other library dirs so domain-specific patterns
    (composition wiring, learning, etc.) get surfaced.
    """
    candidates = [
        root / "library" / "models",
        root / "library" / "compositions",
    ]
    return [p for p in candidates if p.is_dir()]


def _word_re(needle: str) -> re.Pattern[str]:
    """Word-boundary match for ``needle`` (avoids substring false-positives)."""
    return re.compile(r"\b" + re.escape(needle) + r"\b")


def _extract_snippet(
    text: str,
    pattern: re.Pattern[str],
    *,
    max_chars: int,
) -> tuple[int, str] | None:
    """Return ``(line, body)`` for the first occurrence of ``pattern``.

    ``body`` is a window around the match line (a few lines of context
    before, a function-sized chunk after, capped at ``max_chars``).
    Returns ``None`` if the pattern doesn't appear.
    """
    match = pattern.search(text)
    if match is None:
        return None
    # Convert match offset to line number.
    pre = text[: match.start()]
    line_no = pre.count("\n") + 1
    lines = text.splitlines()
    start = max(0, line_no - 1 - _CONTEXT_LINES_BEFORE)
    end = min(len(lines), line_no - 1 + _CONTEXT_LINES_AFTER)
    body = "\n".join(lines[start:end])
    if len(body) > max_chars:
        body = body[: max_chars - 1].rstrip() + "…"
    return line_no, body


def find_examples_for(
    short_name: str,
    *,
    max_examples: int = DEFAULT_MAX_EXAMPLES,
    max_chars_per_snippet: int = DEFAULT_MAX_CHARS_PER_SNIPPET,
) -> list[ExampleSnippet]:
    """Return up to ``max_examples`` canonical usages of ``short_name``.

    ``short_name`` is the PNL class / function short name (e.g.
    ``"TransferMechanism"``, ``"add_projection"``). We word-boundary
    search the ``library/models/`` and ``library/compositions/`` dirs
    of the installed PNL package.

    Returns ``[]`` when PNL isn't importable, the search dirs are
    missing, or no canonical model uses the symbol — a no-op safety
    valve so the regen prompt rendering never depends on this lookup
    succeeding.
    """
    if not short_name:
        return []
    root = _pnl_install_root()
    if root is None:
        return []
    pattern = _word_re(short_name)
    snippets: list[ExampleSnippet] = []
    for d in _candidate_dirs(root):
        # Sort for deterministic prompt output across runs.
        for path in sorted(d.glob("*.py")):
            if path.name.startswith("__"):
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            extracted = _extract_snippet(
                text, pattern, max_chars=max_chars_per_snippet
            )
            if extracted is None:
                continue
            line, body = extracted
            try:
                rel = path.relative_to(root)
                label = str(rel)
            except ValueError:
                label = path.name
            snippets.append(
                ExampleSnippet(file_label=label, line=line, body=body)
            )
            if len(snippets) >= max_examples:
                return snippets
    return snippets


def render_examples_block(snippets: list[ExampleSnippet]) -> str:
    """Render snippets as a markdown block for the regen prompt.

    Empty input → empty string (caller skips the section header).
    """
    if not snippets:
        return ""
    lines = ["", "--- USAGE EXAMPLES FROM PSYNEULINK ---"]
    for snip in snippets:
        lines.append(f"## {snip.file_label}:{snip.line}")
        lines.append("```python")
        lines.append(snip.body)
        lines.append("```")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


__all__ = [
    "ENV_PNL_EXAMPLES_DIR",
    "DEFAULT_MAX_EXAMPLES",
    "DEFAULT_MAX_CHARS_PER_SNIPPET",
    "ExampleSnippet",
    "find_examples_for",
    "render_examples_block",
]
