def vowelCount(user_input):
    
    vowels="aeiouAEIOU"
    
    vowel_count=0
    consonent_count=0
    
    
    for char in input:
        
        if char.isalpha():
            
            vowel_count +=1
            
        else:
            
            consonent_count +=1
            
    return vowel_count,consonent_count

# input from user         
input=input("Enter the string")

# count vowel and consonents

vowels,consonents=vowelCount(input)

print(vowels)
print(consonents)
