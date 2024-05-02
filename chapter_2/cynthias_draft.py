# message = "Hello World"
# print(message)

# new_message = "This is my first line of python"
# print(new_message)

# name = "Cynthia Wahome"
# print(name.title())
# print(name.upper())
# print(name.lower())
# print(name.capitalize())

# 2.3 Personal message
# message = "Hello, Eric, would you like to learn some Python today!"
# print(message)

# famous_person = "Albert Einstein"
# print("\t\t\t",famous_person, "once: said, \"A person who made a \n\t\t\tmistake never tried anythng new \"")

# popular_singer = "Chris Martin"
# print("\t\t\t",popular_singer,"I hear Jeruslem bells ringing \n\t\t\tRoman calvary choirs are singing\"")

# black_president = "   Barack Obama   "
# worst_president = "Donald Trump"
# print("\t\t\t",black_president)
# print(worst_president,"\n\t\t\t" "of all time" )

# best_food = "  KCF"
# worstest_food = "Money follow me   "
# soul_food = "Music is good for the soul"
# print("What is your best food?,", best_food)
# print("The type of food I dont like is:",worstest_food)
# print(" The best kind of food is?",soul_food)
# print("\n\n\n")

#lstrip,rstrip,strip
# name = "\t\tJohn\t\tDoe\n "
# print(name)

# print("remove left", name.lstrip())
# print(f"remove right {name.rstrip()}")
# print("strip" + " " + name.strip())
# print("\n\n\n")

# names = ["Cynthia","Sylvia","Jane","Pius","James"]
# last_name = ['C.W.W.','S.Y.G.', 'A.M.M']
# print(names)
# print(last_name)

# greetings = "How do you do "
# print(greetings,names[0])
# print(greetings,names[1])
# print(greetings,names[2])
# print(greetings,names[3])
# print(greetings,names[4])

# fav_transportation = ["Motorcycle","Car","Bicycle","Train","Bus"]
# print("I would like to ride a ",fav_transportation[0])
# print("I would like to own a ",fav_transportation[1])
# print("I would like to ride a ",fav_transportation[2])
# print("I would like to board a ",fav_transportation[3])

# print("\n\n\n\n")
# guest_list = ["Viola","Michou","Imani","Jenkins"]
# print("Welcome to dinner,",guest_list[0])
# print("Welcome to dinner,",guest_list[2])

# guest_list.append("Matunda")
# guest_list.insert(1, "Markos")


# print("Karibu sana",guest_list[2])
# print("Boonjour!",guest_list[4])
# print("\n\n\n")
# print(guest_list)

# guest_list.pop(1)

# print(guest_list)
# del guest_list [1], guest_list[-1]
# print(guest_list)
# print("\n\n\n\n")

# weekday = "Monday and Friday"
# print("Hello " + weekday)
# print(f"Hello {weekday},\n Looking forward to a good time!")
# print("Hello",weekday, "Thrilled to have you here!")
# print("Hello {} Super stoked to have you here!",format(weekday))

# num = list(range(1,21))
# print(num)

# numbers = list(range(1,11))
# for number in numbers:
#     print(number)

# oddnumbers
# numbers = list(range(1,11))
# print(max(numbers),min(numbers))

# numbers = list(range(1,11,2))
# for number in numbers:
#     print(number)

# multiples of 3
# numbers = list(range(3,31,3))
# for number in numbers:
#     print(number)

# cube
# numbers = list(range(1,11))
# for number in numbers:
#     print(number **3)

# List comprehension
# numbers = [number**3 for number in range(1,11)]
# print(numbers)

# Lists
items = ["Window","Doors","Roof","Cabinet","Table"]
items.append("Bulb")
items.insert(0,"Bathroom")
print(items)
# items.pop()

# print individual lines of items
# for item in items:
#     print("Which are the elements of a house?",item)

#sort in ascending order. does not revert to original
# items.sort()
# print(items)

# sort in descending order
# items.sort(reverse=True)
# print(items)

# sorted sorts once, reverts to original 
# print(sorted(items))
# print(items)

#sort in reverse. last becomes first and so on
# items.reverse()
# print(items)

#length of entries in a list
print("The number of items in this list is: ",len(items))

# use sort and reverse
items.sort()
print(items)
reverse_sort=items.reverse()
print(items)


