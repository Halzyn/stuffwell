import markovify


async def generate_message(message):
    with open("./markov/brain.txt") as f:
        text = f.read()

    text_model = markovify.NewlineText(text, state_size=3, retain_original=False)
    # async with message.channel.typing():
    sentence = text_model.make_sentence()
    await message.channel.send(sentence)


def save_message(message):
    content = message.content.replace("\x00", "").strip()
    if content == "" or content.startswith("$"):
        return
    content = content.replace("<@550768635681964066> ", "")
    if message.channel.id == int("256944846437220352"):
        with open("./markov/brain.txt", "a") as f:
            f.write(content + "\n")
