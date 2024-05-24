filename = 'guest_book.txt'

name = input ("What is your name? ")

while True:
    print("Hello", name)
    break
with open (filename, 'w') as file_object:
    file_object.write(name)