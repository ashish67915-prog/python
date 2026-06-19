class Phone:
    def __init__(self,price,brand,camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("i want only love and care from by sweatheart because she did not know that i want that she always smile and looking beautiful")

class SmartPhone(Phone):
    pass


o1 = SmartPhone(24000,"Android",10)
o1.buy()
