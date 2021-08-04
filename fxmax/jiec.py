"""
----------------------------------------
    File Name: jiec
    Author: Kong
    Date: 2021/7/27
    Description: 
----------------------------------------
"""
def fac(num):
    if num in (0, 1):
        return 1
    return num * fac(num - 1)
print(fac(5))    # 120