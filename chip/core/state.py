"""The internal state of the chatbot."""

from dataclasses import asdict, dataclass


@dataclass(kw_only=True)
class State:
    """Represents the chat state."""

    def to_dict(self) -> dict:
        """Return a dictionary mapping of the class fields."""
        return asdict(self)
