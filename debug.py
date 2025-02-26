def add(a,b):
    
    print(f"debugg: a={a},b={b}")
    
    return a+b
result=add(3,4)
print("output:",result)

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s -%(message)s')


def divide(a, b):
    logging.debug(f"Received values: a={a}, b={b}")
    try:
        result = a / b
        logging.info(f"Division successful: {result}")
        return result
    except ZeroDivisionError as e:
        logging.error(f"Error: {e}")
        return None

divide(10, 2)
divide(10, 0)

import pdb

def multiply(a, b):
    pdb.set_trace()  # Execution will stop here
    return a * b

result = multiply(4, 5)
print(result)