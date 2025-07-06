import requests
import json
from pprint import pprint

base_url = "https://api.datamuse.com"
path = "/words"
params = {
    "sl":"beautiful"
}

response = requests.get(base_url + path, params=params)
response_content = json.loads(response.content)

words = [i["word"] for i in response_content]

# for i in response_content:
#     print(i['word'])
#     words.append(i['word'])

print(words)





