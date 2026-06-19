class Product:
    def review(self):
        print("your is product is very beneficial")

class Phone(Product):
    def __init__(self,price,brand,camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("camera build quality is much better")

class SmartPhone(Phone):
    pass


o1 = SmartPhone(20000,"Android",10)
o1.review()
o1.buy()