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

class Admin(User):
    def __init__(self,first_name,last_name,age,location):
        super(). __init__(first_name,last_name,age,location)
        self.priviledges = "can add post", "can delete post", "can ban user"

        

# user_1 = User('George', 'Washington' , 20 ,'Ontorio, Canada')
# user_1.describe_user()
# user_1.greet_user()

# user_2 = User('Tina','Tunner', 16, 'Ohio, Texas')
# user_2.describe_user()
# user_2.greet_user()

# user_3 = User('Brittney', 'Spears', 20, 'Las Vegas, USA')
# user_3.describe_user()
# user_3.greet_user()