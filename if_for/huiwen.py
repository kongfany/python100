"""
----------------------------------------
    File Name: huiwen
    Author: Kong
    Date: 2021/7/8
    Description: 回文数的判断

    通过整数反转，然后判断是不是相等
----------------------------------------
"""
num = int(input("请输入一个正整数："))
temp = num  # 用temp去操作num，保证num的初始值
num2 = 0    # 记录反转的数

while temp > 0:
    num2 = num2 * 10 + temp%10
    temp //=10

if num == num2:
    print(f"{num}是回文数")
else:
    print(f"{num}不是回文数")