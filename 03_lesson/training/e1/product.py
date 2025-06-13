class Product:
    def __init__(self, name, price):
        self.productName = name
        self.cost = price

    def get_name(self):
        return self.productName

    def get_price(self):
        return self.cost

    def get_info(self):
        return f"Product: {self.productName}, Price: {self.cost}"
