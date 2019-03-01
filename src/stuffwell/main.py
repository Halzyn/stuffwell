import discord

from commands.commands_dict import commands_dict

client = discord.Client()
TOKEN = 'NTUwNzY4NjM1NjgxOTY0MDY2.D1p9Dg.vnjJRoWIiASAk15NtQalQVkD9dg'


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


@client.event
async def on_message(message):
    command = commands_dict.get(message.content)
    if command is None:
        return
    return await command(client, message).run_command()


client.run(TOKEN)
