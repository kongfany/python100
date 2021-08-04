"""
----------------------------------------
    File Name: houz
    Author: Kong
    Date: 2021/7/9
    Description: 输出文件后缀
----------------------------------------
"""
from os.path import splitext




def get_suffix(filename):
    """
    :param filename: 文件名
    :return: 后缀
    """
    # # 从字符串中你想查找.出现的位置
    # pos = filename.rfind(".")
    # # 通过切片来获取后缀
    # # return filename[pos+1:] if pos >0 else ""
    # if pos > 0:
    #     return filename[pos+1:]
    # else:
    #     return ""
    return splitext(filename)[1][1:]



# test
print(get_suffix('readme.txt'))       # txt
print(get_suffix('readme.txt.md'))    # md
print(get_suffix('.readme'))          #
print(get_suffix('readme.'))          #
print(get_suffix('readme'))           #