class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

    def print_address(self):
        print(self.address.get_city(),self.address.pin,self.address.state)  #self.address.get_city()  = _Address__city(but it not good practice so we use first using getter function)


    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.edit_address(new_city,new_pin,new_state)

#here address is a complex entity that contain city,pin,state,house_no,landmarks etc. so that we make a different class for that .
class Address:
    def __init__(self,city,pin,state):
        self.__city  = city
        self.pin = pin
        self.state = state
    def get_city(self):    #we know that according to the aggregation the customer  class owns the address class but it does in sense that it access also the private member so that we use getter function to access its private member
        return self.__city
    
    def edit_address(self,new_city,new_pin,new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state

o1 = Address("gorakhpur",273408,"uttarpradesh")
o2 = Customer("ashish","male",o1)
o2.print_address()
o2.edit_profile("Dorsi","Bernalla",154012,"Punjab")
o2.print_address()

