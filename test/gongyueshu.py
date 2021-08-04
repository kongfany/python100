"""
----------------------------------------
    File Name: gongyueshu
    Author: Kong
    Date: 2021/7/7
    Description: 两个数的最大公约数
----------------------------------------
"""

a = int(input("a = "))
b = int(input("b = "))

if a>b:
    a,b=b,a
for i in range(a,0,-1):
    if a%i == 0 and b%i == 0:
        print(f"{a}和{b}的最大公约数为：{i}")
        break
