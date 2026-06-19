#basic


class User:
    def __init__(self):
        self.name = "Ashish"
        self.gender = "male"

    def login(self):
        print("login to your account")
        
class Student(User):
    #note in inheritance when we inherite parent class into the child class then according to the rule we can access the properties of the parents class
    #but when we make constructor of itself of child class then constructor of the  parent not to be called and members are not initialized so that we cannot access its parent datamember 
    #we learn some method to do it but at that time we donot make the constructor of the child because we have to access the memeber of the parent class
    # def __init__(self):
    #     self.college = "central university of punjab"
    def enroll(self):
        print("kindly enroll in the course it should be beneficial for you all")
    
o1 = User()
o2 = Student()

print(o2.name)
o2.login()
o2.enroll()