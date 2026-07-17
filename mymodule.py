#module is defined as the name given to the file like .py


import modulePackagesLib
modulePackagesLib.say_hello("ashish")

#for excessig the single function from module
from modulePackagesLib import student_dict
print(student_dict['name'])


#packages is defined as the collection of the modules/py files +  __init__.py


#libraries is defined as the collection of the modules and packages
import math
A = 16
print(math.sqrt(A))

#import specific fuction only
from math import factorial
B = 3
print(factorial(B))


#install new library 
#to install packages -> pip install <library_name>
#example pip install pandas
import pandas as pd




