"""Curated tool: lazy-expansion lookup for full tool descriptions.

The 354 generated tools are registered with their *prose lead only*
to keep the ``tools/list`` payload small (see
:mod:`psyneulink_mcp.tool_descriptions` for why). Agents that already
know the tool from the compact listing can call
``describe_psyneulink_tool(name)`` to retrieve the full description —
including the JSON-Schema parameter block and the ``Notes:`` section
the generator wrote.

Pattern for the agent:

1. Read the compact ``tools/list`` to identify a candidate tool.
2. Call ``describe_psyneulink_tool("create_transfer_mechanism")``.
3. Use the returned schema to construct the actual call.

Step 2 is one extra round-trip per *new* tool the agent uses, but the
returned description lives in the agent's own context for the rest of
the conversation, so subsequent calls of the same tool don't repeat
it. Net win: ~258K → ~50K tokens for the up-front tool listing.
"""

from __future__ import annotations

from typing import Any

from ...feedback import captured_tool
from ...tool_descriptions import (
    known_tool_names,
    lookup_full_description,
    lookup_parameters,
    resolve_hierarchy,
)


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="curated")
    def describe_psyneulink_tool(name: str) -> dict[str, Any]:
        """Return the full description + schema + parent classes for a tool.

        WHEN TO CALL: after the compact ``tools/list`` entry tells you
        a tool *might* be the right one but you need the parameter
        names/types, the ``Notes:`` warnings, or the inheritance chain
        before constructing the call. The compact entry intentionally
        omits all three to keep the listing small.

        ``inherits_from`` walks PsyNeuLink's actual class MRO. Each entry
        is ``{"class": <pnl class name>, "qualname": <pkg.qualname>,
        "tool": <create_…> | None}``. When ``tool`` is non-null, it
        names a sibling tool you can drill into with another
        ``describe_psyneulink_tool`` call — that's how you get the
        parent's parameter set without it being repeated in the child's
        description.

        Args:
            name: The tool name as it appears in ``tools/list`` (e.g.
                ``"create_transfer_mechanism"``).

        Returns:
            ``{"name", "description", "parameters", "inherits_from",
            "found"}``. If the tool is unknown, ``found`` is ``False``
            and ``description`` contains a hint with closest-matching
            names. ``inherits_from`` is ``[]`` for non-class tools and
            for tools whose PNL symbol can't be resolved.
        """
        full = lookup_full_description(name)
        if full is None:
            # Don't paginate — 354 names is a lot, but a one-shot dump
            # of the closest matches is more useful than nothing.
            all_names = known_tool_names()
            suggestions = [n for n in all_names if name.lower() in n.lower()][:10]
            hint = (
                f"unknown tool {name!r}. "
                + (
                    f"Did you mean: {', '.join(suggestions)}?"
                    if suggestions
                    else f"Total registered tools: {len(all_names)}."
                )
            )
            return {
                "name": name,
                "description": hint,
                "parameters": None,
                "inherits_from": [],
                "found": False,
            }
        return {
            "name": name,
            "description": full,
            "parameters": lookup_parameters(name),
            "inherits_from": resolve_hierarchy(name),
            "found": True,
        }

    @captured_tool(mcp, layer="curated")
    def list_psyneulink_tools(filter: str | None = None) -> dict[str, Any]:
        """Return every registered tool name, optionally filtered.

        WHEN TO CALL: when the standard ``tools/list`` returned nothing
        matching what you want and you suspect the tool exists under a
        different name. ``filter`` is a simple case-insensitive
        substring match (e.g. ``"control"`` returns
        ``create_control_mechanism``, ``create_lc_control_mechanism``,
        ``create_optimization_control_mechanism``, ...).

        Args:
            filter: Optional case-insensitive substring filter.

        Returns:
            ``{"count": int, "names": list[str]}``.
        """
        names = known_tool_names()
        if filter:
            needle = filter.lower()
            names = [n for n in names if needle in n.lower()]
        return {"count": len(names), "names": names}
