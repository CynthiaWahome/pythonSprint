def sandwich_orders(*toppings):
    print("\nThis sandwich has: ")

    for topping in toppings:
        print("-" + topping)


sandwich_orders('brawn','bread', 'lettuce','tomatoe',)
sandwich_orders('chicken','mushroom','bread','peanut butter')
sandwich_orders('hash browns')