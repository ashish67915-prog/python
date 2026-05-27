#how print works

# print("hello world")

# print(123)

#variable

# a=10
# b=20
# add = a+b
# print(add)

#type

# a=True
# print(type(a))


#arithmetic operator

# num1 = 20
# num2 = 10

# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)
# print(num1%num2)
# print(num1**num2)

#type casting
# a=float(2)
# b=4.25
# sum=a+b
# print(sum)


# #input
# #jab bhi hm input lete hai tb woh hme hamesa string return karta hai esliye hame casting karni padegi

# a=int(input("enter first number : "))
# b=int(input("enter second number : "))

# sum = a+b
# print("sum of the two number: ",sum)



#area of sqaure
# side = float(input("enter side of the square : "))
# area = side*side
# print("area of the square : ",area)


#True False
# a = int(input("enter first number : "))
# b = int (input("enter second number : "))


# print(a>=b)


#logical operator
# print(True and True)
# print(True and False)

# print(True or True)
# print(True or False)
# print(False or False)


# print(not True)


#string
# str = "At that time i am learning python so i can learn backend"
# print(str)

# str = "At that time i am \n learning python so i can learn backend"
# print(str)

# str = "At that time i am \t learning python so i can learn backend"
# print(str)

# str = "At that time i am  learning python so i can learn backend"
# print(len(str))

# str1 = "My Name is : "
# str2 = "Ashish"
# print(str1+str2)


#slicing
# str = "i want to make make my family happy"
# print(str[0:5])
# print(str[-5:-1])
# print(str[0:])
# print(str[:len(str)])
# a = "ashish"
# print(len(a))


#string properties
# str = "this world is become more beautiful when you try to make it"
# print(str.count("t"))
# print(str.capitalize())
# print(str.endswith("it"))
# print(str.find("h"))
# print(str.replace("t","T"))


# str = input("enter the string : ")
# print("length of the string : ",len(str))

# str = "i want money $ because to make my family happy"
# print(str.count("$"))


#conditonal statements 
# marks = 95
# if(marks>=90):
#     print("Grade A")
# elif(marks>=80 and marks<90):
#     print("Grade B")
# elif(marks>=70 and marks<80):
#     print("Grade C")
   
# else:
#     print("Grade D")


# print("code end")


# marks = int(input("enter the marks of the student : "))
# if(marks>=90):
#     Grade = "A"
# elif(marks>=80 and marks<90):
#     Grade = "B"
# elif(marks>=70 and marks<80):
#     Grade = "C"
# else:
#     Grade = "D"

# print("Student Grade is : ",Grade)


# number = int(input("enter the number : "))
# if(number%2==0):
#     print("Even Number")
# else:
#     print("Odd Number")


# a = int(input("enter the first number : "))
# b = int(input("enter the second number : "))
# c = int(input("enter the third number : "))

# if(a>b and a>c):
#     max = a
# elif(b>a and b>c):
#     max = b
# else:
#     max = c

# print("Maximum Number is : ",max)


# num = int(input("enter any number : "))
# if(num%7==0):
#     print("The given number is divisible by 7 ")
# else:
#     print("The number is not divisible by 7 ")



#list
# arr = [1,2,3,4,5]
# print(arr);
# print(type(arr))
# print(arr[0])
# print(arr[1])
# print(len(arr))


#list is different from array because it contain different datatype in the same list
# arr = ["Ashish","Mannat",24,56,12,"Arpit"]
# print(arr)
# arr[0] = "ashish"
# print(arr)


#note string are immutable whereas list are mutable means it can be changable

# arr = ["Ashish","Sumit","Arpit","Nitin"]
# print(arr)
# arr.append("Ayush")
# print(arr)


# arr = [2,3,1,6,4]
# print(arr)
# arr.sort()
# print(arr)

# arr = [2,5,3,6,8,1,4]
# print(arr)
# arr.sort(reverse=True)
# print(arr)

# arr = [1,2,3,4,5]
# print(arr)
# arr.reverse()
# print(arr)


# arr = [1,2,3,4,5]
# print(arr)
# arr.insert(0,6)
# print(arr)


#Tuple
# tup = (1,2,3,4,5)
# print(tup)

# tup = (1)
# print(tup)
# print(type(tup))


# tup = (1,2,3,1)
# print(tup.index(1))
# print(tup.count(1))


# movie1 = (input("enter your first movie : "))
# movie2 = (input("enter your second movies : "))
# movie3 = (input("enter your third movie : "))

# movie = [movie1 ,movie2 ,movie3]
# print(movie)

# movie = [1,2,3,4,5]
# print(movie)


# movie = []
# movie1 = input("enter your first favourate movie : ")
# movie2 = input("enter your second favourate movie : ")
# movie3 = input("enter your third favourate movie : ")

# movie.append(movie1)
# movie.append(movie2)
# movie.append(movie3)
# print(movie)


# list1 = ['n','a','m','a','n']
# copy_list = list1.copy()
# if(copy_list == list1):
#     print("Number is palindrome")
# else:
#     print("Not a palindrome number")


# list = ['A','B','C','D','A','A']
# print(list.count('A'))


#dictionary

# dict = {
#     "name" : "Ashish",
#     "reg_no" : "25bthcse03"
# }

# dict["subject"] = "python"
# print(dict)

# ans = {}
# ans["name"] = "ashish"
# print(ans)



# info = {
#     "name" : "Ashish",
#     "marks" : {
#         "physic" : 87,
#         "chemistry" : 97,
#         "maths" : 93
#     }
# }


# print(info["marks"]["maths"])

# dict = {
#     "name" : "Ashish",
#     "reg_no" : "25bthcse03"
# }

# print(dict.get("name"))


# dict = {
#     "tabel" : "a piece of the furniture",
#     "cat" : "a small animal"
# }

# print(dict)

# dict = {}
# mark1 = int(input("enter the marks of the first subject :  "))
# mark2 = int(input("enter the marks of the second subject : "))
# mark3 = int(input("enter the marks of the third subject"))

# dict.update({"phy" : mark1})
# dict.update({"chem" : mark2})
# dict.update({"maths" : mark3})
# print(dict)


# #set
# collection = {1,2,3,3,"ashish","yadav"}
# print(collection)
# collection.add(4)
# print(collection)

# #empty set 
# group = set()
#empty dict
# dict = {}
# print(type(list))

# #empty list
# list = []
# print(type(list))


# set = {"python","c","c++","javascript","python","python","java","java"}
# print(len(set))




#while loop

# list = [1,2,3,4,5,6,7,8,9,10]

# i=0
# while i<10:
#     print(list[i])
#     i+=1


# list = [1,2,3,4,5,6,7,8,9,10]
# x = 2
# i=0
# while i<len(list):
#     if(list[i] == x):
#         print("index of the target",i)
#         break
#     else:
#         print("finding....")
#     i+=1



# i=0
# while i<=5:
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1

# print("end of the loop")    



# str = "srikrishnagovindharemurarihenathnarayanwasudeva"

# for num in str:
#     if(num == 'k'):
#         print("our k is find")
#         break
#     print(num)


# list = [1,4,9,16,25,36,49,64,81,100]

# for num in list:
#     print(num)


# tup = (1,2,3,4,5,6,7,8,9,10)
# x = 10
# for num in tup:
#     if(num  == 10):
#         print("element found ")
#         break


# list = ["Ashish","sumit","ayush"]
# for num in list:
#     if(num == "Ashish"):
#         continue
#     print(num)

# value = range(10)
# for i in value:
#     pass


# n = int(input("enter any number : "))
# sum=0
# i=0
# while i<=n:
#     sum+=i
#     i+=1

# print(sum)


# class student:
#     name = "karan"

# s1 = student()
# print(s1.name)


# class Student:
#     name = "karan"
#     def __init__(self):
#         print("hello world")

# s1 = Student()


# class Student:
#     def __init__(self,fullname):
#         self.name = fullname
#         print("this is the name of the student")

# s1 = Student("Ashish")
# print(s1.name)


# class Student:
#     #default constructor
#     def __init__(self):
#         print("hello coder army")
#     #parameterised constructor
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("coder army jinda baad")


# s1 = Student("Ashish",9)
# print(s1.name)
# print(s1.marks)

# class Account:
#     def __init__(self,balance,account_no):
#         self.balance = balance
#         self.account_no = account_no

#     def debit(self,amount):
#         self.balance -=amount
#         print("your current balance is : ",self.getbalance())

#     def deposit(self,amount):
#         self.balance +=amount
#         print("your current balance is : ",self.getbalance())

#     def getbalance(self):
#         return self.balance


# s1 = Account(2500,123)
# s1.debit(500)


# class Student:
#     def __init__(self,password):
#         self.__password = password  #two underscore before variable make it private

#     def display(self):
#         print(self.__password)


# s1 = Student(123)
# s1.display()


# class Student:
#     def __init__(self):
#         print("constructor called")

#     def __hello(self):
#         print("hello world")

#     def welcome(self):
#         self.__hello()


# s1 = Student()
# s1.welcome()


# class car:
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stoped..")


# class Toyotocar(car):
#     def __init__(self,name):
#         self.name = name


# car1 = Toyotocar("Fortuner")
# print(car1.name)
# print(car1.start())



# class Student:
#     def __init__(self,name,grade,percentage):
#         self.name = name
#         self.grade = grade
#         self.__percentage = percentage
#     def student_details(self):
#         print(f"{self.name} is studied in class {self.grade} ,with percentage of {self.percentage} %")
#     def get_percentage(self):
#         return self.__percentage

# student1 = Student("Ashish",12,78)
# # student1.student_details()

# # print(student1.__dict__)
# # print(student1.percentage)
# print(student1.get_percentage())



#inheritance
#parent class 
# class Student:
#     def __init__(self,name,grade,percentage):
#         self.name = name
#         self.grade = grade
#         self.percentage = percentage
#     def student_details(self):
#         print(f"{self.name} is studied in class {self.grade} ,with percentage of {self.percentage}")
    
# #child class
# class Monitor(Student):
#     def __init__(self,name,grade,percentage,stream):
#         super().__init__(name,grade,percentage)
#         self.stream = stream
    
#     def student_details(self):
#         super().student_details()
#         print(f"with the stream {self.stream}")
    


# monitor = Monitor("Ashish",12,78,"pcm")
# print(monitor.stream)
    
# monitor.student_details()


#polymorphism

# class Student:
#     def __init__(self,name,grade,percentage):
#         self.name = name
#         self.grade = grade
#         self.percentage = percentage
    
#     def student_details(self):
#         print(f"My name is {self.name} and i am studied in class {self.grade} ,and i got {self.percentage}")

    
# class Monitor(Student):
#     def __init__(self,name,grade,percentage,stream):
#         super().__init__(name,grade,percentage)
#         self.stream = stream
#     def student_details(self):
#         super().student_details()
#         print(f"My name is {self.name} and i am studied in class {self.grade} and i got {self.percentage} from stream {self.stream}")


# student1 = Student("Ashish Yadav",12,78)
# monitor1 = Monitor("Ashish Yadav" ,12,78,"pcm")


# # student1.student_details()
# monitor1.student_details()



# list = ["ashish","arpit","nitin","hariom"]
# print(list)
# list.append("krishna ji")
# print(list)


# list1 = ["ashish","arpit","nitin","hariom"]
# list2 = ["mukesh","shiva"]

# list1.extend(list2)
# print(list1)


# tuple = (1,)
# print(type(tuple))


# tuple = tuple(("madhav","keshav","kanha","murlidhar"))
# print(tuple)
# print(type(tup))


# tuple1 = ("radha",)
# tuple2 = ("krisha",)
# tuple3 = tuple1+tuple2
# print(tuple3)


# tuple = ("radha","krishna","madhav","kishori")*3
# print(tuple)


# tuple = ("radha","krisha","kishori","madhav")
# print("kishori" in tuple)


# tuple = ("radha","krishna","kishori","madhav","murlidhar")
# # i=0
# # while i<len(tuple):
# #     print(tuple[i])
# #     i=i+1


# for i in tuple:
#     print(i)



# tup = (2,1,3,4,7,5,9)
# # print(tuple.count(2))
# # print(tuple.index(2))
# # print(len(tuple))
# # print(min(tuple))
# # print(max(tuple))
# # print(sorted(tuple))


# a = sorted(tup)
# sorted_tuple = tuple(a)
# print(sorted_tuple)


# tuple = ("radha","kishori","krishna","madhav")
# tuple[0]="murlidhar"



# set = {1,2,3,4,5,5,5,5,}
# print(set)

# set_creation = set()
# print(set_creation)
# print(type(set_creation))


# list = [1,2,3,4,5]
# set_convert = set(list)
# print(set_convert)


# set = {"apple","banana","orange","papaya","cherry"}
# # print(set)
# # set.add("mango")
# # print(set)


# set.remove("grapes")



# dict = {
#     "name":"Ashish",
#     "reg_no":"25bthcse03",
#     "passion":"learner"
# }
# print(dict)
# print(type(dict))


# collection = dict(name ="madhav" ,age = 24)
# print(collection)
# print(type(collection))


# dict = {
#     "name":"Ashish",
#     "reg_no":"25bthcse03",
#     "college_name":"Central University of Punjab",
#     "addmission year":2025
# }


# print(dict)
# print(type(dict))


# print(dict["name"])
# print(dict["reg_no"])
# print(dict["college_name"])
# print(dict["addmission year"])


# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(dict.get("name"))


# dict["category"] = "OBC"
# print(dict)
# dict["addmission year"] =2026
# print(dict)


# del dict["name"]
# print(dict)

# dict.pop("name")
# print(dict)

# print(dict["adhar_no"])
# print(dict.get("adhar_no","adhar_no nhi hai"))



dict = {
    "name":"Ashish",
    "reg_no":"25bthcse03",
    "college_name":"Central University of Punjab",
    "addmission year":2025
}


# for keys  in dict:
#     print(keys)


# for value in dict:
#     print(dict[value])


# for value in dict.values():
#     print(value)


# for keys,value in dict.items():
#     print(keys,value)


#nested dictionary
dict_parent = {
    "dict_child1": {
        "name": "Ashish"
    }
    ,

    "dict_child2" : {
        "sur_name":"Yadav",
        "dict_subchild" : {
                "name":"Arpit"
        }
    }
}

# print(dict_parent)

print(dict_parent["dict_child1"])
print(dict_parent["dict_child2"]["dict_subchild"])


