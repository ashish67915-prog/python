class Phone:
    def __init__(self,price,brand,camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("nature is the most beautiful thing but a girl  right intention,support and emotion toward any person is more beautiful than nature")


class SmartPhone(Phone):
    pass

class FeaturePhone(Phone):
    pass 


o1 = SmartPhone(20000,"Android",10)

o1.buy()