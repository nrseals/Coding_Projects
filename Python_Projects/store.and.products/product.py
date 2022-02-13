class Product:
    # Constructor
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        print(f"Product created: {self.name}")
    # update price method
    def update_price(self, precent_change, is_increased):
        if is_increased:
            self.price += (self.price * precent_change)
        else: 
            self.price -= (self.price * precent_change)
    # print info method
    def print_info(self):
        print(f"Name: {self.name}, Category: {self.category}, Price: ${self.price}")