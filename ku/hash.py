"""
----------------------------------------
    File Name: hash
    Author: Kong
    Date: 2021/7/27
    Description: 
----------------------------------------
"""
import hashlib

# 计算字符串"123456"的MD5摘要
print(hashlib.md5('123456'.encode()).hexdigest())

# 计算文件"Python-3.7.1.tar.xz"的MD5摘要
# 当前目录
hasher = hashlib.md5()
with open('123.txt', 'rb') as file:
    data = file.read(512)
    while data:
        hasher.update(data)
        data = file.read(512)
print(hasher.hexdigest())