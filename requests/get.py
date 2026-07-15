import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

respond = requests.get(url)
# print(respond.json())
if respond.status_code == 200:
    data = respond.json()
    print(data["data"]["name"]["first"])
    print(data["data"]["gender"])
    print(data["data"]["location"]["coordinates"]["longitude"])
    print(data["data"]["dob"]["age"])
    with open("data.txt", "a") as file:
        print(file.write(data["data"]["name"]["first"]))

        print(file.write(data["data"]["gender"]))

        print(file.write(data["data"]["location"]["coordinates"]["longitude"]))
