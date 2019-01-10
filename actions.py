# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.achoo.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for s in stores:
        print ("- " + s.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for s in stores:
        if s.name == store_name:
            return s
        
    return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
    select = input("Pick a store by typing its name. Or type 'checkout' to pay your bills and say your goodbyes. \n")
    print ("----------------------------------------")

    while select != "checkout":
        for s in stores:

            if select.lower() == s.name.lower():
                return s
            
        print ("No store with that name. Please try again.")
        
        select = input()
    return select


def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    print ()
    print (picked_store.name + ": ")
    print ()
    picked_store.print_products()

    select = input("""Pick an items you'd like to add in cart by typing the product name exactly as it was spelled above.
Type "back" to go back to the main menu where you can checkout.\n""")

    

    while select != "back":

        for p in picked_store.products:

            if select.lower() == p.name.lower():
                cart.add_to_cart(p)
                
        select = input()
            
            

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    s = pick_store()
    while s != "checkout":
        pick_products(cart, s)
        s = pick_store()
    cart.checkout()

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)