#here we understand the concept of method overriding 
#eska mtlb ye hota hai agar child class me essa method hai so as it is same hai parent class ke method se then it override that method and execute itself

class Phone:
    def __init__(self,price,brand,camera):
        self.price = price
        self.brand = brand
        self.camera = camera

        def buy(self):
            print("we want to buy a phone")

class SmartPhone(Phone):
    def buy(self):
        print("we want to buy a SmartPhone")


o1 = SmartPhone(150000,"apple",13)
o1.buy()