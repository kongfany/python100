"""
----------------------------------------
    File Name: perfect
    Author: Kong
    Date: 2021/7/8
    Description: 完美数
    1
6
28
496
8128
----------------------------------------
"""
import math

for num in range(1, 10000):
    result = 0  # 记录所有因子的和，factor为因子
    for factor in range(1,int(math.sqrt(num))+1): # factor为因子
        if num % factor == 0:
            result +=factor
            if factor >1 and num // factor != factor:
                result+=num//factor
    if result == num:
        print(num)
