def display_message():
    print("I am learning python")
display_message()

# Positonal parameter
def favorite_book(title):
    print("One of my favorite books is ",title)

favorite_book("Alice in wonderland")

# Arguments and parameters
def fav_book(title,author):
    print("My fav book is",title,"its authored by",author)

# Positonal argument
fav_book("Rich dad, poor dad","Robert Kyosaki")

# Keyword Arguments
fav_book(author="Mark Mason", title="The subtle art of not giving F***")

# default values
def fav_food(restaurant, food = 'chicken'):
    print("My favorite food is",food,"offered in", restaurant)

fav_food('Kempinski')

