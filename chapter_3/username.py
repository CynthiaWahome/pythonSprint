usernames = ["Abel","Admin", "mpoa", "Cynthia", "Lucy", "Joy"]

for username in usernames:
    if username.lower() == "admin":
        print("Hello", username, "Would you like to see the status report?")
    else:
        print("Hello", username, "Thank you for logging in again")
