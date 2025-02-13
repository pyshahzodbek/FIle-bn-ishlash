"""
12.02.2025
Mavzu: Json
"""
#json.dumps()
import json
from fileinput import filename

x=10
x_json=json.dumps(x)

ism="anvar"
ism_json=json.dumps(ism)
sonlar=[1,3,45,67,21]
sonlar_json=json.dumps(sonlar)
print(type(x_json))

bemor={
    "ism":"Alijon Valiyev",
    "yosh":30,
    "oila":True,
    "farzandlar":("Ahmad","Bonu"),
    "allergiya":None,
    "dorilar":[
        {"nomi":"Analgin","miqdori":0.5},
        {"nomi":"Panadol","miqdori":1.2}
    ]
}
bemor_json=json.dumps(bemor,indent=4)
print(bemor_json)
with open("bemor.json","w") as f:
    json.dump(bemor,f)
#json.loads()
sonlar=json.loads(sonlar_json)
bemor=json.loads(bemor_json)
print(bemor)
#json.load()
filename="bemor.json"
with open(filename) as f:
    bemor=json.load(f)
print(type(bemor))