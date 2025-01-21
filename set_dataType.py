st=set()
print(type(st))
print(st)

st={"item1","item2","item3","item4"}
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}

print(len(fruits))


for fruit in fruits:
    print(fruit)
    
    if fruit=="orange":
        
        print("the orange shape is round")
        break
        
    else:
        print("do not find organge")
        
print("banana" in fruits)

st.add("item5")
print(st)

fruits.add("lime")
print(fruits)

st={"item1","item2","item3","item4"}

print(st)
st.add("item5")
print(st)
st.update(["item6","item7","item8"])
print(st)
fruits={"'banana', 'orange', 'mango', 'lemon"}
vegitables=("tomato', 'potato', 'cabbage','onion', 'carrot")

fruits.update(vegitables)
print(fruits)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

st={"item1","item2","item3","item4"}

print(st)
st.remove("item2")
print(st)

lst=["item1","item2","item3","item4","Faheem"]
print(type(lst))

st=set(lst)
print(st)

st1={"item1","item2","item3","item4"}
st2={"item1","item3"}

st3=st1.union(st2)
print(st3)

st1.intersection(st2)
print(st1)

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

for it in it_companies:
    print(it)
    
    
it_companies.add("Twitter")

print(it_companies)

it_companies.update(["Ginger","Flipkart"])
    
print(it_companies)

