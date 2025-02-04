f=open("fileone.txt","w+")
f.write("ONE FILE")
f.close()


# f=open("fileone.txt",'w+')
# f.write("One file")
# f.close()


f=open("filtwo.txt","w+")
f.write("TWO FILE")
f.close

import zipfile

comp_file=zipfile.ZipFile("comp_file.zip","w")
comp_file.write("fileone.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.write("filtwo.txt",compress_type=zipfile.ZIP_DEFLATED)

comp_file.close()

zip_obj=zipfile.ZipFile("comp_file.zip","r")

zip_obj.extractall("extracted_content")

print("pwd")

import shutil

dir_to_zip="/home/faheem/Desktop/python_zero_to_hero/extracted_content"

out_put_filename="example"
print(shutil.make_archive(out_put_filename,"zip",dir_to_zip))

shutil.unpack_archive("example.zip","final_unzip","zip")

str="python is good"

reveString=str.split()
print(reveString)

for word in reveString:
    
    print(" ".join(word[::-1]))

# out put "doog is nohtyp"


for word in str.split():
    
    print(word[::-1])
    
str=" ".join(word)
#print(str)


reveString=str.split()
print(reveString)


from collections import Counter

mylist = [1,1,1,2,2,3,4,4,5,5,5]
#output: {1:3,2:2,3:1,4:2,5:3}

frequency=Counter(mylist)

output=dict(frequency)

print(output)


#***********************************************
m=4
n=5

# create a empty list to store the 
list=[]

# loop m times to create a list

for __ in range(m):
    
    # create an empty list for each row
    
    temp_list=[]

    for i in range(1,n+1):
        
        # Step 4: Add numbers from 1 to n in the temp_list
        temp_list.append(i)
       
    # add the temp list to the list 
    list.append(temp_list)
    
# print each list on new line

for l in list:
    
    print(l)
 #*************************************************************   
 
 
import shutil

shutil.unpack_archive("example.zip", " ", "zip")

with open("extracted_content/fileone.txt") as f:
    
    content=f.read()
    print(content)

#****************************************************************
 
    
        
        


