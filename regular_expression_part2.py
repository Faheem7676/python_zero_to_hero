import re
text="My phone number is 401-555-1234"
phone=re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)

print(phone)

print(phone.group())

#text="My phone number is 401-555-1234"

phone=re.search(r'\d{3}-\d{3}-\d{4}',text)

print(phone)

phone_pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')

results=re.search(phone_pattern,text)

print(results.group())

print(results.group(1))

print(results.group(2))

print(results.group(3))

print(results.group(1))