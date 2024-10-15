from os import getenv
from dotenv import load_dotenv
from discord import Intents, Message, Embed
from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime, timedelta
import response
import os
import sys

class BotContainer:
    def __init__(self, bot_token) -> None:
        # Initialize the bot with the provided token
        self.bot_token = bot_token

    def run(self):
        # Set up intents for the bot
        intents = Intents.default()
        intents.message_content = True
        bot = Bot(command_prefix="!", intents=intents, case_insensitive=True)

        @bot.event
        async def on_ready():
            # Print a message when the bot is ready
            print(f"{bot.user} is ready")

        @bot.event
        async def on_message(message: Message):
            # Ignore messages from the bot itself
            if message.author == bot.user:
                return
            
            # Process commands and handle errors
            try:
                await bot.process_commands(message)
            except commands.CommandNotFound:
                await message.channel.send("Det kommandot finns inte. Försök med ett annat kommando.")
            except KeyError:
                await message.channel.send("Ett fel inträffade vid hämtning av menyn.")

            # Define valid commands
            valid_commands = ["!monday", "!tuesday", "!wednesday", "!thursday", 
                              "!friday", "!today", "!restart", "!shutdown"]
            # Check if the message starts with '!' and is not a valid command
            if message.content.startswith("!") and message.content not in valid_commands:
                await message.channel.send("Detta kommando finns inte, försök igen.")

        def get_date_for_day(day_name: str) -> str:
            # Get the date for the specified day of the week
            today = datetime.now()
            days_of_week = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag"]
            target_day_idx = days_of_week.index(day_name)

            delta = target_day_idx - today.weekday()
            if delta < 0:
                delta += 7

            target_date = today + timedelta(days=delta)
            return target_date.strftime("%Y-%m-%d") 

        def create_embed(day: str, menu: list):
            # Create an embed message for Discord with the lunch menu
            date_for_day = get_date_for_day(day)
            description = "\n".join(menu) if menu else "No menu available for today."

            embed = Embed(title=f"{day}s lunch meny ({date_for_day})", description=description, color=0x00ff00)
            embed.set_footer(text="Restaurang 61:an - Karolinska")
            return embed

        @bot.command()
        async def monday(ctx):
            # Command to fetch Monday's lunch menu
            menu = response.fetch_lunch_menu("Måndag")
            embed = create_embed("Måndag", menu)
            await ctx.send(embed=embed)

        @bot.command()
        async def tuesday(ctx):
            # Command to fetch Tuesday's lunch menu
            menu = response.fetch_lunch_menu("Tisdag")
            embed = create_embed("Tisdag", menu)
            await ctx.send(embed=embed)

        @bot.command()
        async def wednesday(ctx):
            # Command to fetch Wednesday's lunch menu
            menu = response.fetch_lunch_menu("Onsdag")
            embed = create_embed("Onsdag", menu)
            await ctx.send(embed=embed)

        @bot.command()
        async def thursday(ctx):
            # Command to fetch Thursday's lunch menu
            menu = response.fetch_lunch_menu("Torsdag")
            embed = create_embed("Torsdag", menu)
            await ctx.send(embed=embed)

        @bot.command()
        async def friday(ctx):
            # Command to fetch Friday's lunch menu
            menu = response.fetch_lunch_menu("Fredag")
            embed = create_embed("Fredag", menu)
            await ctx.send(embed=embed)

        @bot.command()
        async def today(ctx):
            # Command to fetch today's lunch menu
            menu = response.fetch_lunch_menu("Today")
            if menu:
                day = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag"][datetime.today().weekday()]
                embed = create_embed(day, menu)
            else:
                embed = create_embed("Today", ["No menu available for today."])
            await ctx.send(embed=embed)

        @bot.command()
        @commands.has_permissions(administrator=True)
        async def shutdown(ctx):
            # Command to shut down the bot
            await ctx.send("Shutting down... Have a great day!")
            await bot.close()

        @bot.command()
        @commands.has_permissions(administrator=True)
        async def restart(ctx):
            # Command to restart the bot
            await ctx.send("Restarting...")
            os.execv(sys.executable, ['python'] + sys.argv)
        
        bot.run(self.bot_token)

if __name__ == "__main__":
    load_dotenv()
    bot_token = getenv("DISCORD_TOKEN")
    if bot_token:
        bot = BotContainer(bot_token)
        bot.run()
    else:
        print("Bot token not found.")
