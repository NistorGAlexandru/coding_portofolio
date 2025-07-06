import requests

response = requests.get("https://www.link-academy.com/")
print(response)
print(response.status_code)
print(response.content)
content = response.content.decode()
print(content)

with open("link.html", "w") as fwrite:
    fwrite.write(content)

print(response.url)

print(response.headers)
print(response.request.headers)
print(response.headers["Content-Type"])
print(response.headers["User-Agent"])

print(type(response.headers))


with open("link.html", "a", encoding="utf-8") as fwrite:
    fwrite.write(response.text)


