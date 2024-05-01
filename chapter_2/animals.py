animals = ["Cynthia", "dog", "Cat", "cow"]
animals.append("donkey")

animals.insert(0, "rackoon")

print(animals)

#for animal in animals:
#    print(animal)

#for animal in animals:
#    print(f"A {animal} would be a great pet")

for animal in animals:
    print("A {} would be a great pet \n".format(animal))
print("any of these would make a great pet")

