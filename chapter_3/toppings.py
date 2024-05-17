requested_toppings = ['mushrooms', 'extra cheese', 'green peppers', 'extra periperi']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print("Adding " + requested_topping + ".")
        print("Finished making your pizza!\n")