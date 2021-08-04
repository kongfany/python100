"""
----------------------------------------
    File Name: bianli
    Author: Kong
    Date: 2021/7/11
    Description: 
----------------------------------------
"""
items = ['Python', 'Java', 'Go', 'Swift']

for index in range(len(items)):
    print(f'{index}: {items[index]}')

for index, item in enumerate(items):
    print(f'{index}: {item}')

for item in items:
    print(item)

