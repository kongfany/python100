"""
----------------------------------------
    File Name: maxmin
    Author: Kong
    Date: 2021/7/11
    Description: 
----------------------------------------
"""
def find_max_and_min(items):
    max_one,min_one = items[0],items[0]
    for item in items:
        if item > max_one:
            max_one = item
        if item < min_one:
            min_one = item
    return max_one,min_one

a = find_max_and_min([1,2,3,4])
print(a)