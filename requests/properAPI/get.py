import requests

url = "https://api.freeapi.app/api/v1/todos"

response = requests.get(url)

data = response.json()

todos = data["data"]

for todo in todos:
    title = todo["title"]
    description = todo["description"]

    print("Title:", title)
    print("Description:", description)
    print(todo["_id"])