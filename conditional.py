a=4

if a>0:
    print("A is greater than zero")
    
    
a=3

if a<0:
    
    print("A is greater than zero")
    
else:
    print("A is not greater than zero")
    
    
a=-1

if a>0:
    
    print("A is greater than zero")
    
elif a<0:
    print("A is less than zero")
    
else:
    print("A is zero")
    
    
a=10

if a>0:
    
    if a%2==0:
        
        print("A is greater than zero and it is even number too.")
        
    else:
        print("A is greater than zero")
        
elif a==0:
    
    print("A is zero")
    
else:
    print("A is negative number")
    
    
a=1

if a>0 and a%2 ==0:
    
    print("A is an integer and positive number")
    
elif a>0 and a%2 !=0:
    print("A is positive number")
    
elif a==0:
    print("A is zero")
    
else:
    print("A is negative")
    
user="user1"
password=5

if user=="Admin" or password>=5:
    print("Acess granted")
    
else:
    print("Access denied")
    
age=int(input("Enter your age"))

if age>=18:
    print("You are old enough to drive.")
    
else:
    print("You are not enough to driver.")
    
n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))

if n1>n2:
    print("{n1} is greater than {n2}")
    
elif n2>n1:
    print("{n2} is greater than {n1}")
    
else:
    print("{n1} and {n2} is equal")
    