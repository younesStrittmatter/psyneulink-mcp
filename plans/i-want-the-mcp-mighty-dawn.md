# Feedback loop: agent-reported issues + auto-captured runtime errors

## Context

PsyNeuLink's API evolves, so tool descriptions and JSON schemas in `tools/generated/` are regenerated from source. Today nothing closes the loop between *the agent using the MCP at runtime* and *the next generator run*. If a generated tool has a misleading description, an awkward arg, or crashes on edge cases, that signal is lost.

This plan adds a feedback channel exposed by the MCP server itself. Two streams flow into one append-only log:

1. **Auto-captured runtime errors** — every tool call is wrapped; any exception is logged with args + traceback before being re-raised. Free signal, agent doesn't have to do anything.
2. **Agent-reported issues** — a `report_tool_issue` MCP tool the agent calls when something is semantically wrong (unclear description, wrong behavior, missing arg) but didn't crash.

The next `scripts/generate_tools.py` run reads pending entries, groups by tool name, and includes the relevant feedback as context when re-generating each tool. After a successful run, pending feedback is archived under a dated folder.

The repo is currently greenfield (only `CLAUDE.md` exists), so this plan also lays down the minimal surrounding scaffolding the feedback system slots into.

## Design decisions (confirmed with user)

- Both streams enabled (auto-capture + agent reports).
- Feedback is **committed to git** under `feedback/` so it's portable across machines and reviewable in PRs.
- **Write-only** server surface — no `list_known_issues` tool. Dedup happens in the generator.

## Directory layout (new)

```
psyneulink-mcp/
├── pyproject.toml
├── src/psyneulink_mcp/
│   ├── __init__.py
│   ├── server.py              # FastMCP app + entry point
│   ├── feedback.py            # write helpers + auto-capture decorator
│   └── tools/
│       ├── __init__.py
│       ├── generated/         # populated by generator
│       └── curated/           # hand-written
├── scripts/
│   └── generate_tools.py      # consumes feedback/pending/, archives on success
├── feedback/
│   ├── pending/
│   │   └── issues.jsonl       # both streams, discriminated by `source`
│   └── archive/
│       └── <ISO-date>/issues.jsonl
└── tests/
    ├── test_feedback.py
    └── test_tools/
```

## Single log, discriminated by `source`

One file (`feedback/pending/issues.jsonl`), one entry per line. Common envelope, source-specific payload:

```jsonc
// auto-captured
{
  "timestamp": "2026-05-04T17:30:00Z",
  "source": "auto",
  "tool_name": "psyneulink_create_mechanism",
  "tool_layer": "generated",       // or "curated"
  "pnl_version": "0.x.y",
  "server_version": "0.1.0",
  "payload": {
    "args": { /* serialized, with non-JSON values stringified */ },
    "exception_type": "TypeError",
    "exception_message": "…",
    "traceback": "…"
  }
}

// agent-reported
{
  "timestamp": "2026-05-04T17:30:00Z",
  "source": "agent",
  "tool_name": "psyneulink_create_mechanism",
  "tool_layer": "generated",
  "pnl_version": "0.x.y",
  "server_version": "0.1.0",
  "payload": {
    "issue_type": "unclear_description" | "wrong_schema" | "missing_arg" | "wrong_behavior" | "other",
    "description": "free text",
    "suggested_fix": "free text or null",
    "agent_context": "what the agent was trying to do, or null"
  }
}
```

Rationale for one file: simpler tooling; the generator reads one stream and groups by `tool_name`. `source` is just a column.

## `src/psyneulink_mcp/feedback.py`

Three small public surfaces. No external deps beyond stdlib + `psyneulink` (for version) + `mcp`.

```python
# pseudo-signatures, type hints required per project conventions

FEEDBACK_PATH = Path("feedback/pending/issues.jsonl")  # resolved relative to repo root via importlib

def log_runtime_error(
    tool_name: str,
    tool_layer: Literal["generated", "curated"],
    args: dict,
    exc: BaseException,
) -> None: ...

def log_agent_report(
    tool_name: str,
    tool_layer: Literal["generated", "curated"],
    issue_type: Literal["unclear_description", "wrong_schema", "missing_arg", "wrong_behavior", "other"],
    description: str,
    suggested_fix: str | None,
    agent_context: str | None,
) -> None: ...

def captured_tool(layer: Literal["generated", "curated"], **mcp_tool_kwargs):
    """
    Replaces direct use of `@mcp.tool(...)`. Wraps the function so any
    exception is logged to feedback/pending/issues.jsonl, then re-raised
    unchanged so the MCP client still sees the error.
    """
```

- Args serialization: best-effort `json.dumps(default=repr)` so unserializable PsyNeuLink objects become readable strings rather than crashing the logger.
- Append is atomic via `open(..., "a")` + single `write` of one JSON line + `\n`. Acceptable for single-process server.
- The logger MUST NEVER raise. Wrap its own body in `try/except` that prints to stderr on failure — feedback breakage must not turn a normal tool error into a server crash.

## `report_tool_issue` MCP tool

Lives in `src/psyneulink_mcp/tools/curated/feedback.py` (it's hand-written, not generated):

```python
@mcp.tool()
def report_tool_issue(
    tool_name: str,
    issue_type: Literal["unclear_description", "wrong_schema", "missing_arg", "wrong_behavior", "other"],
    description: str,
    suggested_fix: str | None = None,
    agent_context: str | None = None,
) -> dict:
    """
    Report a problem with another tool exposed by this MCP server.

    WHEN TO CALL: after using a tool, if its description was misleading,
    its schema didn't match the actual signature, an obvious arg was missing,
    or the behavior differed from what the description promised. Do NOT call
    this for ordinary domain errors (e.g. invalid PsyNeuLink config) — only
    for problems with the *tool surface itself*.
    """
    log_agent_report(...)
    return {"recorded": True}
```

The description is written for LLM consumers per CLAUDE.md conventions ("focus on WHEN to call").

## Auto-capture wiring

Every tool — generated or curated — uses `captured_tool` instead of `mcp.tool`. The generator emits `@captured_tool(layer="generated", ...)` decorators. Curated tools use `@captured_tool(layer="curated", ...)`.

This means the auto-capture is a property of *how tools are registered*, not a runtime middleware on the MCP server. Cleaner: no global hooks, easy to opt out per-tool if ever needed.

## Generator integration (`scripts/generate_tools.py`)

New steps inserted into the existing flow:

1. **Before generating**: read `feedback/pending/issues.jsonl` (if present), group entries by `tool_name`.
2. **For each tool being generated**: if there are pending entries for it, include them in the LLM prompt under a section like `# Previous feedback to address` — pass the raw entries (the LLM is good at reading JSON and the issue language).
3. **After all tools regenerate successfully**: move `feedback/pending/issues.jsonl` to `feedback/archive/<UTC-date>/issues.jsonl`. If the same date already has a file, append. Truncate `pending/issues.jsonl` to empty.
4. **On failure**: leave `pending/` untouched so the next run still sees the feedback.

Archiving on success (rather than per-entry) keeps the lifecycle dead simple and makes it obvious in `git log` when a feedback batch was consumed.

## Tests (`tests/test_feedback.py`)

- `log_agent_report` writes one well-formed JSON line containing all fields.
- `log_runtime_error` serializes non-JSON args via `repr` without crashing.
- The logger swallows its own exceptions (monkey-patch `open` to raise; assert no propagation).
- `captured_tool` re-raises the original exception unchanged after logging.
- A test for the `report_tool_issue` tool: invoke it via the FastMCP test harness, verify a line lands in the configured feedback path (use `tmp_path` + an env var or fixture override of `FEEDBACK_PATH`).
- Generator: a small unit test that, given a fixture `pending/issues.jsonl`, the grouping logic returns the expected `{tool_name: [entries]}` dict. (No need to test the LLM call itself.)

## Files to create / modify

- `pyproject.toml` — new (uv-managed, FastMCP + pytest + ruff)
- `src/psyneulink_mcp/__init__.py` — new
- `src/psyneulink_mcp/server.py` — new (FastMCP app, entry point `psyneulink-mcp`)
- `src/psyneulink_mcp/feedback.py` — **new, core of this change**
- `src/psyneulink_mcp/tools/__init__.py` — new
- `src/psyneulink_mcp/tools/curated/__init__.py` — new
- `src/psyneulink_mcp/tools/curated/feedback.py` — new (`report_tool_issue`)
- `src/psyneulink_mcp/tools/generated/__init__.py` — new (placeholder until generator runs)
- `scripts/generate_tools.py` — new (with feedback-consumption + archive logic)
- `feedback/pending/.gitkeep` — new
- `feedback/archive/.gitkeep` — new
- `tests/test_feedback.py` — new
- `CLAUDE.md` — update: add a `## Feedback loop` section pointing at `feedback.py`, the `report_tool_issue` tool, and the generator's archive step

## Verification

End-to-end smoke test the user can run:

1. `uv sync` then `uv run psyneulink-mcp` — server starts.
2. `npx @modelcontextprotocol/inspector uv run psyneulink-mcp` — confirm `report_tool_issue` is listed and callable; submit a test report; confirm a line appears in `feedback/pending/issues.jsonl`.
3. Force a tool to raise (a curated tool with a deliberate `raise ValueError("test")` in a test branch) and call it via the inspector — confirm an `auto` entry lands in the same file and the inspector still surfaces the error.
4. `uv run python scripts/generate_tools.py` against a tiny fixture PNL module — confirm pending feedback is included in the LLM prompt (log it for the smoke run) and that on success `pending/issues.jsonl` empties and a dated file appears under `archive/`.
5. `uv run pytest` — all feedback tests green.
