from .command_definitions.quotes import QuoteCommands
from .command_definitions.sleep import Sleep
from .command_definitions.user import UserCommands

commands_dict = {
    "!q": QuoteCommands,
    "!quote": QuoteCommands,
    "!user": UserCommands,
    "!sleep": Sleep,
}
