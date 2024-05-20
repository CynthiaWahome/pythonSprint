class User():
    def __init__(self, first_name, last_name,age,location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print("\n\t\tName: " + self.first_name, self.last_name + "\n\t\tAge: " + str(self.age) + "\n\t\tLocation: " + self.location)

    def greet_user(self):
        print("\t\tHello there", self.first_name, self.last_name + "! \n----------------------------------------------------------------------------")

