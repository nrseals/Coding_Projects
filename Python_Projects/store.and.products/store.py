from product import Product
class Store:
    #constructor
    def __init__(self, name):
        self.name = name
        self.products = []
    #add product method
    def add_product(self, new_product):
        self.products.append(new_product)
        print(f"Product added: {new_product.name}")
    def show_products(self):
        print(f"List of products at {self.name}")
        for product in self.products:
            product.print_info()
    # sell_product
    def sell_product(self, id):
        sold_product = self.products[id]
        print("Product sold!")
        sold_product.print_info()
        self.products.pop(id)
    #inflation method
    def inflation(self, precent_increase):
        for product in self.products:
            product.update_price(product, precent_increase, True)
    # Set Clearance method
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(product, percent_discount, False)

# Test
bestBuy = Store("Best Buy")
print("*"*50)
print(bestBuy.name)
print("*"*50)
mbp = Product("MacBook Pro", 1299.99, "Computer")
xbox = Product("Xbox One", 599.99, "Gaming")
stereo = Product("Bose stereo", 699.99, "Home audio")
print("*"*50)
bestBuy.add_product(mbp)
bestBuy.add_product(xbox)
bestBuy.add_product(stereo)
print("*"*50)
bestBuy.show_products()
print("*"*50)
bestBuy.sell_product(0)
print("*"*50)
bestBuy.show_products()