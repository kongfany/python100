"""
----------------------------------------
    File Name: yanzhengm
    Author: Kong
    Date: 2021/7/9
    Description:
    生成指定位数的随机验证码
    大小写字母＋数字
----------------------------------------
"""

import random
import  string

ALL_CHARS = string.digits + string.ascii_letters

def generate_code(code_len = 4):
    """
    生成指定长度的验证码
    :param code_len: 验证码长度，默认4位
    :return: 由大小写字母和数字组成的随机字符串
    """
    return "".join(random.choices(ALL_CHARS,k = code_len))

for _ in range(10):
    print(generate_code(5))