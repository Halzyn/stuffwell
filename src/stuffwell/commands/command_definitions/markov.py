from ..base import CommandBase


class MarkovCommands(CommandBase):
    def __init__(self, client, message):
        super().__init__(client, message)

    async def run_command(self):
        pass
