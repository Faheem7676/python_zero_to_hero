str="Kareem"

print(str)

print(len(str))

greeting="Hello World"

print(greeting)
    
    
print(len(greeting))

sentence="I hope you are enjoying python code of 30 days"

print(sentence)

multiline_string='''
This is sentence where.\n we can go and enjoy
there is python code program I can give you new
line '''

print(multiline_string)

string_multiline="""
this is the code where we can get all code"""

print(string_multiline)

first_name="Rahul"
last_name="Bosssss"

full_name=first_name+last_name
print(full_name)

print(len(first_name))
print(len(last_name))
print(len(first_name)>(len(last_name)))

print(len(full_name))

print("I am not goin to tell you. \n You get it from your self.")

print("Days\tTopics\tExercise")

print("Day t1\t5\t6")

#string only

first_name="Wakeel"
last_name="juj"
language="python"
print("I am %s %s. I teach %s" %(first_name,last_name,language))

#string and number
radious=10
pi=3.14
area=pi*radious**2

formated_string="The area of circle with the %d is %.2f." %(radious,area)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)

print(formated_string)

python_libraries=["Numpy","Django","Flask","Pandas"]

print("I am learning python libraries. %s" %(python_libraries))

# This formatting is introduced in Python version 3.
first_name="Naaz"
last_name="Ahmed"
language="Python"
print("I am {} {}. and I am learning {}".format(first_name,last_name,language))

a=4
b=3

print("{} + {} = {}".format(a,b,a+b))

print("{}-{}={}".format(a,b,a-b))

print("{} * {}={}".format(a,b,a*b))

print("{} % {}={}".format(a,b,a%b))

print("{}/{}={}".format(a,b, a/b))

print("{}//{}={}".format(a,b, a//b))

print("{}**{}={}".format(a,b,a**b))

language="Python"
print(language)
a,b,c,d,e,f=language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print(len(language)-1)

language="python"
print(language[0])
print(language[1])
last_index=len(language)-1
last_letter=language[last_index]
print(last_letter)

print(language[-1])
print(language[-2])

language="python"
first_three=language[0:3]
# last three
last_three=language[-3:]
print(first_three)

print(last_three)

print(language[3:6])

print(language[3:])

greeting="Hello World"

print(greeting[::-1])

reversestr=""

for i in greeting:
    
    reversestr=reversestr+i
    
print(reversestr)

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto


print(language.capitalize())

string="Faheem is good tester but he is trying to swithc from manual to automation"

print(string.count("automation"))

print(string.endswith("ion"))

print(string.endswith("oon"))

tabspace="thirty\tdays\tof\tpython"

print(tabspace.expandtabs())
print(tabspace.expandtabs(10))

str="Kaleem"

print(str.find("e"))
print(str.find("i"))
print(str.rfind("e"))


first_name="Faheem"
last_name="Farooqui"
job="Software Testing"
sentence="I am {} {} and I am looking for a job in {} industries.".format(first_name,last_name,job)
print(sentence)

challenge="python course of 30 days"
substring="n"

print(challenge.index(substring,5))

checks="pythoncodecourse123"

print(checks.isalnum())

checks="python code is easy"
print(checks.isalnum())

isAlpha="pythoncodeisgoodprograminglanguage"
print(isAlpha.isalpha())

isAlpha="ABC332"
print(isAlpha.isalpha())

isAlpha="ABCfldsjfljsdlfjd"
print(isAlpha.isalpha())

destring="this is python code"
print(destring.isdecimal())

destring="443343980808"
print(destring.isdecimal())

isDigit="-1"
print(isDigit.isdigit())
isDigit="\u00B2"
print(isDigit.isdigit())

isDecimal="1299"
print(isDecimal.isdecimal())

challenge = '\u00B2'
print(challenge.isdigit())   # True

num="23"
print(num.isnumeric())

num="Abc00BD"
print(num.isnumeric())

num="\u00BD"
print(num.isnumeric())
num="3.23"
print(num.isnumeric())

challenge="34string"
print(challenge.isidentifier())
challenge="fadfd43"
print(challenge.isidentifier())
challenge="ff.afd"
print(challenge.isidentifier())

string="THIS_IS_PYTHON_CODE"

print(string.isidentifier())
print(string.islower())
print(string.isupper())

web_tech=["Html","CSS","JavaScript","React"]

result=" ".join(web_tech)

print(result)

string="  Fah  eem   "
print(string)

print(string.strip())

print(string.replace("F","S"))

string="thirty, days, of, python"

print(string.replace("python","coding"))

print(string.split())

print(string.split(","))

string="FaheemamFaheemandlookingforajob"

print(string.title())

print(string.swapcase())

print(string.startswith("ah"))

print(string.isalpha())

company="Coding for all"
print(company)
print(len(company))

print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

first_word="Coding For All string."

print(first_word[0:6])

print(first_word.replace("Coding","Python"))

string="Python for Everyone"
changstring="Python for All"
print(string)

print(string.replace("for Everyone","for All"))

print(string.split())

string="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(string.split(","))

# string="Coding For All"
# print(string.index[0])

print("I am enjoying this challenge.\nI just wonder what is next.")

radious=10
area=3.14 * radious **2

print("The area of circle with radious {} is.".format(area,radious))

a=8
b=6
print("{}+{}={}".format(a,b,a+b))

print("{}-{}={}".format(a,b,a-b))

print("{} * {}={}".format(a,b, a*b))

python_libraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

print("#".join(python_libraries))

variable1="30DaysOfPython"
variable2="thirty_days_of_python"

print(variable1.isidentifier())
print(variable2.isidentifier())

string='   Coding For All      '
print(len(string))
string2=string.strip()
print(len(string2))



string="Try programiz.pro"

string.lower()
string1=string.lower()
print(string1)

# intialize dictionary to store char count
char_counts={}

# iterate each char in the string
for char in string:
    
    if char!=" ":
        
        if char in char_counts:
            
            char_counts[char]+=1
            
        else:
            char_counts[char]=1
        
# repeated_char={char: count for}
#     print(char_counts)

repeated_chars = {char: count for char, count in char_counts.items() if count > 1}
print("repeted_chars:",repeated_chars)


string="I am Faheem"

l=string.split()
print(l)

reverse_string=" ".join(reversed(l))

print(reverse_string)


from collections import Counter

string="ABCDEABCDabcabchkldh"


char_counts=Counter(string)


# Filter and display only the repeated characters
repeated_chars = {char: count for char, count in char_counts.items() if count > 1}

print(repeated_chars)
print(char_counts)


string="ABCdeGFABCTESd"

string.lower()
print(string)

char_count={}

for char in string:
    
    if char!=" ":
        
        if char in char_count:
            
            char_count[char]=char_count[char]+1
            
        else:
            char_count[char]=1
            
repeated_chars = {char: count for char, count in char_count.items() if count > 1}
print("repeted_chars:",repeated_chars)


d={1: "firstValue",2: "secondvalue"}

print(d[1])

string="ABCEDabcd"


    





