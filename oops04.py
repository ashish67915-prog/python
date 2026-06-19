class Person:
    def __init__(self,name_input,country_input):
        self.name = name_input
        self.country = country_input
    
    def greet(self):
        if self.country == "india":
            print("namaste",self.name)

        else:
            print("hello",self.name)



p1 = Person("ashish","india")
p1.greet()
print(p1.country)
print(p1.name)


#ye jaruri nhi ki class member andar hi bane bahar bhi ban skte hai object ki madad se

p1.gender = "male"

print(p1.gender)

#here the p1 is not actually the object it can store only the mememory address of the object
p2 = p1
print(p1.name)
print(p2.name)
p2.name = "arpit"
print(p1.name)
print(p2.name)