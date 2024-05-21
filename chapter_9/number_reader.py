import json

filename = 'numbers.json'

with open(filename, 'r') as file_object:
    content = json.load(file_object)

print(content)
