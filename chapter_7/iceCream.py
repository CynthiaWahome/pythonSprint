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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavour = 'vanilla'

    def display_flavours(self):
        print("The flavour of this ice cream is: ",self.flavour)
        



my_icecream = IceCreamStand("Cold Stone","Icecream palor")
my_icecream.describe_restaurant()
my_icecream.display_flavours()


