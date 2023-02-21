import json

with open('note.json') as file_json:
    data = json.load(file_json)

print(data)
print(data['clientes_a'])
