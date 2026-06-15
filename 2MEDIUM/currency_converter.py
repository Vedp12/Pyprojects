import requests

apikey = "5c51aa2a2d1ab727c77ae04d"
country = "INR"
native_data = input("Enter a native country name: ").upper()
url = f"https://v6.exchangerate-api.com/v6/5c51aa2a2d1ab727c77ae04d/latest/usd"
response = requests.get(url)
country = input("Enter a country name: ").upper()
getting_data_of_ = response.json()["conversion_rates"][country]
currency = int(input("Enter currency: "))
sum = 100 * getting_data_of_

print(f"{currency} {native_data} =  {sum:.2f} {country}")
