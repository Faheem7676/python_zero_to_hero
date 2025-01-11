number1=input("Enter the first number1")
number2=input("Enter the second number2")


sum=float(number1) + float (number2)

print("the sum of {0} and {1} is {2}" .format(number1,number2,sum))


n1=49
n2=43

sum=n1+n2

print("the sum of n1 and n2 is",sum)


def adding(a,b):
    
    return a+b


result=adding(3,4)
print(result)


n1=3
n2=4

import operator

su=operator.add(n1,n2)

print("the sum of {0} and {1} is {2}" .format(n1,n2,su))



add_number=lambda x, y: x + y


number1=2
number2=3

result=add_number(number2,number1)

print("the sum of number1 and number2 is ", result)
