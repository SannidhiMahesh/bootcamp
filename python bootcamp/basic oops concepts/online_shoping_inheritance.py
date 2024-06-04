class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class BillingProcess(ShoppingCart):
    def generate_bill(self):
        total_amount = self.calculate_total()
        print("Generating bill...")
        print("Items in the cart:")
        for item in self.items:
            print(f"- {item.name}: ${item.price}")
        print(f"Total amount: ${total_amount}")
        return total_amount

# Example usage
cart = BillingProcess()

while True:
    item_name = input("Enter the name of the item (or 'done' to finish): ")
    if item_name.lower() == "done":
        break
    item_price = float(input("Enter the price of the item: "))
    item = Item(item_name, item_price)
    cart.add_item(item)

total_bill = cart.generate_bill()