import json


with open('people.json', 'r', encoding='utf-8') as f, open(
    'updated_people.json', 'w', encoding='utf-8') as n:
    bufer_dict = {}
    for i in json.load(f):
        bufer_dict = bufer_dict | i
    for i in json.load(f):
        i = bufer_dict.setdefault()
    print(bufer_dict)