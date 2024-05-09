rivers = {
        'nile': 'Egypt',
        'Turkana': 'Kenya',
        'Jordan': 'Israel',
        }

for river, country in rivers.items():
    print("the", river, "runs through", country)

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)
