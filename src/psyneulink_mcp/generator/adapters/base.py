"""LLM adapter contract.

Every adapter takes a single user-prompt string + the JSON Schema for
:data:`ToolSpec` and returns a :data:`ToolSpec` validated against that
schema. Nothing here imports an LLM SDK or shells out — those concerns
live in the per-adapter modules.
"""

from __future__ import annotations

from typing import Any, Protocol, TypedDict


class ToolSpec(TypedDict):
    """What the LLM returns for one PNL symbol.

    The host system wraps this metadata into a generated Python module
    that registers a single MCP tool. The LLM only emits the metadata —
    the implementation body comes from a fixed template.

    Attributes:
        description: WHEN-to-call focused summary for an LLM consumer.
        parameters: JSON Schema describing the tool's arguments.
        notes: Free-form caveats / known gotchas. May be the empty string.
    """

    description: str
    parameters: dict[str, Any]
    notes: str


class LLMAdapter(Protocol):
    """Adapter Protocol. Implementations must validate against ``schema``."""

    name: str

    def generate(self, prompt: str, *, schema: dict[str, Any]) -> ToolSpec:
        """Call the LLM and return a schema-validated :class:`ToolSpec`.

        Raises:
            AdapterError: on missing dependency, non-zero exit, network
                failure, malformed response, or schema mismatch.
        """
        ...


def validate_tool_spec(spec: Any, schema: dict[str, Any]) -> None:
    """Lightweight ToolSpec validation.

    Both adapters get structural validation for free from their backend
    (``--json-schema`` for the CLI, tool-use ``input_schema`` for the
    API). This helper catches the residual cases — empty / wrong-typed
    fields — without pulling in a JSON-Schema library.

    Raises:
        AdapterError: if ``spec`` is missing a required key, is not a
            mapping, or has the wrong type for a known field.
    """
    from . import AdapterError

    if not isinstance(spec, dict):
        raise AdapterError(
            f"ToolSpec must be a JSON object, got {type(spec).__name__}"
        )
    for key in schema.get("required", []):
        if key not in spec:
            raise AdapterError(f"ToolSpec missing required field {key!r}")

    if not isinstance(spec.get("description", ""), str):
        raise AdapterError("ToolSpec.description must be a string")
    if not isinstance(spec.get("parameters", {}), dict):
        raise AdapterError("ToolSpec.parameters must be a JSON object")
    if not isinstance(spec.get("notes", ""), str):
        raise AdapterError("ToolSpec.notes must be a string")
