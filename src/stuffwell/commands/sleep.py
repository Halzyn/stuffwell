from .base import CommandBase


class Sleep(CommandBase):
    def __init__(self, client, message):
        super().__init__(client, message)

    async def run_command(self):
        await self.client.send_message(self.message.channel, "Zzz...")
