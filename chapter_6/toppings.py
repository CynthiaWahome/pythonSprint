def make_pizza(size, *toppings):
    if toppings:
        for topping in toppings:
            print(topping, "for pizza size", size)

    else:
        print("No topping selected for pizza size", size)

make_pizza("large", "pineapple", "bbq steak")
make_pizza("small", "mushrooms")
make_pizza(" ", "peperoni")
make_pizza("medium")
