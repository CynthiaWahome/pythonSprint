prompt = "\nWhich pizza toppings do you want? "
prompt += "\n(Enter 'quit' when you are finished.)"

# using break statement

# while True:
#     toppings = input(prompt)

#     if toppings == 'quit':
#         break
#     else:
#         print("We will add",toppings, "topping to your pizza!")

# using active variable

active = True
while active:
    message = input (prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# using a conditional test in the while loop
