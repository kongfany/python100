"""
----------------------------------------
    File Name: guess
    Author: Kong
    Date: 2021/7/7
    Description: 猜数1-100，并记录猜数的次数
----------------------------------------
"""
from random import randint

answer = randint(1,100)
counter = 0

while True:
    counter += 1
    number = int(input("请猜数： "))

    if number > answer:
        print("猜大了")
    elif number < answer:
        print("猜小了")
    else:
        print("猜对了",end='\t')
        break

print(f"一共猜了{counter}次")



