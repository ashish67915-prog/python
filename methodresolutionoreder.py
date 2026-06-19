class Phone:
    def __init__(self,price,brand,camera):
        self.price = price
        self.brand = brand
        self.camera = camera
        
    def buy(self):
        print("buy a phone")

class Product:
    def buy(self):
        print("buy a product")

#method resolution order (esme hmm dekhte hai jo order me pehle hoga vahi execute hoga)
class SmartPhone(Product,Phone):
    pass


o1 = SmartPhone(150000,"Apple",13)

o1.buy()