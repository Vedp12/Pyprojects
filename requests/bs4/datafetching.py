import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
}
response = requests.get(url,headers=headers)
soup =BeautifulSoup(response.text,"html.parser")



text_Data = soup.find_all("h3")
price_Data = soup.select(".price_color")
stock_data = soup.select(".instock")


with open("data.txt","a") as file:
    for t,p,s in (zip(text_Data,price_Data,stock_data)):
        file.write("\n")
        file.write(t.text)
        file.write("\n")
        file.write(p.text)
        file.write("\n")
        file.write(s.text.strip())
        file.write("\n")
        file.write("\n")




# images= soup.find_all("img")

# if images:
#     for enum, image in enumerate(images):
#         img_url = image['src']
#         if not img_url.startswith('http'):
#             img_url = url.rstrip('/') + '/' + img_url.lstrip('/')
#             print(img_url)
#         img_data = requests.get(img_url, headers=headers)
#         if img_data.status_code == 200:
#             with open(f'"f{enum}".jpg','wb') as f:
#                 f.write(img_data.content)
#             print("Image downloaded successfully")