import requests
from pprint import pprint
import json

base_url = "https://api.open-meteo.com"
path = "/v1/forecast"
params = {"latitude": "44.4323", 
            "longitude": "26.1063",
            "current": ["temperature_2m", "wind_speed_10m"],
            "past_days": "30",
            "hourly": "temperature_2m"
            }


response = requests.get(base_url + path, params=params)
pprint(json.loads(response.content))