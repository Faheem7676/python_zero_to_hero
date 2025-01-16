count=0

while count<5:
    
    print(count)
    
    count=count+1
    
else:
    print(count)
    
    # print from 0 to 4 
    


print("I hope you are good and ready to move from there.\n Are you?")

count=0

while count<5:
    print(count)
    
    count=count+1
    
    if count==3:
        break
    
# write a while loop to iterate till itterate 5 and as it reached 3 break

count=0

while count<5:
    
    print(count)
    
    count=count+1
    
    
    if count==3:
        
        
        break

print("**********************************")   
count=0

while count<5:
    
    if count==3:
        
        count=count+1
        continue
    
    print(count)
    count=count+1
print("zehan") 
numbers=[1,2,3,4,5,6]

for number in numbers:
    print(number)
    if number==3:
        continue
    print(number)

print("for loop")   
language="python"

for letter in language:
    
    print(letter)
    
    
for i in range(len(language)):
    
    print(language[i])
    
numbers=(1,2,3,4,5,6)

for i in numbers:
    
    print(i)
    
print("*******************************************")

person={
    "firstName": "Rahul",
    "lastName":  "Boass",
    "country":    "India",
    "skills":    ["python","sql","ABC"],
    "address":   {"street": "space street", "pincode":"323433"}
}

for key, value in person.items():
    
    
    print(key,value)
    
print(person["address"]["pincode"])
#print(person["skills"][0])

it_companies={"facebook","Ginger webs","Google","flip cart"}

for company in it_companies:
    
    print(company)
    
    
tuple=(1,2,3,4,5,6)

for i in tuple:
    
    print(i)
    
    if i==3:
        break
    

# list=list(range(11))
# print(list)
st=set(range(1,11))
print(st)

l=list(range(2,21,2))
print(l)

for number in range(1,11):
    
    print(number)
    
    
for key in person:
    
    if key=="skills":
        
        for skill in person["skills"]:
            
            print(skill)
    else:
        print("Not exist")
        
        
for number in range(1,11):
    
    print(number)
    
else:
    print("the loop ended",number)
    
    
for i in range(11):
    pass

print("For loop")
for number in range(11):
    
    print(number)
    
print("while loop")   
i=0

while i <=10:
    print(i)
    i=i+1
    
print("****************************")    
for number in range(10,-1,-1):
    
    print(number)
 
    
print("while loop")    
number=10

while number>-0:
    print(number)
    
    number=number-1
    

for i in range(7):
    
    for j in range(i):
        
        print("#",end=" ")
        
    print('\n')


print("****************************")

for i in range(7):
    
    for j in range(7):
        
        print("#",end=" ")
        
    print('\n')
    
    
for i in range(7):
    
    for j in range(i):
        
        print(i*j,end=" ")
        
    print('\n')
    
    
for i in range(11):
    print(f"{i} X  {i}={i*i}")
    
list=['Python', 'Numpy','Pandas','Django', 'Flask']

for l in list:
    print(l)
    
    
for i in range(0,101):
 
    
    if i % 2==0:
        
        print(i)
        
        
for i in range(0,101):
     
    
    if i % 2!=0:
        
        print(i)
        

print("**********************************")       
print("Sum of the number")

sum=0

for num in range(0,101):
    
    
    sum=sum+num
    print(sum)
    
print("the below code")   
sum_evens=0
sum_odds=0

for i in range(101):
    
    if i%2==0:
        
    
        sum_evens=sum_evens+i
    else:
        
        sum_odds=sum_odds+i
        
print(f"Sum of all the even number",{sum_evens})

print(f"Sum of the all the odds",{sum_odds})
    
    
# Import the countries list from the countries.py file
from countries import countries # Adjust the import path if necessary

# Initialize an empty list to store countries containing "land"
countries_with_land = []

# Loop through each country
for country in countries:
    if "land" in country:  # Check if "land" is in the country's name
        countries_with_land.append(country)

# Print the results
print("Countries containing 'land':")
print(countries_with_land)
    