# A list of Dictionaries

animal_1 = {
    'name': 'chiwawa',
    'breed': 'dog',
    'owner': 'cynthia'
}

animal_2 = {
    'name': 'opticut',
    'breed' : 'cat',
    'owner' : 'samuel'
}

animal_3 = {
    'name': 'angus',
    'breed' : 'cow',
    'owner' : 'xaiver'
}

pets = [animal_1, animal_2, animal_3]

# for pet in pets:
#     for pet_name, pet_owner in pet.items():
#         print(pet_name.title(), pet_owner.title()) # How can I change the case?


# pets = [
#     { 'breed': 'dog', 'owner': 'cynthia' },
#     { 'breed' : 'cat', 'owner' : 'samuel' }
# ]

for pet in pets:
    print(pet['name'], "of", pet['breed'], "belongs to", pet['owner'])
