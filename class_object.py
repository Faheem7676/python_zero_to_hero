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


class Person:
    
    def __init__(self,firstName="Raheem",lastName="Alam",age=33,country="India",city="DBG"):
        
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        self.country=country
        self.city=city
        
    def person_info(self):
        
        return f"{self.firstName} {self.lastName} is {self.age} years old. He lives in {self.city}",
    
obj=Person()
print(obj.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())


class Person:
    
    def __init__(self,firstName="Raheem",lastName="Alam",age=33,country="India",city="DBG"):
        
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        self.country=country
        self.city=city
        self.skills=[]
        
    def person_info(self):
        
        return f"{self.firstName} {self.lastName} is {self.age} years old. He lives in {self.city}",
    
    def add_skill(self,skill):
        self.skills.append(skill)
        
p1=Person()
print(p1.person_info())
p1.add_skill("HTML")
p1.add_skill("Ruby")
p1.add_skill("JavaScript")
p2=Person("Kareem","Raheem",41,"India","kolkata")
print(p2.person_info())
p2.add_skill("python")
p2.add_skill("UFT")
p2.add_skill("VB Script")
print(p1.skills)
print(p2.skills)


class Student(Person):
    
    pass

object=Student("Automation","Testing",20,"US","Los Angels")
print(object.person_info())
object.add_skill("SQL")
object.add_skill("Swagger")
object.add_skill("zephyr")
print(object.skills)


class Student(Person):
    
    def __init__(self,firstName="A",lastName="B",age=45,country="India",city="M",gender="Male"):
        
        self.gender=gender
        super().__init__(firstName,lastName,age,country,city)
        
    def person_info(self):
        
        gender="He" if self.gender=="male" else "She"
        return f" {self.firstName} {self.lastName} is {self.age} years old.{self.gender} lives in {self.city}, {self.country}."
    
s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)


    