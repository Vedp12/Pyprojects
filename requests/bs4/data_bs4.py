import requests
import csv
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

name = soup.find_all("h3")
price = soup.select('.price_color')
stock = soup.select('.instock')

data = []

for  i,j, k in zip(name,price, stock):
    names  = i.a["title"]
    prices = j.text.strip()
    stocks  = k.text.strip()
    data.append([names,prices,stocks])
    
with open("data.csv", "w",newline="") as file:
    csv_writer = csv.writer(file)
    headers = ("name","price", "instock")
    csv_writer.writerow(headers)
    csv_writer.writerows(data)

