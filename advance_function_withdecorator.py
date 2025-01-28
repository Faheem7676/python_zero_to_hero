# function as parameter

def sum_numbers(nums):
    
    return sum(nums)

def higher_order_function(f,lst):
    
    summation=f(lst)
    
    return summation

result=higher_order_function(sum_numbers,[1,2,3,4,5])
print(result)

def square(x):
    
    return x ** 2

def cube(x):
    
    return x ** 3

def absolute(x):
    
    if x>=0:
        
        return x
    else:
        return -(x)
    
    
def higher_order_function(type):
    
    if type=="square":
        return square
    
    elif type=="cube":
        
        return cube
    elif type=="absolute":
        return absolute
    
result=higher_order_function('square')
print(result(2))

result=higher_order_function("cube")
print(result(3))

result=higher_order_function("absolute")
print(result(10))

print("*******************************")

def add_ten():
    
    ten=10
    
    def add(num):
        
        return num + ten
    return add

clouser_result=add_ten()
print(clouser_result(5))
print(clouser_result(3))

#######################################

# Normal function
def greeting():
    
    return "Welcom to python"

def uppercase_decorator(function):
    
    def wrapper():
        
        func=function()
        
        make_uppercase=func.upper()
        
        return make_uppercase
    
    return wrapper

g=uppercase_decorator(greeting)
print(g())

## Let us implement the example above with a decorator

'''this decorator function is higher order function that takes a function as a parameter'''

def uppercase_decorator(function):
    
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    
    return wrapper

@uppercase_decorator
def greeting():
    
    return "Welcome to python class"

print(greeting())

print("************************************")

# Applying Multiple Decorators to a single Funtions
'''These dacorator function are higher order function that take functions as 
parameter'''

# first decorator

def uppercase_decorator(function):
    
    def wrapper():
        
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    
    return wrapper

# second decorator
def split_string_decorator(function):
    
    def wrapper():
        
        func=function()
        splitted_string=func.split()
        
        return splitted_string
    
    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON


# Accepting parameters in Decorator functions

def decorator_with_parameters(function):
    
    def wrapper_accepting_parameters(para1,para2,para3):
        function(para1,para2,para3)
        print("I live in {}".format(para3))
        
    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(firsname,lastname,country):
    print("I am {} {}.I love to teach." .format(firsname,lastname,country))


print(print_full_name("Automation","Testing", "India"))     


# python map function

numbers=[1,2,3,4,5]

def square(x):
    
    return x ** 2

numbers_squared=map(square,numbers)
print(list(numbers_squared)) 
        
n=[1,2,3,4,5,6,7,8,9]

def square(x):
    
    return x ** 2


n_square=map(square,n)
print(list(n_square))

numbers=[1,2,3,4,5]

def square(x):
    
    return x ** 2

numbers_squared=map(square,numbers)

print(list(numbers_squared))

# using with lamda
numbers_squared=map(lambda x: x**2, numbers)
print(list(numbers_squared))

number_string=["1","2","3","4","5"]

number_int=map(int,number_string)

print(list(number_int))


name=["automation","testing","python","coding"]

def change_upper_case(name):
    
    return name.upper()

name_upper_cased=map(change_upper_case,name)

print(list(name_upper_cased))


name=["automation","testing","python","coding"]

def change_upper_case(name):
    
    return name.upper()

obj=map(change_upper_case,name)
print(list(obj))

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), name)
print(list(names_upper_cased))    # ['AUTOMATION', 'TESTING', 'PYTHON', 'CODING']


numbers=[1,2,3,4,5]

def is_even(num):
    
    if num % 2 ==0:
        
        return True
    else:
        return False
    
evennumber=filter(is_even,numbers)
print(list(evennumber))

numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers)) 


name=["Automation","python_code","teting","Vb"]

def is_long_name(name):
    
    if len(name)>7:
        
        return True
    
    return False

islognname=filter(is_long_name,name)
print(list(islognname))
    