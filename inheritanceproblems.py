# class A:
#     def m1(self):
#         return 20

# class B(A):
#     def m1(self):
#         return 30
    
#     def m2(self):
#         return 40

# class C(B):
#     def m2(self):
#         return 20
    
# o1 = A()
# o2 = B()
# o3 = C()
      
# #      20     +    30    +    20
# print(o1.m1() + o3.m1() + o3.m2())




#maximum recursion depth exceeded
class A:
    def m1(self):
        return 20
    
class B(A):
    def m1(self):
        val = super().m1()+30
        return val
    
class C(B):
    def m1(self):
        val = self.m1()+20    #yaha self.m1() khud ko hi baar baar call karega of recursive ho jayega
        return val
    

o1 = C()
print(o1.m1())