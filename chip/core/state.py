"""The internal state of the chatbot."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Union

Key = Union[str, int]


@dataclass
class State:
    """Represents the chat state."""

    _store: dict[str, Any] = field(default_factory=dict, init=False, repr=False)

    def __str__(self) -> str:
        """Represetation of the state as a string."""

    def __getitem__(self, key: Key) -> Any:
        """Return the state value with the given key."""
        key = str(key)

    def __setitem__(self, key: Key, value: Any) -> None:
        """Set the value of the given key."""
        key = str(key)

    def __delitem__(self, key: Key) -> None:
        """Delete the value with the given key."""
        key = str(key)

    def to_dict(self) -> dict[str, Any]:
        """Return a dict represenation of the state."""

