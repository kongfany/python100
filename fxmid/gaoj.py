"""
----------------------------------------
    File Name: gaoj
    Author: Kong
    Date: 2021/7/26
    Description: 
----------------------------------------
"""
import operator
def calc(*args, init_value, op, **kwargs):
    result = init_value
    for arg in args:
        result = op(result, arg)
    for value in kwargs.values():
        result = op(result, value)
    return result

# def add(x, y):
#     return x + y
#
#
# def mul(x, y):
#     return x * y

# print(calc(1, 2, 3, init_value=0, op=add, x=4, y=5))      # 15
# print(calc(1, 2, x=3, y=4, z=5, init_value=1, op=mul))    # 120

print(calc(1, 2, 3, init_value=0, op=operator.add, x=4, y=5))
print(calc(1, 2,init_value=1, op=operator.mul, x=3, y=4, z=5))