"""
----------------------------------------
    File Name: test
    Author: Kong
    Date: 2021/7/27
    Description: 
----------------------------------------
"""
# file = open('致橡树.txt', 'r', encoding='utf-8')
# print(file.read())
# file.close()
import time

# file = open('致橡树.txt', 'r', encoding='utf-8')
# for line in file:
#     print(line, end='')
#     time.sleep(0.5)
# file.close()


file = open('致橡树.txt', 'a', encoding='utf-8')
file.write('\n标题：《致橡树》')
file.write('\n作者：舒婷')
file.write('\n时间：1977年3月')
file.close()
file = open('致橡树.txt', 'r', encoding='utf-8')
lines = file.readlines()
for line in lines:
    print(line, end='')

file.close()