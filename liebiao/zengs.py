"""
----------------------------------------
    File Name: zengs
    Author: Kong
    Date: 2021/7/9
    Description: 
----------------------------------------
"""

items = [x for x in range(6)]
print(items)

items.append(6)
print(items)

items.insert(2,"hello")
print(items)

items.remove("hello")
print(items)

items.pop(0)
items.pop(len(items)-1)
print(items)



items.append(7)
print(items)
items.reverse()
print(items)
print()
print(items.sort())
print(items)
items.sort()
print(items)



