class Product:
    def __init__(self, name, quantity, cost_price):
        self.name = name
        self.quantity = quantity
        self.cost_price = cost_price

class Inventory:
    def __init__(self, name):
        self.name = name
        self.products = {}
        self.low_stock_threshold = 2
    
    def add_product(self, product):
        if product.name in self.products:
            self.products[product.name].quantity += product.quantity
        else:
            self.products[product.name] = product
    
    def check_inventory(self):
        low_stock_products = []
        for product in self.products.values():
            if product.quantity <= self.low_stock_threshold:
                low_stock_products.append(product.name)
        return low_stock_products

class Sales:
    def __init__(self, name):
        self.name = name
        self.daily_sales = 0
    
    def record_sale(self, product_name, quantity, selling_price):
        if product_name in self.products:
            self.products[product_name].quantity -= quantity
            self.daily_sales += quantity * selling_price
        else:
            print(f"Product {product_name} not found in inventory")

class StoreManagement(Inventory, Sales):
    def __init__(self, name):
        super().__init__(name)
    
    def calculate_profit(self):
        total_cost = 0
        for product in self.products.values():
            total_cost += product.quantity * product.cost_price
        return self.daily_sales - total_cost

store = StoreManagement("My Store")

shirt = Product("Shirt", 300, 30000)
pants = Product("Pants", 50, 10000)
bag = Product("bag", 30, 2000)

store.add_product(shirt)
store.add_product(pants)
store.add_product(bag)

store.record_sale("Shirt", 200, 850)
store.record_sale("Pants", 50, 700)
store.record_sale("bag", 20, 200)

low_stock_products = store.check_inventory()
print("Low stock products:", low_stock_products)

profit = store.calculate_profit()
print("Todays Profit: ", store.daily_sales)
print("Total profit:", profit)