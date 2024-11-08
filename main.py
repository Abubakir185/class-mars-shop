class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shop:
    def __init__(self):
        self.products = []
    
    def addProduct(self, product):
        self.products.append(product)

class Cart:
    def __init__(self):
        self.products = []
        self.totalPrice = 0

    def addProduct(self, shop, name, quantity):
        for p in shop.products:
            if p.name == name:
                product = p
        self.totalPrice += product.price * quantity
        self.products.append(product)

    def checkout(self):
        checkout = []
        for p in self.products:
            checkout.append(f"{p.name}: {p.price}")
        return checkout

    def buy(self):
        self.products = []
        self.totalPrice = 0
        print("thanks for pursaching!")

    def clear(self):
        self.products = []
        self.totalPrice = 0

mouse = Product("mouse", 250)
mars_shop = Shop()
cart = Cart()

mars_shop.addProduct(mouse)
cart.addProduct(mars_shop, "mouse", 3)
print(cart.totalPrice) 
print(cart.checkout())
cart.buy()
