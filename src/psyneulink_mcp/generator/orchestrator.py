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
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from psyneulink_mcp import corpus
from psyneulink_mcp.generator import feedback_loop
from psyneulink_mcp.generator.adapters import (
    AdapterError,
    LLMAdapter,
    get_adapter,
)
from psyneulink_mcp.generator.adapters.base import ToolSpec
from psyneulink_mcp.generator.introspection import (
    SymbolMeta,
    discover_seed_symbols,
)
from psyneulink_mcp.generator.prompts import TOOL_SPEC_SCHEMA, render_prompt
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
            f"TODO: regen with adapter. Placeholder wrapper for "
            f"{symbol.qualname} ({symbol.kind})."
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


def _should_skip(
    symbol: SymbolMeta,
    generated_dir: Path,
    feedback_by_tool: dict[str, list[dict[str, Any]]],
    *,
    force: bool,
    dry_run: bool,
) -> bool:
    """True when nothing changed and there's no pending feedback to address."""
    if force:
        return False
    existing = _existing_sha(generated_dir, symbol)
    if existing is None:
        return False  # no committed file yet
    if existing != symbol.source_sha256:
        return False  # PNL source changed
    if feedback_by_tool.get(tool_name_for(symbol)):
        return False  # feedback is the whole reason to regen
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
        p.stem
        for p in generated_dir.iterdir()
        if p.suffix == ".py" and not p.name.startswith("__")
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


def _generate_one(
    symbol: SymbolMeta,
    feedback: list[dict[str, Any]],
    adapter: LLMAdapter | None,
    *,
    dry_run: bool,
) -> str:
    if dry_run or adapter is None:
        spec = _placeholder_spec(symbol)
    else:
        prompt = render_prompt(symbol, feedback)
        spec = adapter.generate(prompt, schema=TOOL_SPEC_SCHEMA)
    return render_module(symbol, spec, generated_by=_generated_by(adapter, dry_run))


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="psyneulink-mcp-generate",
        description=(
            "Regenerate the auto layer of psyneulink-mcp tools from "
            "PsyNeuLink's public API."
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
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

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
    print(
        f"[generate_tools] {len(selected)} of {len(symbols)} seed symbol(s) "
        f"selected; mode={mode}",
        file=sys.stderr,
    )

    successful_stems: list[str] = []
    skipped_stems: list[str] = []
    failures: list[tuple[str, str]] = []

    for symbol in selected:
        tool_feedback = feedback_by_tool.get(tool_name_for(symbol), [])
        if _should_skip(
            symbol,
            GENERATED_DIR,
            feedback_by_tool,
            force=args.force,
            dry_run=args.dry_run,
        ):
            skipped_stems.append(module_stem_for(symbol))
            continue
        try:
            body = _generate_one(symbol, tool_feedback, adapter, dry_run=args.dry_run)
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
