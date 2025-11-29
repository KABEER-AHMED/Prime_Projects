#design and create an online store for products(name, price)
#track total products being created ----- done
#create a static method to calculate the discount on each product based on a % parameter

class Store():
    products = {}
    total_products = 0
    def __init__(self):
        print("Welcome to Saravana Stores")
    def add_product(self,name,price):
        Store.products[name] = price
        Store.total_products+=1
    @staticmethod
    def discounted_price()