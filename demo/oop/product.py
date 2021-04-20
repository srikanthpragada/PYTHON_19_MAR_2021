class Product:
    tax = 12

    def __init__(self, name, price, qoh=0):
        self.name = name
        self.price = price
        self.qoh = qoh

    def purchase(self, qty):
        self.qoh += qty

    def sell(self, qty):
        self.qoh -= qty

    @property
    def sellingprice(self):
        return self.price + (self.price * Product.tax / 100)


p = Product("Product1", 10000, 10)
print(p.sellingprice)
