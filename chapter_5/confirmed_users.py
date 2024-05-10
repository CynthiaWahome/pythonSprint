unconfirmed_users = ['Alice', 'Johnes', 'Brian', 'Candy']

confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user:", current_user.title())
    confirmed_users.append(current_user)
    print(confirmed_users)

