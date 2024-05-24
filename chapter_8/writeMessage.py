filename = 'guest.txt'

birthday = input("When is your birthday? ")
with open(filename,'w') as file_object:
    file_object.write(birthday)