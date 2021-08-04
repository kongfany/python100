"""
----------------------------------------
    File Name: dingyi
    Author: Kong
    Date: 2021/7/9
    Description: 
----------------------------------------
"""
items1 = [x for x in range(1,10)]
print(items1)

items2 = [x for x in "hello world" if x not in " aeiou"]
print(items2)

items3 = [x+y for x in  "ABC" for y in "123"]
print(items3)