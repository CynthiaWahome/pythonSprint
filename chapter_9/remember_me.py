import json

name = input("What is your name? ")

with open('username.json', 'w') as file_object:
    json.dump(name, file_object)
    print("success, we will remember you", name, "Ukirudi")


