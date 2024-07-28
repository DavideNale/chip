"""Example usage of the chip package."""

from typing import List

import chip


@tool(description="...")
def set_x(state: State, value: Any) -> None:
    ...

@tool(description="...")
def set_y(state: State, value: Any) -> None:
    ...

# @chip.stateless @chip.statefull
class State(chip.State):  # noqa: D101
    history: List[str]


logger = chip.logger.get_logger()

# also behavise as a multable mapping accessible with dot notation
state = State()

chatbot = Chatbot(
    state=state,
    tools=[
        set_x(),
        set_y(),
    ],
    logger=logger,
    debug=False,
)

chatbot.chat()
