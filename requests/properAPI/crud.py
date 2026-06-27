import requests

BASE_URL = "https://api.freeapi.app/api/v1/todos"

# CREATE
todo = {
    "title": "it's an 12 ",
    "description": "py meeting"
}

response = requests.post(BASE_URL, json=todo)
print("Created:", response.status_code)

# READ
response = requests.get(BASE_URL)

for todo in response.json()["data"]:
    print(todo["title"])

# UPDATE
todo_id = "648e070a36b0cc220c8a7883"

response = requests.patch(
    f"{BASE_URL}/{todo_id}",
    json={"isDone": True}
)

print("Updated:", response.status_code)

# DELETE
response = requests.delete(
    f"{BASE_URL}/{todo_id}"
)

print("Deleted:", response.status_code)