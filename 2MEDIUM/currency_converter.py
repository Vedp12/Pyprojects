import requests

apikey = ""
country = "INR"
native_data = input("Enter a native country name: ").upper()
url = f"https://v6.exchangerate-api.com/v6/{apikey}/latest/{native_data}"
response = requests.get(url)
country = input("Enter a country name: ").upper()
getting_data_of_ = response.json()["conversion_rates"][country]
currency = int(input("Enter currency: "))
sum = 100 * getting_data_of_

print(f"{currency} {native_data} =  {sum:.2f} {currency}")
