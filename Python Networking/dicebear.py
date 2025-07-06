import requests
import json

style = "lorelei"
base_url = f"https://api.dicebear.com/9.x/{style}/svg"
params = {"seed": "Felix"}


response = requests.get(base_url, params=params)

with open(f"{style}.svg", "w", encoding="utf-8") as f:
    f.write(response.text)

