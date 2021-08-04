"""
----------------------------------------
    File Name: csv3
    Author: Kong
    Date: 2021/7/31
    Description: 
----------------------------------------
"""
import csv
import random

with open('scores.csv', 'w') as file:
    writer = csv.writer(file)
    #writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_ALL)
    writer.writerow(['姓名', '语文', '数学', '英语'])
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    for i in range(5):
        verbal = random.randint(50, 100)
        math = random.randint(40, 100)
        english = random.randint(30, 100)
        writer.writerow([names[i], verbal, math, english])