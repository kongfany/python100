"""
----------------------------------------
    File Name: sushu
    Author: Kong
    Date: 2021/7/8
    Description: 100以内的素数
    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
----------------------------------------

for num in range(2,100):
    is_prime=True
    mid=int(num**0.5)
    for i in range(2,mid+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num,end=" ")"""

for num in range(2, 100):  # 2~99
    # 假设num是素数
    is_prime = True
    # 在2到num-1之间找num的因子
    for factor in range(2, num):
        # 如果找到了num的因子，num就不是素数
        if num % factor == 0:
            is_prime = False
            break
    # 如果布尔值为True在num是素数
    if is_prime:
        print(num,end=" ")



print("\\\\")
