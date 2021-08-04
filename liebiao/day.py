"""
----------------------------------------
    File Name: day
    Author: Kong
    Date: 2021/7/12
    Description:
    首先先判断是不是闰年
    闰年2月29，否则28
    列表day_of_month记录每个月对应的天数，嵌套，第一个元素为28,29
----------------------------------------
"""
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
def which_day(year,month,date):
    day_of_month=[
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ]

    days = day_of_month[is_leap_year(year)]
    total = 0
    for index in range(month-1):
        total+=days[index]
    return total+date
print(which_day(1980,11,28))