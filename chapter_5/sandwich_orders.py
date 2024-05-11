sandwich_orders = ['Peanut butter and Cheese', 'Tuna','Bread and Ham', 'Sandwich beef', 'Sandwich chicken']
finished_sandwiches = []


while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("I made you a sandwich.Its "+ current_order.upper()+" you fav. Bon Appetite!")

    finished_sandwiches.append(current_order)
    print("The following sandwiches have been made ", finished_sandwiches,"\n")
