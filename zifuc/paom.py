"""
----------------------------------------
    File Name: paom
    Author: Kong
    Date: 2021/7/9
    Description: 跑马灯
----------------------------------------
"""
import os
import time
content = "北 京 欢 迎 你 "
for _ in  range(4):
    print(content)
    time.sleep(0.2)
    content = content[1:] + content[0]