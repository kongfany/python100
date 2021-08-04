"""
----------------------------------------
    File Name: bij
    Author: Kong
    Date: 2021/7/13
    Description: 
----------------------------------------
"""
set1 = {1,3,5}
set2 = {1,2,3,4,5}
set3 = set2
print(set1<set2,set1<=set2)
print(set2<set3,set2<=set3)
print(set1.issubset(set2))
print(set2.issuperset(set1))
print(set2>set1)
