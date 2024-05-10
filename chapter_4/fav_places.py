# A list in a Dictionary

fav_places = {
    'diana':['denmark','everest','genever'],
    'derrick': ['denver','burkingham','czetch','ireland'],
    'daughtry': ['dodoma', 'joburg','iowa','pretoria']
}

for name, places in fav_places.items():
    print("\n" + name.upper() + "'s favourite places to visit are: ")

    for place in places:
        print("\t" + place.title())