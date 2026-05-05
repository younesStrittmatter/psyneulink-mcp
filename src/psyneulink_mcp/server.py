"""Entry point for the psyneulink-mcp server."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from .tools.curated import brainlike as curated_brainlike
from .tools.curated import composition as curated_composition
from .tools.curated import feedback as curated_feedback
from .tools.generated import register_all as register_generated

mcp = FastMCP("psyneulink-mcp")

curated_feedback.register(mcp)
curated_brainlike.register(mcp)
curated_composition.register(mcp)
register_generated(mcp)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
