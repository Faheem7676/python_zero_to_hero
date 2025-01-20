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

# modifiying list
fruits=["Apple","Banana","Carrot","Orange","Grapes"]

fruits[0]="Alpha"
print(fruits)
fruits[1]="Apple"
print(fruits)

last_index=len(fruits)-1
print(last_index)

fruits[last_index]="lime"
print(fruits)

does_exist="Carrot" in fruits

print(does_exist)

isexist="Orange" in fruits
print(isexist)

fruits.append("Apple")
print(fruits)
fruits.append("lime")
print(fruits)

fruits=["Apple","Banana","Carrot","Orange","Grapes"]

fruits.insert(1,"Narangi")
print(fruits)
fruits.insert(1,"Narangi")
print(fruits)

fruits.remove("Narangi")
print(fruits)
fruits.insert(4,"Narangi")
print(fruits)
fruits.remove("Narangi")
print(fruits)

fruits.remove("Carrot")
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)

del fruits[1]
print(fruits)
del fruits[1:3]
print(fruits)
fruits = ['banana', 'orange', 'mango', 'lemon']

print(fruits)

fruits.clear()
print(fruits)

fruits=['banana', 'orange', 'mango', 'lemon']

fruit_copy=fruits.copy()
print(fruit_copy)

l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
zero=[0]

output=l1+zero+l2
print(output)

fruits=['banana', 'orange', 'mango', 'lemon']
vegitables=["Tomatt","Potato","Cabbage","Onion","Carrot"]
fruit_and_veg=fruits+vegetables
print(fruit_and_veg)

list1=["item1","item2"]
list2=["item3","item4","item5"]

list1.extend(list2)

print(list1)

num1=[1,2,3,4,5,6]
num2=[1,2,7,8,9]

num1.extend(num2)
print("Numbers:",num1)

negative_num=[-1,-2,-3,-4]
positive_num=[1,2,3,4,5]
zero=[0]
negative_num.extend(zero)
print(negative_num)

fruits=['banana', 'orange', 'mango', 'lemon',"lemon","lemon"]

count_of_repeated=fruits.count("lemon")
print(count_of_repeated)

ages=[22,44,22,44,55,22,11,22]
print(ages.count(22))

# index of the list

index1=fruits.index("orange")
print(index1)

print(ages.index(44))
print(fruits)
fruits.reverse()
print(fruits)

ages.reverse()
print(ages)

integer_list=[10,9,8,7,6,5,4,3,2,1]

integer_list.reverse()

print(integer_list)

fruits.sort()

print(fruits)

fruits.sort(reverse=True)
print(fruits)

ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

empty_list=[]
print(type(empty_list))
# empty_list=list()
# print(type(empty_list))

lst=["Rahul", 43, "Johan",3,2,4,5]

print(lst)
print(len(list))
print(len(lst))

mix_data_type=["name","age","height","marital status","Address","city"]
print(mix_data_type)
print(type(mix_data_type))
print(len(mix_data_type))
print(mix_data_type[0])
print(mix_data_type[-1])
middle_item=mix_data_type[len(mix_data_type)//2]
print(middle_item)

it_companies=["Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon"]

print("IT_Companies:",it_companies)
companies=it_companies.count("Apple")
print("companies number:",companies)



it_companies.count("Microsoft")
print(it_companies)

it_companies.append("Ginger")
print(it_companies)

it_companies.insert(1,"TATA")

print(it_companies)

deosExist="Microsoft" in it_companies
print(deosExist)