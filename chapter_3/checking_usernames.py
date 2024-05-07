current_users = ["Abel", "Admin", "joy", "Effie", "Cynthia", "John"]

new_users = ["Mwathi", "Njung\'e", "Kimani", "ruraciu", "Abel", "Joy", "JOHN"]


for new_user in new_users:

    if new_user.lower() in [current_user.lower() for current_user in current_users]:
        print(new_user, "HAS ALREADY BEEN TAKEN, YOU NEED TO ENTER A NEW USERNAME")

    else:
        print(new_user, "is available, thank you for choosing us")

