"""
----------------------------------------
    File Name: f2
    Author: Kong
    Date: 2021/7/28
    Description: 
----------------------------------------
"""
from math import sqrt


def is_prime(n):
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True


# 试一试有什么不一样
#with open('prime.txt', 'a') as f:
with open('prime.txt', 'w') as f:
    for num in range(2, 100):
        if is_prime(num):
            f.write(str(num) + '\n')
print('写入完成!')