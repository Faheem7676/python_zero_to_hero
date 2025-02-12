# Simple iteration
item_list=[]

for n in range(10):
    
    item_list.append(n)
    
print(item_list)



for n in range(2,101,2):
    
    item_list.append(n)
    
print(item_list)

l=list("I was learning Python.")
print(l)

print(l[0])
print(l[1])
print(l[2])
print(l[3])

list2=[]
for i in l:
    
    print(i)
    
    
    list2.append(i)

    
print(list2)

item_list=[]

for i in range(1,11):
    
    item_list.append(i*2)
    
print(item_list)

# list comprehension
item1=[i*2 for i in range(10)]
print(item1)

item1={i:i*2 for i in range(10)}

print(item1)
print("****************")

item1={n1:n1*2 for n1 in range(10)}

newdic=item1.copy()
print(newdic)
    
    
    


