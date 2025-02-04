class NameHandler:
    
    name="Rahul"
    Age=34
    Education="BCA"
    
    def display(self,name):
        self.name=name
        
        print("displayed executed")
        
        result=self.name.lower()
        
        print("Name:", result)
        
        if result=="faheem":
            
            return result
            
            #return self.name.lower()
            
        return None
        
    
    
    
p1=NameHandler()
print(p1.name)
print(p1.Age)
print(p1.Education)
inputname=(input("Enter the name"))
print(p1.display(inputname))

p2=NameHandler()
print(p2.name)
print(p2.Age)
print(p2.Education)    
