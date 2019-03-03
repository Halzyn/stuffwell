from cobe.brain import Brain


async def generate_message(message):
    content = message.content.replace("\x00", "").strip()
    content = content.replace("<@550768635681964066> ", "")
    b = Brain("./markov/brain.db")
    # async with message.channel.typing():
    words = b.reply(content).split(" ")
    for word in words:
        if word.startswith("<@"):
            words.remove(word)
    response = " ".join(words)
    await message.channel.send(response)


def save_message(client, message):
    content = message.content.replace("\x00", "")
    content = content.replace("<@550768635681964066>", "").strip()
    if content == "" or content.startswith(("$", "p!", "!")):
        return
    if message.author.id != client.user.id:
        b = Brain("./markov/brain.db")
        b.learn(content)


# Code for manually training the markov chain.
# def main():
#     with open("temp_copy.txt", errors="ignore") as f:
#         content = f.readlines()
#     content = [x.strip() for x in content]
#     b = Brain("brain.db")
#     for line in content:
#         b.learn(line)


# if __name__ == "__main__":
#     main()
