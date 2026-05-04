"""Build-time tool generator. Not imported by the runtime server.

Anything in this package may import an LLM adapter; nothing imported by
``psyneulink_mcp.server`` may. Keeping LLM dependencies off the runtime
path is a hard rule (see ``CLAUDE.md``).
"""
