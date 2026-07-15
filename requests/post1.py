import requests

BASE_URL = "https://api.freeapi.app/api/v1/todos"

# Step 1: Create a new todo
payload = {
    "title": "OOPs",
    "description": "complete oops in python work",
    "isComplete": False,
    "message": "hello world",
}

response = requests.post(BASE_URL, json=payload)
if response.status_code == 201:
    data = response.json()
    print("Todo created successfully!")
    print("Title:", data["data"]["title"])
    print("Description:", data["data"]["description"])
    print("Is Complete:", data["data"]["isComplete"])
    print("Created At:", data["data"]["createdAt"])
    print("Message:", data.get("message", "No message"))
