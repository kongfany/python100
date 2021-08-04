"""
----------------------------------------
    File Name: date
    Author: Kong
    Date: 2021/7/11
    Description:
----------------------------------------
"""
def is_leap_year(year):
    return year%4==0 and year%100!=0 or year%400 == 0

def which_day(year,month,date):
    days_of_month = [[31,28,31,30,31,30,31,31,30,31,30,31],
                     [31,29,31,30,31,30,31,31,30,31,30,31]]
    days = days_of_month[is_leap_year(year)]
    total = 0
    for index in range(month -1):
        total+=days[index]
    return total+date

print(which_day(1980,11,28))