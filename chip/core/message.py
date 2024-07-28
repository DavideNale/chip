"""core.message provides the Message class.

The message class includes the role and content of a chat message.
It provides methods for creating, serializing, and deserializing messages,
as well as validating message roles.
"""

import json
from dataclasses import asdict, dataclass

VALID_ROLES = ["user", "system", "message"]


class InvalidRoleError(Exception):
    """Exception raised for invalid roles."""

    def __init__(self, role: str) -> None:
        """Initialize the InvalidRoleError."""
        super().__init__(f"{role} is not a supported role: user, system, assistant.")

class InvalidFormatError(Exception):
    """Exception raised if format is incorrect during deserialization."""

    def __init__(self) -> None:
        """Initialize the InvalidFormatError."""
        super().__init__("Dictionary must contain 'role' and 'content' keys")


@dataclass(kw_only=True, frozen=True)
class Message:
    """Representation of a chat message."""

    role: str
    content: str

    def __post_init__(self) -> None:
        """Validate the role after initialization."""
        if self.role not in VALID_ROLES:
            raise InvalidRoleError(self.role)

    @classmethod
    def user(cls, content: str) -> "Message":
        """Create a user message."""
        return Message(
            role="user",
            content=content,
        )

    @classmethod
    def system(cls, content: str) -> "Message":
        """Create a system message."""
        return Message(
            role="system",
            content=content,
        )

    @classmethod
    def assistant(cls, content: str) -> "Message":
        """Create an assistant message."""
        return Message(
            role="assistant",
            content=content,
        )

    def to_json(self) -> str:
        """Serialize the Message object to JSON."""
        return json.dumps(asdict(self))

    @classmethod
    def from_dict(cls, data: dict) -> "Message":
        """Create a Message instance from a dictionary."""
        if "role" not in data or "content" not in data:
            raise InvalidFormatError
        return cls(role=data["role"], content=data["content"])
