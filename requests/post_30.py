import requests

base_url = "https://api.freeapi.app/api/v1/todos"

payload = {
    "title": "oops",
    "description": "compete oops in python work",
    "iscomplete": False,
    "mesage": "hellow world",
}

response = requests.post(base_url, json=payload)
if response.status_code == 201:
    data = response.json()
    print("Todo created succesfully!")
    print("Title:", data["data"]["title"])
    print("description:", data["data"]["description"])
    print("Is complete:", data["data"]["isComplete"])
    print("Create at:", data["data"]["createdAt"])
    print("Message:", data.get("message", "No message"))
