import json

with open('username.json', 'r') as file_object:
    name = json.load(file_object)
    print("Welcome back", name, "Proceed from where you left off")
