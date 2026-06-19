#agar child class ka constructor bana hai to vo parent class ke constructor ko call nhi karega 
#vo kewal child constructor called hoga aur usi ka attribute assing honge 
#es case me child class me val assing hoga jisse jb hm get_num() ko call karenge to error dega


class Parent:
    def __init__(self,num):
        self.__num = num


    def get_num(self):
        return self.__num
    

class Child(Parent):
    def __init__(self,val,num):
        self.__val = val


    def get_val(self):
        return self.__val
    
o1 = Child(10,20)
# print(o1.get_num())
print(o1.get_val())
