"""Example usage of the chip package."""

from typing import List

import chip


# @chip.stateless @chip.statefull
class State(chip.State):  # noqa: D101
    history: List[str]


state = State()

chatbot = chip.Chatbot(
    state=state,
    tasks=[],
    logger=chip.logger.new(),
    debug=True,
)


chatbot.chat()
