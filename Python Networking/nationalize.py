import requests
import json
from pprint import pprint

base_url = "https://api.nationalize.io/"
params = {
    "name":"Mariana"
}

response = requests.get(base_url, params=params)
response_content = json.loads(response.content)
response_list = response_content['country']
country = [i['country_id'] for i in response_list]
pprint(response_content)




