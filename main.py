from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import Responses

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

response_handler = Responses(os.getenv("OPENAI_TOKEN"))


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message empty')
        return
    is_private = user_message[0] == '?'
    if is_private:
        user_message = user_message[1:]

    try:
        response: str = response_handler.get_response(user_message, str(message.author.name))
        if response != "0000000000000000000":
            if is_private:
                await message.author.send(response)
            else:
                await message.channel.send(response)
    except Exception as e:
        print(e)


@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return
    user_message = message.content
    await send_message(message, user_message)


@client.event
async def on_ready():
    print(f'{client.user} is now running')


def main() -> None:
    client.run(TOKEN)


if __name__ == '__main__':
    main()
