class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 20

# define method get_descriptive_name and put the cars attribute into one string
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

# define a new method to read the cars mileage
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

# pass  a new value to a method that handles the updating interally, instead of accessing the attribute directly

# add a logic to make sure that no one tries to roll back the ofdometer reading
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back the odometer!")

# increase an attributes value by a certain amount rather than set an entirely new value
    def increment_odometer(self, miles):
        self.odometer_reading += miles


 # create a child class
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
# defning attributes and methods for the child class

        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "KWH battery")


# Instances as Attributes
# Define a new class tha doesnt inherit from any other class

class Battery():
    def __init__(self, battery_size=90):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWH battery")
    
    def upgrade_battery(self, battery_size = 85):
        print("Battery size :",self.battery_size)

    def get_range(self):



# STUCK page 178
       

# my_tesla = ElectricCar('tesla','model,',2020)
# my_tesla.battery.upgrade_battery()