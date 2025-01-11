class Cylinder:
    
    def __init__(self,height=1,radious=1):
        
        self.height=height
        self.radious=radious
    
    def volume(self):
        
        return self.height * 3.14 *(self.radious)**2
    
    def surfacearea(self):
        
        top=3.14 * (self.radious **2)

        return (2*top)+(2*3.14* self.radious*self.height)    
    
        
mycylinder=Cylinder(3,5)

print(mycylinder.volume())

print(mycylinder.surfacearea())