from bs4 import BeautifulSoup
import requests
from datetime import datetime 

def fetch_lunch_menu(dag : str) -> list:

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
        
        if dag == 'Today':
            today = datetime.today()
            if today.weekday() not in (5, 6):  # Om det inte är lördag eller söndag
                return menu_items[days[today.weekday()]]
            else:
                return None