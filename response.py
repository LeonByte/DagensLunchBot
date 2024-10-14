from bs4 import BeautifulSoup
import requests
import schedule
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
            if datetime.today().weekday() not in (5, 6):
                return menu_items[days[datetime.today().weekday()]]
            else:
                return None
        else:
            return menu_items[dag]

print(datetime.today().weekday())
#schedule.every().monday.at("10:00").do(fetch_lunch_menu)
#while True:
#schedule.run_pending()
#time.sleep(1)

