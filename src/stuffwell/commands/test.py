from base import CommandBase


class Test(CommandBase):
    def __init__(self):
        super()

    def run_command(self):
        counter = 0
        tmp = await self.client.send_message(self.message.channel, 'Calculating messages...')
        async for log in self.client.logs_from(self.message.channel, limit=100):
            if log.author == self.message.author:
                counter += 1

        await self.client.edit_message(tmp, 'You have {} messages.'.format(counter))