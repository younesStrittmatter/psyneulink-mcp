# MCP corpus integration

## What this plan is

Phase 3 of the `psyneulink-ai` polyrepo build-out. It adds read-only corpus
access to the MCP server: fetching community brainlike views and merging
GitHub Issues from `psyneulink-corpus` into the feedback-driven tool
generator.

## What's already done

| Phase | Repo | Status |
|-------|------|--------|
| 1 — polyrepo restructure | `psyneulink-mcp` | ✅ done |
| 2 — corpus skeleton (schema, templates, CI) | `psyneulink-corpus` | see `psyneulink-corpus/plans/corpus-skeleton.md` |
| 3 — MCP corpus integration (**this plan**) | `psyneulink-mcp` | 🔲 pending |
| 4 — agent first connection | `psyneulink-agent` | see `psyneulink-agent/plans/agent-first-connection.md` |

The feedback loop itself is fully built: `src/psyneulink_mcp/feedback.py`,
`tools/curated/feedback.py`, `scripts/generate_tools.py`, and
`tests/test_feedback.py` all exist and pass. What is **not** built yet is the
corpus read path and the brainlike curated tools.

## Architecture context (read before coding)

Three sibling repos under `~/Documents/code/AutoGrad/psyneulink-ai/`:

- **`psyneulink-mcp` (this repo):** passive MCP server wrapping PsyNeuLink.
  No LLM at runtime. Reads from `psyneulink-corpus`; never writes.
- **`psyneulink-corpus`:** community brainlike YAMLs + GitHub Issues as the
  canonical tool-feedback queue. Humans contribute via PRs/Issues.
- **`psyneulink-agent`:** the modeling agent (Layer 2). Calls MCP only,
  never PsyNeuLink directly.

**Hard rule:** cross-repo writes are forbidden. If a feature seems to need to
live in two repos, the design is wrong. See `CLAUDE.md §Separation of concerns`.

## Stack

- `uv` + `pyproject.toml`
- `mcp` (FastMCP) for the server
- `ruff` + `pytest`
- `gh` CLI as the only auth surface for GitHub (no SDK dependency)

## New module: `src/psyneulink_mcp/corpus.py`

Read-only. No external deps beyond stdlib and `gh`.

```python
CORPUS_REPO_DEFAULT = "younesStrittmatter/psyneulink-corpus"
ENV_CORPUS_REPO  = "PSYNEULINK_MCP_CORPUS_REPO"   # owner/name
ENV_CORPUS_REF   = "PSYNEULINK_MCP_CORPUS_REF"    # branch/tag/sha, default "main"
ENV_CORPUS_CACHE = "PSYNEULINK_MCP_CORPUS_CACHE"  # local cache dir, default ~/.cache/psyneulink-mcp

class CorpusUnavailable(RuntimeError): ...

def fetch_brainlike_views(force: bool = False) -> list[dict]:
    """Pull community/brainlike/*.yaml from the corpus repo.
    Caches locally; re-pulls only when force=True or cache TTL expired (1 h)."""

def fetch_pending_feedback_issues() -> list[dict]:
    """List open issues with label `feedback` from the corpus repo.
    Returns entries in the same envelope shape as feedback/pending/issues.jsonl
    so the generator can treat them uniformly."""
```

Implementation: shell out to `gh api repos/<owner>/<name>/contents/...` and
`gh issue list --repo <owner>/<name> --label feedback --json ...`.

If `gh` is missing or unauthenticated, raise `CorpusUnavailable` with a clear
message. The MCP server itself must not crash — callers handle the error
gracefully.

## New curated tools: `src/psyneulink_mcp/tools/curated/brainlike.py`

```python
@captured_tool(mcp, layer="curated")
def get_community_brainlike_views() -> list[dict]:
    """Return the community-curated list of brainlike definitions.
    WHEN TO CALL: when the agent needs to know what the community considers
    'brainlike' — e.g., to compare against the user's preferences, or to
    pick canonical examples to show. Read-only; to propose new entries the
    user files a PR on psyneulink-corpus."""

@captured_tool(mcp, layer="curated")
def get_my_brainlike_view() -> dict:
    """Return the user's personal brainlike preferences from
    ~/.config/psyneulink-mcp/me.yaml (or $PSYNEULINK_MCP_PERSONAL_PROFILE).
    Returns an empty dict if no profile is configured."""
```

Add a starter `examples/me.yaml.example` to the repo so users know the
format. Personal profile is intentionally not writable by the MCP — users
edit it themselves.

## Generator integration (`scripts/generate_tools.py`)

The existing generator already reads `feedback/pending/issues.jsonl`. Extend
`gather_feedback()` to merge corpus issues:

```python
def gather_feedback() -> dict[str, list[dict]]:
    local = group_by_tool(read_pending(PENDING_PATH))
    try:
        remote = group_by_tool(corpus.fetch_pending_feedback_issues())
    except corpus.CorpusUnavailable as e:
        print(f"[generate_tools] corpus unavailable, local only: {e}", file=sys.stderr)
        remote = {}
    merged: dict[str, list[dict]] = {}
    for d in (local, remote):
        for k, v in d.items():
            merged.setdefault(k, []).extend(v)
    return merged
```

After successful regeneration, for each consumed corpus issue:
- Comment `"consumed in regen <sha>"` on the issue.
- Apply label `consumed`.
- Do **not** auto-close — humans verify and close.

On failure, leave both pending JSONL and corpus issues untouched.

## Wire brainlike tools into the server

In `src/psyneulink_mcp/server.py`, import and register the new brainlike
tools (same pattern as `tools/curated/feedback.py`).

## Tests

**`tests/test_corpus.py`** — monkeypatch `subprocess.run` to fake `gh` responses:
- `fetch_brainlike_views` parses YAML correctly.
- `fetch_pending_feedback_issues` returns envelope-shaped dicts.
- `CorpusUnavailable` is raised on auth failure.
- Cache hit skips the `gh` call.

**Update `tests/test_feedback.py`** — extend the generator `gather_feedback`
tests so the merge function works when remote returns `[]`, raises
`CorpusUnavailable`, or has overlapping tool names.

## Files to create or modify

| Path | Action |
|------|--------|
| `src/psyneulink_mcp/corpus.py` | **new** |
| `src/psyneulink_mcp/tools/curated/brainlike.py` | **new** |
| `examples/me.yaml.example` | **new** |
| `tests/test_corpus.py` | **new** |
| `src/psyneulink_mcp/server.py` | modify — import brainlike tools |
| `scripts/generate_tools.py` | modify — merge corpus feedback, comment+label on success |
| `tests/test_feedback.py` | modify — add merge tests |

## Verification

1. `uv run pytest` — all tests green including `test_corpus.py`.
2. `uv run psyneulink-mcp` then MCP Inspector:
   - `get_community_brainlike_views` returns the canonical-transfer example
     (requires corpus Phase 2 to be done and `gh` authenticated).
   - `get_my_brainlike_view` returns `{}` with no profile, or your predicates
     with `~/.config/psyneulink-mcp/me.yaml` in place.
3. `uv run python scripts/generate_tools.py` — prints merged feedback
   grouping (corpus issues + local JSONL); on success, corpus issues get the
   "consumed" comment.

## Dependency on Phase 2

`get_community_brainlike_views` needs at least one YAML in
`psyneulink-corpus/community/brainlike/` to return real data. Run Phase 2
first (or point `PSYNEULINK_MCP_CORPUS_REPO` at a fork that has the file).
The tool degrades gracefully to `[]` if the corpus is empty; it does **not**
crash.
