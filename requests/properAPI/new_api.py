import requests
import csv

headers = {
    'Authorization': 'tKkL5zzeQqS50-z5UUilwMe6oeTxLj00zJP8cwHI9UJHP_jh'
}
url = "https://api.currentsapi.services/v1/latest-news"
response = requests.get(url, headers=headers)
data = response.json()
data1 = data["news"]

with open("book.csv", "w") as file:
    csv_writer = csv.writer(file)
    headers = ["id", "title", "description"]
    csv_writer.writerow(headers)
    for i in data1:
        csv_writer.writerow([i["id"], i["title"], i["description"]])
