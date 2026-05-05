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

## Multi-repo dev sessions: switch workspace first

A *multi-repo dev session* authors changes in more than one of the
three sibling repos in one sitting (e.g., spawning subagents that
operate in `../psyneulink-corpus/` or `../psyneulink-agent/`, or
coordinating a label rename that has to land in two repos together).

If you find you need one, **stop and ask the user to open a new Cursor
chat at the parent folder**:

```
~/Documents/code/AutoGrad/psyneulink-ai/
```

That folder has its own `AGENTS.md` and is the correct workspace for
multi-repo dev sessions. The shell sandbox restricts writes to the
workspace root; running cross-repo writes from this sub-repo workspace
forces a permission prompt for every shell call into a sibling. Don't
work around it with `required_permissions: ["all"]` — switch workspaces
once, work freely thereafter.

This is *not* the same as the forbidden cross-repo coupling above. A
multi-repo dev session produces independent commits in independent
repos that each respect the boundary. **Smell test:** if the work
would survive being done in two separate chats on different days with
no shared state, it's a dev-session convenience. If it requires
runtime/import coupling between repos, the polyrepo rule applies and
the design is wrong — fix the design.

## The generator pattern

1. Introspect the `psyneulink` module at build time, driven by
   `generator/seeds.txt` (four directives: `import-walk:`, `symbol:`,
   `package:`, `method:`).
2. For each resolved symbol, send source + docstring to an LLM adapter.
   The default adapter shells out to the local `claude` CLI in
   `--print --json-schema` mode, which uses the user's Claude Max
   subscription via the CLI's local OAuth — **no API key needed**.
   The Anthropic API adapter (opt-in via
   `$PSYNEULINK_MCP_LLM_ADAPTER=anthropic_api`) is the fallback for
   environments without the CLI.
3. LLM writes an LLM-friendly tool description + JSON schema.
4. Output is committed Python files in `src/psyneulink_mcp/tools/generated/`.
5. Re-run when PNL updates; review the diff. Source-hash skip means
   only changed symbols re-hit the LLM.

This is build-time codegen, not runtime. Server itself has no LLM
dependency.

### Regenerating the auto layer

```bash
uv run psyneulink-mcp-generate                # full regen, real LLM
uv run psyneulink-mcp-generate --dry-run      # placeholder ToolSpecs (CI sanity)
uv run psyneulink-mcp-generate --only Composition,TransferMechanism
uv run psyneulink-mcp-generate --rerender     # re-template from on-disk metadata,
                                              # no LLM call
```

Override the model with `$PSYNEULINK_MCP_CLAUDE_MODEL` (default:
`sonnet`); the per-call timeout with `$PSYNEULINK_MCP_CLAUDE_TIMEOUT_S`
(default: 300s, sized for `Composition`).

### Source install of PsyNeuLink (NOT PyPI)

`pyproject.toml` pins `psyneulink` to the upstream `devel` branch via
`[tool.uv.sources]`:

```toml
psyneulink = { git = "https://github.com/PrincetonUniversity/PsyNeuLink", branch = "devel" }
```

This is intentional and symmetric with how `experiment-mcp` pulls
`sweetpea` + `sweetbean` from upstream branches — the generator must
codegen against the live API surface, and PyPI lags `devel` by months
in practice. The first `uv lock` after a fresh clone takes ~1-2 min
while uv clones PNL; subsequent ones are instant.

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
4. `uv run psyneulink-mcp-generate` (or `uv run python
   scripts/generate_tools.py`) to regenerate the auto layer. Default
   adapter is `claude_cli`; see "Regenerating the auto layer" above.