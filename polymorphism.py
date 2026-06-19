#method overriding
#method overloading
#operator overloading

#method overloading
#according to the theory that we would studied the logic below is correct but in reality it is a wrong method it gives error
# class Shape:
#     def area(self,rad):
#         return 3.14*rad*rad
    
#     def area(self,l,b):
#         return l*b
    

# o1 = Shape()
# o1.area(2)
# o1.area(3,4)


#so the right code is
# class Shape:
#     def area(self,a,b=0):
#         if b==0:
#             return 3.14*a*a
        
#         else:
#             return a*b
        
# o1 = Shape()
# print(o1.area(2))
# print(o1.area(3,4))




#operator overloading
#here single plus operator do works in a multiple way

#concatination
# print("hello"+"world")

#sum
# print(1+2)

#merging

# print([1,2,3]+[4,5])
