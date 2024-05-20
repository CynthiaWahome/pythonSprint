file_path = '/home/abel/Documents/projects/pythonSprint/chapter_9/python_work/text_files/pi_digits.txt'

with open(file_path) as file_object:
    #contents = file_object.read()
    #print(contents.rstrip())
    print("\n Start loop--------------\n")
    for line in file_object:
        print(line)


with open(file_path) as file_1:
    lines = file_1.readlines()
    print(lines)

pi_string = ''

for line in lines:
    #print(line.rstrip())
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

#irthday = input("your birthday: mmddyy")

#if birthday in pi_string:
#   print("Your birthday exists in first mil")
#else:
#   print("We ishia buana")


with open(file_path, 'a') as file_2:
    file_2.write("I love Programming")
    file_2.write("Cynthia loves me")
    
