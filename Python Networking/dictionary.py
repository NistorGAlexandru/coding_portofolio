import json

d = ["valoare", 1, (2, 3), True, None,  ]
{"cheie": "valoare", "(1,2)":  "bine", "cheie2": "foarte bine"}
print(d)


dumped_d = json.dumps(d)
print(dumped_d)
print(type(dumped_d))

with open("lista.json", "w") as f:
    f.write(dumped_d)

with open("lista.json", "r") as f:
    read_d = f.read()
    print("Am citit:", read_d)


reloaded_d = json.loads(dumped_d)
print(reloaded_d)
print(type(reloaded_d))














