import requests

urls= "https://api.freeapi.app/api/v1/public/randomusers/user/random"

respond = requests.get(urls)
if respond.status_code == 200:
    data1 = respond.json()
    image_data = data1['data']['picture']
    for enu,i in enumerate( image_data.values()):
        print(i)
        img = requests.get(i)
        with open (f"image{enu}.jpg","wb")as f:
            f.write(img.content)

