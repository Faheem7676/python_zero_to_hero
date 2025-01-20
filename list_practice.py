empty_list=list()
print(len(empty_list))

lst=[]
empty_list=[]
print(empty_list)

print(len(empty_list))

fruits=["Banana","organge","Manago","Lemon"]
print(list(fruits))
print(fruits[0])
#print the lists and length
print("Fruits:",fruits)
print("Number of fruits:",len(fruits))

vegetables=["potato","tomato","Cabbage","Onion","Carrot"]

print(vegetables)

animal_product=["milk","meat","butter","yoghurt"]
print(animal_product)
countries=['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
print(countries)

web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']

print("web technologies:",web_techs)

print("Number of web techs:",len(web_techs))

# list can have items of different data type, like dictionary , string, integer

list=["Rahul",250, True ,{"Name": "Rahul Boss", "Age": 45, "Address": "India"}]

print(list)

fruits=["Banana","organge","Manago","Lemon"]

first_fruit=fruits[0]
print(first_fruit)

second_fruit=fruits[1]
print(second_fruit)

last_fruit=fruits[3]
print(last_fruit)

#last_index
last_index=len(fruits)-1
print(last_index)
last_fruit=fruits[last_index]
print(last_fruit)

l=["Kareem","Raheem","Faheem","Saleem","Hareem"]

last_index=len(l)-1
print(last_index)
lastName=l[last_index]
print(l[last_index])
print(lastName)

fruits=["Banana","Apple","Orange"]
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

# unpacking list items
lst=["item1","item2","item3","item4","item5","item6"]

first_item,second_item,third_item, * rest=lst

print(first_item)
print(second_item)
print(third_item)
print(rest)

fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']

first_fruit,second_fruit,third_fruit,fourth_fruit, *rest=fruits

print(first_fruit)
print(second_fruit)
print(third_fruit)
print(fourth_fruit)
print(rest)
    
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia',"Espasia"]
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
# print all items by using slice
print(fruits[0:7])
print(fruits[0:])
print(fruits[::])
print(fruits[2:4])

print(fruits[1:])
print(fruits[::2])

all_fruits=fruits[-4:]
print(all_fruits)
print(fruits[-3:-1])
print(fruits[-3:])
print(fruits[::-1])
string="Kaleem"
print(string[::-1])
    
