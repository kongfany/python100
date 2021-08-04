"""
----------------------------------------
    File Name: zhengshufanzhuan
    Author: Kong
    Date: 2021/7/8
    Description: 正整数反转
    123--321
    关键在于每次得到最低为 3，然后将数字变成 12
    继而得出次低位，并将最低位的十倍加上次低位
----------------------------------------
"""

num = int(input("请输入一个正整数："))
# reversed_num = 0
#
# while num > 0:
#     reversed_num = num % 10 + reversed_num * 10
#     num //= 10
# print(reversed_num)

s = str(num)
l=list(s) # 字符串转列表
l.reverse() # 列表反转
result = "".join(l) #列表转字符串
f=int(result)
print(f,type(f))