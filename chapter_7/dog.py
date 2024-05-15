class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " just rolled over")




chihuahua = Dog('abel', 20)
print("My dogs name is ", chihuahua.name.title())
print("My dogs age is", str(chihuahua.age), "years old")


chihuahua.sit()
chihuahua.roll_over()

your_dog = Dog("Cynthia", 16)
your_dog.sit()
your_dog.roll_over()
