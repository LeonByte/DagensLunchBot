from bs4 import BeautifulSoup
import requests
import schedule
import time
import discord
from datetime import datetime
from discord.ext import commands

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

        for day, dishes in menu.items():
            print(f"{day}:")
            for dish in dishes:
                print(f"- {dish}")
                
    # url = "https://61an.gastrogate.com/dagens-lunch/"
    # response = requests.get(url)

    # if response.status_code == 200:
    #     soup = BeautifulSoup(response.text, "html.parser")

    #     menu = soup.find_all(class_="lunch-day-content")    
    #     menu_list = {}
    #     for item in menu:
    #         # title = item.find("h3")
    #         # description = item.find("p")
    #         title = item.find("h3", class_="td_title")
    #         description = item.find("p", class_="description")
    #         lunch_menu = {"title": title, "description": description}

    #         menu_list.append(lunch_menu)
    #         print(title, description)

    #     print(menu_list)

    # else:
    #     print("Failed to fetch data!")
    #     return None


print(fetch_lunch_menu())

#schedule.every().monday.at("10:00").do(fetch_lunch_menu)

#while True:
schedule.run_pending()
time.sleep(1)

