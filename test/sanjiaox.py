"""
----------------------------------------
    File Name: sanjiaox
    Author: Kong
    Date: 2021/7/7
    Description:画三角形

*
**
***
****
*****

    *   0-0123,4
   **   1-012,34
  ***
 ****
*****

    *       0-1
   ***      1-3
  *****     2-5
 *******    3-7
*********   4-9

每行的个数是2*i+1


----------------------------------------
"""

row = int(input("请输入行数:"))

for i in range(row):
    for j in range(i+1):
        print("*",end="")
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(" ",end="")
        else:
            print("*",end="")
    print()

for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()