
# file_path ='\C:\Users\Wamzy\Documents\myProjects\pythonSprint\chapter_8\learningPython.txt'
# use raw strings by prefixing the string with r.
file_path = r'C:\Users\Wamzy\Documents\myProjects\pythonSprint\chapter_8\learningPython.txt'

# read an entire file
print(".............................................\n\t\tThis reads an entire file: ")
with open(file_path) as fileObject:
    contents = fileObject.read()
    print(contents)


# read line by line
print(".............................................\n\t\t This reads line by line: ")
with open(file_path) as fileObject:
    for line in fileObject:
        print(line)


# make list of lines
print(".............................................\n\t\t This makes a list of items: ")
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# replace
with open(file_path) as file_object:
    contents = file_object.readlines()
    contents = contents.replace('python','C')

    for content in contents:
        print(content)
        
    # STUCK AT REPLACE PAGE 230