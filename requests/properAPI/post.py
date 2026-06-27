import requests

url = "https://api.freeapi.app/api/v1/todos"

new_todo = {
    "title": "Learn flask",
    "description": "Build a blog project"
}

response = requests.post(url, json=new_todo)

print("Status Code:", response.status_code)
print(response.json())