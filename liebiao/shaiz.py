"""
----------------------------------------
    File Name: shaiz
    Author: Kong
    Date: 2021/7/9
    Description: 掷骰子
----------------------------------------
"""
import random
items = []*6
print(items)
counters = [0] * 6
print(counters)
for _ in range(6000):
    face = random.randint(1,6)
    counters[face-1] += 1
for face in range(1,7):
    print(f"{face}点出现了{counters[face-1]}次")
