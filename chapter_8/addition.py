try:
    first_num = int(input("Enter a number: "))
    second_num = int(input("Enter a second number: "))
    print(first_num + second_num)
    
except (TypeError, ValueError):
    print("Please insert a number")
