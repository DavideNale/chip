"""core.state provides the State class. It represents the state of a chat session.

The State class acts as a wrapper around a dictionary, providing a convenient interface
for storing, retrieving, and manipulating chat state data. It includes methods for
accessing, modifying, and deleting state entries, as well as converting the state to
a dictionary representation.
"""

from __future__ import annotations  # noqa: I001

from dataclasses import dataclass, field
from typing import Any, Union, KeysView, ValuesView, ItemsView

Key = Union[str, int]


@dataclass
class State:
    """Represents the current state of a chat session."""

    _store: dict[str, Any] = field(default_factory=dict, init=False, repr=False)

    def __str__(self) -> str:
        """Return a string representation of the state."""
        items = ", ".join(f"{k}={v!r}" for k, v in self._store.items())
        return f"State({items})"

    def __getitem__(self, key: Key) -> Any:
        """Retrieve the value associated with the given key."""
        return self._store[str(key)]

    def __setitem__(self, key: Key, value: Any) -> None:
        """Set the value for the given key in the state."""
        self._store[str(key)] = value

    def __delitem__(self, key: Key) -> None:
        """Delete the entry with the given key from the state."""
        del self._store[str(key)]

    def to_dict(self) -> dict[str, Any]:
        """Convert the state to a dictionary."""
        return self._store.copy()

    def __contains__(self, key: Key) -> bool:
        """Check if the given key exists in the state."""
        return str(key) in self._store

    def get(self, key: Key, default: Any = None) -> Any:
        """Get the value for the given key or a default value if the key doesn't exist."""
        return self._store.get(str(key), default)

    def clear(self) -> None:
        """Remove all items from the state."""
        self._store.clear()

    def keys(self) -> KeysView[str]:
        """Return a view of the state's keys."""
        return self._store.keys()

    def values(self) -> ValuesView[Any]:
        """Return a view of the state's values."""
        return self._store.values()

    def items(self) -> ItemsView[str, Any]:
        """Return a view of the state's items (key-value pairs)."""
        return self._store.items()
