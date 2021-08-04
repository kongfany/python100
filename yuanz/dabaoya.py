"""
----------------------------------------
    File Name: dabaoya
    Author: Kong
    Date: 2021/7/11
    Description: 
----------------------------------------

a = 1,10,100
print(type(a),a)

i,j,k=a
print(i,j,k)
a =1,10,100,1000
i,j,*k=a
print(i,j,k,type(k))

a,b,*c = range(1,10)
print(a,b,c)
a,b,c = [1,10,100]
print(a,b,c)"""

def add(*args):
    print(type(args),args)
    total = 0
    for val in args:
        total += val
    print(type(total),total)
    return total

add(1,10,100)
add(1,2,3,4,5)
