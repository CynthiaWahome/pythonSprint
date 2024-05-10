prompt = "\n Tell me something and I will repeat it back to you\n Enter 'quit' to end the program: \t"

active = True

message = ""

while active:
    message = input(prompt)

    if message == "quit":
       # active = False
       break
    else:
        print(message)


print("USer has entered quit and flag has been set to false terminating the program")
