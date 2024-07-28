"""History."""

from dataclasses import dataclass


@dataclass(kw_only=True)
class Message:
    """Repersentation of a chat message."""

    role: str
    content: str

