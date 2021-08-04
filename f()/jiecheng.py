"""
----------------------------------------
    File Name: jiecheng
    Author: Kong
    Date: 2021/7/8
    Description: 阶乘
----------------------------------------
"""
"""
输入M和N计算C(M,N)
从m中选n的结果
"""

# 定义函数：def是定义函数的关键字、fac是函数名，num是参数
def fac(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    # 返回num的阶乘（因变量）
    return result

m = int(input('m = '))
n = int(input('n = '))
# 当需要计算阶乘的时候不用再写重复的代码而是直接调用函数fac
# 调用函数的语法是在函数名后面跟上圆括号并传入参数
print(fac(m) // fac(n) // fac(m - n))