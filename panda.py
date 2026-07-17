import numpy as np
import pandas as pd



#making series using list
# country = ['india', 'america', 'australia', 'south africa']
# d = pd.Series(country)
# print(d)

#custom indexing
# state = ['punjab','arunachal','meghalaya','kerala']
# position = [1,2,3,4]
# a = pd.Series(state,index=position,name="beautiful places")
# print(a)


#making series using the dictionary
# marks = {
#     'maths':89,
#     'english':90,
#     'c++':95
# }

# c = pd.Series(marks,name="arpit marks")
# print(c)

#Series Attributes

#size
# marks = {
#     'maths':89,
#     'english':90,
#     'c++':95
# }
# d = pd.Series(marks,name="marks of arpit verma")
# print(d)
# print(d.size)

#dtype
# print(d.dtype)


#name
# print(d.name)


#is_unique
# print(d.is_unique)



#index
# marks = ['maths','english','science','hindi']
# d = pd.Series(marks)
# print(d.index)


# #values
# print(d.values)

#indexing

#positive indexing
# x = pd.Series([1,2,3,4,5,6,7,8,9,10])
# print(x[0])



#note ->negative indexing in padas series allow only when we make custom index it not work with the default index


#slicing
#positve slicing
# x = pd.Series([1,2,3,4,5,6,7,8,9,10])
# print(x[1:5])
# print(x[:5])

#negative slicing
# print(x[-5:])


#fancy indexing
# x = pd.Series([1,2,3,4,5,6,7,8,9,10])
# print(x[[1,2,3,4,5]])

#indexing with labels
# x = ['ashish','arpit','hariom','pavan','nitin']
# y = [3,8,9,51,4]
# a = pd.Series(y,name="registration numbers",index = x)
# print(a)
# print(a['arpit']) #label indexing


#editing in the padas series 
#through indexing 
# x = ['maths','english','science']
# y = [89,98,90]
# a = pd.Series(y,index =x)
# a['maths'] = 100 #editing
# print(a)

#if you want to perform editing but that index is not present then we you try to edit it will become a new member of that pandas series
# a['sst'] = 89
# print(a)


#editing throw slicing
# x = ['ashish','ayush','arpit','adarsh']
# a = pd.Series(x)
# a[1:3] = ["akash","vikash"]
# print(a)


#editing through fancy indexing
# x = ['ashish','ayush','arpit','adarsh']
# a = pd.Series(x)
# a[[0,2,3]]=["aman","naman","prakash"]
# print(a)

#editing through label
# x = ['maths','english','science','social science']
# y = [87,98,90,89]
# a = pd.Series(y,name="marks of the student",index = x)
# print(a)


#series with python functionality
# x = [10,20,30,40,50]
# a = pd.Series(x)
# print(len(a))
# print(type(a))
# print(dir(a))
# print(sorted(a))
# print(max(a))
# print(min(a))


#type conversion
# x = ['maths','science','social science','hindi','english']
# y =  [90,89,98,78,87]
# a = pd.Series(y,name="marks of the student",index =x)
# print(a)
# b = list(a)
# print(b)
# d = dict(a)
# print(d)



#membership opertor
#here we find either the element is a part of our pandas series or not
#bydefault this work only on index not on the value so for value we have to additionally add that .value
# x = ['maths','english','science','social science','hindi']
# y = [87,89,90,80,85]
# a = pd.Series(y,name="marks of the student",index=x)
# print('maths' in a)


#looping
# x =[10,20,30,40,50]
# for  i in x:
#     print(i)


#arithmetic operators
# x =  ['maths','science','social studies','hindi','english']
# y = [98,89,87,97,90]
# a = pd.Series(y,name =  "marks of the student",index = x)
# #for finding marks required to get 100 out of 100 marks
# print(100-a) #arithmetic operators


#relational operator
# x = [78,87,98,45,67,34]
# a = pd.Series(x)
# print(a>=50)



#boolean indexing in series
# x = [23,45,89,0,98,67,0,78,0]
# a = pd.Series(x)
# print(a[a>=50].size)
# print(a[a==0].size)


#graph plotting
# x = [20,30,40,50,60,70,80,90,100]
# a = pd.Series(x)
# print(a.plot(kind='bar'))






