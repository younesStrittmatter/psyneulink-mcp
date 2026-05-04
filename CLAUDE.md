# psyneulink-mcp

An MCP server exposing PsyNeuLink as LLM-friendly tools, with auto-generated 
tool descriptions for an evolving API.

## Working with Claude on this project

I'm using this project to learn how to use Claude (Code, API, SDK, MCP) 
efficiently and in a modern way. While we work:

- **Surface better tools.** When I do something the long way, point out the 
  faster idiom — slash commands, skills, subagents, hooks, MCP, plan/auto 
  mode, parallel tool calls, the right model for the job (Haiku/Sonnet/Opus).
- **Suggest, don't silently do.** If you spot a more idiomatic approach 
  (better prompt structure, prompt caching, structured outputs, batch API, 
  thinking blocks, etc.) mention it briefly so I can choose.
- **Flag anti-patterns.** If I'm pasting context that should be a file, 
  re-prompting instead of editing, skipping caching, or building something 
  Claude already provides, call it out.
- **Be concrete.** Prefer "use `/skill X` instead of …" over generic advice.

This applies to *how we collaborate*, not the runtime architecture (which 
deliberately has no LLM — see below).

## Architecture (three repos)

This repo is one of three siblings under `psyneulink-ai/`:

- **`psyneulink-mcp` (this repo):** a passive MCP server that wraps 
  PsyNeuLink. No LLM in the runtime. Reusable across any MCP client 
  (Claude Desktop, the agent, custom clients).
- **`psyneulink-corpus`:** community-curated brainlike YAMLs and the 
  canonical GitHub Issues queue for human-reported tool feedback. The MCP 
  *reads* from this repo; humans contribute via PRs and Issues.
- **`psyneulink-agent`:** the modeling agent (Layer 2). Decides how to 
  combine personal vs community brainlike views during modeling. The only 
  place where modeling logic lives. Out of scope for this repo.

## Separation of concerns is pure (hard rule)

Each repo does one thing. Cross-repo writes are forbidden:

- The MCP must never write to the corpus. It only fetches.
- The corpus must never contain Python tool code, only data + contribution 
  rules.
- The agent must never call PsyNeuLink directly — only via the MCP.

If a feature seems to need to live in two repos, that's a signal the 
design is wrong, not that we should make an exception.

## The generator pattern

1. Introspect the `psyneulink` module at build time
2. For each public class/function, send source + docstring to LLM (make an adapter for this that uses API token or Claude Max plan)
3. LLM writes an LLM-friendly tool description + JSON schema
4. Output is committed Python files in `src/psyneulink_mcp/tools/generated/`
5. Re-run when PNL updates; review the diff

This is build-time codegen, not runtime. Server itself has no LLM dependency.

## Tool surface

- `tools/generated/` — auto-generated, covers all of PNL
- `tools/curated/` - additional tools

## Feedback loop

Closes the loop between agents using the MCP at runtime and the next 
generator run. Three streams feed the generator:

- **Auto-captured runtime errors** (local JSONL). `captured_tool` (in 
  `feedback.py`) wraps every registered tool — generated or curated — and 
  logs args + traceback to `feedback/pending/issues.jsonl` before 
  re-raising any exception.
- **Agent-reported issues** (local JSONL). The `report_tool_issue` curated 
  tool (`tools/curated/feedback.py`) lets the agent flag problems that 
  didn't crash but are still wrong: misleading description, schema 
  mismatch, missing arg, surprising behavior. Same JSONL file as above.
- **Human-reported issues** (GitHub Issues on `psyneulink-corpus`). 
  Humans file issues with the `tool_feedback` template and `feedback` 
  label. The MCP never writes to GitHub; the generator pulls these via 
  `gh issue list` at regen time.

Local entries share a common envelope (`source`, `tool_name`, 
`tool_layer`, `pnl_version`, `server_version`, `timestamp`, `payload`). 
The logger swallows its own exceptions — feedback breakage must never 
turn a normal tool error into a server crash.

`scripts/generate_tools.py` merges local pending entries with open 
`feedback`-labeled issues from the corpus, groups them by `tool_name`, 
and includes the relevant feedback in the LLM prompt when re-generating 
each tool. On overall success: local pending moves to 
`feedback/archive/<UTC-date>/issues.jsonl`; corpus issues get a 
"consumed in regen <sha>" comment + `consumed` label (no auto-close — 
humans verify and close). On failure, both stay untouched.

The local feedback path is overridable via `PSYNEULINK_MCP_FEEDBACK_PATH`. 
The corpus repo is overridable via `PSYNEULINK_MCP_CORPUS_REPO` 
(default: `younesStrittmatter/psyneulink-corpus`).

## Stack

- `uv` for deps and venvs
- `pyproject.toml` only (no setup.py, no requirements.txt)
- `mcp` (FastMCP) for the server
- `ruff` for lint+format
- `pytest` for tests
- MCP Inspector for manual testing
- Claude Desktop for end-to-end LLM testing

## Conventions

- Python 3.10+
- Type hints everywhere
- Tool descriptions written for LLMs: focus on WHEN to call, not just what
- Every tool has at least one pytest test
- Generator output is reviewed before commit

## Workflow

1. `uv run psyneulink-mcp` to start the server
2. `npx @modelcontextprotocol/inspector uv run psyneulink-mcp` for the inspector
3. `uv run pytest` for tests
4. `uv run python scripts/generate_tools.py` to regenerate the auto layer