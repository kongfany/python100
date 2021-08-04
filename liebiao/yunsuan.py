"""
----------------------------------------
    File Name: yunsuan
    Author: Kong
    Date: 2021/7/9
    Description:
    拼接 重复 成员运算 长度 索引
    切片 比较
----------------------------------------
"""
items1 = [x for x in range(5)]
print(items1)
items2 = [x for x in range(5,10)]
print(items2)

items3 = items1 + items2
print(items3)

items4 = items1*3
print(items4)

print(1 in items1)
print(5 in items1)

size = len(items3)
print(size)

print(items3[0],items3[9])

items3[0]=100
print(items3[0],items3[-size])

# 切片
items3[0]=0
print(items3)

print(items3[:4])
print(items3[5:])
print(items3[4::2])
print(items3[-1])

for item in items3:
    print(item,end=" ")
for index in range(len(items3)):
    print(items3[index],end=" ")