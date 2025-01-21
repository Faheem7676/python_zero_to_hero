num=10
print(type(num))

string="faheem"
print(type(string))

boolean=True
print(boolean)

lst=[]
print(type(lst))

class list:
    pass

class Person:
    
    pass
print(Person)

class Person:
    
    def __init__(self,name):
        
        self.name=name
        
obj=Person("Kaleem")
print(obj.name)

class Person:
    
    def __init__(self,firstName,lastName,age,country,city):
        
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        self.country=country
        self.city=city
        
obj=Person("Kaleem","Rahul",34,"India","Dbg")
print(obj.firstName)
print(obj.lastName)
print(obj.age)
print(obj.country)
print(obj.city)

class Person:
    
    def __init__(self,firstName,lastName,age,country,city):
        
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        self.country=country
        self.city=city
        
    def person_info(self):
        
        return f"{self.firstName} {self.lastName} is {self.age} years old. He lives in {self.city}",
    
obj=Person("kaleem","kumar",45,"India","DBG")
print(obj.person_info())