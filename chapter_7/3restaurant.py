class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Karibu sana to ", self.restaurant_name, " offering",  self.cuisine_type)

hotel_1 = Restaurant('Nagasaki', 'Japanese Cuisine')
hotel_2 = Restaurant('Yokozuna', 'Korean Cuisine')
hotel_3 = Restaurant('ShakaZulu', 'Ghananian Cuisine')

print("My favourite joint is called " + hotel_1.restaurant_name.upper() + "!")
print(hotel_1.restaurant_name.title() + " serves only " + hotel_1.cuisine_type) 
hotel_1.describe_restaurant()

print("\nMy second favorite joint is the famous " + hotel_2.restaurant_name.upper() + "!")
print("The " + hotel_2.restaurant_name.title() + "serves the best " + hotel_2.cuisine_type + "in town!")
hotel_2.describe_restaurant()

print("\nMy bestie really loves " + hotel_3.restaurant_name.title() + "!")
print("She claims that "+ hotel_3.restaurant_name.title() + "has the best " + hotel_3.cuisine_type.upper() + " in East Africa!")
hotel_3.describe_restaurant()



