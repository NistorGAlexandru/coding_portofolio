import requests

base_url  = "https://techy-api.vercel.app"
json_path = "/api/json"
out_file  = "techy.txt"

response = requests.get(base_url + json_path)
response.raise_for_status()   

data = response.json()        
print("Got:", data)

message = data.get("message", "")


with open(out_file, "a", encoding="utf-8") as f:
    f.write(message + "\n")

print(f"Appended to {out_file!r}: {message!r}")