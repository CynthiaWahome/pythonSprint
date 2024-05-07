cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

print("this sis the end of the loop")

requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("hold the mushrooms")

my_age = 16
your_age = 14

if my_age >= 18 or your_age <=14:
    print("We are meant to be")
else:
    print("oopsie")

if "audi" in cars:
    print("Got that in my collection")
else:
    print("Will get that one")

