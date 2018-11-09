print("=========我爱鱼C工作室")
temp=input("心里想的数字：")
guess=int(temp)
while guess != 8:
    temp=input("出错了：")
    guess=int(temp)
    #条件分支语法，while循环
    if guess==8:
        print("你是蛔虫")
        print("中了也没有奖励")
    else:
        if guess > 8:
            print("哥，大了大了")
        else:
            print("黑，小了！小了")
print("游戏结束")