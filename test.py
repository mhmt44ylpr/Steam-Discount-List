import requests
from bs4 import BeautifulSoup
import json
from pyfiglet import Figlet
import colorama
import time
from tqdm import tqdm

fig = Figlet(font='slant')
print(colorama.Fore.RED+fig.renderText("Steam Discount"))
inp = input( colorama.Fore.GREEN +"<<<Press Enter to Continue>>> \n \n \n")
for i in tqdm(range(100)):
    time.sleep(0.01)

class Steam_Discount(object):
    def __init__(self):
        self.url = "https://steam250.com/discounts"
        self.game_name_list = list()
        self.game_price_list = list()
        self.game_discount_list = list()
        self.dict_Game_List = dict()
        self.Store_Url = list()
    def Discount(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'lxml')
            game_soup = soup.find_all('span', class_="title")
            num = 1
            for game in game_soup:
                if num <=250:
                    if game.find("a").text != ' ':
                        self.game_name_list.append(game.find('a').text)
                        num += 1
            game_price = soup.find_all('span', class_="price")
            num2 = 1
            for i in game_price:
                if num2 <=250:
                    self.game_price_list.append(i.text)
            game_discount = soup.find_all("a" , class_="discount")
            num3 = 1
            for n in game_discount:
                if num3 <=250:
                    self.game_discount_list.append(n.text)
            game_store = soup.find_all('a', class_="store")
            num4 = 1
            for s in game_store:
                if num4 <=250:
                    self.Store_Url.append(s.get("href"))
        else:
            print(colorama.Fore.GREEN + "Something went wrong")

    def Print_Game_List(self):
        for i in range(250):
            name = f"{self.game_name_list[i]}"
            price =f"{self.game_price_list[i]}"
            discount = f"{self.game_discount_list[i]}"
            url = f"{self.Store_Url[i]}"
            dict_list = {"name":name,
                         "price":price,
                         "discount":discount,
                         "Url": url}
            with open("new.json" , "a" , encoding="utf-8") as f:
                f.write(json.dumps(dict_list , indent=4))
            print(colorama.Fore.CYAN + f"Name:{name}" + colorama.Fore.RED + f" Price:{price}" + colorama.Fore.GREEN +f" Discount:{discount}" + colorama.Fore.BLUE +f"\n    Url:{self.Store_Url[i]}" + "\n")
            time.sleep(0.04)

Discount = Steam_Discount()
Discount.Discount()
Discount.Print_Game_List()


