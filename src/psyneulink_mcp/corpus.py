"""Read-only access to `psyneulink-corpus` over the `gh` CLI.

This module is the only place where the MCP touches the corpus repo. It
fetches community brainlike YAMLs and open `feedback`-labeled issues, plus
exposes a write helper that the *generator* (not the server) uses to mark
issues as consumed after a successful regen.

Hard rules (mirror `CLAUDE.md §Separation of concerns`):

* The MCP server itself never writes to the corpus. Only
  `scripts/generate_tools.py` may call `mark_issues_consumed`.
* If `gh` is missing or unauthenticated, raise `CorpusUnavailable`. Callers
  must degrade gracefully — the server must not crash because GitHub is down.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

import yaml

CORPUS_REPO_DEFAULT = "younesStrittmatter/psyneulink-corpus"
CORPUS_REF_DEFAULT = "main"

ENV_CORPUS_REPO = "PSYNEULINK_MCP_CORPUS_REPO"
ENV_CORPUS_REF = "PSYNEULINK_MCP_CORPUS_REF"
ENV_CORPUS_CACHE = "PSYNEULINK_MCP_CORPUS_CACHE"

BRAINLIKE_DIR = "community/brainlike"
SCHEMA_FILENAME = "_schema.yaml"
FEEDBACK_LABEL = "feedback"
CONSUMED_LABEL = "consumed"

CACHE_TTL_SECONDS = 60 * 60  # 1 hour


class CorpusUnavailable(RuntimeError):
    """Raised when the corpus repo cannot be reached.

    Reasons: `gh` not installed, not authenticated, network failure, repo
    missing, or any non-zero exit from a `gh` invocation. The message
    explains which.
    """


# --------------------------------------------------------------------------- #
# config helpers                                                              #
# --------------------------------------------------------------------------- #


def corpus_repo() -> str:
    """`owner/name` of the corpus repo. Override via $PSYNEULINK_MCP_CORPUS_REPO."""
    return os.environ.get(ENV_CORPUS_REPO, CORPUS_REPO_DEFAULT)


def corpus_ref() -> str:
    """Branch / tag / sha to read from. Override via $PSYNEULINK_MCP_CORPUS_REF."""
    return os.environ.get(ENV_CORPUS_REF, CORPUS_REF_DEFAULT)


def cache_dir() -> Path:
    """Local cache root. Override via $PSYNEULINK_MCP_CORPUS_CACHE."""
    override = os.environ.get(ENV_CORPUS_CACHE)
    if override:
        return Path(override)
    return Path.home() / ".cache" / "psyneulink-mcp"


# --------------------------------------------------------------------------- #
# subprocess seam                                                             #
# --------------------------------------------------------------------------- #


def _run_gh(args: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    """Run a `gh ...` invocation. Raises CorpusUnavailable on missing/failed."""
    if shutil.which("gh") is None:
        raise CorpusUnavailable(
            "`gh` CLI not found on PATH. Install it from https://cli.github.com/ "
            "and run `gh auth login`."
        )
    try:
        result = subprocess.run(
            ["gh", *args],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError as e:
        raise CorpusUnavailable(f"`gh` invocation failed: {e}") from e

    if check and result.returncode != 0:
        stderr = (result.stderr or "").strip()
        if "authentication" in stderr.lower() or "not logged in" in stderr.lower():
            raise CorpusUnavailable(
                "`gh` is not authenticated. Run `gh auth login` and retry. "
                f"Detail: {stderr}"
            )
        raise CorpusUnavailable(
            f"`gh {' '.join(args)}` exited {result.returncode}: {stderr}"
        )
    return result


# --------------------------------------------------------------------------- #
# brainlike views                                                             #
# --------------------------------------------------------------------------- #


def _brainlike_cache_file() -> Path:
    """Cache key includes repo + ref so switching either invalidates the cache."""
    repo_slug = corpus_repo().replace("/", "__")
    return cache_dir() / "brainlike" / f"{repo_slug}@{corpus_ref()}.json"


def _cache_is_fresh(path: Path, ttl: int = CACHE_TTL_SECONDS) -> bool:
    if not path.exists():
        return False
    return (time.time() - path.stat().st_mtime) < ttl


def _list_brainlike_yaml_paths() -> list[str]:
    """Recursive tree listing, filtered to YAMLs under community/brainlike/.

    Excludes the schema file and any dotfiles.
    """
    repo, ref = corpus_repo(), corpus_ref()
    result = _run_gh(
        ["api", f"repos/{repo}/git/trees/{ref}?recursive=1"]
    )
    try:
        tree = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        raise CorpusUnavailable(f"Could not parse tree response: {e}") from e

    paths: list[str] = []
    for entry in tree.get("tree", []):
        if entry.get("type") != "blob":
            continue
        path = entry.get("path", "")
        if not path.startswith(f"{BRAINLIKE_DIR}/"):
            continue
        name = path.rsplit("/", 1)[-1]
        if name == SCHEMA_FILENAME or name.startswith("."):
            continue
        if not (name.endswith(".yaml") or name.endswith(".yml")):
            continue
        paths.append(path)
    return paths


def _fetch_raw_file(path: str) -> str:
    """Fetch a single file's raw contents at the configured ref."""
    repo, ref = corpus_repo(), corpus_ref()
    result = _run_gh(
        [
            "api",
            "-H",
            "Accept: application/vnd.github.raw",
            f"repos/{repo}/contents/{path}?ref={ref}",
        ]
    )
    return result.stdout


def fetch_brainlike_views(force: bool = False) -> list[dict[str, Any]]:
    """Pull `community/brainlike/**/*.yaml` from the corpus repo.

    Caches the parsed list locally for 1 h. Set `force=True` to bypass.

    Each returned dict is the YAML payload with two extra fields:

    * ``__source_path__`` — relative path within the corpus repo.
    * ``__source_repo__`` — ``owner/name@ref`` of the source.

    Returns an empty list if the corpus has no brainlike entries yet.
    Raises ``CorpusUnavailable`` if the corpus cannot be reached.
    """
    cache_file = _brainlike_cache_file()
    if not force and _cache_is_fresh(cache_file):
        try:
            return json.loads(cache_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass  # fall through to a fresh fetch

    paths = _list_brainlike_yaml_paths()
    repo, ref = corpus_repo(), corpus_ref()
    views: list[dict[str, Any]] = []
    for p in paths:
        raw = _fetch_raw_file(p)
        try:
            doc = yaml.safe_load(raw)
        except yaml.YAMLError as e:
            print(
                f"[corpus] skipping malformed YAML {p}: {e}",
                file=sys.stderr,
            )
            continue
        if doc is None:
            continue
        if not isinstance(doc, dict):
            print(
                f"[corpus] skipping non-mapping YAML {p} (got {type(doc).__name__})",
                file=sys.stderr,
            )
            continue
        doc["__source_path__"] = p
        doc["__source_repo__"] = f"{repo}@{ref}"
        views.append(doc)

    try:
        cache_file.parent.mkdir(parents=True, exist_ok=True)
        cache_file.write_text(json.dumps(views), encoding="utf-8")
    except OSError as e:
        print(f"[corpus] could not write cache {cache_file}: {e}", file=sys.stderr)

    return views


# --------------------------------------------------------------------------- #
# feedback issues                                                             #
# --------------------------------------------------------------------------- #


# Issue forms (`.github/ISSUE_TEMPLATE/tool_feedback.yml`) render each field
# as `### <Label>\n\n<value>\n\n`. We extract the canonical fields here so
# the generator gets the same envelope shape as local JSONL entries.
_FORM_FIELD_RE = re.compile(
    r"^###\s+(?P<label>[^\n]+?)\s*\n+(?P<value>(?:(?!^###\s).)+)",
    re.MULTILINE | re.DOTALL,
)

_LABEL_TO_KEY = {
    "tool name": "tool_name",
    "issue type": "issue_type",
    "description": "description",
    "suggested fix": "suggested_fix",
    "agent context": "agent_context",
}


def _parse_issue_body(body: str) -> dict[str, str]:
    """Best-effort extraction of `tool_feedback` form fields from issue body."""
    fields: dict[str, str] = {}
    for m in _FORM_FIELD_RE.finditer(body or ""):
        label = m.group("label").strip().lower()
        value = m.group("value").strip()
        if value in {"_No response_", "*No response*"}:
            value = ""
        key = _LABEL_TO_KEY.get(label)
        if key:
            fields[key] = value
    return fields


def _issue_to_envelope(issue: dict[str, Any]) -> dict[str, Any]:
    body = issue.get("body") or ""
    parsed = _parse_issue_body(body)

    tool_name = parsed.get("tool_name") or "unknown"
    issue_type = parsed.get("issue_type") or "other"

    author = (issue.get("author") or {}).get("login")
    labels = [label.get("name") for label in issue.get("labels") or [] if label.get("name")]

    return {
        "timestamp": issue.get("createdAt") or "",
        "source": "human-github",
        "tool_name": tool_name,
        "tool_layer": "generated",  # humans rarely distinguish; default to generated
        "pnl_version": "unknown",
        "server_version": "unknown",
        "payload": {
            "issue_number": issue.get("number"),
            "issue_url": issue.get("url"),
            "title": issue.get("title") or "",
            "body": body,
            "issue_type": issue_type,
            "description": parsed.get("description") or body,
            "suggested_fix": parsed.get("suggested_fix") or None,
            "agent_context": parsed.get("agent_context") or None,
            "author": author,
            "labels": labels,
        },
    }


def fetch_pending_feedback_issues() -> list[dict[str, Any]]:
    """Open issues on the corpus repo with the `feedback` label, but not yet
    `consumed`, mapped into the same envelope shape as local JSONL entries.

    Raises ``CorpusUnavailable`` on auth/network failure.
    """
    repo = corpus_repo()
    result = _run_gh(
        [
            "issue",
            "list",
            "--repo",
            repo,
            "--label",
            FEEDBACK_LABEL,
            "--state",
            "open",
            "--json",
            "number,url,title,body,labels,author,createdAt",
            "--limit",
            "500",
        ]
    )
    try:
        issues = json.loads(result.stdout or "[]")
    except json.JSONDecodeError as e:
        raise CorpusUnavailable(f"Could not parse `gh issue list` output: {e}") from e

    envelopes: list[dict[str, Any]] = []
    for issue in issues:
        labels = {label.get("name") for label in issue.get("labels") or []}
        if CONSUMED_LABEL in labels:
            continue  # already pulled into a previous regen
        envelopes.append(_issue_to_envelope(issue))
    return envelopes


# --------------------------------------------------------------------------- #
# write path (generator-only)                                                 #
# --------------------------------------------------------------------------- #


def mark_issues_consumed(issue_numbers: list[int], regen_sha: str) -> list[int]:
    """Comment + label `consumed` on each issue.

    Called only by `scripts/generate_tools.py` after a successful regen.
    Never called from server code (the server is read-only on the corpus).

    Returns the list of issue numbers successfully marked. Failures for
    individual issues are logged to stderr but do not abort the loop, so a
    transient GitHub error on one comment does not block the others.
    """
    repo = corpus_repo()
    succeeded: list[int] = []
    for n in issue_numbers:
        try:
            _run_gh(
                [
                    "issue",
                    "comment",
                    str(n),
                    "--repo",
                    repo,
                    "--body",
                    f"consumed in regen {regen_sha}",
                ]
            )
            _run_gh(
                [
                    "issue",
                    "edit",
                    str(n),
                    "--repo",
                    repo,
                    "--add-label",
                    CONSUMED_LABEL,
                ]
            )
            succeeded.append(n)
        except CorpusUnavailable as e:
            print(
                f"[corpus] could not mark issue #{n} consumed: {e}",
                file=sys.stderr,
            )
    return succeeded
