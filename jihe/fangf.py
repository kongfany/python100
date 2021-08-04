"""
----------------------------------------
    File Name: fangf
    Author: Kong
    Date: 2021/7/13
    Description: 
----------------------------------------
"""
set1 = set()
set1.add(33)
set1.add(55)
set1.update({1,10,100,1000})
print(set1)

set1.discard(100)
set1.discard(99)
print(set1)
if 10 in set1:
    set1.remove(10)
print(10)

print(set1.pop())

set1.clear()
print(set1)