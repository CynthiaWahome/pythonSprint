#div_num = input("Enter number to divide by 5 \n")

while True:
    div_num = input("Enter a num to div by 5 \n\t")    
    try:
        result = 5/int(div_num)
    except ZeroDivisionError:
        print("Cannot divide 5 by 0")
        break
    except ValueError:
        print("Please enter a number value")
    else:
        print(result)
        break




