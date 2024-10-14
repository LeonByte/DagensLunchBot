from os import getenv
from dotenv import load_dotenv
from discord import Intents, Message, Embed
from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime
import response


class BotContainer:
    def __init__(self, bot_token) -> None:
        self.bot_token = bot_token

    def run(self):

        intents = Intents.default()
        intents.message_content = True
        bot = Bot(command_prefix='!', intents=intents, case_insensitive=True)

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
            res = '\n'.join(response.fetch_lunch_menu('Måndag'))
            today_date = datetime.now().strftime("%Y-%m-%d")
            await message.channel.send(f"Dagens datum: {today_date}\n{res}")

        @bot.command()
        async def tuesday(message : Message):
            res = '\n'.join(response.fetch_lunch_menu('Tisdag'))
            today_date = datetime.now().strftime("%Y-%m-%d")
            await message.channel.send(f"Dagens datum: {today_date}\n{res}")

        @bot.command()
        async def wednesday(message : Message):
            res = '\n'.join(response.fetch_lunch_menu('Onsdag'))
            today_date = datetime.now().strftime("%Y-%m-%d")
            await message.channel.send(f"Dagens datum: {today_date}\n{res}")
        
        @bot.command()
        async def thursday(message : Message):
            res = '\n'.join(response.fetch_lunch_menu('Torsdag'))
            today_date = datetime.now().strftime("%Y-%m-%d")
            await message.channel.send(f"Dagens datum: {today_date}\n{res}")

        @bot.command()
        async def friday(message : Message):
            res = '\n'.join(response.fetch_lunch_menu('Fredag'))
            today_date = datetime.now().strftime("%Y-%m-%d")
            await message.channel.send(f"Dagens datum: {today_date}\n{res}")

        @bot.command()
        async def today(message : Message):
            res = '\n'.join(response.fetch_lunch_menu('Today'))
            today_date = datetime.now().strftime("%Y-%m-%d")
            await message.channel.send(f"Dagens datum: {today_date}\n{res}")
        
        @bot.command()
        @commands.is_owner()
        async def shutdown(ctx):
            await ctx.send("Shutting down... Hejdå!")
            await bot.close()
        

        bot.run(self.bot_token)

if __name__ == '__main__':
    load_dotenv()
    bot_token = getenv('DISCORD_TOKEN')
    # if bot_token:
    bot = BotContainer(bot_token)
    bot.run()
    # else:
        # print("Bot token not found.")

