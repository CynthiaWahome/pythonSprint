"""THIS IS A DOC STRING COMMENT .. SHOULD BE AT THE TOP OF EVERY MODULE YOU CREATE TO SHOW WHAT IT DOES"""

from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
