import numpy as np

#ways to create the numpy array
#1d array
# a = np.array([1,2,3])
# print(a)

#2d array
# a = np.array([[1,2],[3,4]])
# print(a)

#3d array
# c = np.array([[[1,2],[3,4],[5,6]]])
# print(c)

#dtype
# c = np.array([2,4,5],dtype = float)
# print(c)

#range
# d = np.arange(1,11)
# print(d)

#reshape
# c = np.arange(1,11).reshape(2,5)
# print(c)

#ones 
# d = np.ones((3,4))
# print(d)

#zeroes
# d = np.zeros((3,4))
# print(d)


#random
# d = np.random.random((3,4))   #note here first random used is class and second random used is its method
# print(d)

#linspace
# d = np.linspace(-10,10,10)   #(lower limit , upper limit , number of objects)
# print(d)

#identity
# c = np.identity(3)
# print(c)


#Note point  -> bydefault during creating numpy array all the element are in float if you want in int then mention datatype int i.e dtype =  int.






#Array attributes 

#ndim- >it gives the information that either the array is 1d ,2d,3d
# a = np.arange(10)
# b = np.arange(12,dtype = float).reshape(3,4)
# c = np.arange(8).reshape(2,2,2)   #note -> it 3d array the first represent number of 2d array and remain represent the 2d array order that is 2*2



# print(a.ndim)
# print(b.ndim)
# print(c.ndim)


#shape -> it tells about the number of rows and columns
# print(a.shape)
# print(b.shape)
# print(c.shape)


#size->it tells about the size of the array
# print(a.size)
# print(b.size)
# print(c.size)


# #itemsize
# print(a.itemsize)
# print(b.itemsize)
# print(c.itemsize)


#dtype
# print(a.dtype)
# print(b.dtype)
# print(c.dtype)


#astype -> to fixed the  memory occupation size 
# a.astype(np.int32)   #it makes the memory occupation of all the elements according to the 32bit compilar means int -> 4



#array operation

#scalar operation
# a = np.arange(12).reshape(3,4)
# b = np.arange(12,24).reshape(3,4)


# print(a*2)
# print(a/2)


#relational
# print(a>5)
# print(a==5)

#vector operation
# print(a*b)
# print(a+b)


#Array function
# a = np.arange(1,10).reshape(3,3)
# print(a)

#note that axis  = 1 means in row and axis = 0 means in columns
# print(np.max(a))
# print(np.min(a))
# print(np.sum(a))
# print(np.prod(a))
# print(np.max(a,axis = 1))
# print(np.min(a,axis =0))


#mean ,median ,std(standard deviation),var(varience)
# print(np.mean(a))
# print(np.median(a))
# print(np.std(a))
# print(np.var(a))
# print(np.mean(a,axis = 1))
# print(np.mean(a,axis = 0))


#dot product -> Rule (column of the firstt matrix is equal to the row of the second matrix)
# a = np.arange(1,10).reshape(3,3)
# b = np.arange(1,13).reshape(3,4)
# print(np.dot(a,b))


#log and exponential function
# a = np.arange(1,10).reshape(3,3)
# print(np.log(a))
# print(np.exp(a))



#trigonometric(usually very less use)
# a = np.arange(1,10).reshape(3,3)
# print(np.sin(a))


#round,floor,ceil
# print(np.round(np.random.random((3,4))))
# print(np.floor(np.random.random((2,3))))
# print(np.ceil(np.random.random((4,5))))


#indexing and slicing
# a = np.arange(10)
# b = np.arange(12).reshape(3,4)
# c = np.arange(8).reshape(2,2,2)

# print(a[0])
# print(a[-1])
# print(b[1][1])
# print(b[1][0])
# print(c[1][0][0])  # (2d matrix index ,row index in this 2d matrix,column index in this 2d matrix)
# print(c[0][0][0])


#numpy tricks

#np.sort
# a = np.array([1,3,5,2,6,8,9])
# print(a)
# print(np.sort(a))





