empty_dict={}
print(empty_dict)

dct={"key1":"value1","key2":"value2","key3":"value3",'key4':'value4'}

print(dct["key1"])
print(dct["key2"])
print(dct["key3"])


person={
    
    "first_name":"john",
    "last_name": "khan",
    "age": 44,
    "country":"India",
    "is_married": True,
    "skills":["python","UFT","VB Script"],
    "address":{"street": "Space street", "zip code": '453213'}
    
}

print(len(dct))
print(len(person))

# accessing dictionary values

print(dct["key1"])
print(dct["key4"])

print(person["first_name"])
print(person["last_name"])
print(person["country"])
print(person["is_married"])
print(person["skills"])
print(person["skills"][2])
print(person["address"]["street"])
# print(person["city"])

print(person.get("first_name"))
print(person.get("last_name"))
print(person.get("country"))
print(person.get("skills"))
print(person.get("city"))

dct['key5']='value5'

print(dct["key5"])
print(dct)

person["job_title"]="software engineer"

print(person)
print(person["job_title"])
print(person["skills"].append("Sql"))
print(person)
print(person["skills"])

dct["key1"]="Faheem"
print(dct)
person["first_name"]="ABC"
person["age"]=54
print(person)
print("changes dic to list itmes below")
print(dct.items())

print("key5" in dct)
print("key8" in dct)

print(dct.pop("key1"))
print(dct)
print(dct.popitem())

del dct['key2']
print(dct)
dct_copy=dct.copy()
print(dct_copy)

print(dct_copy.keys())
print(dct_copy.values())

print(dct_copy["key3"])