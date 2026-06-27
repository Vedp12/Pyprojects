import requests

url="https://api.useragent.app/parse?key=0PWpZrKIL2A6ys8U69CMTfVhwT4kcrGsGXKhLK64by20IqnuJ9qA1esy7cqewwhNas82a2Ox"

respond = requests.get(url)

if respond.status_code == 200:
    data = respond.json()
    print(data)
    