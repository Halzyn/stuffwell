from ..base import CommandBase


class UserCommands(CommandBase):
    def __init__(self, client, message):
        super().__init__(client, message)
        self.commands = {"!say": self.say}

    async def run_command(self):
        command = self.commands.get(self.message.content.split(" ")[0])
        await command()

    async def say(self):
        if self.message.author.id == 137701909552300032:
            await self.message.channel.send(self.message.content.split(" ", 1)[1])
