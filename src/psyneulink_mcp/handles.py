"""In-process registry of live PsyNeuLink objects.

Generated tools that construct a non-JSON-serialisable PNL object (a
Mechanism, a Composition, a Function, a Projection) push the instance
into this registry and return a small ``HandleRef`` payload — a stable
string ID plus light metadata. Subsequent tool calls (e.g. ``add_node``,
``run_composition``, or even another generated constructor with a
``function=<handle>`` argument) take handle strings as inputs; the impl
walks its kwargs and rehydrates each handle into the live object before
calling into PNL.

The registry is **process-scoped**: a fresh MCP subprocess starts with
an empty dict, and entries live until the process dies. Each
``psyneulink-agent --chat`` session spawns its own MCP, which matches
the natural "modeling session" lifecycle. We deliberately do not
persist handles or share them across sessions — the moment we'd need
that, the right move is real PNL serialisation, not a pickle of opaque
strings.
"""

from __future__ import annotations

import copy
import re
import uuid
import warnings
from dataclasses import dataclass, field
from typing import Any, Literal

HANDLE_PREFIX = "h_"
HANDLE_PATTERN = re.compile(r"^h_[0-9a-f]{12}$")

_HANDLES: dict[str, Any] = {}

# ---- Composition revision counter ----------------------------------------- #
#
# The UI's graph pane needs a cheap way to ask "did this composition change
# since I last rendered it?". Re-rendering a graph means shelling out to
# graphviz, which is way more expensive than checking an int. So we keep a
# per-handle integer counter that the curated composition-mutating tools
# (``add_node``, ``add_linear_pathway``, ``add_projection``) bump after the
# underlying mutation succeeds. Running a composition is *not* a mutation in
# the topology sense — ``run_composition`` does not bump.
#
# The counter is process-scoped, like ``_HANDLES`` and the journal.

_COMPOSITION_REVISION: dict[str, int] = {}


def get_revision(handle: str) -> int:
    """Current revision of a composition handle (0 if never bumped)."""
    return _COMPOSITION_REVISION.get(handle, 0)


def bump_revision(handle: str) -> int:
    """Increment the revision counter for ``handle`` and return the new value.

    Used by composition-mutating curated tools so that the UI's graph pane
    can cheaply detect "this composition changed, re-render". No-op (returns
    0) if the handle isn't currently registered — prevents stray bumps from
    leaking into the dict.
    """
    if handle not in _HANDLES:
        return 0
    _COMPOSITION_REVISION[handle] = _COMPOSITION_REVISION.get(handle, 0) + 1
    return _COMPOSITION_REVISION[handle]


# ---- Session journal ------------------------------------------------------- #
#
# Every generated tool's ``_impl`` and every composition-mutating curated tool
# appends a ``JournalEntry`` here. ``persistence.export_python_script`` walks
# the journal to render a runnable ``.py`` script that reproduces the model
# built in this session; ``persistence.load_python_script`` replays it.
#
# The journal is process-scoped, just like ``_HANDLES``. It is intentionally
# *not* persisted: when the MCP subprocess dies, so does the journal.

ToolLayer = Literal["generated", "curated"]


@dataclass
class JournalEntry:
    """One recorded tool call.

    ``args`` preserves handle strings verbatim (i.e. it is the PRE-resolved
    kwargs dict the tool was called with). ``result_handle`` is the handle
    string the tool returned, or ``None`` for tools that don't produce one
    (``run_composition``, JSON-serialisable returns, etc.). ``tool_layer``
    distinguishes generated wrappers from curated tools so the script
    renderer knows which call site to emit.
    """

    tool_name: str
    args: dict[str, Any]
    result_handle: str | None = None
    tool_layer: ToolLayer = "generated"
    extras: dict[str, Any] = field(default_factory=dict)


_JOURNAL: list[JournalEntry] = []
_JOURNAL_CAP = 5000
_JOURNAL_CAP_WARNED = False


def is_handle_string(value: Any) -> bool:
    """True iff *value* looks like a registered handle ID."""
    return isinstance(value, str) and HANDLE_PATTERN.match(value) is not None


def _handle_payload(handle: str, obj: Any) -> dict[str, Any]:
    return {
        "handle": handle,
        "type": type(obj).__name__,
        "name": getattr(obj, "name", None) or "",
        "repr": repr(obj),
    }


def register_handle(obj: Any) -> dict[str, Any]:
    """Stash *obj* and return its handle payload.

    ``None`` and primitives that round-trip through JSON are returned
    as-is; the agent should never see a handle for something it could
    just read directly.
    """
    if obj is None:
        return None  # type: ignore[return-value]
    handle = HANDLE_PREFIX + uuid.uuid4().hex[:12]
    _HANDLES[handle] = obj
    return _handle_payload(handle, obj)


def resolve_handle(handle: str) -> Any:
    """Return the live object for *handle*, raising on miss."""
    try:
        return _HANDLES[handle]
    except KeyError as exc:
        raise KeyError(
            f"unknown handle: {handle!r}. "
            "Either it was never created in this session or the MCP "
            "subprocess restarted and lost in-memory state."
        ) from exc


_CLASS_NAME_KEYS: frozenset[str] = frozenset(
    {
        # Most generated PNL constructors take a function-type parameter
        # whose value the JSON schema describes as "name of the X
        # function class". The agent obediently passes a string like
        # ``"Linear"``; PNL then calls ``issubclass(value, Function)``
        # and dies with ``TypeError: issubclass() arg 1 must be a
        # class``. We resolve those strings to the underlying ``pnl.X``
        # class before they reach PNL. Listed by key name (not by
        # *value*) so naming a mechanism literally ``"Linear"`` doesn't
        # accidentally promote the name to a class object.
        "function",
        "integrator_function",
        "combine_function",
        "combination_function",
        "aggregation_function",
        "objective_function",
        "output_function",
        "transfer_function",
        "noise_function",
        "selection_function",
        "exponent",
        "termination_measure",
    }
)


def _maybe_resolve_class_name(key: str, value: Any) -> Any:
    """If *key* is a class-name carrier and *value* is a ``pnl.<value>``
    class name, return the class object. Otherwise return *value*.
    """
    if key not in _CLASS_NAME_KEYS:
        return value
    if not isinstance(value, str) or not value:
        return value
    if not value[0].isupper():
        return value
    try:
        import inspect

        import psyneulink as pnl
    except Exception:
        return value
    candidate = getattr(pnl, value, None)
    if candidate is not None and inspect.isclass(candidate):
        return candidate
    return value


def resolve_in(value: Any, *, _parent_key: str | None = None) -> Any:
    """Walk *value* recursively, swapping handle strings for live objects.

    Used by every generated tool's ``_impl`` so an agent can pass a
    previously-returned handle anywhere a PNL constructor expects an
    object: ``create_transfer_mechanism(args={"function": "h_abc..."})``
    just works.

    Also resolves bare class-name strings under known function-type keys
    (e.g. ``{"function": "Linear"}`` → ``pnl.Linear``). The MCP's
    JSON-schema-only contract with the LLM means tool descriptions
    advertise these as strings; PNL itself wants the actual class.
    """
    if is_handle_string(value):
        return resolve_handle(value)
    # Class-name resolution is keyed by parent dict key, so apply it
    # only when descending from a dict — never to the top-level call.
    if _parent_key is not None and isinstance(value, str):
        return _maybe_resolve_class_name(_parent_key, value)
    if isinstance(value, list):
        return [resolve_in(item) for item in value]
    if isinstance(value, tuple):
        return tuple(resolve_in(item) for item in value)
    if isinstance(value, dict):
        return {
            key: resolve_in(item, _parent_key=key)
            for key, item in value.items()
        }
    return value


def list_handles() -> list[dict[str, Any]]:
    """Snapshot of every handle currently alive in this MCP process."""
    return [_handle_payload(handle, obj) for handle, obj in _HANDLES.items()]


def describe_handle(handle: str) -> dict[str, Any]:
    """Single-handle view (errors if unknown)."""
    return _handle_payload(handle, resolve_handle(handle))


def record_call(
    tool_name: str,
    args: dict[str, Any],
    result_handle: str | None = None,
    tool_layer: ToolLayer = "generated",
) -> None:
    """Append one ``JournalEntry`` to the per-process session journal.

    ``args`` is **deep-copied** so that any subsequent in-place mutation by
    the caller (e.g. ``handles.resolve_in`` swapping handle strings for live
    objects on the same dict) cannot corrupt the journal. The dict that
    lands in the journal therefore preserves handle strings as the agent
    originally passed them — exactly what ``export_python_script`` needs.

    When the journal exceeds ``_JOURNAL_CAP``, a one-shot ``UserWarning``
    fires (subsequent overflows stay silent) so a runaway session is
    visible but doesn't drown the operator in noise.
    """
    global _JOURNAL_CAP_WARNED
    try:
        snapshot_args = copy.deepcopy(args) if args else {}
    except Exception:
        snapshot_args = dict(args) if args else {}
    _JOURNAL.append(
        JournalEntry(
            tool_name=tool_name,
            args=snapshot_args,
            result_handle=result_handle,
            tool_layer=tool_layer,
        )
    )
    if len(_JOURNAL) > _JOURNAL_CAP and not _JOURNAL_CAP_WARNED:
        _JOURNAL_CAP_WARNED = True
        warnings.warn(
            f"psyneulink-mcp session journal exceeded {_JOURNAL_CAP} entries; "
            "exported scripts may grow large. Consider clearing handles "
            "between modeling sessions.",
            stacklevel=2,
        )


def journal_snapshot() -> list[JournalEntry]:
    """Return a list copy of the current journal (mutating it is safe)."""
    return list(_JOURNAL)


def clear_journal() -> int:
    """Drop the session journal; returns count cleared."""
    global _JOURNAL_CAP_WARNED
    n = len(_JOURNAL)
    _JOURNAL.clear()
    _JOURNAL_CAP_WARNED = False
    return n


def clear_handles() -> int:
    """Drop everything; primarily for tests. Returns count of handles cleared.

    Also clears the session journal and the composition-revision counter as
    side-effects — callers that need to distinguish the counts can call
    :func:`clear_journal` first, or inspect ``len(journal_snapshot())``
    before calling.
    """
    n = len(_HANDLES)
    _HANDLES.clear()
    _COMPOSITION_REVISION.clear()
    clear_journal()
    return n
