players = ["Michael", "John", "Ahab", "Cynthia", "Joseph"]
#my_team = players[1:4]
#my_team = players[:2]
#my_team = players[2:]
my_team = players[-3:]
print(my_team)

#looping through a slice

for player in players[-3:]:
    print(player, "is the best guy")
