"""
----------------------------------------
    File Name: quji
    Author: Kong
    Date: 2021/7/26
    Description: 
----------------------------------------
"""
# def is_even(num):
#     return num % 2 == 0
#
#
# def square(num):
#     return num ** 2
#
#
# numbers1 = [35, 12, 8, 99, 60, 52]
# numbers2 = list(map(square, filter(is_even, numbers1)))
# print(numbers2)
# numbers3 = list(filter(is_even,numbers1))
# print(numbers3) # [12, 8, 60, 52]

numbers1 = [35, 12, 8, 99, 60, 52]
numbers3 = [x for x in numbers1 if x % 2 == 0]
print(numbers3) # [12, 8, 60, 52]
numbers2 = [num ** 2 for num in numbers1 if num % 2 == 0]
print(numbers2)    # [144, 64, 3600, 2704]