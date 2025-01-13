def is_prim(num):
    
    if num<2:
        
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        
        if num % i ==0:
            
            return False
    return True
            
# input validation using a while loop

while True:
    
    try:
        
        start=int(input("Enter the start value"))
        end=int(input("Enter the end value"))
        
        if start>end:
            print("Enter the the valid start value")
            
        else:
            
            break
    
    except ValueError:
        
        print("enter valid integer")
        
# Find the prime numbers in the range
prime_number=[]

for number in range(start,end+1):
    
    if is_prim(number):
        
        prime_number.append(number)
        
# Display the result
if prime_number:
    print(f"Prime numbers between {start} and {end}: {prime_number}")
else:
    print(f"There are no prime numbers between {start} and {end}.")
    