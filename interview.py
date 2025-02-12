input="this.is.world"
output="world.is.this"

print(input.split())
print(type(input))

reverse=" ".join(reversed(input))
print(reverse)

reverstring=""

for char in input:
    
    reverstring=char+reverstring
    
print(reverstring)

# splt=input.split()
# print(splt)
output=".".join(input.split(".")[::-1])
print(output)


input="this.is.world"

reverse=input.split(".")

reverse=reverse[::-1]

print(reverse)

string=".".join(reverse)
print(string)
print(type(string))

input="this.is.world"

l=input.split(".")

print(l)

reverse=l[::-1]
print(reverse)

output=".".join(reverse)
print(output)