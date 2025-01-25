
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