class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone class")
        self.__price = price
        self.brand  = brand
        self.camera = camera

    def __show(self):
            print(self.__price)

class SmartPhone(Phone):

    def display(self):
        print(self.__price)

o1 = SmartPhone(150000,"Apple",13)
#we donot use the private memeber of the class 
o1.show()
#child class can't access the private member of the class
o1.display()
