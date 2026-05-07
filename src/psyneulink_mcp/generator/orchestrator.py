"""Build-time tool generator entry point.

Orchestrates: seed-symbol discovery (``introspection``) → feedback
aggregation (``feedback_loop``) → LLM call (``adapters``) → module
rendering (``template``) → write into ``tools/generated/``.

The runtime server never imports this module — it's invoked via the
``psyneulink-mcp-generate`` console script (or
``scripts/generate_tools.py``).

CLI:

  --force                Regenerate every selected symbol unconditionally,
                         ignoring the source-hash skip.
  --only QNAME[,QNAME]   Comma-separated allowlist of qualnames or short
                         names. Other selected symbols are skipped.
  --limit N              Cap number of symbols processed (smoke testing).
                         Applied after --only.
  --dry-run              Skip the LLM call; emit a placeholder ToolSpec
                         and template each module. Existing files on disk
                         are not overwritten unless --force is also set.
  --adapter NAME         Override ``$PSYNEULINK_MCP_LLM_ADAPTER``.
  --seeds-file PATH      Override the default ``generator/seeds.txt``.

Incremental regen: a symbol is skipped when the existing generated module
on disk encodes the same ``__source_sha256__`` AND the tool name has no
pending feedback. ``--force`` bypasses the skip.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from psyneulink_mcp import corpus
from psyneulink_mcp.generator import feedback_loop, framework_issue_loop
from psyneulink_mcp.generator.adapters import (
    AdapterError,
    LLMAdapter,
    get_adapter,
)
from psyneulink_mcp.generator.adapters.base import ToolSpec
from psyneulink_mcp.generator.framework_issue_loop import FrameworkIssue
from psyneulink_mcp.generator.framework_issue_verifier import (
    Status as _FwStatus,
)
from psyneulink_mcp.generator.framework_issue_verifier import verify as verify_framework_issue
from psyneulink_mcp.generator.introspection import (
    SymbolMeta,
    discover_seed_symbols,
)
from psyneulink_mcp.generator.prompts import TOOL_SPEC_SCHEMA, render_prompt
from psyneulink_mcp.generator.rerender import rerender_directory
from psyneulink_mcp.generator.template import (
    module_filename_for,
    module_stem_for,
    render_init,
    render_module,
    tool_name_for,
)

REPO_ROOT = Path(__file__).resolve().parents[3]
GENERATED_DIR = REPO_ROOT / "src" / "psyneulink_mcp" / "tools" / "generated"
DEFAULT_SEEDS_FILE = REPO_ROOT / "generator" / "seeds.txt"

# Matches the literal `__source_sha256__ = "..."` line that
# `template.render_module` emits, so we can read the previous hash
# without importing the generated module (which might fail if PNL is
# present but mis-installed).
_SHA_LINE_RE = re.compile(
    r'^__source_sha256__\s*=\s*[\'"]([0-9a-f]+)[\'"]\s*$',
    re.MULTILINE,
)

# Matches the `__pnl_parent_sha256s__ = {...}` block. We literal-eval
# the captured dict body to get the parent → SHA map for cascade
# invalidation. Older generated modules (pre-Phase-3) don't carry this
# field; their absence is treated as "no parent SHAs recorded → don't
# cascade-invalidate" so the rollout stays gradual rather than
# triggering a full 354-tool regen on first run after the upgrade.
_PARENT_SHA_BLOCK_RE = re.compile(
    r'^__pnl_parent_sha256s__\s*=\s*(\{.*?\})\s*$',
    re.MULTILINE | re.DOTALL,
)


# --------------------------------------------------------------------------- #
# placeholder used by --dry-run                                               #
# --------------------------------------------------------------------------- #


def _placeholder_spec(symbol: SymbolMeta) -> ToolSpec:
    """Sentinel ToolSpec used by ``--dry-run``.

    The description carries a TODO marker so a code reviewer noticing it
    in committed output knows the file was generated without hitting the
    LLM.
    """
    return {
        "description": (
            f"TODO: regen with adapter. Placeholder wrapper for {symbol.qualname} ({symbol.kind})."
        ),
        "parameters": {"type": "object", "properties": {}, "required": []},
        "notes": "",
    }


# --------------------------------------------------------------------------- #
# selection                                                                   #
# --------------------------------------------------------------------------- #


def _parse_only(only: str | None) -> set[str] | None:
    if not only:
        return None
    return {item.strip() for item in only.split(",") if item.strip()}


def _matches_only(symbol: SymbolMeta, only: set[str]) -> bool:
    return symbol.qualname in only or symbol.short_name in only


def _select_symbols(
    symbols: list[SymbolMeta],
    only: set[str] | None,
    limit: int | None,
) -> list[SymbolMeta]:
    selected = symbols
    if only is not None:
        selected = [s for s in selected if _matches_only(s, only)]
        if not selected:
            print(
                f"[generate_tools] --only {sorted(only)!r} matched nothing.",
                file=sys.stderr,
            )
    if limit is not None and limit >= 0:
        selected = selected[:limit]
    return selected


# --------------------------------------------------------------------------- #
# incremental skip                                                            #
# --------------------------------------------------------------------------- #


def _existing_sha(generated_dir: Path, symbol: SymbolMeta) -> str | None:
    path = generated_dir / module_filename_for(symbol)
    if not path.exists():
        return None
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    match = _SHA_LINE_RE.search(text)
    return match.group(1) if match else None


def _existing_parent_sha256s(
    generated_dir: Path, symbol: SymbolMeta
) -> dict[str, str] | None:
    """Read the recorded ``__pnl_parent_sha256s__`` map from the on-disk module.

    Returns ``None`` when the file doesn't exist OR when it predates
    Phase 3 (no ``__pnl_parent_sha256s__`` block) — in both cases the
    caller treats the parent SHAs as untracked and skips cascade
    invalidation. We literal-eval the captured block so a corrupted or
    hand-edited file doesn't crash the generator (we just bail out and
    let the regen proceed if other reasons demand it).
    """
    path = generated_dir / module_filename_for(symbol)
    if not path.exists():
        return None
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    match = _PARENT_SHA_BLOCK_RE.search(text)
    if not match:
        return None
    import ast

    try:
        value = ast.literal_eval(match.group(1))
    except (ValueError, SyntaxError):
        return None
    if not isinstance(value, dict):
        return None
    return {str(k): str(v) for k, v in value.items()}


def _should_skip(
    symbol: SymbolMeta,
    generated_dir: Path,
    feedback_by_tool: dict[str, list[dict[str, Any]]],
    *,
    force: bool,
    dry_run: bool,
) -> bool:
    """True when nothing changed and there's no pending feedback to address.

    Checks, in order:

    1. ``--force`` flag — never skip.
    2. No committed file yet — never skip.
    3. The symbol's own source SHA differs from the on-disk file → regen.
    4. Pending feedback names this tool → regen.
    5. **Cascade invalidation**: any of this class's PNL parent classes
       has a different source SHA now than what was recorded when the
       module was last generated → regen, because the parent docstring
       included in the regen prompt has changed and the description
       written against it is stale.

    (5) only applies to modules generated post-Phase-3 (older ones have
    no recorded parent SHAs and are left alone to keep the migration
    gradual).
    """
    if force:
        return False
    existing = _existing_sha(generated_dir, symbol)
    if existing is None:
        return False  # no committed file yet
    if existing != symbol.source_sha256:
        return False  # PNL source changed
    if feedback_by_tool.get(tool_name_for(symbol)):
        return False  # feedback is the whole reason to regen
    recorded_parents = _existing_parent_sha256s(generated_dir, symbol)
    if recorded_parents is not None:
        current_parents = symbol.parent_source_sha256s_dict
        for parent_name, current_sha in current_parents.items():
            recorded_sha = recorded_parents.get(parent_name)
            if recorded_sha is not None and recorded_sha != current_sha:
                return False  # parent's PNL source changed → regen child
    if dry_run:
        # In dry-run mode we never overwrite an up-to-date file —
        # a no-LLM placeholder would actively destroy work.
        return True
    return True


# --------------------------------------------------------------------------- #
# I/O                                                                         #
# --------------------------------------------------------------------------- #


def _write_module(symbol: SymbolMeta, body: str, generated_dir: Path) -> Path:
    generated_dir.mkdir(parents=True, exist_ok=True)
    path = generated_dir / module_filename_for(symbol)
    text = body if body.endswith("\n") else body + "\n"
    path.write_text(text, encoding="utf-8")
    return path


def _write_init(stems: list[str], generated_dir: Path) -> Path:
    init_path = generated_dir / "__init__.py"
    init_path.write_text(render_init(stems), encoding="utf-8")
    return init_path


def _existing_stems(generated_dir: Path) -> list[str]:
    """Stems of all already-on-disk generated modules (for index rewrite).

    We rebuild the index from the union of "regenerated this run" plus
    "untouched on disk" so a partial run doesn't drop modules from the
    server's tool surface.
    """
    if not generated_dir.is_dir():
        return []
    return sorted(
        p.stem for p in generated_dir.iterdir() if p.suffix == ".py" and not p.name.startswith("__")
    )


# --------------------------------------------------------------------------- #
# main pipeline                                                               #
# --------------------------------------------------------------------------- #


def _git_head_sha() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return "unknown"
    if result.returncode != 0:
        return "unknown"
    return result.stdout.strip() or "unknown"


def _generated_by(adapter: LLMAdapter | None, dry_run: bool) -> str:
    if dry_run:
        return "dry-run"
    if adapter is None:
        return "unknown"
    name = getattr(adapter, "name", type(adapter).__name__)
    model = getattr(adapter, "model", None)
    return f"{name}@{model}" if model else name


_HISTORICAL_FAILURES_HEADER = "## HISTORICAL FAILURES"


def _truncate_one_line(text: str, *, max_chars: int = 240) -> str:
    """First non-empty line of ``text``, collapsed + truncated for the section."""
    for raw in (text or "").splitlines():
        line = raw.strip()
        if not line:
            continue
        if len(line) > max_chars:
            return line[: max_chars - 1] + "…"
        return line
    return ""


def _render_historical_failures_block(
    failures: list[dict[str, Any]],
) -> str:
    """Deterministic markdown block for the closed-issue history of one tool.

    Empty list → empty string (caller skips appending). The block is
    stable across re-runs given the same closed issues in the same
    order — that's why ``fetch_historical_failures`` sorts by issue
    number desc + caps the list before this function ever sees it.
    """
    if not failures:
        return ""
    lines = [_HISTORICAL_FAILURES_HEADER]
    for issue in failures:
        number = issue.get("number") or "?"
        title = (issue.get("title") or "").strip() or "(no title)"
        summary = _truncate_one_line(issue.get("body") or "")
        if summary:
            lines.append(f"- #{number} — {title}: {summary}")
        else:
            lines.append(f"- #{number} — {title}")
    return "\n".join(lines)


def _augment_with_historical_failures(
    spec: ToolSpec,
    failures: list[dict[str, Any]],
) -> ToolSpec:
    """Append a ``## HISTORICAL FAILURES`` block to ``spec['description']``.

    Returns a new ``ToolSpec`` (shallow copy) with the augmented
    description; leaves the original alone so caller-side state
    (test assertions, retries, …) isn't surprised by mutation.
    Empty ``failures`` → returns ``spec`` unchanged.
    """
    if not failures:
        return spec
    block = _render_historical_failures_block(failures)
    if not block:
        return spec
    augmented = dict(spec)
    base = (augmented.get("description") or "").rstrip()
    augmented["description"] = f"{base}\n\n{block}\n" if base else f"{block}\n"
    return augmented  # type: ignore[return-value]


# Override for the model the orchestrator escalates "complicated"
# symbols to. The intuition: the cheap default model handles the long
# tail of straightforward PNL classes / functions just fine; the harder
# cases — tools with active feedback to address, tools with closed
# historical failures, methods (which have port-routing nuance the
# template helper has to convey faithfully) — benefit from a stronger
# model. Override via ``$PSYNEULINK_MCP_CLAUDE_MODEL_ESCALATED``.
ENV_ESCALATED_MODEL = "PSYNEULINK_MCP_CLAUDE_MODEL_ESCALATED"
DEFAULT_ESCALATED_MODEL = "opus"


def _pick_model_for_symbol(
    symbol: SymbolMeta,
    feedback: list[dict[str, Any]],
    historical_failures: list[dict[str, Any]],
    framework_limitations: list[FrameworkIssue] | None = None,
) -> str | None:
    """Return an override model for ``symbol``, or ``None`` for the default.

    Escalate to opus (or ``$PSYNEULINK_MCP_CLAUDE_MODEL_ESCALATED``)
    whenever any of these holds:

    * Pending feedback exists for this tool — addressing user-reported
      problems is exactly the case where a stronger model pays off.
    * Closed historical failures exist — the regen LLM has to write a
      description that doesn't re-trigger the same closed bugs, which
      benefits from longer reasoning.
    * Verified framework limitations exist — describing an upstream
      bug + its workaround clearly without recommending a different
      tool by name takes more careful prose than a default-case rewrite.
    * The symbol is a class with 4+ PNL parents — deep MRO chains
      mean more inheritance to compress correctly.

    Cheap default for everything else; opus for the stuff that breaks.
    """
    if feedback:
        return os.environ.get(ENV_ESCALATED_MODEL, DEFAULT_ESCALATED_MODEL)
    if historical_failures:
        return os.environ.get(ENV_ESCALATED_MODEL, DEFAULT_ESCALATED_MODEL)
    if framework_limitations:
        return os.environ.get(ENV_ESCALATED_MODEL, DEFAULT_ESCALATED_MODEL)
    if symbol.kind == "class" and len(symbol.parent_short_names) >= 4:
        return os.environ.get(ENV_ESCALATED_MODEL, DEFAULT_ESCALATED_MODEL)
    return None


def _verify_and_consume_framework_issues(
    adapter: LLMAdapter | None,
) -> tuple[dict[str, list[FrameworkIssue]], list[int]]:
    """Verify every open framework_issue, partition into still-present + fixed.

    Returns ``(grouped_still_present, fixed_issue_numbers)``:

    * ``grouped_still_present`` keys on ``related_mcp_tool`` so the
      per-symbol regen prompt can attach them to the right tool.
      Issues with no ``related_mcp_tool`` are dropped from the
      returned dict (we have no tool description to inject the warning
      into) but are still counted in the verifier output.
    * ``fixed_issue_numbers`` are the GH issue numbers the caller
      should hand to ``corpus.mark_issues_consumed``.

    The reproducer pass runs first (no LLM cost). LLM-judged
    verification only runs for issues whose reproducer was
    inconclusive AND we have an adapter to ask. ``UNKNOWN`` verdicts
    are conservatively treated as still-present (kept in the prompt,
    not auto-consumed) so we never drop a real bug from the warning
    set on a flaky verifier reply.
    """
    try:
        issues = framework_issue_loop.gather_framework_issues()
    except Exception as exc:  # noqa: BLE001 — never abort regen for a verifier hiccup
        print(
            f"[generate_tools] could not gather framework_issue issues: "
            f"{type(exc).__name__}: {exc}",
            file=sys.stderr,
        )
        return {}, []

    if not issues:
        return {}, []

    print(
        f"[generate_tools] verifying {len(issues)} open framework_issue(s) "
        f"on {corpus.corpus_repo()}",
        file=sys.stderr,
    )

    llm_judge_callable = _build_llm_judge(adapter)
    still_present: dict[str, list[FrameworkIssue]] = {}
    fixed_numbers: list[int] = []
    for issue in issues:
        verdict = verify_framework_issue(issue, llm_judge=llm_judge_callable)
        print(
            f"  #{issue.number} ({issue.library}) → {verdict.status.value} "
            f"[{verdict.method}] {verdict.note[:160]}",
            file=sys.stderr,
        )
        if verdict.status is _FwStatus.FIXED:
            fixed_numbers.append(issue.number)
            continue
        # Conservatively treat UNKNOWN as still-present: keep the
        # warning in the prompt, don't auto-mark consumed.
        if issue.related_mcp_tool:
            still_present.setdefault(issue.related_mcp_tool, []).append(issue)
    return still_present, fixed_numbers


def _build_llm_judge(adapter: LLMAdapter | None) -> Any:
    """Wrap the regen adapter as a (prompt -> str) callable for the verifier.

    Returns ``None`` when no adapter is available (dry-run path) — the
    verifier then reports ``UNKNOWN`` for any issue the reproducer
    can't decide.

    The judge wrapper uses a 1-property "verdict" schema instead of
    the full ``ToolSpec`` schema so we get a structured one-line
    response without paying the price of a full description regen.
    """
    if adapter is None:
        return None

    judge_schema: dict[str, Any] = {
        "type": "object",
        "properties": {
            "verdict": {
                "type": "string",
                "description": (
                    "Two short lines. Line 1 is exactly one of "
                    "STILL_PRESENT / FIXED / UNKNOWN. Line 2 is a "
                    "one-sentence justification."
                ),
            }
        },
        "required": ["verdict"],
        "additionalProperties": False,
    }

    def _judge(prompt: str) -> str:
        try:
            spec = adapter.generate(prompt, schema=judge_schema)
        except Exception as exc:  # noqa: BLE001 — propagate as empty + log
            print(
                f"[generate_tools] llm_judge generate() raised: "
                f"{type(exc).__name__}: {exc}",
                file=sys.stderr,
            )
            return ""
        return str(spec.get("verdict", ""))  # type: ignore[union-attr]

    return _judge


def _generate_one(
    symbol: SymbolMeta,
    feedback: list[dict[str, Any]],
    historical_failures: list[dict[str, Any]],
    adapter: LLMAdapter | None,
    *,
    dry_run: bool,
    framework_limitations: list[FrameworkIssue] | None = None,
) -> str:
    """Render one symbol's tool module, optionally with verified framework limitations.

    ``framework_limitations`` are corpus framework_issue entries that
    the verifier confirmed still reproduce in the current PNL build.
    They flow into the regen prompt's ``KNOWN FRAMEWORK LIMITATIONS``
    section so the LLM writes ``notes`` warning the agent off the
    broken call shapes.
    """
    if dry_run or adapter is None:
        spec = _placeholder_spec(symbol)
    else:
        prompt = render_prompt(
            symbol, feedback, framework_limitations=framework_limitations
        )
        model_override = _pick_model_for_symbol(
            symbol, feedback, historical_failures, framework_limitations
        )
        spec = adapter.generate(
            prompt, schema=TOOL_SPEC_SCHEMA, model=model_override
        )
    spec = _augment_with_historical_failures(spec, historical_failures)
    return render_module(symbol, spec, generated_by=_generated_by(adapter, dry_run))


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="psyneulink-mcp-generate",
        description=(
            "Regenerate the auto layer of psyneulink-mcp tools from PsyNeuLink's public API."
        ),
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-generate every selected symbol, ignoring source-hash skip.",
    )
    parser.add_argument(
        "--only",
        metavar="QNAME[,QNAME...]",
        default=None,
        help="Comma-separated allowlist of qualnames or short names.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Cap number of symbols processed (smoke testing).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Skip LLM call; emit placeholder ToolSpec.",
    )
    parser.add_argument(
        "--adapter",
        default=None,
        help="Adapter name to use (overrides $PSYNEULINK_MCP_LLM_ADAPTER).",
    )
    parser.add_argument(
        "--seeds-file",
        type=Path,
        default=DEFAULT_SEEDS_FILE,
        help="Path to seeds.txt (default: <repo>/generator/seeds.txt).",
    )
    parser.add_argument(
        "--rerender",
        action="store_true",
        help=(
            "Re-template every existing generated module from its on-disk "
            "metadata. Skips introspection and the LLM. Use after changing "
            "template.py."
        ),
    )
    return parser.parse_args(argv)


def _run_rerender() -> int:
    written, failures = rerender_directory(GENERATED_DIR)
    print(
        f"[generate_tools] re-templated {len(written)} module(s); {len(failures)} failure(s).",
        file=sys.stderr,
    )
    for path, msg in failures:
        print(f"  - {path.name}: {msg}", file=sys.stderr)
    # Refresh the index too: rerender doesn't add or remove files but a
    # stale index from a partial regen could be sitting on disk.
    _write_init(_existing_stems(GENERATED_DIR), GENERATED_DIR)
    return 0 if not failures else 1


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    if args.rerender:
        return _run_rerender()

    only = _parse_only(args.only)

    feedback_by_tool = feedback_loop.gather_feedback()
    total_entries = sum(len(v) for v in feedback_by_tool.values())
    if total_entries:
        print(
            f"[generate_tools] consuming {total_entries} feedback entries "
            f"across {len(feedback_by_tool)} tool(s) "
            f"(local + corpus@{corpus.corpus_repo()}#{corpus.corpus_ref()})",
            file=sys.stderr,
        )

    adapter: LLMAdapter | None
    if args.dry_run:
        adapter = None
    else:
        try:
            adapter = get_adapter(args.adapter)
        except AdapterError as e:
            print(f"[generate_tools] adapter unavailable: {e}", file=sys.stderr)
            return 2

    try:
        symbols = discover_seed_symbols(args.seeds_file)
    except Exception as e:  # noqa: BLE001 — surface introspection bugs clearly
        print(
            f"[generate_tools] could not discover seed symbols: {e}",
            file=sys.stderr,
        )
        return 2

    selected = _select_symbols(symbols, only=only, limit=args.limit)
    if not selected:
        print(
            "[generate_tools] no symbols selected; nothing to do.",
            file=sys.stderr,
        )
        return 1

    mode = "dry-run" if args.dry_run else f"adapter {type(adapter).__name__}"
    base_model = getattr(adapter, "model", None) if adapter else None
    escalated_model = os.environ.get(ENV_ESCALATED_MODEL, DEFAULT_ESCALATED_MODEL)
    print(
        f"[generate_tools] {len(selected)} of {len(symbols)} seed symbol(s) selected; mode={mode}",
        file=sys.stderr,
    )
    if not args.dry_run and base_model:
        print(
            f"[generate_tools] base model: {base_model!r}; escalating to "
            f"{escalated_model!r} for tools with feedback / historical "
            f"failures / deep MRO chains",
            file=sys.stderr,
        )

    selected_tool_names = sorted({tool_name_for(s) for s in selected})
    historical_by_tool = feedback_loop.gather_historical_failures(selected_tool_names)
    if historical_by_tool:
        print(
            f"[generate_tools] including HISTORICAL FAILURES blocks for "
            f"{len(historical_by_tool)} tool(s) "
            f"(closed pnl:* issues on {corpus.corpus_repo()})",
            file=sys.stderr,
        )

    # Verify open `framework_issue` corpus issues. Fixed ones get
    # auto-marked `consumed`; still-present ones get attached to the
    # affected MCP tool's regen prompt as a "KNOWN FRAMEWORK
    # LIMITATIONS" section. Skipped entirely on dry-run (no LLM judge,
    # no consumption). See `framework_issue_loop` + `framework_issue_verifier`.
    framework_limitations_by_tool: dict[str, list[FrameworkIssue]] = {}
    if not args.dry_run:
        framework_limitations_by_tool, fixed_issue_numbers = (
            _verify_and_consume_framework_issues(adapter)
        )
        if fixed_issue_numbers:
            sha = _git_head_sha()
            try:
                marked = corpus.mark_issues_consumed(
                    fixed_issue_numbers, regen_sha=sha
                )
                print(
                    f"[generate_tools] marked {len(marked)}/{len(fixed_issue_numbers)} "
                    f"framework_issue(s) consumed (verified fixed in regen {sha})",
                    file=sys.stderr,
                )
            except corpus.CorpusUnavailable as e:
                print(
                    f"[generate_tools] could not mark framework issues consumed: {e}",
                    file=sys.stderr,
                )
        if framework_limitations_by_tool:
            print(
                f"[generate_tools] {sum(len(v) for v in framework_limitations_by_tool.values())} "
                f"verified-still-present framework limitation(s) across "
                f"{len(framework_limitations_by_tool)} tool(s); "
                f"will inject as KNOWN FRAMEWORK LIMITATIONS in the regen prompts",
                file=sys.stderr,
            )

    successful_stems: list[str] = []
    skipped_stems: list[str] = []
    failures: list[tuple[str, str]] = []

    for symbol in selected:
        tool_name = tool_name_for(symbol)
        tool_feedback = feedback_by_tool.get(tool_name, [])
        tool_history = historical_by_tool.get(tool_name, [])
        if _should_skip(
            symbol,
            GENERATED_DIR,
            feedback_by_tool,
            force=args.force,
            dry_run=args.dry_run,
        ):
            skipped_stems.append(module_stem_for(symbol))
            continue
        tool_framework_limitations = framework_limitations_by_tool.get(
            tool_name, []
        )
        try:
            body = _generate_one(
                symbol,
                tool_feedback,
                tool_history,
                adapter,
                dry_run=args.dry_run,
                framework_limitations=tool_framework_limitations,
            )
        except Exception as e:  # noqa: BLE001 — keep going past per-symbol bugs
            failures.append((symbol.qualname, repr(e)))
            print(
                f"[generate_tools] FAILED {symbol.qualname}: {e}",
                file=sys.stderr,
            )
            continue
        if not body.strip():
            failures.append((symbol.qualname, "empty adapter output"))
            print(
                f"[generate_tools] FAILED {symbol.qualname}: empty output",
                file=sys.stderr,
            )
            continue
        try:
            _write_module(symbol, body, GENERATED_DIR)
        except OSError as e:
            failures.append((symbol.qualname, f"write failed: {e}"))
            print(
                f"[generate_tools] FAILED {symbol.qualname}: write failed: {e}",
                file=sys.stderr,
            )
            continue
        successful_stems.append(module_stem_for(symbol))

    # Index always reflects every committed/written .py in the dir, so
    # skipped-but-still-on-disk modules stay registered.
    all_stems = sorted(set(_existing_stems(GENERATED_DIR)) | set(successful_stems))
    _write_init(all_stems, GENERATED_DIR)

    print(
        f"[generate_tools] wrote {len(successful_stems)} new/updated; "
        f"skipped {len(skipped_stems)} up-to-date; "
        f"{len(failures)} failure(s); "
        f"index lists {len(all_stems)} module(s).",
        file=sys.stderr,
    )

    if not successful_stems:
        # Nothing was actually regenerated this run; don't archive
        # feedback (that would silently consume entries without acting
        # on them) and don't touch corpus issues.
        if failures:
            print(
                "[generate_tools] every selected symbol failed; "
                "leaving feedback and corpus untouched.",
                file=sys.stderr,
            )
            for q, why in failures:
                print(f"  - {q}: {why}", file=sys.stderr)
            return 1
        return 0

    if args.dry_run:
        # Dry runs intentionally never archive feedback or touch corpus.
        return 0

    archived = feedback_loop.archive_pending()
    if archived:
        print(
            f"[generate_tools] archived pending feedback to {archived}",
            file=sys.stderr,
        )

    issue_numbers = feedback_loop.consumed_issue_numbers(feedback_by_tool)
    if issue_numbers:
        sha = _git_head_sha()
        try:
            marked = corpus.mark_issues_consumed(issue_numbers, regen_sha=sha)
            print(
                f"[generate_tools] marked {len(marked)}/{len(issue_numbers)} "
                f"corpus issue(s) consumed (regen {sha})",
                file=sys.stderr,
            )
        except corpus.CorpusUnavailable as e:
            print(
                f"[generate_tools] could not mark corpus issues consumed: {e}",
                file=sys.stderr,
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
