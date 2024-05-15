class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("We are", self.restaurant_name, "offering", self.cuisine_type, "Cuisine")

    def open_restaurant(self):
        print(self.restaurant_name.upper(), "is now open", "enter with", self.sum(), "dollars")

    def sum(self):
        my_bill = 1 + 1;
        print(my_bill)
        return my_bill



hotel_1 = Restaurant("Yokonagasaki", "Chinese")

print("\n\n------------EXCITING NEWS FROM-------", hotel_1.restaurant_name, "restaurant \n\n")

hotel_1.describe_restaurant()

print("\n")

hotel_1.open_restaurant()
