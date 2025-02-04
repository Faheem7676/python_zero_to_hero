def func_one(n):
    
    return [str(num)for  num in range(n)]

print(func_one(10))


def func_two(n):
    
    return list(map(str,range(n)))

print(func_two(10))

import time
# current time before
start_time=time.time()
print(start_time)
# run code
result=func_one(100000)
# current time after running code
end_time=time.time()
print(end_time)
# Elapsed time
Elapsed_time=end_time-start_time
print(Elapsed_time)


import timeit

stmt="""
func_one(100)
"""

setup='''
def func_one(n):
    return [str(num) for num in range(n)]
    '''

print(timeit.timeit(stmt,setup,number=1000000))

stmt2='''
func_two(100)
'''

