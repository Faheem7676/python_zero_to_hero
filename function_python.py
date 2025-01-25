
def fun1():
    
    print("Hello World")

fun1()

# function without parameter

def generate_full_name():
    
    first_name="Automation"
    last_name="Testing"
    space=" "
    fullName=first_name+space+last_name
    print(fullName)
    
generate_full_name()

def add_two_number():
    
    num_one=4
    num_two=2
    add_num=num_one+num_two
    print(add_num)
    
add_two_number()


def generate_full_name():
    
    first_name="Jira"
    last_name="zephyr"
    space=" "
    fullName=first_name+space+last_name
    return fullName
    
print(generate_full_name())


def add_two_numbers ():
    num_one = 7
    num_two = 8
    add= num_one + num_two
    return add
print(add_two_numbers())

########################################
# declaring a function

def function_name(parameter):
    
    print("The parameter value is:", parameter)

function_name(4)

#########################################

def greetings(name):
    
    result=name + " ,Welcome to python classes."
    return result
    
print(greetings("Rahul"))

############################################

def add_ten(num):
    ten=20
    
    return num+ten

print(add_ten(5))

###########################################

def square_num(num):
    
    return num * num

print(square_num(6))

#########################################

def squar(n):
    
    return n **2

print(squar(9))

############################

def area_circle(r):
    
    pi=3.14
    area=pi*r**2
    return area

print(area_circle(2))

######################################

def sum_of_num(n):
    
    total=0
    
    for i in range(n+1):
      
        
        total=total+i
        
    print(total)
        
sum_of_num(10)
sum_of_num(100)
    
#######################################
    
# with two parameters

def generate_full_name(firstName,lastName):
    
    space=" "
    
    fullName=firstName + space +lastName
    
    return fullName

print("Full Name:",generate_full_name("Automation","Testing"))

# sum of two number

def sum_of_two_num(n1,n2):
    
    sum=n1+n2
    return sum

print("sum of two number is:",sum_of_two_num(5,3))

# calculate age

def calculate_age(current_year,birth_year):
    
    age=current_year-birth_year
    
    return age

print(calculate_age(2025,1965))


###############################################

def print_fullName(firstname,lastname):
    
    space=" "
    
    full_name=firstname+space+lastname
    return full_name

print(print_fullName(firstname="Automation",lastname="Testing"))

##############################################

def addtwo_number(a,b):
    
    return a+b

print(addtwo_number(a=4,b=2))
    
    
def is_even(n):
    
    if n %2==0:
        print("Even")
        
        return True
    else:
        return False
    
print(is_even(10))
print(is_even(7))
print(is_even(20))

############################
# find even number

def find_even_number(n):
    
    even=[]
    
    for i in range(n+1):
        
        if i %2 ==0: 
        
            even.append(i)
        
    return even

print(find_even_number(10))

#############################
        
        
        

