#design and create an online store for products(name, price)
#track total products being created ----- done
#create a static method to calculate the discount on each product based on a % parameter

class Store():
    products = {}
    total_products = 0
    def __init__(self):
        print("Welcome to Saravana Stores")
        for i in Store.products.items(): 
            print (i)
    def add_product(self,name,price):
        Store.products[name] = price
        Store.total_products+=1
    @staticmethod
    def discounted_price(price, discount_percent):
        final_price = price - ((discount_percent*price)/100)
        print(final_price)
        
    # pretty useless function 

Apple = Store()
Apple.add_product("macbook air m1",500)
Apple.add_product("macbook air m2",600)
Apple.add_product("macbook air m3",700)
Apple.add_product("macbook air m4",750)
Apple.add_product("macbook pro m2",1000)
print(Store.total_products)


