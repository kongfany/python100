"""
----------------------------------------
    File Name: feib
    Author: Kong
    Date: 2021/7/27
    Description: 
----------------------------------------
"""
def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


# 打印前20个斐波那契数
for i in range(1, 21):
    print(fib(i),end=" ")

print()
def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

for i in range(1,21):
    print(fib2(i),end=" ")