fav_hobbies = {
    'anna':'swimming',
    'abraham': 'cricket',
    'alice': 'cycling',
    'amos': 'hiking',
}
# assignment
fav_hobbies['bugs bunny'] : "watching cartoons"
fav_hobbies['brian'] : "programming"
fav_hobbies['bernard'] : "teaching algebra"
fav_hobbies['barbra'] : "singing in the shower"

print(fav_hobbies,"\n")

for people in sorted(fav_hobbies.keys()):
    print("Thank you",people.title(),"for telling us your hobby!")

for outdoor in fav_hobbies.values():
    print('\n'+ outdoor.lower())

# Check these again
# people_indoors = ["brian", "bernard","barbara","bugs bunny"]
# outdoors = ['cycling', 'cricket','hiking', 'swimming']


# Exra extra...read all about it :-)
# loop through a dictionaries keys in order
for name in sorted(fav_hobbies.keys()):
    print(name.upper() + ", that sounds so much FUN!")

# loop through all values in a dictionary
for name, hobby in fav_hobbies.items():
    print(name.title()+ "s favourite hobby is "+ hobby.upper(),"!!\n" )

# loop through all the keys in a dictionary
for name in fav_hobbies.keys():
    print("This is the Key: "+ name, "and this is the Value", fav_hobbies[name])

# loop through all the Key-Value Pairs
for name, hobby in fav_hobbies.items():
    print("\nKey: " + name)
    print("Value: " + hobby)

# loop through all the values 
print("\n\nThe following hobbies have been mentioned:")
for hobby in fav_hobbies.values():
    print(hobby.casefold())