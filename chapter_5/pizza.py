prompt = "\nWhich pizza toppings do you want? "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print("We will add",toppings, "topping to your pizza!")
    