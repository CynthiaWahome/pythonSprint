def make_shirt(size,message):
    print("Function 1: \n\t\tThis t-shirt is of size",size,"\n\tIt should be printed:",message)
make_shirt("XL","Straight Outta Campton!")

def order_shirt(a,b):
    print("\nFunction 2: \n\t\tThis is a size",a,"its",b)
order_shirt("XL", "red in colour")

def buy_shirt(size= 'Large' ,design ='I love PYTHON!'):
    print("\nFunction 3: \n\t\tMy tshirt is",size,"it says",design)
buy_shirt()
buy_shirt("Medium")