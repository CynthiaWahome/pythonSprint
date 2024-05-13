#way 1

#import pizza

#pizza.make_pizza(16, 'pepperoni')
#pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Way 2

#from pizza import make_pizza

#make_pizza(16, 'pepperoni')
#make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#using as to give a function an alias

#from pizza import make_pizza as mp

#mp(16, 'peperoni')


# giving a moule an alias 

#import pizza as p

import pizza as p

p.make_pizza(16, 'peperoni')
