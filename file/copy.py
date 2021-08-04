"""
----------------------------------------
    File Name: copy
    Author: Kong
    Date: 2021/7/27
    Description: 
----------------------------------------
"""
try:
    with open('kong.png', 'rb') as file1:
        data = file1.read()
    with open('hhh.png', 'wb') as file2:
        file2.write(data)
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
print('程序执行结束.')