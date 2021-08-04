"""
----------------------------------------
    File Name: tihuan
    Author: Kong
    Date: 2021/7/29
    Description: 
----------------------------------------
"""
import re

sentence = 'Oh, shit! 你丫是傻叉吗? Fuck you.'
purified = re.sub('fuck|shit|[傻煞沙][比逼叉缺吊碉雕]',
                  '*', sentence, flags=re.IGNORECASE)
print(purified)  # Oh, *! 你丫是*吗? * you.