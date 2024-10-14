from bs4 import BeautifulSoup
import requests
import schedule
import time
import discord
from discord.ext import commands

def fetch_lunch_menu():
    url = "https://61an.gastrogate.com/dagens-lunch/"
    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
    else:
        print("Failed fetch data!")

schedule.every().monday.at("10:00").do(fetch_lunch_menu)

while True:
    schedule.run_pending()
    time.sleep(1)