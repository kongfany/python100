"""
----------------------------------------
    File Name: sushu
    Author: Kong
    Date: 2021/7/7
    Description: 判断素数
----------------------------------------
"""
number = int(input("输入一个整数："))

end = int(number**0.5)
flag=True

for i in range(2,end+1):
    if number%i == 0:
        flag = False
        break
    if flag and number !=1:
        print(f"{number}是素数")
    else:
        print(f"{number}不是素数")
