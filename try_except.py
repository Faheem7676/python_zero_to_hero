try:
    
    print(10 + "2")
    
except:
    print("something went wrong")
    
    
    
try:
    
    name=input("Enter your name")
    year_born=input("Enter you janam year")
    age=2025-year_born
    print(f"Yor are {name}, and your age is today {age} years.")  
    
except TypeError:
    
    print("type error occored")
    
except ValueError:
    print("value error occored")
    
except ZeroDivisionError:
    print("zero division error occored")
    
    
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
    
print("****************************************")   
    
def sum_of_five_numbers(a,b,c,d,e):
    
    return a+b+c+d+e

list=[1,2,3,4,5]
sumobj=sum_of_five_numbers(*list)
print(sumobj)

