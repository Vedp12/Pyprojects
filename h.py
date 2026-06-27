import requests

API_KEY = "YOUR_API_KEY"  # put your key here

amount = 1
from_currency = "INR"
to_currency = "USD"

url = f"https://v6.exchangerate-api.com/v6/5622b5716b09e6ba2ee89fa7/latest/{from_currency}"
data = requests.get(url).json()

rate = data["conversion_rates"][to_currency]
print(f"{amount} {from_currency} = {amount * rate:.2f} {to_currency}")

