from commands.commands_dict import commands_dict

import discord

from discord.ext.commands import Bot

from markov.models import generate_message, save_message


bot_activity = discord.Activity(
    application_id=1,
    name="in hazel's server!",
    type=discord.ActivityType.watching,
    state="in hazel's server!",
    details="i dont know what this is",
)

client = Bot(command_prefix="!", activity=bot_activity)
TOKEN = "NTUwNzY4NjM1NjgxOTY0MDY2.D1p9Dg.vnjJRoWIiASAk15NtQalQVkD9dg"


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


@client.event
async def on_message(message):
    save_message(message)

    if client.user.id in [user.id for user in message.mentions]:
        await generate_message(message)
        return
    command = commands_dict.get(message.content.split(" ", 1)[0])
    if command is None:
        return
    return await command(client, message).run_command()


client.run(TOKEN)
