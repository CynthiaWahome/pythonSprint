responses = {}


is_polling_active = True
while is_polling_active:
    name = input("What is your name? ")
    places = input("If you could visit one place in the world, where would you go?")
    
    responses[name] = places

    repeat = input("Would you like to continue? (yes/ no)")
    if repeat == 'no':
        is_polling_active = False

for name,places in responses.items():
    print(places,"is the one place that",name, "would live to visit!")
