import requests
import csv
from bs4 import BeautifulSoup as bs4
import os

api_url = []

headers = {"Authorization": "tKkL5zzeQqS50-z5UUilwMe6oeTxLj00zJP8cwHI9UJHP_jh"}
url = "https://api.currentsapi.services/v1/latest-news"
response = requests.get(url, headers=headers)
data = response.json()
data1 = data["news"]

with open("book.csv", "w") as file:
    csv_writer = csv.writer(file)
    headers = ["id", "title", "description", "url"]
    csv_writer.writerow(headers)
    for i in data1:
        csv_writer.writerow([i["id"], i["title"], i["description"], i["url"]])
        api_url.append(i["url"])
    # print(api_url)

    # if os.path.exists(r"Documents/PyProj/requests/properAPI/api_data"):
    # os.mkdir("api_data")
    os.chdir(r"/home/tux_106/Documents/PyProj/requests/properAPI/api_data")
    print(os.listdir())

    for enu, i in enumerate(api_url):
        response = requests.get(i)
        soup = bs4(response.text, "html.parser")
        with open(f"{enu}.html", "w") as file:
            file.write(soup.html)
