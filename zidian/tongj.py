"""
----------------------------------------
    File Name: tongj
    Author: Kong
    Date: 2021/7/13
    Description:
    输入一段话，统计出现的字母的数
----------------------------------------
"""
sentence = input("请输入一段话：")
counter = {}
for ch in sentence:
    if "A"<=ch<="Z" or "a"<=ch<="z":
        counter[ch] =  counter.get(ch,0)+1
print(counter)
for key,value in counter.items():
    print(f"字母{key}出现了{value}次")