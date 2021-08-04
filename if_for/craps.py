"""
----------------------------------------
    File Name: craps
    Author: Kong
    Date: 2021/7/8
    Description: craps赌博

我们设定游戏开始时玩家有1000元的赌注
游戏结束的条件是玩家破产（输光所有的赌注）
----------------------------------------
"""

from random import randint

money=100

while money > 0:
    print()
    print(f"当前你还有 {money} 元")
    go_on = False

    # 下注
    while True:
        debt = int(input("请下注："))
        if 0<debt<=money: #wc!
            break

    # 第一次掷骰子
    first = randint(1,6) + randint(1,6)
    print(f"摇出来了{first}点")

    if first == 7 or first == 11:
        print("玩家获胜！")
        money += debt
    elif first == 2 or first == 3 or first ==12:
        print("庄家获胜！")
        money -= debt
    else:
        print("未分出胜负，继续摇骰子")
        go_on = True

    # 未分出胜负，继续
    while go_on:
        go_on = False
        current = randint(1,6) + randint(1,6)
        print(f"摇出来了{current}点")

        if current == 7:
            print("庄家胜！")
            money -= debt
        elif current == first:
            print("玩家获胜！")
            money +=debt
        else:
            print("未分出胜负，继续摇骰子")
            go_on = True

print("你破产了，游戏结束！")
