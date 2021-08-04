"""
----------------------------------------
    File Name: jason2
    Author: Kong
    Date: 2021/7/27
    Description: 
----------------------------------------
"""
import json



mydict = {
    'name': 'kong',
    'age': 38,
    'qq': 957658,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BYD', 'max_speed': 180},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 320}
    ]
}


file=open('data2.json', 'w',encoding="utf-8")
file.write(json.dump(mydict, ensure_ascii=False))
file.close()


