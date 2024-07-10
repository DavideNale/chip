"""Task."""
import abc
from dataclasses import dataclass
from typing import Any

from .state import State


@dataclass
class Task(abc.ABC):
    """Abstract representation of a Task."""

    name: str
    description: str
    params: dict

    @abc.abstractmethod
    def run(self, state: State, **kwargs: Any) -> Any:  # noqa: ANN401
        """Run the task."""
