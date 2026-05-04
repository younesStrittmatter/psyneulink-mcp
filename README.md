# psyneulink-mcp

A passive MCP server that exposes [PsyNeuLink](https://princetonuniversity.github.io/PsyNeuLink/)
as LLM-friendly tools. The runtime has **no** LLM dependency — tool
descriptions are committed Python written by a build-time generator.

For the polyrepo architecture (`psyneulink-mcp` ↔ `psyneulink-corpus` ↔
`psyneulink-agent`), the separation-of-concerns rules, and the feedback
loop, see [`CLAUDE.md`](./CLAUDE.md). This README is for usage.

## Quickstart

```sh
uv sync
uv run psyneulink-mcp
```

Manual testing in the MCP Inspector:

```sh
npx @modelcontextprotocol/inspector uv run psyneulink-mcp
```

Tests and lint:

```sh
uv run pytest
uv run ruff check
```

## Configuring the LLM adapter (build-time only)

The MCP server itself never talks to an LLM. Adapters are used **only**
by the generator (`uv run psyneulink-mcp-generate`, equivalently
`python scripts/generate_tools.py`), which writes
`tools/generated/*.py` files that get reviewed and committed. Once
committed, the running server is plain Python.

Selection is env-only via `$PSYNEULINK_MCP_LLM_ADAPTER`
(default: `claude_cli`).

### Default — Claude Max plan via the `claude` CLI

No API key required. Just have the
[`claude` CLI](https://docs.anthropic.com/en/docs/claude-code)
installed and signed in:

```sh
uv run psyneulink-mcp-generate
```

Optional knobs (all read at adapter construction time):

| Env var                                   | Effect                                |
|-------------------------------------------|---------------------------------------|
| `PSYNEULINK_MCP_CLAUDE_CMD`               | path to the `claude` binary           |
| `PSYNEULINK_MCP_CLAUDE_MODEL`             | alias / full model name (default `sonnet`) |
| `PSYNEULINK_MCP_CLAUDE_MAX_BUDGET_USD`    | spend cap forwarded to `--max-budget-usd` |
| `PSYNEULINK_MCP_CLAUDE_TIMEOUT_S`         | per-call subprocess timeout (default 120) |

### Alternative — Anthropic API key

```sh
uv pip install 'psyneulink-mcp[anthropic-api]'
export ANTHROPIC_API_KEY=sk-...
export PSYNEULINK_MCP_LLM_ADAPTER=anthropic_api
uv run psyneulink-mcp-generate
```

Optional knobs:

| Env var                              | Effect                                  |
|--------------------------------------|-----------------------------------------|
| `PSYNEULINK_MCP_ANTHROPIC_MODEL`     | model id (default `claude-sonnet-4-5`)  |
| `PSYNEULINK_MCP_ANTHROPIC_TIMEOUT_S` | per-call SDK timeout (default 120)      |

### Adding another adapter

One-file change in `src/psyneulink_mcp/generator/adapters/`:

1. Drop a new module next to `claude_cli.py` / `anthropic_api.py`
   implementing the `LLMAdapter` protocol from `base.py`
   (`generate(self, prompt, *, schema) -> ToolSpec`).
2. Register the constructor in the `ADAPTERS` registry in
   `adapters/__init__.py`.
3. If the adapter needs extra deps, add a new
   `[project.optional-dependencies]` group in `pyproject.toml` so users
   on the default path don't pay for them.

## Regenerating the tool surface

```sh
uv run psyneulink-mcp-generate                          # regen seed surface
uv run psyneulink-mcp-generate --limit 2                # smoke (first two)
uv run psyneulink-mcp-generate --only LinearCombination # one symbol
uv run psyneulink-mcp-generate --dry-run                # template w/o LLM
uv run psyneulink-mcp-generate --force                  # ignore hash skip
```

(Same script is reachable as `uv run python scripts/generate_tools.py`
for backward compatibility.)

What it does:

* Reads `generator/seeds.txt` to pick which PNL symbols to wrap. The
  default seed (`import-walk: psyneulink.library.models`) covers
  everything the bundled canonical model examples actually use; extend
  the file with `symbol:` / `package:` / additional `import-walk:`
  lines as the surface grows.
* For each selected symbol, asks the configured adapter for a
  schema-validated `ToolSpec` (`description` / `parameters` / `notes`).
* Renders that ToolSpec into a Python module under
  `src/psyneulink_mcp/tools/generated/` that registers a single MCP
  tool via `@captured_tool(mcp, layer="generated")`.
* Rewrites `tools/generated/__init__.py` so the server picks the new
  modules up automatically.
* Skips a symbol when its source hash matches the embedded
  `__source_sha256__` AND no pending feedback targets that tool — so
  re-runs are cheap when nothing changed. `--force` overrides.
* On overall success, archives consumed local feedback and marks
  consumed corpus issues. Per-symbol failures are logged and skipped;
  only a run where zero symbols generated successfully leaves feedback
  untouched.

**Generator output is reviewed before commit.** Diff the result,
sanity-check a handful of generated tool descriptions, then commit. The
generator is allowed to leave a dirty working tree — that is the review
step.

## Feedback loop

`captured_tool` wraps every registered tool (curated and generated) and
appends any raised exception to `feedback/pending/issues.jsonl`. Agents
can also call the curated `report_tool_issue` tool to flag non-crashing
problems. Humans file `feedback`-labeled issues on `psyneulink-corpus`.

The next generator run merges all three streams, includes the relevant
entries in each tool's prompt, and on success archives local pending +
labels corpus issues `consumed`. See
[`CLAUDE.md`](./CLAUDE.md#feedback-loop) for the full design.
