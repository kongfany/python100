"""
----------------------------------------
    File Name: yanghui
    Author: Kong
    Date: 2021/7/13
    Description: 
----------------------------------------
"""

num =4
yh = [[]] * num
print(yh,len(yh))
for row in range(len(yh)):
    yh[row] = [None] * (row + 1)
    print(yh[row])
    print(yh)
    for col in range(len(yh[row])):
        if col == 0 or col == row:
            yh[row][col] = 1
        else:
            yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
        print(yh[row][col], end='\t')
    print()


