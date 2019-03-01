from .base import CommandBase


class Test(CommandBase):
    def __init__(self, client, message):
        super().__init__(client, message)

    async def run_command(self):
        counter = 0
        tmp = await self.client.send_message(self.message.channel, 'Calculating...')
        async for log in self.client.logs_from(self.message.channel, limit=100):
            if log.author == self.message.author:
                counter += 1

        await self.client.edit_message(tmp, 'You have {} messages.'.format(counter))
