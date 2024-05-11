age = int(input("What is your age? "))

while  True:
    if age <= 2:
        print("The ticket is free!")
    if age >= 3 and age <= 12:
        print("The ticket is $10")
    if age >= 13:
        print ("The ticket is $15")
    break

