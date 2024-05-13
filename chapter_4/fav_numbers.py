fav_numbers = {
    'Abel': 3, 
    'Matunda': 2, 
    'Morara': 4
    }

print (fav_numbers)

# modify so each person has more than 1 fav number
fav_numbers['Hannah'] = 4, 7, 9, 4 # new member

fav_numbers.update({"Abel" : (9, 5, 7, 1)}) # How do I avoid the overwrite?
print(fav_numbers)