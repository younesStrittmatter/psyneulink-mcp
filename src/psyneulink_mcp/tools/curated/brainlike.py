"""Curated brainlike tools.

Two surfaces:

* ``get_community_brainlike_views`` — fetch the community-curated YAMLs
  from `psyneulink-corpus`. Read-only; cached.
* ``get_my_brainlike_view`` — read the user's personal brainlike profile
  from a local YAML file. Read-only; the MCP never writes here.

Mutation lives outside the server (PRs to the corpus repo for community
entries; user editing their own file for the personal profile).
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml

from ... import corpus
from ...feedback import captured_tool

ENV_PERSONAL_PROFILE = "PSYNEULINK_MCP_PERSONAL_PROFILE"


def _personal_profile_path() -> Path:
    """User's personal brainlike profile location.

    Resolution order:

    1. ``$PSYNEULINK_MCP_PERSONAL_PROFILE`` if set (absolute or ~-expandable).
    2. ``$XDG_CONFIG_HOME/psyneulink-mcp/me.yaml`` if XDG_CONFIG_HOME is set.
    3. ``~/.config/psyneulink-mcp/me.yaml`` (XDG-style default).
    """
    override = os.environ.get(ENV_PERSONAL_PROFILE)
    if override:
        return Path(override).expanduser()
    xdg = os.environ.get("XDG_CONFIG_HOME")
    base = Path(xdg).expanduser() if xdg else Path.home() / ".config"
    return base / "psyneulink-mcp" / "me.yaml"


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="curated")
    def get_community_brainlike_views() -> dict[str, Any]:
        """Return the community-curated list of brainlike definitions.

        WHEN TO CALL: when you need to know what the community considers
        "brainlike" — to compare against the user's personal preferences,
        to pick canonical examples to show, or to ground a modeling
        recommendation in shared definitions. Read-only.

        DO NOT CALL repeatedly within a single turn — the result is stable
        for ~1 hour (cached). Calling once and reusing is correct.

        To propose a new entry: the user files a PR on the
        ``psyneulink-corpus`` repo. This tool cannot write.

        Returns:
            ``{"views": [...], "source": "owner/name@ref", "count": N}``
            on success.

            On corpus unavailability (no ``gh``, not authenticated, network
            failure) returns ``{"views": [], "error": "...", "source": ...}``
            instead of raising — the agent can still proceed with the
            user's personal view alone.
        """
        try:
            views = corpus.fetch_brainlike_views()
        except corpus.CorpusUnavailable as e:
            return {
                "views": [],
                "count": 0,
                "source": f"{corpus.corpus_repo()}@{corpus.corpus_ref()}",
                "error": str(e),
            }
        return {
            "views": views,
            "count": len(views),
            "source": f"{corpus.corpus_repo()}@{corpus.corpus_ref()}",
        }

    @captured_tool(mcp, layer="curated")
    def get_my_brainlike_view() -> dict[str, Any]:
        """Return the user's personal brainlike preferences.

        WHEN TO CALL: when modeling, before consulting the community view,
        so the user's own definition takes precedence. Personal profile is
        the authoritative source for *this* user; community views are for
        comparison and grounding only.

        Reads from (in order of precedence):
          1. ``$PSYNEULINK_MCP_PERSONAL_PROFILE``
          2. ``$XDG_CONFIG_HOME/psyneulink-mcp/me.yaml``
          3. ``~/.config/psyneulink-mcp/me.yaml``

        Returns:
            ``{"view": <yaml mapping>, "source": "<absolute path>"}`` if a
            profile exists.

            ``{"view": {}, "source": "<path>", "configured": False}`` if no
            profile is configured. This is normal — most users won't have
            one. Treat the empty case as "no personal preferences expressed".

        The MCP cannot write here. To set or change the profile, the user
        edits the file with their own editor (see ``examples/me.yaml.example``).
        """
        path = _personal_profile_path()
        if not path.exists():
            return {"view": {}, "source": str(path), "configured": False}
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as e:
            return {
                "view": {},
                "source": str(path),
                "configured": True,
                "error": f"could not read profile: {e}",
            }
        if doc is None:
            return {"view": {}, "source": str(path), "configured": True}
        if not isinstance(doc, dict):
            return {
                "view": {},
                "source": str(path),
                "configured": True,
                "error": (
                    f"profile must be a YAML mapping at top level, got "
                    f"{type(doc).__name__}"
                ),
            }
        return {"view": doc, "source": str(path), "configured": True}
