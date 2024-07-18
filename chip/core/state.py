"""The internal state of the chatbot."""

from dataclasses import dataclass, field
from typing import Any, Dict, Union

Key = Union[str, int]

@dataclass(kw_only=True, eq=False, order=False)
class State:
    """Represents the chat state."""

    _store: Dict[str, Any] = field(default_factory=dict, init=False, repr=False)

    def __str__(self) -> str:
        """Represetation of the state as a string."""

    def __getitem__(self, key: Key) -> Any:  # noqa: ANN401
        """Return the state value with the given key."""
        key = str(key)

    def __setitem__(self, key: Key, value: Any) -> None:  # noqa: ANN401
        """Set the value of the given key."""
        key = str(key)

    def __delitem__(self, key: Key) -> None:
        """Delete the value with the given key."""
        key = str(key)

    def to_dict(self) -> Dict[str, Any]:
        """Return a dict represenation of the state."""

