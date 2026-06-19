#instance variable -> it contain 1 or more than 1 memory at a time that make it different from the other variables
class Person:
    def __init__(self,user_name,user_country):
        self.name = user_name
        self.country = user_country
        print("my name is : ",self.name,"i belongs to : ",self.country)
p1 = Person("ashish","india")
p2 = Person("arpit","canada")


