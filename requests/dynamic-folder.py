import requests
from bs4 import BeautifulSoup
import os


url = "https://sandbox.oxylabs.io/products"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
}
response = requests.get(url, headers= headers)
soup = BeautifulSoup(response.text, "html.parser")

name = soup.select(".title")
price = soup.select(".price-wrapper")
des = soup.select(".description")

with open(f"a1.txt" ,"w") as file:
    for i,j,k in zip(name,price,des):
        file.write(f"\n\nname: {i.text}\nprice: {j.text}\ndescription: {k.text} \n")
