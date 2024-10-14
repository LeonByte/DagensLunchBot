from os import getenv
from dotenv import load_env
from discord import Intents, Message
from discord.ext.commands import Bot


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

        @bot.event
        async def on_message(message : Message):
            if message.author == bot.user:
                return
            
            await bot.process_commands(message)

        @bot.command()
        async def monday(message : Message):
            pass
        async def tuesday(message : Message):
            pass
        async def wednesday(message : Message):
            pass
        async def thursday(message : Message):
            pass
        async def friday(message : Message):
            pass
        async def today(message : Message):
            pass
        

        bot.run(self.bot_token)

if __name__ == '__main__':
    load_env()