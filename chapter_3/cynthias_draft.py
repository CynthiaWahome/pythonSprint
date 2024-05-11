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

# # Lists
# items = ["Window","Doors","Roof","Cabinet","Table"]
# items.append("Bulb")
# items.insert(0,"Bathroom")
# print(items)
# # items.pop()

# # print individual lines of items
# # for item in items:
# #     print("Which are the elements of a house?",item)

# #sort in ascending order. does not revert to original
# # items.sort()
# # print(items)

# # sort in descending order
# # items.sort(reverse=True)
# # print(items)

# # sorted sorts once, reverts to original 
# # print(sorted(items))
# # print(items)

# #sort in reverse. last becomes first and so on
# # items.reverse()
# # print(items)

# #length of entries in a list
# #print("The number of items in this list is: ",len(items))

# # use sort and reverse
# # items.sort()
# # print(items)
# # reverse_sort=items.reverse()
# # print(items)

# # check if sring is a paledrome string
# str = "abccba"

# str=str.casefold()
# #for casesensitive string

# str1 = reversed(str)
# #reversed the string

# if list(str) == list(str1):
#     print(str,"is a paledrome")
# else:
#     print("is not a paledrome")

# # String Sorting
# str = "Python programming is super easy to learn!"

# str1 = str.split()
# #split the string to words

# str1.sort()
# #sort the splitted words

# for words in str1:
#     print(words)

# # Give user input
# str = input("Enter a string: ")

# str1 = str.split()
# str1.sort()
# for words in str1:
#     print(words)

# # deleting items in a list

# p = [1,2,3,4,5,6,7,8,9,0]

# del p[2]
# print(p[:])

# del p[-3]
# print(p[:])

# p.remove(0)
# print(p[:])

# p.pop()
# print(p[:])

# p.clear()
# print(p[:])

# print("\n\n\n")
# c = [6,4,8,4,2,1,9,0]

# c.remove(4)
# print(c[:])

# c.sort()
# print(c[:])

# c.reverse()
# print(c[:])

# c.clear()
# print(c[:])

# foods = ["Rice","Spaghetti","Chapati","Ugali"]
# print("\nThis is a list of food: ",foods,"\n")
# print("\n\t\t\tI like",foods[0],"and maybe",foods[2],"a littu bit of", foods[3],"\n\t\t\tnot so much a fan of", foods[1],"\n")
# for food in foods:
#     print("We have:",food,"\n")
# print("\nThe price of",foods[0],foods[3],"is 50 USD")
# print("The most popular food is",foods[1],foods[2],"\nTheses would also cost a fortune btw\n")
# foods.append("Chicken curry")
# print("Appended list of foods:",foods,"\n")
# foods.insert(1,"Beef Stew")
# print("Insert a beefy stew at index 2: ",foods,"\n")
# famous_quote = "'Mimi ni Mukurima, nanyi Muzabibu, zaleni matunda iri mukure'"
# famous_quoter = "Martin Luther"
# print(f"{famous_quoter} once spoke gibberish and said {famous_quote} \n")

# Indentation


# password = input("Please type in a password: ")

# if password == "kittycat":
#     print("\n\tYou knew the password!")
#     print("\tYou must be either the intended user...")
#     print("\t...or quite an accomplished hacker.\n")
# print("The program has finished its executin. Thanks and bye!\n")

# Order of magnitude
# number = int(input("Please type in a number: "))

# if number < 1000:
#     print("This number is smaller than 1000")
# if number < 100:
#     print("This number is smaller than 100")
# if number < 10:
#     print("This number is smaller than 10")
# print("Thank you!")

# name = input("What is your name? ")

# # Soup or No soup
# if name != 'Jerry':
#     portions = int(input("How many portions of soup? "))
#     print("The total cost is",portions * 5.90,"\nNext please!")
# elif name == 'Jerry':
#     print

# # using break
# prompt = int(input("Which level do you want to play? (Choose from 1-10)\n (press 0 to quit) "))

# while True: 
#     if prompt == 0:
#         break
#     else:
#         print("Get ready for level", prompt)
#         break

# # letting user decided when to quit
# prompt_1 = "What is your favorite colour? "
# prompt_1 += "\n [Enter 'quit' to exit]\n"

# message = ""
# while message != 'quit':
#     message = input(prompt_1)
#     print(message)

# # Using flags
# prompt_1 = "What is your favorite colour? "
# prompt_1 += "\n [Enter 'quit' to exit]\n"

# active = True
# while active:
#     message = input(prompt_1)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# # Using break to exit a loop

# prompt_1 = "What is your favorite colour? "
# prompt_1 += "\n [Enter 'quit' to exit]\n"

# while True:
#     message = input(prompt_1)

#     if message == 'quit':
#         break
#     else:
#         print(message,"is a beautiful colour!")

# # using continue in a loop

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# Moving items from one list to another

# unconfirmed_users = ['alice', 'brian', 'candance']
# confirmed_users = []

# while unconfirmed_users:
#     currrent_user = unconfirmed_users.pop()

#     print("Veryfying user: " + currrent_user.title())
#     confirmed_users.append(currrent_user)
    
#     print("\nThe following users have been confirmed: ")
#     for confirmed_user in confirmed_users:
#         print(confirmed_user.title())

# # Removing all instances of specific values from a list

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# Filling a dictionary with user input

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")
     
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n-- Poll Results ---")
for name, response in responses.items():
    print(name + "would like to climb "+ response + ".")