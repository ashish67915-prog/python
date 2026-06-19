# dhyan dene wali baat attribute tb tk assign nahi hota jb tk self.var1 =var1 na ho jaye
#agar hmm var1 ke liye 200 value pass kar rhe hai to vo tab tak assign nahi hoga jb tk self.var1 = var1 na ho jaye
#means in total var1 != self.var1

class A:
    def __init__(self):
        self.var1 = 100

    def display1(self,var1):
        # self.var1 = var1    then result would be 200
        print("class A : ",self.var1)

class B(A):
    def display2(self,var1):
        print("class B : ",self.var1)


o1 = B()
o1.display1(200)