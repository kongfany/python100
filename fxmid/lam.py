"""
----------------------------------------
    File Name: lam
    Author: Kong
    Date: 2021/7/27
    Description: 
----------------------------------------
"""
# def calc(*args, init_value=0, op=lambda x, y: x + y, **kwargs):
#     result = init_value
#     for arg in args:
#         result = op(result, arg)
#     for value in kwargs.values():
#         result = op(result, value)
#     return result
#
#
# # 调用calc函数，使用init_value和op的默认值
# print(calc(1, 2, 3, x=4, y=5))    # 15
# # 调用calc函数，通过lambda函数给op参数赋值
# print(calc(1, 2, 3, x=4, y=5, init_value=1, op=lambda x, y: x * y))    # 120

import operator, functools

# 一行代码定义求阶乘的函数
fac = lambda num: functools.reduce(operator.mul, range(1, num + 1), 1)
# 一行代码定义判断素数的函数
is_prime = lambda x: x > 1 and all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))

# 调用Lambda函数
print(fac(3))        # 3628800
print(is_prime(9))    # False
a = [1,2,3,4]
b = functools.reduce(operator.mul,a,1)
print(b)