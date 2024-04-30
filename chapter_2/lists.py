pals = ["Abel","effie","Lucy","victor","Martin","Teddy", 8, 6.34]
print(pals[0],"is apparently a good friend")
print(pals[6], "is a good number")
print(pals[-3], "is my good friend")
print(pals[-3].upper(), "is my good friend")
print(pals[2].lower(), "anything about her")
print(pals[3].title())
print(pals[1].capitalize())
pals[0] = "Matunda" # change values in a list
print(pals)
pals.append("Wambui")
print(pals)

# Fruits append
fruits = []
fruits.append("Banana")
fruits.append("Pineapple")
fruits.append("Apple")
fruits.append("Apple")
fruits.insert(0,"Avocado")

# Delete
# del fruits[1]
fruits.pop(1) #removes the last entry by default
hated_fruit = fruits.pop(1)
print(hated_fruit)

# Remove
fruits.remove("Apple")
print(fruits)