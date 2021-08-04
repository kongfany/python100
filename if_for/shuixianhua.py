"""
----------------------------------------
    File Name: shuixianhua
    Author: Kong
    Date: 2021/7/8
    Description: 寻找所有水仙花数
    水仙花：三位数，个位的3次方之和为本省
    关键得出数字的三位
    个位：num % 10
    十位：num // 10 % 10
    百位：num // 100

    153 370 371 407
----------------------------------------

for num in range(100,1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100

    if num == low ** 3 +mid **3 +high ** 3:
        print(num,end=" ")
"""
"""
找出所有水仙花数
"""
for num in range(100, 1000):
    low = num % 10			# 个位（取余）
    mid = num // 10 % 10	# 十位，先去掉个位（整除），然后取余
    high = num // 100		# 百位，直接去掉后两位（整除）
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)