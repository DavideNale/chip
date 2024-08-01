"""Chatbot."""
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .history import Message
from .state import State
from .tool import Tool


@dataclass
class ChatbotABC(ABC):
    """Abstract chatbot."""

    client: Any
    system_prompt: str
    initial_state: State
    logger: Optional[logging.Logger] = None
    debug: bool = False
    history: List[Message] = field(default_factory=list)
    tools: List[Tool] = field(default_factory=list)


    def __post_init__(self) -> None:  # noqa: D105
        self.state = self.initial_state
        self.add_message("system", self.system_prompt)
        self.tools = self.generate_tools()

        if self.logger is None:
            self.logger = self._setup_logger()

    @abstractmethod
    def complete(self, message: str) -> str:
        """Process user input and generate a response."""

    def add_message(self, role: str, content: str) -> None:
        """Add a message to the conversation history."""
        self.history.append(Message(role=role, content=content))

    def get_history(self) -> List[Message]:
        """Return the conversation history."""
        return self.history

    @abstractmethod
    def generate_tools(self) -> List[Tool]:
        """Generate tools configuration."""

    def _setup_logger(self) -> logging.Logger:
        """Set up and configure the logger."""
        logger = logging.getLogger(self.__class__.__name__)
        logger.setLevel(logging.DEBUG if self.debug else logging.INFO)
        return logger

    def log(self, level: int, message: str) -> None:
        """Log a message using the configured logger."""
        self.logger.log(level, message)
