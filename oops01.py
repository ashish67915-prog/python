class ATM:
    #constructor
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hi how can I help you ?
        1.Press 1 to create pin
        2.Press 2 to change pin
        3.Press 3 to check balance
        4.Press 4 to withdrawal
        5.Anything else to exit

        """) 

        if user_input == '1':
            #create pin
            self.create_pin()
        elif user_input == '2':
            #change pin
            self.change_pin()
        elif user_input == '3':
            #check balance
            self.check_balance()
        elif user_input == '4':
            #withdrawal
            self.withdrawal()
        else:
            exit()


    def create_pin(self):
        user_pin = input("enter your pin : ")
        self.pin = user_pin

        user_balance = int(input("enter balance : "))
        self.balance = user_balance


        print("Pin created successfully")
        self.menu()


    def change_pin(self):
        old_pin = input("enter the old pin : ")

        if old_pin == self.pin:
            new_pin = input("enter the new pin : ")
            self.pin = new_pin
            print("pin created successfully")
            self.menu()
        else:
            print("mai nahi kar skta re baba")
        
        self.menu()
    
    def check_balance(self):
        user_pin = input("enter the pin : ")
        if user_pin == self.pin:
            print("Your balance is : ",self.balance)
        else:
            print("pehli furshat me nikal")
        
        self.menu()
    def withdrawal(self):
        amount = int(input("enter the amount : "))
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("widrawal get successful and your availabel balance is : ",self.balance)

        else:
            print("jb aadmi garid ho na to wo saalla apni addat se garib howe hai")

        self.menu()

        

        

obj = ATM()
print(type(obj))

