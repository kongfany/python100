"""
----------------------------------------
    File Name: replace
    Author: Kong
    Date: 2021/7/30
    Description: 
----------------------------------------
"""
from PIL import Image
# 读取neymarjr的照片获得Image对象
ney_image = Image.open('ney.jpg')
# 读取messi的照片获得Image对象
messi_image = Image.open('messi.jpg')
# 从messi的照片上剪裁出messi的头
messi_head = messi_image.crop((200, 150, 480, 400))
width, height = messi_head.size
# 使用Image对象的resize方法修改图像的尺寸
# 使用Image对象的paste方法将messi的头粘贴到ney的照片上
ney_image.paste(messi_head.resize((int(width / 3), int(height / 3))), (200, 40))
ney_image.show()