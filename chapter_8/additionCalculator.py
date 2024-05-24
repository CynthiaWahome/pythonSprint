
while True:
        first_num = input("First number: ")
        second_num = input("Second number: ")


        answer = int((first_num + second_num))
    
    except (TypeError, ValueError):
        print("Please insert a number")

    else:
        print(answer)

# STUCK page 119