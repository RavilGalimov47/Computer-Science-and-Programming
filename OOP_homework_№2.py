class Product:
    def __init__(self, name, product_id, price, rating, stock):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.rating = rating
        self.stock = stock

    def add_stock(self, quantity):
        self.stock += quantity

    def remove_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
        else:
            print("Not enough stock available")

    def update_rating(self, new_rating):
        self.rating = new_rating

    def update_price(self, new_price):
        self.price = new_price

class Category:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product_id):
        for item in self.items:
            if item.product_id == product_id:
                self.items.remove(item)

    def get_item(self, product_id):
        for item in self.items:
            if item.product_id == product_id:
                return item

class Basket:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product_id):
        for item in self.items:
            if item.product_id == product_id:
                self.items.remove(item)

    def get_item(self, product_id):
        for item in self.items:
            if item.product_id == product_id:
                return item

    def make_purchase(self, product_ids):
        purchased_items = []
        for product_id in product_ids:
            for item in self.items:
                if item.product_id == product_id:
                    purchased_items.append(item)
                    self.items.remove(item)
                    break
        print("Purchased items:")
        for item in purchased_items:
            print(item.name)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.basket = Basket()

# Пример использования
product1 = Product("Laptop", 1, 1000, 4.5, 10)
product2 = Product("Phone", 2, 500, 4.0, 20)

category1 = Category("Electronics")
category1.add_item(product1)
category1.add_item(product2)

user1 = User("user1", "password1")
user2 = User("user2", "password2")

user1.basket.add_item(product1)
user1.basket.add_item(product2)
user1.basket.make_purchase([1, 2])
