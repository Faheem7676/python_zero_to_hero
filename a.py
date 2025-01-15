car1="volvo"
car2="Ford"
car3="BMW"

print(car1,car2,car3)

import numpy as np


# create an array

arr=np.array([1,2,3,4,5])

# perform operation
print("Original Array",arr)
print("Array squared",arr**2)

print(arr)
print(arr[1])

import array

arr=array.array("i",[1,2,3,4,5])

print(arr)

print(arr[0])
print(arr[-1])

print(arr[:-1])


myset={0,1,0}

print(any(myset))

mydict = {0 : "Apple", 1 : "Orange"}
x = any(mydict)
