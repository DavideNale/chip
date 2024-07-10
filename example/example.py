"""Example usage of the chip package."""

import chip

state = chip.State(
        
)

chatbot = chip.Chatbot(
    tasks=[],
    state=state,
    logger=chip.logger.new(),
    debug=True,
)


chatbot.chat()
