print("Testing")
import re

print(re.search(r'cat|dog','the cat is here'))

print(re.findall(r'at', "The cat in the hat sat there"))

print(re.findall(r'.at', "The cat in the hat sat there"))

print(re.findall(r'...at', "The cat in the hat sat went splat"))

print(re.findall(r'^\d', '2 is number'))

print(re.findall(r'^\d', 'the 2 is number'))

print(re.findall(r'\d$', 'the number is 2'))

phrase="there are 3 numbers 34 inside 5 this sentence"

pattern=r'[^\d]+'

print(re.findall(pattern,phrase))

test_phrase="This is a string! But it has puntuation. How can we remove it?"

print(re.findall(r'[^!.? ]+',test_phrase))

clean=re.findall(r'[^!.? ]+',test_phrase)

print(clean)

print(" ".join(clean))



text="Only find the hypen-words in this sentence. But you dont know how-long is that"

pattern=r'[\w]+-[\w]+'

print(re.findall(pattern,text))

text="Hello, would you like some catfish?"
texttwo="Hello, would you like to   take catnap"
textthree="Hellow,have you seen this caterpillar"

print(re.search(r'cat(fish|nap|erpillar)',textthree))
