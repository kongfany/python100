"""
----------------------------------------
    File Name: f1
    Author: Kong
    Date: 2021/7/28
    Description: 
----------------------------------------
"""
birth = input('请输入你的生日: ')
with open('pi_million_digits.txt') as f:
    lines = f.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    if birth in pi_string:
        print('Bingo!!!')