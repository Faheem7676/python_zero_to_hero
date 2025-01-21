tuple=tuple()
print(type(tuple))

tuple=()
print(tuple)
print(type(tuple))

# tuple=(1,2,3)
# print(tuple.count())

empty_tuple=()

# tuple construct
# empty_tuple=tuple()

tpl=(1,2,3,4,5,"tuple1","tuple2")

print(tpl)
fruits=("Banana","Mango","Lemon","Orange")
print(fruits)
print(len(fruits))

print(fruits[0])
print(tpl[0])
print(fruits[1])
print(fruits[-1])
print(fruits[0:])

fruits=("Banana","Mango","Lemon","Orange")

first_fruit=fruits[0]
print(first_fruit)
second_fruit=fruits[1]
print(second_fruit)

lastIndex=len(fruits)-1
print(lastIndex)

last_fruit=fruits[lastIndex]
print(last_fruit)
print(fruits[1:])

print(tpl[0:4])
print(tpl[0:])
print(tpl[1:3])

# Range of negative 

print(fruits[-4:])

print(tpl[-2])

print(fruits[-3:-1])

print(fruits[-3:])

tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)

print(middle_two_items)

# chenging tuple to list list to tuple
tpl=("item1","item2","item3","item4")
print(type(tpl))
lst=list(tpl)
print(type(lst))

fruits = ('banana', 'orange', 'mango', 'lemon')

print(type(fruits))
print(fruits)

fruits=list(fruits)
print(type(fruits))
print(lst)

fruits[0]="Apple"
print(fruits)
tuple(fruits)
print(fruits)
print(type(fruits))