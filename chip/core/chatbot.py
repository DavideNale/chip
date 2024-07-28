"""Chatbot."""
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List

from .history import Message
from .state import State
from .tool import Tool


@dataclass
class ChatbotABC(ABC):
    """Abstract chatbot."""

    client: Any
    prompt: str
    state: State
    tools: List[Tool] = field(default_factory=list)
    history: List[Message] = field(default_factory=list)
    logger: logging.Logger = None
    debug: bool = False

    @abstractmethod
    def complete(self, message: str) -> str:
        """Process user input."""

    @abstractmethod
    def add_message(self, role: str, content: str) -> None:
        """Add message to the history."""
        message = Message(role=role,content=content)
        self.history.append(message)

    @abstractmethod
    def get_history(self) -> list:
        """Return message history."""
        return self.history

    def __post_init__(self) -> None:  # noqa: D105
        self.add_message("system", self.prompt)
        self.tools = self._generate_tools()


def generate_tools() -> List[Dict[str, Any]]:
    """Generate tools configuration from tasks."""
