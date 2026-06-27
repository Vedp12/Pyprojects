import requests
url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
respond = requests.get(url)

#print(respond.json())
if respond.status_code==200:
    data=respond.json()
    print(data["data"]["phone"])
    print(data["data"]["id"])
    
    
  
    

    
    