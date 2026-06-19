class Parent:
    def __init__(self,num):
        self.__num = num
    
       
    def get_num(self):
        return self.__num
    
class Child(Parent):

    def show(self):
        print("this is the child class")


o1 = Child(100)
#by using getter we can access the private member it returns the private member
print(o1.get_num())
