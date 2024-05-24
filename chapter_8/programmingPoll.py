
filename = 'responses.txt'

reasons = [" "]
active = True
while active:
    print ("Enter q to quit")
    reasons = input("Why do you like programming? ")

    if reasons == 'q':
        active = False

    else:
        repeat = (input("Do you have another reason? (y/n) "))
        if repeat == 'n':
            break
        # if repeat != 'y':
        #     continue

    if reasons != 'q':
        with open (filename, 'a') as file_object:
            file_object.write(reasons + '\n')

# The last repeated responses is not being printed why???