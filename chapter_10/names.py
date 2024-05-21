from name_function import get_formatted_name as format_name
#import get_formatted_name as format_name from name_function

print("Enter q to quit")

while True:
    first = input("\nPlease give me your fiest name: ")
    if first == 'q':
        break

    middle = input("\nPlease enter your middle name [optional]: ")
    if middle == 'q':
        break

    last = input("\nplease enter last name: ")
    if last == 'q':
        break

    formatted_name = format_name(first, last, middle)
    print("\n\nYou neat name", formatted_name)
