from bs4 import BeautifulSoup
import requests
import schedule
import time
import discord
from datetime import datetime
from discord.ext import commands

# def fetch_lunch_menu(day : str):
def fetch_lunch_menu():

    url = "https://61an.gastrogate.com/dagens-lunch/"
    response = requests.get(url)


    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        days = soup.find_all('h3')

        menu = {}
        for day in days:
            day_name = day.text.strip()

            dishes = day.find_next("tbody").find_all('td', class_="td_title")

            list_dish = [dish.text.strip() for dish in dishes]

            menu[day_name] = list_dish

        days = ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag']

        menu_items = {}

        for key, value in menu.items():
            for day in days:
                if day in key:
                    menu_items.update({day: value})

        return menu_items

print(fetch_lunch_menu())

#schedule.every().monday.at("10:00").do(fetch_lunch_menu)

#while True:
schedule.run_pending()
time.sleep(1)

