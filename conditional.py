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