# Polyrepo restructure + corpus repo + brainlike feature

## Context

The current single-folder layout is starting to mix concerns: the MCP server (pure tooling) is going to grow features that are really *content* (community brainlike views, human-filed issues, contribution review). Putting that data in the MCP repo couples release cadence, contributor pool, and review rules across two very different things.

This plan does three things at once because they're entangled — splitting them later is more work than doing them together:

1. **Restructure** to a 3-repo polyrepo under a wrapping folder `psyneulink-ai/`.
2. **Create `psyneulink-corpus`** as the home for community brainlike YAMLs and the canonical GitHub Issues queue for human-reported tool feedback.
3. **Make the MCP a strict consumer** of corpus data (read-only fetch + cache), and route human feedback through GitHub Issues rather than local JSONL.

The "Working with Claude" / "Separation of concerns is pure" principle becomes a hard rule in CLAUDE.md.

## Target layout

```
~/Documents/code/AutoGrad/psyneulink-ai/         (wrapping folder, NOT a repo)
├── psyneulink-mcp/                              (existing, moves here)
│   └── … (everything that currently lives at AutoGrad/psyneulink-mcp/)
├── psyneulink-agent/                            (new, scaffold only)
│   ├── pyproject.toml
│   ├── src/psyneulink_agent/__init__.py
│   ├── plans/.gitkeep
│   └── CLAUDE.md                                (Layer 2 description)
└── psyneulink-corpus/                           (new, the data + review home)
    ├── community/
    │   └── brainlike/
    │       ├── _schema.yaml                     (the YAML schema definition)
    │       └── examples/
    │           └── canonical-transfer.yaml      (one starter example)
    ├── users/                                   (optional personal profiles)
    │   └── .gitkeep
    ├── .github/
    │   ├── CODEOWNERS                           (community/** -> @maintainers, users/<h>/** -> @<h>)
    │   ├── ISSUE_TEMPLATE/
    │   │   └── tool_feedback.yml                (matches the JSON schema MCP knows)
    │   └── PULL_REQUEST_TEMPLATE.md             (brainlike submissions)
    ├── docs/
    │   ├── BRAINLIKE_SCHEMA.md
    │   ├── CONTRIBUTING.md                      (GH account required, PR workflow)
    │   └── ISSUE_WORKFLOW.md                    (humans → GH Issues w/ `feedback` label)
    └── README.md
```

**No wrapping git repo.** `psyneulink-ai/` is just a filesystem container. Each of the three children is an independent git repo with its own GitHub remote.

## Why polyrepo (already decided, recorded for posterity)

- Tooling release cadence ≠ data contribution cadence. The MCP can ship binaries; the corpus is a living dataset.
- Different review rules: code PRs need maintainer review for correctness; corpus PRs need domain review for "is this brainlike?".
- Different contributor pool: a neuroscientist contributing a brainlike YAML shouldn't have to navigate Python tooling.
- The "passive Layer 1" principle from the existing `CLAUDE.md` survives: the MCP repo never grows opinions about what's brainlike.

## Phase 1 — Restructure (must happen first; one-shot)

Mechanical move + scaffold. No feature work yet. After this phase the user restarts the Claude Code session at the new path.

### Steps

1. `mkdir -p ~/Documents/code/AutoGrad/psyneulink-ai`
2. `mv ~/Documents/code/AutoGrad/psyneulink-mcp ~/Documents/code/AutoGrad/psyneulink-ai/psyneulink-mcp`
   - **Side effect:** the running session's cwd becomes invalid. The user must `cd` to the new path and start a fresh Claude Code session. This is called out at exit-plan time.
3. Inside `psyneulink-mcp/`:
   - `git init` (the repo isn't versioned yet — verified by `ls .git` returning nothing pre-move).
   - First commit: everything currently in the project (the work from the prior plan).
   - Create the GitHub repo: `gh repo create ystrittm/psyneulink-mcp --private --source=. --push` (private chosen as default; can flip to public later — confirmed at exit time).
4. Create `psyneulink-agent/` sibling:
   - `mkdir psyneulink-agent && cd psyneulink-agent`
   - Minimal `pyproject.toml`, empty `src/psyneulink_agent/__init__.py`, `CLAUDE.md` describing the Layer-2 role and that it consumes psyneulink-mcp via stdio MCP.
   - `git init` + initial commit. `gh repo create ystrittm/psyneulink-agent --private --source=. --push`.
5. Create `psyneulink-corpus/` sibling — same pattern. Initial commit contains only the directory skeleton + README + CONTRIBUTING.md draft (Phase 2 fills in the rest).

### CLAUDE.md updates inside `psyneulink-mcp/` (still in Phase 1)

Add a top-level section near `## Architecture (two layers)`:

```markdown
## Separation of concerns is pure (hard rule)

Each repo in the `psyneulink-ai/` family does one thing. Cross-repo writes
are forbidden:

- **`psyneulink-mcp` (this repo):** pure tooling. Wraps PsyNeuLink. Reads
  community data; never writes to it. Never authoritative for what is
  "brainlike" or what tool feedback exists.
- **`psyneulink-corpus`:** the only home for community brainlike YAMLs and
  human-filed tool issues. The MCP fetches from it; humans + reviewers
  contribute to it via GitHub PRs and Issues.
- **`psyneulink-agent`:** the modeling agent. Decides *how* to combine
  personal vs community brainlike views. The MCP just exposes them.

If a feature needs to live in two repos, that's the signal that the design
is wrong — not that we should make an exception.
```

Also rename `## Architecture (two layers)` → `## Architecture (three repos)` and update the body to reflect the corpus.

## Phase 2 — Corpus repo skeleton (in `psyneulink-corpus/`)

The corpus repo is mostly *documents and rules*, not code. Goal: make it possible for a human to file an issue or open a brainlike PR following templates, and for the MCP to fetch the data.

### Files to write

- `README.md` — what this repo is, who it's for, how to contribute (links to docs/).
- `docs/CONTRIBUTING.md` — **GitHub account required**. Two flows:
  - File tool feedback → "New issue" with the `tool_feedback` template, label `feedback` auto-applied.
  - Propose brainlike entry → fork, add YAML under `community/brainlike/<slug>.yaml`, open PR using the PR template.
- `docs/BRAINLIKE_SCHEMA.md` — prose description of the YAML schema. Backed by `community/brainlike/_schema.yaml` (a JSON-schema-style document validated in CI).
- `community/brainlike/_schema.yaml` — the schema. Minimum fields (open to refinement):
  ```yaml
  $id: https://psyneulink-ai/brainlike/v1
  required: [id, title, description, predicates, examples]
  properties:
    id:           { type: string, pattern: "^[a-z0-9-]+$" }
    title:        { type: string, maxLength: 80 }
    description:  { type: string }
    predicates:   { type: array, items: { type: string } }   # what makes it brainlike
    examples:     { type: array, items: { type: string } }   # PNL configs/snippets
    references:   { type: array, items: { type: string } }   # papers/URLs
    contributor:  { type: string }                            # GH handle
  ```
- `community/brainlike/examples/canonical-transfer.yaml` — one fully-filled example so contributors have a template.
- `.github/CODEOWNERS`:
  ```
  community/**            @ystrittm
  users/*/                @\1     # placeholder; per-user CODEOWNERS need a generator
  /docs/**                @ystrittm
  /community/brainlike/_schema.yaml  @ystrittm
  ```
  (Per-user CODEOWNERS can't be done with wildcards; we'll either keep `users/` open and trust GitHub's "first commit wins ownership" or add a tiny script later. Out of scope for v1.)
- `.github/ISSUE_TEMPLATE/tool_feedback.yml` — form fields that match the existing JSONL schema (`tool_name`, `issue_type`, `description`, `suggested_fix`, `agent_context`). Auto-applies label `feedback`.
- `.github/PULL_REQUEST_TEMPLATE.md` — checklist for brainlike submissions: schema-valid, has examples, has references.
- `.github/workflows/validate.yml` — CI that validates every `community/brainlike/*.yaml` against `_schema.yaml`. Lightweight; uses `check-jsonschema` or similar.

### What this phase does NOT do

- No moderation bot, no auto-merge, no CLA. Humans review PRs the normal way.
- No personal `users/<handle>/` content yet — the directory exists but is empty.

## Phase 3 — MCP corpus integration (in `psyneulink-mcp/`)

The MCP gains the ability to *read* corpus data. It never writes.

### New module: `src/psyneulink_mcp/corpus.py`

```python
# All read-only.

CORPUS_REPO_DEFAULT = "ystrittm/psyneulink-corpus"
ENV_CORPUS_REPO = "PSYNEULINK_MCP_CORPUS_REPO"   # owner/name
ENV_CORPUS_REF  = "PSYNEULINK_MCP_CORPUS_REF"    # branch/tag/sha, default "main"
ENV_CORPUS_CACHE = "PSYNEULINK_MCP_CORPUS_CACHE" # local cache dir, default ~/.cache/...

def fetch_brainlike_views(force: bool = False) -> list[dict]: ...
    """Pull community/brainlike/*.yaml from the corpus repo. Caches locally;
    re-pulls only when `force=True` or cache TTL expired (1h)."""

def fetch_pending_feedback_issues() -> list[dict]: ...
    """List open issues with label `feedback` from the corpus repo, returned
    in the same envelope shape as feedback/pending/issues.jsonl entries
    (so the generator can treat them uniformly)."""
```

Implementation: shells out to `gh api repos/<owner>/<name>/contents/...` and `gh issue list --repo <owner>/<name> --label feedback --json ...`. No GitHub SDK dependency — `gh` is the only auth surface.

If `gh` is missing or unauthenticated, these functions raise a clear `CorpusUnavailable` error and the caller (curated tool, generator) reports it gracefully. The MCP itself does not crash.

### New curated tools (in `src/psyneulink_mcp/tools/curated/brainlike.py`)

```python
@captured_tool(mcp, layer="curated")
def get_community_brainlike_views() -> list[dict]:
    """Return the community-curated list of brainlike definitions.
    WHEN TO CALL: when the agent needs to know what the community considers
    'brainlike' — e.g., to compare against the user's preferences, or to
    pick canonical examples to show. Read-only; for proposing new entries
    the user files a PR on psyneulink-corpus."""

@captured_tool(mcp, layer="curated")
def get_my_brainlike_view() -> dict:
    """Return the user's personal brainlike preferences from
    ~/.config/psyneulink-mcp/me.yaml (or `$PSYNEULINK_MCP_PERSONAL_PROFILE`).
    Returns an empty dict if no profile is configured."""
```

A starter `me.yaml.example` lives in `psyneulink-mcp/examples/`. Personal profile is *intentionally* not a tool the MCP can write to — users edit the file with their own editor.

### Generator integration (`scripts/generate_tools.py`)

Replace the local-only feedback read with a merge:

```python
def gather_feedback() -> dict[str, list[dict]]:
    local = group_by_tool(read_pending(PENDING_PATH))
    try:
        remote = group_by_tool(corpus.fetch_pending_feedback_issues())
    except corpus.CorpusUnavailable as e:
        print(f"[generate_tools] corpus unavailable, using local only: {e}", file=sys.stderr)
        remote = {}
    # merge: local entries first, then remote (order shouldn't matter for the LLM)
    merged: dict[str, list[dict]] = {}
    for d in (local, remote):
        for k, v in d.items():
            merged.setdefault(k, []).extend(v)
    return merged
```

After successful regeneration:
- Local pending → archive (existing behavior).
- Remote issues → **comment on the issue** with "consumed in regen <sha>" and apply label `consumed`. The issue stays open until a human decides to close it after verifying the fix. (No auto-close: the corpus is human-reviewed.)

### Human feedback path

Per our discussion: humans don't go through the MCP. Two options for them:

1. **`gh` CLI directly:** `gh issue create --repo ystrittm/psyneulink-corpus --label feedback --template tool_feedback`. Document this in `docs/ISSUE_WORKFLOW.md` in the corpus repo.
2. **Optional convenience CLI** in `psyneulink-mcp`: `scripts/file_issue.py` that wraps `gh issue create` with the right repo/label baked in. Does *not* live in `src/psyneulink_mcp/` (not part of the server).

We'll do (1) only for v1 — fewer moving parts. (2) can come later if the friction is real.

### Tests

- `tests/test_corpus.py` — uses `monkeypatch` on `subprocess.run` to fake `gh` responses; verifies `fetch_brainlike_views` and `fetch_pending_feedback_issues` parse correctly, and `CorpusUnavailable` raises on auth failure.
- Update `tests/test_feedback.py` generator tests so the merge function works when remote returns []  / errors / has overlapping tool names.

### CLAUDE.md updates (additional — in `psyneulink-mcp/`)

- Update the `## Feedback loop` section to explain the merge with corpus issues.
- Add a `## Corpus integration` section linking to the corpus repo and the schema.
- Reaffirm the "Separation of concerns is pure" rule with concrete examples ("the MCP must not contain a brainlike YAML; if you find one, move it to the corpus").

## Phase 4 — Agent scaffold (in `psyneulink-agent/`)

Just enough to exist:

- `pyproject.toml` (uv-managed, depends on the `mcp` client package and `pyyaml`).
- `src/psyneulink_agent/__init__.py` — empty.
- `src/psyneulink_agent/main.py` — placeholder: connects to a local `psyneulink-mcp` via stdio, lists the tools, prints them. No modeling logic yet.
- `CLAUDE.md`:
  - "This is Layer 2. It uses psyneulink-mcp via the MCP protocol. It is the only place where 'modeling decisions' live."
  - Reference back to `psyneulink-mcp/CLAUDE.md` for the separation rule.
  - Inherit the "Working with Claude" preferences (or extract those into `~/.claude/CLAUDE.md` so they apply automatically across sibling repos — already done in our earlier session).

## Phasing & how to execute

The three phases are sequential because each consumes the previous:

1. Phase 1 (restructure) — done in this Claude session immediately after ExitPlanMode. **User restarts the session** at `psyneulink-ai/psyneulink-mcp/` afterward.
2. Phase 2 (corpus skeleton) — separate Claude session opened in `psyneulink-corpus/`. Smaller and focused.
3. Phase 3 (MCP integration) — back in `psyneulink-mcp/`. Tests run there.
4. Phase 4 (agent scaffold) — separate Claude session in `psyneulink-agent/`.

**Why one session per repo:** keeps each session's context lean, lets each repo's CLAUDE.md fully steer its session, mirrors how a human developer would work.

## Files this plan will create or modify

### Phase 1 (this session, post-exit)
- Move existing tree into `psyneulink-ai/psyneulink-mcp/`.
- New: `psyneulink-mcp/CLAUDE.md` — add `## Separation of concerns is pure`, rename architecture section.
- New empty repos: `psyneulink-agent/`, `psyneulink-corpus/` with minimal scaffolds + GH remotes.

### Phase 2 (separate session)
- All under `psyneulink-corpus/`: `community/brainlike/_schema.yaml`, `community/brainlike/examples/canonical-transfer.yaml`, `.github/CODEOWNERS`, `.github/ISSUE_TEMPLATE/tool_feedback.yml`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/workflows/validate.yml`, `docs/CONTRIBUTING.md`, `docs/BRAINLIKE_SCHEMA.md`, `docs/ISSUE_WORKFLOW.md`, `README.md`.

### Phase 3 (back in psyneulink-mcp)
- New: `src/psyneulink_mcp/corpus.py`, `src/psyneulink_mcp/tools/curated/brainlike.py`, `examples/me.yaml.example`, `tests/test_corpus.py`.
- Modify: `src/psyneulink_mcp/server.py` (register brainlike tools), `scripts/generate_tools.py` (merge corpus feedback, comment+label on success), `tests/test_feedback.py` (update generator tests), `CLAUDE.md` (corpus section + feedback-loop update).

### Phase 4 (separate session)
- All under `psyneulink-agent/`: `pyproject.toml`, `src/psyneulink_agent/__init__.py`, `src/psyneulink_agent/main.py`, `CLAUDE.md`.

## Verification

End-to-end smoke (after all four phases):

1. Three repos exist, each with a `gh repo view` showing private + the right description.
2. From `psyneulink-mcp/`: `uv run pytest` — all tests pass including new `test_corpus.py`.
3. From `psyneulink-mcp/`: `uv run python scripts/generate_tools.py` — pulls corpus issues, merges with local feedback, prints the per-tool grouping. (LLM call still stubbed; archive step still gated.)
4. From `psyneulink-mcp/`: start the MCP, call `get_community_brainlike_views` via the inspector, see the `canonical-transfer` example returned.
5. From `psyneulink-mcp/`: write a real `~/.config/psyneulink-mcp/me.yaml` with two predicates, call `get_my_brainlike_view`, see them returned.
6. Manually: `gh issue create --repo ystrittm/psyneulink-corpus --template tool_feedback` and walk through the form — confirm the issue lands with label `feedback`.
7. Manually: open a tiny PR adding a second YAML under `community/brainlike/` — confirm CI validates it against `_schema.yaml`.
8. From `psyneulink-agent/`: `uv run python -m psyneulink_agent.main` — connects to a local mcp instance, prints the tool list including the new corpus tools.

## Open questions to resolve at execution time

- Confirm the GitHub owner (`ystrittm` assumed throughout). If the org/personal account differs, swap before running `gh repo create`.
- Confirm "private" default for all three repos. Public is fine if the user wants visibility for the learning project.
- Personal `me.yaml` location: `~/.config/psyneulink-mcp/me.yaml` is the XDG-style default. Override via `PSYNEULINK_MCP_PERSONAL_PROFILE`. Users who *want* their personal profile committed can put it under `psyneulink-corpus/users/<handle>/brainlike.yaml` and configure the MCP to read from there instead — both paths supported.
