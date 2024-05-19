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

    def show_priviledges(self):
        print("These are the admin priviledges",self.priviledges)

admin = Admin("Cynthia", "Wahome",29,"Washington DC")
print(admin, admin.show_priviledges())
