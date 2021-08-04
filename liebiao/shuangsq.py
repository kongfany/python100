"""
----------------------------------------
    File Name: shuangsq
    Author: Kong
    Date: 2021/7/12
    Description:
    双色球
    1-33红色中选6个，1-16蓝色选1个
----------------------------------------
"""
from random import randint,sample

def display(balls):
    for index,ball in enumerate(balls):
        if index == len(balls)-1:
            print("|",end=" ")
        print(f"{ball:0>2d}",end=" ")
    print()

def random_select():
    red_balls = [x for x in range(1,34)]
    select_balls = sample(red_balls,6)
    select_balls.sort()
    select_balls.append(randint(1,16))
    return select_balls

n = int(input("机选几注："))
for _ in range(n):
    display(random_select())