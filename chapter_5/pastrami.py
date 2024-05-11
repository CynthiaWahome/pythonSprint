sandwich_orders = ['Peanut butter and Cheese', 'Pastrami', 'Tuna','Bread and Ham', 'Pastrami', 'Sandwich beef', 'Sandwich chicken', 'Pastrami']
finished_sandwiches = []

print("Unfortunately, Cafe Deli has run out of Pastrami")
print("--------------------------------------------------------------------------")

while'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("\n\t\t\tI made you a sandwich.Its "+ current_order.upper()+" you fav. Bon Appetite!\n")
    print("\t\t****************************************************************************************\n")

    finished_sandwiches.append(current_order)
    print("The following sandwiches have been made:\n", finished_sandwiches,"\n")
    print("---------------------------------------------------------------------------------------------------------------------------")

# What if the occurrences of pastrami have different case eg PASTRAMI and pastrami?