import mymodule
from mymodule import generate_full_name, sum_of_two_number,person
from mymodule import generate_full_name as fullname, sum_of_two_number as total
import os

print(mymodule.generate_full_name("Automation", "Testing"))

print(sum_of_two_number(5,3))

print(person("Automation","Testing"))

# creating directory
#os.mkdir("pythonD")

# changing the correct director path
#os.chdir("Desktop")

#print(os.getcwd)

# removing directory
#os.rmdir()

# some usefull sys command

# to exist command
import sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know the evironment path
sys.path
# to know the version of python you are using

sys.version

from statistics import *

ages=[20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))