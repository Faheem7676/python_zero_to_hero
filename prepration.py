
# data type
# str, 
# int,float,complex
# list,tuple,set,range
# dict,
# bool
# bytes,bytearray,memoryview
# NoneType

x=4
print(type(x))
str1="Faheem"
print(type(str))
l=[2,3,4,4]
print(type(l))
tuple=(1,3,5)
print(type(tuple))
set={4,3,"Faheem"}
print(type(set))

dict1={1: "value1",2: "value2"}

print(type(dict))

print(dict1[1])

x=str("Hello world")
print(x)
x=int(20)
print(type(x))
x=complex(5j)
print(type(x))

x=list((2,"Faheem","testing",4,"Banana","cherry"))

print(type(x))

for i in x:
    
    print(i)
    
x=dict(name="Faheem",Age=44)
print(type(x))

print(x["name"])
print(x["Age"])

x=4
x=4j
y=4.4
print(x)
print(x)
print(y)
x=3
x1=43334453355664322
y=-4345
print(type(x))
print(type(x1))
print(type(y))

x=1.22
y=3.2
z=43.43

print(type(x))
print(type(y))
print(type(z))

x=4+4j
y=43j
z=-33j

print(type(x))
print(type(y))
print(type(z))

a=3
b=3.4
c=23j

print(float(a))
print(int(b))
print(complex(a))
# print(int(c))

import random

print(random.randrange(1,10))

