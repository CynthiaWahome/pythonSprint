import json

filename = "username.json"

try:
    with open(filename, 'r') as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
        print("Hi", username, "We will remember you")
else:
    print("Welcome back like you never left", username)

