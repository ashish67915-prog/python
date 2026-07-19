import numpy as numpy
import pandas as pd


#creating dataframe using list
# student_list = [
#     [100,95,10],
#     [95,80,8],
#     [90,75,6]
# ]

# a = pd.DataFrame(student_list,columns=['iq','marks','package'])
# print(a)


#creating pandas dataframe using dictionary
# student_dict = {
#     'iq':[100,95,90,80],
#     'marks':[95,90,85,70],
#     'package':[10,8,78,8.5]
# }

# a = pd.DataFrame(student_dict)
# print(a)


#pandas  dataframes using the csv files
movies = pd.read_csv('movies (1).csv')
# print(movies)


#Dataframe attributes and method

#shape
# print(movies.shape)


#dtypes
# print(movies.dtypes)


# #index
# print(movies.index)


# #columns
# print(movies.columns)


# #values
# print(movies.values)


#info
# print(movies.info)


#describe
# print(movies.describe)


#rename
# student_dict = {
#     'Name':['Ashish','Akash','Aman','Anuj'],
#     'Age' :[20,21,24,19],
#     'Package':[10,20,30,40]
# }

# a = pd.DataFrame(student_dict)
# a.rename(columns={'Name':'Student name','Package':'LPA'},inplace=True)
# print(a)


#math functions
#sum
#bydefault when we apply sum then it sum the values column wise . For row wise use sum(axis=1)
# student_dict = {
#     'Student iq':[100,90,89,80],
#     'Age' :[20,21,24,19],
#     'Package':[10,20,30,40]
# }


# a = pd.DataFrame(student_dict)
# print(a)
# print(a.sum())


#mean
# print(a.mean())


#median
# print(a.median())


#var(varience)
# print(a.var())


#std(standard deviation)
# print(a.std())
#if you want to appy row wise math method then use axis=1.




#selecting column from the dataframe
# a = pd.read_csv('movies (1).csv')
# print(a)

# print(a[['title_x','release_date']])



#use of iloc and loc
# student_dict = {
#     'name':['ashish','akash','aman','aditya','aryan'],
#     'age':[20,22,25,20,19],
#     'package':[10,20,30,40,50],
    
# }

# a = pd.DataFrame(student_dict)
# print(a)

#iloc->using index
# print(a.iloc[0])


#loc->using labels
#here we understand a important concept i.e set_index()
# a.set_index('name',inplace=True)
# print(a)

# print(a.loc['ashish'])


#using slicing and fancy indexing
# print(a.iloc[0:4])
# print(a.iloc[[0,1,2]])


#selecting both row and columns
#note->index wise me ek kam tk jata hai aur labelwise me pura last tk jata hai
#using iloc->according to default indexing
# student_dict = {
#     'name':['ashish','arpit','hariom','nitin','pavan','rajiv'],
#     'age':[20,19,21,18,18,17],
#     'package':[10,20,30,40,50,60]
# }

# a = pd.DataFrame(student_dict)
# print(a.iloc[0:3,0:3])

#using loc->according to the labels
# student_dict = {
#     'name':['ashish','hariom','arpit','nitin','rajiv','pavan'],
#     'age':[20,20,19,18,17,18],
#     'package':[10,20,30,40,50,60]
# }

# a = pd.DataFrame(student_dict)
# print(a.loc[0:2,'name':'age'])



#creating new column
# student_dict = { 
#     'name':['ashish','nitish','aman','aryan','vivek'],
#     'age':[20,34,20,20,21],
#     'package':[10,20,30,40,50]
# }


# a = pd.DataFrame(student_dict)
# a['experience'] = [5,4,7,6,3]   #here we create the new column
# print(a)



#some dataframe fuctions 
#astype -> use to reduce the size or memory
# student_dict = {
#     'age':[10,20,30,120,140,150,180,220,200,250]
# }

# a = pd.DataFrame(student_dict)
# # print(a)
# result = a[a['age'].between(100, 200)]
# print(result)


#clip

# student_dict = {
#     "age":[70,80,90,120,140,170,190,210,240,280]
# }

# a = pd.DataFrame(student_dict)
# result = a.clip(100,200)
# print(result)


#drop_duplicates
student_dict = {
    'age':[2,2,3,4,5,6,6,6,7]
}

a = pd.DataFrame(student_dict)


