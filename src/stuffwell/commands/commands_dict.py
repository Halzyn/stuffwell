from .command_definitions.markov import MarkovCommands
from .command_definitions.quotes import QuoteCommands
from .command_definitions.sleep import Sleep
from .command_definitions.user import UserCommands

commands_dict = {
    "!q": QuoteCommands,
    "!quote": QuoteCommands,
    "!remove_duplicates": MarkovCommands,
    "!user": UserCommands,
    "!sleep": Sleep,
}
