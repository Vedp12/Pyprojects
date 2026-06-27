import requests

todo_id = "6a1c869279a6035e15c9d3c8"

url = f"https://api.freeapi.app/api/v1/todos/{todo_id}"

response = requests.delete(url)

print("Status Code:", response.status_code)
print(response.text)