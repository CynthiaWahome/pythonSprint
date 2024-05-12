def format(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name

    return full_name.title()

#print(format("abel", "morara", middle_name="matunda"))
#output = format("abel", "morara", "matunda")
#print(output)

while True:
    f_name = input("\nPlease enter your first name: ")
    l_name = input("\n PLease enter your last name: ")

    guest = format(f_name, l_name)

    print("Hello", guest, "Welcome to the partye")
    break
    
