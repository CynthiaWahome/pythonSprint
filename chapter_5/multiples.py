prompt = int(input("Guess a number: "))

if prompt % 10 == 0:
    print(f"{prompt} is a multiple of 10")

else:
    print(f"{prompt} is not a multiple of 10")