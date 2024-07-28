"""Tool."""
import abc
from dataclasses import dataclass
from typing import Any

from .state import State


@dataclass
class Tool(abc.ABC):
    """Abstract representation of a Tool."""

    name: str
    description: str
    params: dict

    @abc.abstractmethod
    def run(self, state: State, **kwargs: Any) -> Any:
        """Run the task."""
