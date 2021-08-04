"""
----------------------------------------
    File Name: cans
    Author: Kong
    Date: 2021/7/26
    Description: 
----------------------------------------
"""
def calc(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for value in kwargs.values():
        result += value
    return result


print(calc())                  # 0
print(calc(1, 2, 3))           # 6
print(calc(a=1, b=2, c=3))     # 6
print(calc(1, 2, c=3, d=4))    # 10