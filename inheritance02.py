#childclass constructor example ->2

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price  = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self,os,ram):
        print("Inside smartphone constructor")
        self.os = os
        self.ram = ram

o2 = SmartPhone("Android",16)
o2.price   #here we donot acces this

