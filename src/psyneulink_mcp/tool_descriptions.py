"""Compact-by-default tool descriptions + on-demand full-description lookup.

The generator emits every tool with a long ``TOOL_DESCRIPTION`` that
inlines the full JSON-Schema parameter block AND a trailing ``Notes:``
section so an LLM consumer reading ``tools/list`` sees the schema
without FastMCP being able to attach a real ``inputSchema`` to a
``args: dict`` wrapper. That tradeoff was acceptable when there were
~50 tools; with 354 generated tools it costs ~258K tokens just for
the listing, which blows past sonnet's 200K context window before
any conversation has even started.

This module solves that by *registering tools with the prose lead
only* and parking the full description in a side registry that the
``describe_psyneulink_tool`` curated tool reads. When the LLM needs
the schema to construct a call, it asks for it once. After that the
expanded description lives in the LLM's own context for the rest of
the conversation, but the up-front ``tools/list`` payload stays small.

This is purely a server-side change — the generated modules are not
touched. ``compact_description`` is a pure function over the existing
``TOOL_DESCRIPTION`` string, so it works on every already-rendered
tool without a regen.

Hierarchy lookup
----------------

``resolve_hierarchy`` reads PsyNeuLink's actual class MRO at runtime
using ``inspect.getmro`` and maps each parent class to the tool that
exposes it (via the ``create_<snake_case_name>`` naming convention).
This means the agent can drill from ``create_transfer_mechanism`` to
``create_processing_mechanism`` (its parent) without needing to know
PNL's class structure up front, and without us baking anything extra
into the generated modules. Since it's computed live from PNL's MRO,
it's automatically self-healing: a PsyNeuLink rename or refactor is
reflected on the next MCP startup with zero regen needed.
"""

from __future__ import annotations

import importlib
import inspect
import re
from typing import Any

# tool name → full description (the original TOOL_DESCRIPTION the
# generator wrote). Populated as each generated/curated tool is
# registered through ``feedback.captured_tool``.
_FULL_DESCRIPTIONS: dict[str, str] = {}

# tool name → JSON-serialisable parameter schema, when the calling
# module surfaced one. Today the schema is embedded inside the
# description text (see ``compact_description``); we still expose the
# raw structured form for callers that want it without re-parsing.
_TOOL_PARAMETERS: dict[str, dict[str, Any]] = {}

# tool name → __pnl_qualname__ (e.g. "psyneulink.…TransferMechanism") for
# class/function/method-kind tools. Populated alongside the description
# so ``resolve_hierarchy`` can walk PNL's MRO for class-kind tools.
_TOOL_QUALNAMES: dict[str, str] = {}

# tool name → __pnl_kind__ ("class" / "function" / "method"). Used to
# decide whether ``resolve_hierarchy`` even tries — only "class" has an
# inheritance chain worth surfacing to the agent.
_TOOL_KINDS: dict[str, str] = {}


def compact_description(full: str) -> str:
    """Return the prose lead of a generated tool description.

    Strips the embedded ``Parameters (JSON Schema):`` block and the
    trailing ``Notes:`` block — both are recoverable via
    ``describe_psyneulink_tool``. The result is a self-contained
    prose summary that explains *when* the LLM should reach for this
    tool, which is what ``tools/list`` actually needs.

    Pure function. Idempotent. A description that doesn't contain the
    schema marker is returned unchanged (so curated tools, which write
    short descriptions by hand, are unaffected).
    """
    if not full:
        return ""
    text = full
    # The generator's exact marker is "\n\nParameters (JSON Schema):".
    # Be lenient about leading newline count so future template tweaks
    # don't silently bypass the strip.
    for marker in (
        "\n\nParameters (JSON Schema):",
        "\nParameters (JSON Schema):",
        "Parameters (JSON Schema):",
    ):
        idx = text.find(marker)
        if idx != -1:
            text = text[:idx]
            break
    # Some tools may have a Notes block without a Parameters block.
    for marker in ("\n\nNotes:", "\nNotes:"):
        idx = text.find(marker)
        if idx != -1:
            text = text[:idx]
            break
    return text.strip()


def register_full_description(
    name: str,
    full: str,
    parameters: dict[str, Any] | None = None,
    qualname: str | None = None,
    kind: str | None = None,
) -> None:
    """Stash a tool's full description + PNL provenance for lookup.

    Called by ``feedback.captured_tool`` at registration time. Safe to
    call repeatedly — later registrations overwrite earlier ones, which
    is what we want when a regen produces a new description for the
    same tool name.

    ``qualname`` and ``kind`` come from the generated module's
    ``__pnl_qualname__`` / ``__pnl_kind__`` markers. They power the
    runtime hierarchy resolution in ``resolve_hierarchy`` — for
    class-kind tools we walk PNL's MRO and surface parent class names
    + their corresponding tools so the agent can drill the inheritance
    chain via repeated ``describe_psyneulink_tool`` calls.
    """
    if not name:
        return
    if full:
        _FULL_DESCRIPTIONS[name] = full
    if parameters is not None:
        _TOOL_PARAMETERS[name] = parameters
    if qualname:
        _TOOL_QUALNAMES[name] = qualname
    if kind:
        _TOOL_KINDS[name] = kind


def lookup_full_description(name: str) -> str | None:
    """Return the stashed full description for ``name``, or ``None``."""
    return _FULL_DESCRIPTIONS.get(name)


def lookup_parameters(name: str) -> dict[str, Any] | None:
    """Return the stashed JSON-Schema parameters for ``name``, or ``None``."""
    return _TOOL_PARAMETERS.get(name)


def lookup_qualname(name: str) -> str | None:
    """Return the stashed PNL qualname for ``name``, or ``None``."""
    return _TOOL_QUALNAMES.get(name)


def known_tool_names() -> list[str]:
    """Sorted list of tool names that have a stashed full description."""
    return sorted(_FULL_DESCRIPTIONS)


# Mirror of ``generator.template.snake_case`` so we can predict tool
# names from class names without importing the generator (which is a
# build-time-only module). Keep in lockstep with that file.
_SNAKE1 = re.compile(r"(.)([A-Z][a-z]+)")
_SNAKE2 = re.compile(r"([a-z0-9])([A-Z])")


def _snake_case(name: str) -> str:
    s = _SNAKE1.sub(r"\1_\2", name)
    s = _SNAKE2.sub(r"\1_\2", s).lower()
    s = re.sub(r"[^0-9a-z_]+", "_", s).strip("_")
    return s or "tool"


def _class_to_create_tool(class_short_name: str) -> str:
    """Predict the tool name a class would register under.

    Mirrors ``generator.template.tool_name_for(symbol)`` for class-kind
    symbols (always ``create_<snake>``). When that prediction matches a
    name in our description registry, the agent can drill into the
    parent's tool.
    """
    return f"create_{_snake_case(class_short_name)}"


def resolve_hierarchy(tool_name: str) -> list[dict[str, Any]]:
    """Return the parent-class chain for a class-kind tool, in MRO order.

    For each parent class that lives in the ``psyneulink`` package, we
    return ``{"class": <short_name>, "qualname": <pkg.qualname>,
    "tool": <create_…> | None}``. ``tool`` is the tool name when a
    matching tool is registered (so the agent knows it can drill into
    it via another ``describe_psyneulink_tool`` call); ``None`` when
    only the conceptual lineage is exposed (abstract base, not
    surfaced as its own tool).

    Returns ``[]`` for non-class tools, unknown tools, abstract bases
    that we can't import, and on any unexpected failure — the goal is
    to give the agent useful hierarchy info, not to crash the lookup
    when one parent in the chain misbehaves.
    """
    if _TOOL_KINDS.get(tool_name) != "class":
        return []
    qualname = _TOOL_QUALNAMES.get(tool_name)
    if not qualname or "." not in qualname:
        return []
    package_qualname, _, attr = qualname.rpartition(".")
    try:
        package = importlib.import_module(package_qualname)
        cls = getattr(package, attr, None)
    except (ImportError, AttributeError):
        return []
    if not inspect.isclass(cls):
        return []

    chain: list[dict[str, Any]] = []
    for parent in cls.__mro__[1:]:
        if parent is object:
            continue
        # Only surface PsyNeuLink-internal parents; mixing in framework
        # bases like Mapping or list isn't useful to the agent.
        parent_module = getattr(parent, "__module__", "") or ""
        if not parent_module.startswith("psyneulink"):
            continue
        parent_short = parent.__name__
        candidate_tool = _class_to_create_tool(parent_short)
        chain.append(
            {
                "class": parent_short,
                "qualname": f"{parent_module}.{parent_short}",
                "tool": candidate_tool if candidate_tool in _FULL_DESCRIPTIONS else None,
            }
        )
    return chain


__all__ = [
    "compact_description",
    "register_full_description",
    "lookup_full_description",
    "lookup_parameters",
    "lookup_qualname",
    "known_tool_names",
    "resolve_hierarchy",
]
