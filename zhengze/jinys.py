"""
----------------------------------------
    File Name: jinys
    Author: Kong
    Date: 2021/7/29
    Description: 
----------------------------------------
"""
import re

poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
sentences_list = re.split(r'[，。, .]', poem)

print(sentences_list)
sentences_list = [sentence for sentence in sentences_list if sentence]
print(sentences_list)
for sentence in sentences_list:
    print(sentence)