"""
----------------------------------------
    File Name: test
    Author: Kong
    Date: 2021/7/8
    Description: 
----------------------------------------
"""
import module3

module3.foo()
# 导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__