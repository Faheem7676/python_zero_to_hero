
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

