# xtics of a person 
# name => Cynthia
# gender => prefer not to say
# height => 5'8

person_1 = {
        'name': 'Abel',
        'gender': 'PnT',
        'height': 5.8
        }

print(person_1)

print(person_1['name'])

person_1['shoe size'] = 38
person_1['is_happy'] = True
person_1['fav_fruit'] = 'Matunda'
person_1['name'] = 'Cynthia Wahome'
del person_1['gender']

print(person_1)


cities = {
    'Nairobey': {
        'country': 'Kenya',
        'population in millions': 4.397,
        'fact': 'The only capital ciy with a national park'
    },
    'Kigali' : {
        'country': 'Rwanda',
        'population in millions': 1.208,
        'fact': 'The cleanest city in Africa'
    },
    'Johannesburg' : {
        'country': 'South Africa',
        'population in millions': 5.635,
        'fact': 'Home to the worlds biggest man made forest',
    } 
}

cities['Ougadoudou'] = [
    'country',
    'population in millions',
    'fact'
]

print(cities)