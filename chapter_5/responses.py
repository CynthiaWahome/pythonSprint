responses = {}

is_polling_active = True

while is_polling_active:
    name = input("\n What is your name ")
    print("The current name in the loop is: ",name)
    
    response = input("\nWhich mt would you like to climb? ")
    print(name, "would like to climb Mt", response)

    #person_1['name'] = 'Abel'
    #person_1['height'] = 3.8
    
    responses[name] = response

    print(responses)

    repeat = input("Anyone else? (Enter Y/N)")

    if repeat == 'N':
        is_polling_active = False

print("\n---------------Polling complete - Results ------")

for name, response in responses.items():
    print(name, "Would like to climb", response)


