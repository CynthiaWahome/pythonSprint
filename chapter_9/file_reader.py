file_path = '/home/abel/Documents/projects/pythonSprint/chapter_9/python_work/text_files/pi_digits.txt'

with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
