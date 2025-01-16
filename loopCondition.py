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
print(person["skills"][0])

it_companies={"facebook","Ginger webs","Google","flip cart"}

for company in it_companies:
    
    print(company)
    
    
tuple=(1,2,3,4,5,6)

for i in tuple:
    
    print(i)
    
    if i==3:
        break
