"""
----------------------------------------
    File Name: luck
    Author: Kong
    Date: 2021/7/12
    Description: 
----------------------------------------
"""
persons = [True]*30
# counter 死的人
# index 访问列表的索引
# number 报的人数
counter,index,number = 0,0,0
while counter<15:
    if persons[index]:
        number+=1
        if number ==9:
            persons[index]=False
            counter+=1
            number = 0
    index+=1
    index%=30
for person in persons:
    print("女" if person else "男",end=" ")