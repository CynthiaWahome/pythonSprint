magicians = ["JOy", "Effie", "Sharon", "Ken"]

def show_magicians(magicians_list):
    for magician in magicians_list:
        print(magician)


#show_magicians(magicians)

def make_great(magicians_list):
    counter = 0
    while counter < len(magicians_list):
        magicians_list[counter] = magicians_list[counter] + " is great"
        counter += 1

    print(magicians_list)


#make_great(magicians[:])

make_great(magicians)

show_magicians(magicians)
