from os import getenv
from dotenv import load_env
from discord import Intents, Message
from discord.ext.command import Bot

class BotContainer:
    def __init__(self, bot_token) -> None:
        self.bot_token = bot_token

    def run(self):

        intents = Intents.default()
        intents.message_content = True
        bot = Bot(command_prefix='!', Intents=intents, case_insenstive=True)


        @bot.event
        async def on_ready():
            print(f'{bot.user} is ready')

        @bot.command()
        async def 