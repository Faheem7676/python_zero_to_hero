str_input = "abcacdeff"
str_count={} # Dictionary to store character counts
output=""  # Output string

for char in str_input:
    
    print(char)
    
    str_count[char]=str_count.get(char,0)+1  # Count occurrences

# Maintain order of first appearance
seen = set()
for char in str_input:
    
    if char not in seen:
        
        output+=char+str(str_count[char])
        seen.add(char)
        
print(output)


d={"Ravi":10,"Rajnish":9,"Sanjeev":15}

print(d["Rajnish"])

print(d.keys())

dict={1:"Faheem",2:"Testing",4:"Automation Testing",5:"API Testing",3:"Database testing"}

print(dict)

print(dict[1])
print(dict[2])
print(dict[3])

print(dict.keys())
print(dict.values())

myKeys=list(dict.keys())
myKeys.sort()

print(myKeys)

# sorted dictionary
sd={i:dict[i]for i in myKeys }
print(sd)

l=list(dict.values())
l.sort()
print(l)


def example_function(*args):
    print(args)  # args is a tuple

example_function(1, 2, 3, 4)


def add(*args):
    
    return a+b+c

a,b,c=10,20,20
print(add(a,b,c))

def example(*args):
    
    print(args)
    
example("Testing","automation testing")


# def sum(*args):
    
    
#     return sum(args)

# print(sum(2,2,2))


def sum_numbers(*args):
    return sum(args)

print(sum_numbers(5, 10, 15))  # Output: 30


def sum_numbers(**args):
    
    return sum(args)

print("**************************************************")

def example_function(**kwargs):
    
    print(kwargs) # kwargs  is a dictionary 
    
    
example_function(name="Alice", age=25, city="New York")

def example_function(**kwargs):
    
    print(kwargs)
    
example_function(name="Testing",age=24,city="New York")


def info(**kwargs):
    
    for key, value in kwargs.items():
        
        print(f"{key}:{value}")

info(name="Testing",age=43,City="New Delhi")

num="100"
result=isinstance(num,int)
if result:
    print("Yes")
    
else:
    print("No")
    
import csv

# Open the file
data=open("login_data.csv",encoding='utf-8')
# csv.reader
csv_data=csv.reader(data)
# reform it into a python object list of list 
data_line=list(csv_data)
print(data_line)
print(data_line[1])
print(len(data_line))

for line in data_line[:2]:
    
    print(line)

print(data_line[3][1])

all_items=[]

for line in data_line[1:]:
    
    all_items.append(line[0])
    
print(all_items)
    

    





    

