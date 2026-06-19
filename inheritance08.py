#use of super in inheritance 
#super cannot access attributes of the class 
#it used inside child class not outside
#it only access the constructor and method of the class 

# class Phone:
#     def __init__(self,price,brand,camera):
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print("Phone class")


# class SmartPhone(Phone):
#     def buy(self):
#         print("SmartPhone class")
#         #syntax to call parent ka buy method
#         super().buy()



# o1 = SmartPhone(20000,"Android",13)

# o1.buy()



# class Phone:
#     def __init__(self,price,brand,camera):
#         print("we want to buy a phone")
#         self.price = price
#         self.brand = brand
#         self.camera = camera



# class SmartPhone(Phone):
#         def __init__(self,price,brand,camera,os,ram):
#             print("we want to buy SmartPhone")
#             #it redirect to the base class constructor
#             super().__init__(price,brand,camera)
#             self.os =  os
#             self.ram = ram
#             print("we want to buy a SmartPhone")



# o1 = SmartPhone(20000,"vivo",12,"Android",16)



#as we know that the if child class contain the constructor then constructor of the parent class would not be called but here we use the concept of the super so it also called and initializes the parent class attributes
# class Parent:
#     def __init__(self,num):
#         self.__num = num
    
#     def get_num(self):
#         return self.__num
    

# class Child(Parent):
#     def __init__(self,num,val):
#         super().__init__(num)
#         self.__val = val

#     def get_val(self):
#         return self.__val
    

# o1 = Child(100,200)
# print(o1.get_num())
# print(o1.get_val())



# class Parent:
#     def __init__(self):
#         self.num = 100

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.val = 200

#     def display(self):
#         print(self.num)
#         print(self.val)

# o1 = Child()
# o1.display()








