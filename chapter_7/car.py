class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has", str(self.odometer_reading), "miles")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer")

    def increase_odometer(self, miles):
        self.odometer_reading = self.odometer_reading + miles
        #self.odometer_reading += miles



my_new_car = Car('audi', 'a4', 2014)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 50
my_new_car.read_odometer()

my_new_car.update_odometer(20)
my_new_car.read_odometer()

my_new_car.increase_odometer(1000)
my_new_car.read_odometer()


