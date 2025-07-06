import requests
import json
import pprint

headers = {
    "Accept":"text/plain",
    "Accept":"application/json"
}
response = requests.get("https://icanhazdadjoke.com/", headers=headers)

print(json.loads(response.content)["joke"])

with open("glume.txt", "a") as f:
    f.write(json.loads(response.content)["joke"])
    f.write("\n")
















