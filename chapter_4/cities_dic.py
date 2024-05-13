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

print(cities)

for city, city_info in cities.items():
    print("\nCity: " + city)
    country = city_info['country'] 
    population = float(city_info['population in millions'])
    fact = city_info['fact']

    print("These are some of intersting things about",city +':' )
    print("\tCountry: " + country.title())
    print("\tPopulation: " ,population)
    print("\tFun fact: " + fact.title())
   