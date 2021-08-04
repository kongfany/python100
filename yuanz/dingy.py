"""
----------------------------------------
    File Name: dingy
    Author: Kong
    Date: 2021/7/11
    Description: 
----------------------------------------
"""

t1 = (30,40,50)
t2 = ("孔",40,True,"徐州")

print(type(t1),type(t2))
print(len(t1),len(t2))

print(t1[0],t1[-3])
print(t2[3],t2[-2])

for member in t2:
    print(member,end=" ")
print()

print(30 in t1)
print("kong" in t2)

t3 = t1 + t2
print(t3)

#切片
print(t3[::-1])
print(t3[::3])