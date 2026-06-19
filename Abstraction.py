#In abstraction we study the concept of the abstract class 
#abstract class -> class that contain atleast one abstract method
#note -> hmm abstract class ka object nhi bana sakte
#jitne bhi abstract method bane hai abstract class me utne hi child class mei bhi banane padhenge


from abc import ABC ,abstractmethod

class BankApp:
    def database(self):
        print("your system is connected with the database")

    @abstractmethod
    def security(self):
        pass
    @abstractmethod
    def display(self):
        pass

class MobileApp(BankApp):
    def login(self):
        print("login to your database")

    def security(self):
        print("your mobile is secure")

    def display(self):
        print("display that contain all the security methods")


o1 = MobileApp()
o1.database()
o1.login()
    