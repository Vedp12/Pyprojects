import csv
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


text_Data = soup.find_all("h3")
price_Data = soup.select(".price_color")
stock_data = soup.select(".instock")

with open("book_data.csv", "w") as file:
    headers = ("Name", "Price", "Instock")
    csv_writer = csv.writer(file)
    csv_writer.writerow(headers)
    for t, p, s in zip(text_Data, price_Data, stock_data):
        data = (t.text, p.text, s.text)
        csv_writer.writerows(data)
