"""
----------------------------------------
    File Name: zhuan
    Author: Kong
    Date: 2021/7/30
    Description: 
----------------------------------------
"""
from PIL import Image
image = Image.open('messi.jpg')
# 使用Image对象的rotate方法实现图像的旋转
image.rotate(45).show()
# 使用Image对象的transpose方法实现图像翻转
# Image.FLIP_LEFT_RIGHT - 水平翻转
# Image.FLIP_TOP_BOTTOM - 垂直翻转
image.transpose(Image.FLIP_TOP_BOTTOM).show()