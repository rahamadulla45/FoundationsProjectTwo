# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!
        self.products = []
        self.name = name

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        for p in self.products:
            print (p)


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        # your code goes here!
        return "       Product Name: %s \n       Description: %s \n       Price: %d KWD\n" % (self.name, self.description, self.price)


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        self.products = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.products.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total = 0
        for p in self.products:
            total += p.price

        return total

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!
        print ("Here's your receipt: ")
        for p in self.products:
            print (p)

        print ()
        print ("The total price is " +"KD"+str(self.get_total_price()))

    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!
        print ()
        self.print_receipt()

        exit = False

        select = input("Confirm?(yes/no)")

        while exit != True:

            if select.lower() == "yes":
                print ("Your order has been placed.")
                exit = True
            elif select.lower() == "no":
                print ("Your order has been cancelled")
                exit = True
            else:
                print ("Invalid input please try again: ")
                select = input()

