import sandwiches
sandwiches.sandwich_orders('peas','beans','bread','peanut butter')

from sandwiches import sandwich_orders
sandwich_orders('banana','kiwi','apple','pineapple')

from sandwiches import sandwich_orders as so 
so('roof', 'window', 'door','mirror')

import sandwiches as sw 
sw.sandwich_orders('Russia', 'Ukraine','Iraq', 'Israel')

from sandwiches import *
sandwiches.sandwich_orders("Chelsea", 'Arsenal','Machester','Barcelona')