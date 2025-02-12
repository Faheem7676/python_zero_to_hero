class Tests:  
    def __init__(self, names):  
        self.cards = []  
        self.name = names  
    def __str__(self):  
        return '{} holds ...'.format(self.name)   
obj11 = Tests('obj11')  
print(obj11.__dict__)
#print(obj11) 
obj22 = Tests('obj22')  
#print(obj22) 

print(type(obj11))


def fast(item2=[]):
    
    item2.append(1)
    
    return item2

print(fast())
print(fast())
print(fast())

l=["a","a","b","a","c","d","b","F"]
s=set(l)
print(s)
print(list(s))

print(list(set(l)))

import sys
print(sys.version)


