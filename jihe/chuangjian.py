"""
----------------------------------------
    File Name: chuangjian
    Author: Kong
    Date: 2021/7/12
    Description: 
----------------------------------------
"""
set1 = {1,2,3,3,3,2}
print(set1,len(set1))

set2 = set("hello")
print(set2)

set3 = set([1,2,3,3,2,1])
print(set3)

set4 = {num for num in range(1,20) if num%3==0 or num%5==0}
print(set4)

for elem in set4:
    print(elem)
