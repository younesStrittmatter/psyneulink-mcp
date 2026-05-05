# Plan: Persist & exchange models (MDF loader + Python export)

**Status:** queued, not yet implemented. Created 2026-05-04.
**Sources:**

- [ModECI/MDF](https://github.com/ModECI/MDF) — open-standard
  serialised model description (JSON / YAML / BSON) with bidirectional
  PsyNeuLink support already in `modeci_mdf`.
- Local "session script" export — a runnable `.py` file that
  reconstructs whatever the agent built, so the user has a tangible
  artifact they can read, run standalone, edit, or commit.

## Why

Today everything the agent builds lives in the MCP subprocess's RAM
and dies when the chat ends. That's fine for one-shot exploration but
useless for: (a) re-loading a prior model, (b) sharing models across
people / chats, (c) reading the model in a non-LLM context, and (d)
treating the artifact as code that can be edited or version-controlled.

Two complementary export surfaces, picked deliberately:

* **MDF** is the right cross-tool exchange format. ModECI maintains a
  PNL ↔ MDF bridge, so we don't have to invent serialisation, and a
  model dumped here also opens to ONNX / NeuroML / WebGME consumers.
  Best for archive / interchange / corpus inclusion.
* **A runnable `.py` script** is the right human-readable artifact. It
  IS the model in the language the user already knows; you can `cat`
  it, diff it in PRs, run it without any of our infra, paste it into a
  notebook. Best for "I built something I want to keep / share with my
  collaborator who doesn't use this MCP."

Both need to exist. MDF without a Python export feels opaque; Python
export without MDF leaves the corpus without a structured format.

Once this lands, an agent can:

1. Browse / fetch a corpus YAML that contains an `mdf:` block.
2. Load it with `load_mdf_model(...)` → handle for the resulting PNL
   `Composition` (and per-node handles).
3. Inspect, mutate, or run it with the existing curated tools.
4. At any point dump the current state via `dump_mdf_model(...)` or
   `export_python_script(...)` — get a file the user can keep.

## Scope (MVP)

Three curated tools, no new generated tools:

* `load_mdf_model(source, format=None) -> {composition, nodes}`
  - `source`: file path, raw text, or URL. Auto-detect format from
    extension when `format` is omitted; otherwise one of `"json"`,
    `"yaml"`, `"bson"`.
  - Uses `modeci_mdf.utils.load_mdf` (or `load_mdf_json` /
    `load_mdf_yaml` per the API the loader needs) to get a `Model`.
  - Calls `modeci_mdf.interfaces.psyneulink.import_mdf_to_psyneulink`
    (or the equivalent in the version we pin) to materialise the PNL
    `Composition`.
  - Registers the composition + every node in `handles`. Returns
    `{"composition": "h_...", "nodes": {"node_name": "h_..."}}` so
    the agent can immediately pass them to `add_*` / `run_composition`.

* `dump_mdf_model(composition, format="yaml") -> {text, format}`
  - Reverse direction. Calls
    `modeci_mdf.interfaces.psyneulink.model_to_mdf` (or whatever the
    pinned version exposes), then serialises with the requested
    format. Returns the text directly so the agent can show it /
    save it.

* `export_python_script(composition=None, path=None) -> {path, text}`
  - Writes a runnable `.py` file that, when executed, reconstructs
    the same PNL composition (and every other handle that fed into
    it) and runs it.
  - **Mode-agnostic**: this is an MCP tool, so every front-end gets
    it for free — interactive terminal chat, web UI, headless batch
    runner. The MCP doesn't know or care which one is calling.
  - Mechanism: every `_impl` for a generated tool, plus every
    composition-mutating curated tool (`add_node`,
    `add_linear_pathway`, `add_projection`, `run_composition`),
    appends a structured record to a per-process **session journal**
    (kept in `handles.py` next to `_HANDLES`). The record captures:
    `tool_name`, `args` (with handle strings preserved), and the
    resulting handle (if any). `export_python_script` walks the
    journal in order and renders Python that:
    1. `import psyneulink as pnl`
    2. assigns each create-call to a Python variable named after the
       handle's PNL `name` (collision-suffixed if needed),
    3. emits the corresponding `Composition.add_*` calls,
    4. ends with the `comp.run(...)` calls under
       `if __name__ == "__main__":` plus a `print(comp.results)`.
  - `composition` arg filters the journal to operations that touch
    that composition + its constituent nodes' construction; omitted
    means "everything in the session".
  - `path` defaults to `~/Documents/psyneulink-models/<name>-<utc-ts>.py`
    (creating dirs as needed). Returns both the absolute path and the
    rendered text so the agent can show the user a preview without a
    second tool call.

* `load_python_script(path) -> {handles, summary}`
  - The reverse of `export_python_script`: read a `.py` file
    produced by us (or hand-written following the same shape),
    materialise the PNL objects, and register them as handles.
  - Two implementation strategies, both worth shipping:
    1. **Replay mode** (preferred): the file optionally carries a
       trailing `# psyneulink-mcp:journal` JSON block (emitted by
       `export_python_script`). When present, replay the journal
       through the same MCP tool implementations — no Python `exec`
       needed, no arbitrary-code-execution risk.
    2. **Exec mode** (fallback): for hand-written files or scripts
       without the journal block, exec the script in an isolated
       module namespace, then introspect the resulting globals for
       PNL objects (Mechanisms, Compositions, Functions) and
       register every one as a handle. Required tool-description
       warning: "this runs the script as Python; only load files
       you trust."
  - Returns `{"handles": {var_name: handle, …}, "summary":
    "loaded 1 Composition + 3 Mechanisms from foo.py"}`.

## Out of scope for MVP

- ONNX / NeuroML / WebGME bridges. MDF supports those but our agent
  doesn't need them in the first cut.
- Stateful `Conditions` round-tripping if upstream MDF doesn't yet
  faithfully convert PNL conditions. Punt with a clear error.
- Corpus integration of MDF blocks (separate plan in
  `psyneulink-corpus/plans/` once this lands here).
- "Reverse engineer Python from a live `Composition`" (i.e., walking
  the object graph instead of the journal). PNL has no official
  `to_python` and the object graph is lossy w.r.t. construction
  intent. The journal-replay approach is honest about what was done
  and degrades gracefully — a model loaded via `load_mdf_model` whose
  internals were never journalled simply gets exported as
  `model = load_mdf_model("...mdf.yaml"); model.run(...)` instead of
  full reconstruction.

## Implementation notes

- `modeci-mdf` is a heavy dep (numpy, sympy, scipy chain via PNL
  interfaces). Add as `[project.optional-dependencies] mdf =
  ["modeci-mdf>=0.4"]` so the base server install stays lean. The two
  MDF tools should `try: import modeci_mdf` at call time and return a
  `{"error": "modeci-mdf not installed; pip install
  'psyneulink-mcp[mdf]'"}` payload rather than crashing on import.
- All three tools live in `src/psyneulink_mcp/tools/curated/persistence.py`
  (new file) and register in `server.py` next to `composition`.
  `export_python_script` has zero new deps so it ships unconditionally;
  the MDF tools sit behind the optional extra.
- The MDF library itself does the PNL construction, so we benefit
  from upstream maintenance — but we should pin the version we
  validated against and bump deliberately, since the converter is
  still pre-1.0.
- Test with the canonical examples in `ModECI/MDF/examples/PyTorch/`
  and `ModECI/MDF/examples/PsyNeuLink/`. Mark as `integration`
  because of the heavy import chain.

### Session journal mechanics

- Add `_JOURNAL: list[JournalEntry]` next to `_HANDLES` in
  `handles.py`, plus `record_call(tool_name, args, result_handle=None)`
  and `journal_snapshot()` accessors. `clear_handles()` clears it too.
- The generated-tool template's `_impl` already has the call site —
  add a single `handles.record_call(TOOL_NAME, kwargs, result_handle)`
  there, behind a no-op when the result isn't a handle.
- Curated composition tools record themselves the same way.
- `JournalEntry` shape:
  `{tool_name, args (handle strings preserved verbatim),
   result_handle (None for run_composition / list_handles / etc.),
   tool_layer ("generated" | "curated")}`.
- The renderer:
  1. Build a handle → variable-name map by walking entries that
     produced a handle, snake-casing each object's `name` and
     suffixing on collision.
  2. For each `create_*` entry, emit
     `var = pnl.<ClassName>(**rehydrated_args)` where rehydrated args
     swap any handle string for the corresponding variable identifier.
  3. For each composition-mutating entry, emit
     `comp.<method>(...)` with the variable identifiers in place of
     handles.
  4. For each `run_composition` entry, emit it under the `__main__`
     block.
  5. Always preface with the standard header (`# Generated by
     psyneulink-mcp on <utc-ts> from chat session …`,
     `import psyneulink as pnl`).
- Cap the journal at e.g. 5000 entries with a soft warning emitted
  once it exceeds, to avoid OOMing a runaway session.
- Tests (`tests/test_session_journal.py`): record a small sequence,
  render the script to a string, `compile()` it for syntax, and
  also `exec` it under a sandboxed namespace to confirm it produces
  the same `output_values` as the original session. Marked
  `integration` (needs PNL).

## Risks / unknowns

- Bidirectional fidelity (MDF): `model_to_mdf` may not capture every
  PNL feature (controllers, schedulers, learning specs). Document
  the gaps in the tool description so the agent doesn't promise
  more than it can deliver.
- Naming collisions: MDF nodes and our handle registry both use
  `name` — make sure the handle payload's `name` is the PNL name
  (after MDF→PNL conversion), not the MDF source name.
- Version skew: PNL ↔ MDF compatibility is a moving target. Add a
  `--check-mdf` smoke target to CI that just imports and round-trips
  one example.
- Python export of MDF-loaded models: when the agent loads a model
  via `load_mdf_model` and only mutates it, the journal can't
  reconstruct the loaded portion from primitives. The renderer
  should emit `comp = load_mdf_model("<original-source>")["composition"]`
  as the first line in that case, then the journalled mutations
  on top — honest, lossless, and round-trippable.
- Argument fidelity in the script: `args` dicts can contain numpy
  arrays or other non-literal values (e.g., when matrices arrive as
  `np.ndarray`). Renderer must `repr` floats/ints/strings inline,
  use `numpy.array([...])` for arrays (with a `numpy as np` import
  emitted lazily), and refuse-with-warning for anything else. Better
  to leave a `# TODO: <repr>` placeholder than emit a syntactically
  invalid script.

## Cross-link

The `.py` create / load / store loop is the canonical model
artifact for **every** front-end of the agent (terminal chat, web
UI, headless batch). All three live under
`psyneulink-agent/plans/ui-pdfs-psyche.md`; this plan owns the MCP
tools that make it possible. The two plans must land in either
order — the agent's front-ends feature-detect the tools at session
start and hide the corresponding UI affordances if missing.

## Done when

- `load_mdf_model` returns handles for a checked-in MDF YAML and
  `run_composition` on the result produces the same output the MDF
  example reports.
- `dump_mdf_model` round-trips that same composition.
- `export_python_script` writes a `.py` file that runs standalone
  (`python that-file.py`) and produces the same `output_values` the
  original chat session reported.
- `load_python_script` round-trips a file produced by
  `export_python_script` back into a fresh session — same handles,
  same `output_values` on re-run.
- All three surfaces are documented in `README.md`'s tool list, and
  the agent's system prompt mentions when to suggest each one
  ("save this model" → script for humans, MDF for archive / corpus).
- This file is deleted in the same commit that ships the loader
  (per `<repo>/AGENTS.md`).
