language="python"
print(language[2])
print(type(language))
lst=list(language)
print(type(lst))
print(lst)

print(lst[2])

# second way : list comprehencsion
lst=[i for i in language]
print(type(lst))
print(lst)

# generating numbers
numbers=[i for i in range(11)]
print(numbers)

squares=[i*i for i in range(11)]
print(squares)

numbers=[(i,i*i)for i in range(11)]

print(numbers)

even_numbers=[i for i in range(21) if i%2==0]
print(even_numbers)

odd_numbers=[i for i in range(21) if i%2!=0]
print(odd_numbers)

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]

# Filter numbers: let's filter out positive even numbers from the list below

positive_number=[i for i in numbers if i%2==0 and i>0]

print(positive_number)

# Named function
def add_two_number(a,b):
    
    return a+b

print(add_two_number(3,4))

add_two_numbers=lambda a,b: a+b
print(add_two_numbers(4,1))

squares=lambda x : x ** 2
print(squares(3))

cube=lambda x: x ** 3
print(cube(3))

#multiple variables
multiple_variables=lambda a,b,c: a **2 -3*b+4*c
print(multiple_variables(5,5,3))


numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative_number=[i for i in numbers if i<=0]

print(negative_number)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

d=dict(countries)
print(type(d))