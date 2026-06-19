class Phone:
    def __init__(self,price,brand,camera):
        self.price = price
        self.brand = brand
        self.camera = camera


    def buy(self):
        print("buy a phone")

class Product:
    def review(self):
        print("customer review")


class SmartPhone(Phone,Product):
    pass

o1 = SmartPhone(25000,"Android",13)
o1.buy()
o1.review()