"""Decide whether a ``framework_issue`` still reproduces in current PNL.

Two strategies, in order:

1. **Reproducer** — when the issue body has captured args from a
   construction-style MCP tool (``create_*``), we re-call the tool's
   generated ``_impl`` with those args and compare the new exception
   to the captured one. Hard signal:
   - Same exception type + similar message ⇒ ``STILL_PRESENT``
   - No exception ⇒ ``FIXED``
   - Different exception type ⇒ ``FIXED`` (the original code path no
     longer triggers; conservatively treat it as fixed and let a human
     re-classify if needed)

2. **LLM judge** — fallback when the reproducer can't run (issue has
   no captured args, or the tool requires runtime state we can't
   reconstruct). We hand the LLM the issue body + the current source
   of the deepest PNL frame in the captured traceback and ask "is the
   bug still present in this code?" Soft signal: ``STILL_PRESENT``,
   ``FIXED``, or ``UNKNOWN``.

The orchestrator treats ``UNKNOWN`` conservatively — keeps the issue
in the prompt as a known-limitation warning, doesn't auto-mark
``consumed``. Real fixes get auto-consumed only when the verifier is
confident.
"""

from __future__ import annotations

import importlib
import re
import sys
from dataclasses import dataclass
from enum import Enum
from typing import Any

from .framework_issue_loop import FrameworkIssue


class Status(Enum):
    STILL_PRESENT = "still_present"
    FIXED = "fixed"
    UNKNOWN = "unknown"


@dataclass
class Verdict:
    """One verifier decision for a single framework_issue."""

    status: Status
    method: str  # "reproducer" / "llm_judge" / "skipped"
    note: str  # human-readable reason

    @property
    def is_fixed(self) -> bool:
        return self.status is Status.FIXED

    @property
    def is_still_present(self) -> bool:
        return self.status is Status.STILL_PRESENT


def verify(
    issue: FrameworkIssue,
    *,
    llm_judge: Any | None = None,
) -> Verdict:
    """Try the reproducer; fall back to ``llm_judge`` if available.

    ``llm_judge`` is a callable ``(prompt: str) -> str`` (or None).
    The orchestrator passes the same adapter it uses for tool regen,
    wrapped to call ``adapter.generate(prompt, schema=...)``.
    """
    repro = _try_reproducer(issue)
    if repro is not None:
        return repro
    if llm_judge is None:
        return Verdict(
            status=Status.UNKNOWN,
            method="skipped",
            note="no captured args for reproducer; no LLM judge configured",
        )
    return _llm_judge(issue, llm_judge)


def _try_reproducer(issue: FrameworkIssue) -> Verdict | None:
    """Re-call the affected MCP tool with the captured args.

    Returns ``None`` when the reproducer can't run (no args, not a
    construction tool, tool not found, runtime-state required, etc.) —
    caller falls back to the LLM judge.
    """
    if not issue.related_mcp_tool:
        return None
    if not issue.captured_args:
        return None
    if not issue.related_mcp_tool.startswith("create_"):
        # Method-style tools ("add_node", "run_composition", etc.)
        # require pre-existing handles; we don't try to reconstruct
        # session state.
        return None

    try:
        from psyneulink_mcp.tools.generated import ALL
    except Exception as exc:  # noqa: BLE001 — defensive
        return Verdict(
            status=Status.UNKNOWN,
            method="reproducer",
            note=f"could not import generated tools: {exc!r}",
        )

    target_module = None
    for module in ALL:
        if getattr(module, "TOOL_NAME", "") == issue.related_mcp_tool:
            target_module = module
            break
    if target_module is None:
        return Verdict(
            status=Status.UNKNOWN,
            method="reproducer",
            note=f"no generated tool named {issue.related_mcp_tool!r}",
        )

    impl = getattr(target_module, "_impl", None)
    if not callable(impl):
        return None

    try:
        impl(dict(issue.captured_args))
    except Exception as exc:  # noqa: BLE001
        new_type = type(exc).__name__
        new_msg = str(exc)
        if (
            issue.exception_type
            and new_type == issue.exception_type
            and _messages_similar(new_msg, issue.exception_message or "")
        ):
            return Verdict(
                status=Status.STILL_PRESENT,
                method="reproducer",
                note=f"same exception ({new_type}) with similar message",
            )
        return Verdict(
            status=Status.FIXED,
            method="reproducer",
            note=(
                f"different exception now ({new_type}: "
                f"{new_msg[:120]}); original was {issue.exception_type or '?'}"
            ),
        )
    # Successful call — bug is gone.
    return Verdict(
        status=Status.FIXED,
        method="reproducer",
        note="call now succeeds",
    )


_NORMALIZE_RE = re.compile(r"\s+")


def _normalize_for_compare(s: str) -> str:
    """Lowercase + collapse whitespace + strip non-alphanumeric punctuation.

    Matches "DriftOnASphereIntegrator Function-4" against
    "DriftOnASphereIntegrator Function-12" by reducing both to
    something compare-friendly without losing the meaningful bits.
    """
    out = _NORMALIZE_RE.sub(" ", s.lower()).strip()
    # Replace numeric runs with a wildcard so "Function-4" matches
    # "Function-12" — these change with PNL's instance counter and
    # aren't part of the bug signature.
    out = re.sub(r"\d+", "#", out)
    return out


def _messages_similar(a: str, b: str, *, prefix_chars: int = 80) -> bool:
    """Two error messages are 'similar' if their normalized prefixes match.

    Tolerates instance-id drift (Function-4 vs Function-12) without
    needing exact-match. 80 chars is enough to capture the semantic
    error shape ("DriftOnASphereIntegrator: parameters with len>1
    don't have the same length...") without depending on the trailing
    list of violator names.
    """
    return (
        _normalize_for_compare(a)[:prefix_chars]
        == _normalize_for_compare(b)[:prefix_chars]
    )


_LLM_JUDGE_PROMPT = """\
You are deciding whether a previously-reported PsyNeuLink bug is still present
in the current installed version of PsyNeuLink.

Here is the original issue, captured by the orchestrator at the time of failure:

--- ISSUE TITLE ---
{title}

--- ISSUE BODY ---
{body}

Current PNL source for the affected file (deepest psyneulink frame in the
captured traceback) — this is what's running RIGHT NOW:

--- CURRENT SOURCE ({source_label}) ---
{source}

Decide one of: STILL_PRESENT (the bug is still in the current source),
FIXED (the source no longer has the bug — the relevant code path has been
patched, removed, or refactored), UNKNOWN (you can't tell from what's shown).

Reply with EXACTLY ONE WORD on the first line: STILL_PRESENT, FIXED, or UNKNOWN.
On the second line, a one-sentence justification.
"""


def _llm_judge(issue: FrameworkIssue, llm_judge: Any) -> Verdict:
    """Ask the configured LLM whether the bug is still present.

    ``llm_judge`` is a callable taking a prompt string and returning the
    LLM's text response. The orchestrator wraps its existing adapter so
    we get the same model + auth path as tool regen itself.

    The prompt extracts the deepest PNL frame from the captured
    traceback, reads the current source of that file from the installed
    psyneulink package (so we judge against what's *running*, not what
    was running when the bug was filed), and asks for a 3-way verdict.
    """
    source_label, source = _extract_current_source_for_traceback(issue.body)
    if not source:
        return Verdict(
            status=Status.UNKNOWN,
            method="llm_judge",
            note="could not locate the affected PNL file from the traceback",
        )
    prompt = _LLM_JUDGE_PROMPT.format(
        title=issue.title,
        body=issue.body[:6000],  # cap so an unusually-long body doesn't blow the model
        source_label=source_label,
        source=source[:8000],
    )
    try:
        response = llm_judge(prompt)
    except Exception as exc:  # noqa: BLE001 — never propagate
        return Verdict(
            status=Status.UNKNOWN,
            method="llm_judge",
            note=f"llm_judge raised: {type(exc).__name__}: {exc}",
        )
    return _parse_llm_verdict(response)


_PNL_FRAME_RE = re.compile(
    r'File "(?P<path>[^"]*?/psyneulink/[^"]+\.py)", line (?P<line>\d+)',
)


def _extract_current_source_for_traceback(body: str) -> tuple[str, str]:
    """Find the deepest psyneulink/* frame in the body's traceback and read it.

    Returns ``(label, source)`` — ``label`` is the short PNL-relative
    path (e.g. ``components/component.py``) for prompt-rendering;
    ``source`` is the FULL current contents of that file.

    Returns ``("", "")`` when no PNL frame can be parsed or the file
    isn't readable from the installed psyneulink package.
    """
    matches = list(_PNL_FRAME_RE.finditer(body))
    if not matches:
        return "", ""
    last = matches[-1]
    path_str = last.group("path")
    # Resolve via the installed package so we judge against current code.
    try:
        import psyneulink

        pkg_root = psyneulink.__file__
    except ImportError:
        return "", ""
    if not pkg_root:
        return "", ""
    from pathlib import Path

    pkg_dir = Path(pkg_root).resolve().parent
    # Try to locate the suffix path under the installed package — the
    # traceback's full path may point at any install location, but the
    # tail relative to ``psyneulink/`` should be stable.
    marker = "/psyneulink/"
    if marker in path_str:
        rel = path_str.split(marker, 1)[1]
    else:
        rel = path_str
    candidate = pkg_dir / rel
    try:
        text = candidate.read_text(encoding="utf-8")
    except OSError:
        return "", ""
    return rel, text


def _parse_llm_verdict(response: str) -> Verdict:
    """Map the LLM's first-word reply onto a Verdict."""
    if not response:
        return Verdict(
            status=Status.UNKNOWN,
            method="llm_judge",
            note="empty LLM response",
        )
    lines = [line.strip() for line in response.strip().splitlines() if line.strip()]
    head = (lines[0] if lines else "").upper()
    note = lines[1] if len(lines) > 1 else ""
    if "STILL_PRESENT" in head:
        return Verdict(status=Status.STILL_PRESENT, method="llm_judge", note=note)
    if "FIXED" in head:
        return Verdict(status=Status.FIXED, method="llm_judge", note=note)
    return Verdict(status=Status.UNKNOWN, method="llm_judge", note=note or head)


__all__ = [
    "Status",
    "Verdict",
    "verify",
]


# Suppress an unused-import warning for the module-load helper we keep
# around for future on-demand reproducer expansions (importlib is the
# canonical way to grab a module by its TOOL_NAME without iterating the
# ALL tuple).
_ = importlib
_ = sys
