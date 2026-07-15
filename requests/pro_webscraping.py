import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
useragent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
response = requests.get(url, useragent)

soup = BeautifulSoup(response.text, "html.parser")

#
# print(soup.title)
# print(soup.title.text)
# heading = soup.find_all("h1")
# print(heading)
# print(heading.text)

price = soup.find(class_="price")
print(price)
