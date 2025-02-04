str="my dog is great"


for i in str:
    
    if i=="dog":
        
        print("exist")
        
    else:
        print("Not exist")
        
        
text="The Agent's phone number is 480-555-1234. call soon"

'phone' in text

import re

pattern="phone"

print(re.search(pattern,text))

pattern="Not In Text"

print(re.search(pattern,text))

pattern="phone"

print(re.search(pattern,text))

match=re.search(pattern,text)
print(match)

print(match.span())

print(match.start())
print(match.end())

text="my phone once, my phone twice"

match=re.search('phone',text)

print(match)

matches=re.findall('phone',text)
print(matches)

print(len(matches))

for match in re.finditer('phone',text):
    
    #print(match)
    print(match.span())