from user.models import add_quote, list_quotes

from ..base import CommandBase


class QuoteCommands(CommandBase):
    def __init__(self, client, message):
        super().__init__(client, message)
        self.quotes_dict = {"add": self.add, "list": self.list_quotes}

    async def run_command(self):
        arguments = self.message.content.split(" ")
        if len(arguments) < 2:
            await self.message.channel.send("You must enter an argument!")
            return
        command = self.quotes_dict.get(arguments[1])
        if command is None:
            await self.message.channel.send("Invalid parameters")
            return
        await command(arguments)

    def select_user(self):
        mentions = self.message.raw_mentions
        if not mentions:
            return self.message.author
        return self.client.get_user(mentions[0])

    async def add(self, arguments):
        """Adds a quote for a user. Syntax: !q add [message_id] [user]
        """
        if len(arguments) == 2:
            await self.message.channel.send("You need to specify a message ID!")
            return
        discord_user = self.select_user()
        message = await self.message.channel.get_message(arguments[2])
        if message.author.id is not discord_user.id:
            await self.message.channel.send(
                "This message was not sent by the user you're assigning it to!"
            )
            return
        add_quote(discord_user, message.content)
        await self.message.channel.send(f"Quote added: {message.content}")

    async def list_quotes(self, arguments):
        discord_user = self.select_user()
        await self.message.channel.send(
            f"Quotes for {discord_user.name}: {list_quotes(discord_user)}"
        )
