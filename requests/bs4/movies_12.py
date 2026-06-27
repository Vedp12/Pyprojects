import requests
from bs4 import BeautifulSoup as BS4
from os import listdir,chdir,remove 
# mkdir,rmdir rem
# 


url = "https://sandbox.oxylabs.io/products"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
}
response = requests.get(url, headers= headers)
soup = BS4(response.text, "html.parser")

name = soup.select(".title")
price = soup.select(".price-wrapper")
# stock = soup.select(".css-1pewyd6") #in-stock css-1w904rj eag3qlw1
des = soup.select(".description")
# des = soup.select(".product-card css-e8at8d ")

# for i,j,k in zip(name,price,des):
#     # print(i.text.strip())
#     # print(j.text.strip())
#     # print(k.text.strip())

# with open("movies.txt","w")as file:
#     for i,j,k in zip(name,price,des):
#         file.write(i.text)
#         file.write(j.text)
#         file.write(k.text)
        
        # print(file.write(l.text.strip()))
# import os
# chdir(r"/home/tux_106/Documents/movies")        
for i,j,k in zip(name,price,des):
    with open(f"{i.text}.txt","w") as file:
        # print(i.text)
        remove(f"{i.text}.txt")
        # file.write(f"name={i.text}\nprice={j.text}\ndes={k.text}")
        # file.write(i.text)
        # file.write("\n")
        # file.write(j.text)
        # file.write("\n")
        # file.write(k.text)
        # file.write("\n")
    # print(i.text.strip())
    # print(j.text.strip())
    # print(k.text.strip())
print(listdir())
 
