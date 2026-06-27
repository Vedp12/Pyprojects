import requests
amount = 20
from_currency ="INR"
to_currency   ="NGN"
BASE_URL =f"https://v6.exchangerate-api.com/v6/5622b5716b09e6ba2ee89fa7/latest/{from_currency}"
url = requests.get(BASE_URL)
data = url.json()
rate = data["conversion_rates"][f"{to_currency}"]

print(f"{amount}:{from_currency}-> {amount*rate:.2f}:{to_currency}")
