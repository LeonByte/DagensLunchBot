from os import getenv
from dotenv import load_dotenv
from discord import Intents, Message, Embed
from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime, timedelta
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

        def create_embed(day: str, menu: list):
            current_date = datetime.now().strftime('%Y-%m-%d')
            if menu:
                description = "\n".join(menu)
            else:
                description = "No menu available for today."

            embed = Embed(title=f"{day}s Lunch Meny ({current_date})", description=description, color=0x00ff00)
            embed.set_footer(text="Restaurang 61:an - Karolinska")
            return embed

        @bot.command()
        async def monday(ctx):
            menu = response.fetch_lunch_menu('Måndag')
            embed = create_embed('Måndag', menu)
            await ctx.send(embed=embed)

        @bot.command()
        async def tuesday(ctx):
            menu = response.fetch_lunch_menu('Tisdag')
            embed = create_embed('Tisdag', menu)
            await ctx.send(embed=embed)
            

        @bot.command()
        async def wednesday(ctx):
            menu = response.fetch_lunch_menu('Onsdag')
            embed = create_embed('Onsdag', menu)
            await ctx.send(embed=embed)
        
        @bot.command()
        async def thursday(ctx):
            menu = response.fetch_lunch_menu('Torsdag')
            embed = create_embed('Torsdag', menu)
            await ctx.send(embed=embed)

        @bot.command()
        async def friday(ctx):
            menu = response.fetch_lunch_menu('Fredag')
            embed = create_embed('Fredag', menu)
            await ctx.send(embed=embed)

        @bot.command()
        async def today(ctx):
            menu = response.fetch_lunch_menu('Today')
            if menu:
                day = ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag'][datetime.today().weekday()]
                embed = create_embed(day, menu)
            else:
                embed = create_embed('Today', ["No menu available for today."])
            await ctx.send(embed=embed)
        
        @bot.command()
        async def shutdown(ctx):
            await ctx.send("Shutting down... Hejdå! Have a great day!")
            await bot.close()
        

        bot.run(self.bot_token)

if __name__ == '__main__':
    load_dotenv()
    bot_token = getenv('DISCORD_TOKEN')
    if bot_token:
        bot = BotContainer(bot_token)
        bot.run()
    else:
        print("Bot token not found.")

