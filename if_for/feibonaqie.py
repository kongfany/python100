"""
----------------------------------------
    File Name: feibonaqie
    Author: Kong
    Date: 2021/7/8
    Description: 斐波那契数列
    前两个数是1 1 然后后面的数为前两个数的和
----------------------------------------
"""
a = 1
b = 1

print(a,b,end=" ")

for i in range(18):
    a,b=b,a+b
    print(b,end=" ")
