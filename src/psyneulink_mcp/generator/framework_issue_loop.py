"""Fetch + parse `framework_issue` labeled issues from the corpus repo.

Sibling to ``feedback_loop`` — but for issues that the orchestrator
flagged as upstream-library bugs (PsyNeuLink, SweetPea, SweetBean)
rather than MCP-tool description bugs.

Workflow at regen time:

1. Pull every open issue labeled ``framework_issue`` and NOT
   ``consumed``.
2. Hand each one to ``framework_issue_verifier`` which decides
   whether the bug is still present.
3. Bugs that no longer reproduce get marked ``consumed`` automatically
   so future regen passes skip them.
4. Bugs that still reproduce get attached to the affected MCP tool's
   regen prompt as a "KNOWN FRAMEWORK LIMITATIONS" section so the
   description can warn the agent + suggest the workaround.

The local feedback JSONL doesn't carry framework-issue entries — those
go to GitHub directly via ``orchestrator-agent.report_framework_issue``
(plus its sync CLI for retries). Auto-captured runtime errors that
turn out to be PNL bugs go through the regular ``feedback`` queue;
they only become framework_issues when a human (or the LLM-driven
audit) explicitly re-classifies them.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from typing import Any

from psyneulink_mcp import corpus

FRAMEWORK_ISSUE_LABEL = "framework_issue"


@dataclass
class FrameworkIssue:
    """One open ``framework_issue`` labeled corpus issue, parsed.

    ``related_mcp_tool`` is what the affected MCP tool's regen prompt
    will key off — present in the body if the issue was filed by
    ``orchestrator-agent.report_framework_issue`` (which puts it in
    the body's "Related MCP tool" section). Issues filed without that
    field have ``related_mcp_tool=None`` and won't be attached to any
    specific tool's regen prompt; they still get verified, just not
    surfaced in any description until someone tags them.
    """

    number: int
    title: str
    body: str
    library: str  # "psyneulink" / "sweetpea" / "sweetbean" / "unknown"
    description: str
    related_mcp_tool: str | None
    workaround_used: str | None
    captured_args: dict[str, Any] | None
    exception_type: str | None
    exception_message: str | None
    labels: list[str] = field(default_factory=list)


# These regexes match the markdown sections that
# ``orchestrator_agent.core.issue_reporting._format_issue_for_gh`` writes.
# Keep them tolerant of whitespace and trailing punctuation so that hand-
# edited issue bodies don't silently fail to parse.
_LIBRARY_RE = re.compile(r"\*\*Library:\*\*\s*`([^`]+)`")
_RELATED_TOOL_RE = re.compile(r"\*\*Related MCP tool:?\*\*\s*\n+`([^`]+)`", re.MULTILINE)
_RELATED_TOOL_HEADING_RE = re.compile(
    r"^##\s*Related MCP tool\s*$\s*(?:\n+`([^`]+)`)?", re.MULTILINE
)
_DESCRIPTION_RE = re.compile(
    r"^##\s*Description\s*$\s*\n+(.*?)(?=^##|\Z)", re.MULTILINE | re.DOTALL
)
_WORKAROUND_RE = re.compile(
    r"^##\s*Workaround used\s*$\s*\n+(.*?)(?=^##|\Z)", re.MULTILINE | re.DOTALL
)
_EXCEPTION_TYPE_RE = re.compile(r"`?(\w+Error|TypeError|ValueError|KeyError|IndexError|AttributeError)`?:")
_AUTO_PAYLOAD_RE = re.compile(
    r'"args":\s*(\{.+?\})\s*,\s*"exception_type"', re.DOTALL
)


def _parse_body(body: str) -> dict[str, Any]:
    """Extract the structured fields the orchestrator wrote into the body."""
    library = "unknown"
    m = _LIBRARY_RE.search(body)
    if m:
        library = m.group(1).strip().lower()

    related_mcp_tool: str | None = None
    m = _RELATED_TOOL_HEADING_RE.search(body)
    if m and m.group(1):
        related_mcp_tool = m.group(1).strip()

    description = body
    m = _DESCRIPTION_RE.search(body)
    if m:
        description = m.group(1).strip()

    workaround_used: str | None = None
    m = _WORKAROUND_RE.search(body)
    if m:
        workaround_used = m.group(1).strip()

    # Pull captured args + exception out of the description text. The
    # auto-published feedback (via psyneulink-mcp's own publisher) wraps
    # the raw JSONL payload in a code-fenced block; orchestrator-filed
    # framework issues don't currently include that, so this is best-
    # effort only.
    captured_args: dict[str, Any] | None = None
    exception_type: str | None = None
    exception_message: str | None = None
    m = _AUTO_PAYLOAD_RE.search(body)
    if m:
        try:
            args_blob = json.loads(m.group(1))
            # The auto-capture envelope nests as args.kwargs.args.
            inner = args_blob
            for key in ("kwargs", "args"):
                if isinstance(inner, dict) and key in inner:
                    inner = inner[key]
            if isinstance(inner, dict):
                captured_args = inner
        except json.JSONDecodeError:
            pass
    m = _EXCEPTION_TYPE_RE.search(description)
    if m:
        exception_type = m.group(1)
    # Exception message: first line of description, stripped of the type prefix.
    if description:
        first_line = description.splitlines()[0].strip()
        if exception_type and first_line.startswith(exception_type):
            exception_message = first_line[len(exception_type) :].lstrip(": ").strip()
        else:
            exception_message = first_line

    return {
        "library": library,
        "description": description,
        "related_mcp_tool": related_mcp_tool,
        "workaround_used": workaround_used,
        "captured_args": captured_args,
        "exception_type": exception_type,
        "exception_message": exception_message,
    }


def gather_framework_issues() -> list[FrameworkIssue]:
    """Return every open ``framework_issue`` labeled issue, parsed.

    Filters out issues already labeled ``consumed`` server-side via the
    ``--label`` filter (gh's ``--label X --label Y`` is AND, not OR; we
    pass only ``framework_issue`` and exclude ``consumed`` by walking).
    """
    repo = corpus.corpus_repo()
    try:
        result = subprocess.run(
            [
                "gh",
                "issue",
                "list",
                "--repo",
                repo,
                "--label",
                FRAMEWORK_ISSUE_LABEL,
                "--state",
                "open",
                "--json",
                "number,title,body,labels",
                "--limit",
                "200",
            ],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError) as exc:
        print(
            f"[generate_tools] could not fetch framework_issue issues: {exc}",
            file=sys.stderr,
        )
        return []
    if result.returncode != 0:
        print(
            f"[generate_tools] could not fetch framework_issue issues: "
            f"gh exited {result.returncode}: {(result.stderr or '').strip()}",
            file=sys.stderr,
        )
        return []
    try:
        raw = json.loads(result.stdout or "[]")
    except json.JSONDecodeError:
        return []

    issues: list[FrameworkIssue] = []
    for item in raw:
        labels = [
            label.get("name", "")
            for label in item.get("labels") or []
            if label.get("name")
        ]
        if "consumed" in labels:
            continue
        body = item.get("body") or ""
        parsed = _parse_body(body)
        issues.append(
            FrameworkIssue(
                number=int(item.get("number") or 0),
                title=item.get("title") or "",
                body=body,
                library=parsed["library"],
                description=parsed["description"],
                related_mcp_tool=parsed["related_mcp_tool"],
                workaround_used=parsed["workaround_used"],
                captured_args=parsed["captured_args"],
                exception_type=parsed["exception_type"],
                exception_message=parsed["exception_message"],
                labels=labels,
            )
        )
    return issues


def group_by_tool(
    issues: list[FrameworkIssue],
) -> dict[str, list[FrameworkIssue]]:
    """Bucket issues by ``related_mcp_tool`` for prompt injection.

    Issues with no ``related_mcp_tool`` are bucketed under the empty
    string — the regen orchestrator skips that bucket since it has no
    tool description to attach the warning to.
    """
    out: dict[str, list[FrameworkIssue]] = {}
    for issue in issues:
        key = issue.related_mcp_tool or ""
        out.setdefault(key, []).append(issue)
    return out


__all__ = [
    "FRAMEWORK_ISSUE_LABEL",
    "FrameworkIssue",
    "gather_framework_issues",
    "group_by_tool",
]
