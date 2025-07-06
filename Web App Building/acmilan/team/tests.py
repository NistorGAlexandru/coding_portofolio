from pprint import pprint
import json

# Create your tests here.
jucatori = [[["Dida","12"]], [["Oddo","44"], ["Nesta","13"], ["Maldini","3"], ["Jankulovski","18"]],
                       [["Gattuso","8"], ["Pirlo","21"], ["Ambrosini","23"]],
                          [["Kaka","22"], ["Seedorf","10"]],
                           [["Inzaghi","9"]] ]

pprint(jucatori)

with open("dreamteam.json", "w") as fwriter:
    json.dump(jucatori, fwriter)