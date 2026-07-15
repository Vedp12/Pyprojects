import requests

from_country = "USD"
to_country = "INR"
url = (
    f"https://v6.exchangerate-api.com/v6/a4725442db114a008054d412/latest/{from_country}"
)

respond = requests.get(url)
data = respond.json()
rate = data["conversion_rates"][to_country]
currency = 2
print(f"{currency} {from_country} = {currency * rate:.2f} {to_country}")
