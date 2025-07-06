import requests
import random
import json

valoare = random.choice([1, 2, 3, 4, "", "-gcp"])
base_url = f"https://api{valoare}.binance.com"
path = "/api/v3/avgPrice"

params = {"symbol": "ETHUSDT"}
response = requests.get(base_url + path, params=params)
print(response)
print(response.url)
print(response.content)
full_response = json.loads(response.content)
print(full_response)
print(full_response['price'])







