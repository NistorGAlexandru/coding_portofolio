import requests
from pprint import pprint
import json

base_url = "https://api.zippopotam.us"
path = "/us/90210"
# params = {
#     "post code": "90210",
#     "country": "United States",
#     "country abbreviation": "US",
#     "places": [{"place name": "Beverly Hills", "longitude": "-118.4065", "state": "California", "state abbreviation": "CA", "latitude": "34.0901"}]
# }

response = requests.get(base_url + path)
data = json.loads(response.content)
pprint(json.response["places"][0]["place name"])


