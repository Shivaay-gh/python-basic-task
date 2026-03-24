import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

class PriceTracker:
    def __init__(self, url, target_price):
        self.url = url
        self.target_price = target_price

        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', "Accept-Language": "en-US,en;q=0.9"}

        self.response = requests.get(url=self.url, headers=self.headers)
        print("Status code: ", self.response.status_code)

        if self.response.status_code == 200:
            self.soup = BeautifulSoup(self.response.text, 'html.parser')
        else:
            self.soup = None

    def product_title(self):
        if self.soup is None:
            return "Page not loaded"

        title = self.soup.find("span", attrs={'id':"productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag not found"

    def product_price(self):
        if self.soup is None:
            return None

        price = self.soup.find("span", attrs={'id':"a-price-whole"})
        if price is not None:
            price_text = price.text.strip()
            price_text = price_text.replace(",", "").replace(".", "")

            try:
                return int(price_text)
            except ValueError:
                return None
        else:
            return None

    def save_data(self, title, price):
        with open('price_history.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now(), title, price])

    def check_price(self):
        if self.soup is None:
            print("Failed to fetch webpage")
            return

        title = self.product_title()
        price = self.product_price()

        print("Product:", title)

        if price is not None:
            print("Current price:", price)
            self.save_data(title, price)

            if price <= self.target_price:
                print("Price dropped below your target price")
            else:
                print("Price is still higher than your target price")

        else:
            print("Price not found")


product_url = input("Enter your product url: ")
target = int(input("Enter your target price: "))

device = PriceTracker(product_url, target)
device.check_price()

