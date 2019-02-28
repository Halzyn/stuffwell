import discord

from .commands_dict import commands

client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


@client.event
async def on_message(message):
    command = commands.get_command(message.content)
    return command(client, message).run_command()


client.run("token")
