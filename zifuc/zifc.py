"""
----------------------------------------
    File Name: zifc
    Author: Kong
    Date: 2021/7/30
    Description: 
----------------------------------------
"""
#import pyperclip

# 转义字符
print('My brother\'s name is \'007\'')
# 原始字符串
print(r'My brother\'s name is \'007\'')

str = 'hello123world'
print('he' in str)
print('her' in str)
# 字符串是否只包含字母
print(str.isalpha())
# 字符串是否只包含字母和数字
print(str.isalnum())
# 字符串是否只包含数字
print(str.isdecimal())

print(str[0:5],str[0:5].isalpha())
print(str[5:8],str[5:8].isdecimal())

list = ['床前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
print('-'.join(list))
sentence = 'You go your way I will go mine'
words_list = sentence.split()
print(words_list)
email = '     jackfrued@126.com          '
print(email)
print(email.strip())
print(email.lstrip())


