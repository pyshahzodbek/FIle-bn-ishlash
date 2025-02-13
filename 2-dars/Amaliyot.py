"""
Amaliyot
"""
import json

data={"Model":"Malibu","Rang":"Qora","Yil":2025,"Narh":40000}
data_json=json.dumps(data)
print(data_json)
print(type(data_json))

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba=json.loads(talaba_json)
print(talaba['ism'],talaba['familiya'])

with open('talaba.json','w') as fayl:
    json.dump(talaba,fayl)
with open("data.json","w") as f:
    json.dump(data,f)
#student={"student": [{"id": "01", "name": "Tom", "lastname": "Price", "year": 4, "faculty": "Engineering"}, {"id": "02", "name": "Nick", "lastname": "Thameson", "year": 3, "faculty": "Computer Science"}, {"id": "03", "name": "John", "lastname": "Doe", "year": 2, "faculty": "ICT"}]}
with open('students.json') as f:
    students=json.load(f)
print(students.keys())
talaba1=f"{students['student'][0]['name']} {students['student'][0]['lastname']} {students['student'][0]['year']}"
print(talaba1)
talaba2=f"{students['student'][1]['name']} {students['student'][1]['lastname']} {students['student'][1]['year']}"
print(talaba2)
talaba3=f"{students['student'][2]['name']} {students['student'][2]['lastname']} {students['student'][2]['year']}"
print(talaba3)
with open("api-result.json") as f:
     wkipediya=json.load(f)
print(wkipediya.keys())
print(wkipediya['query']['pages']['13801']['title'])
print(wkipediya['query']['pages']['13801']['extract'])