filename = 'alice.txt'

try:
    with open(filename, 'r') as file_object:
        content = file_object.read()
        #print(content)

except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist"
    print(msg)

else:
    words = content.split()
    num_words = len(words)
    
    print("The file", filename, "has about", num_words, "words")

