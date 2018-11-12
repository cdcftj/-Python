import random #random模块，整形函数randint
secret = random.randint(1,10)
print("=========我爱鱼C工作室")
temp=input("心里想的数字：")
guess=int(temp)
while guess != secret:
    temp=input("出错了：")
    guess=int(temp)
    #条件分支语法，while循环
    if guess==secret:
        print("你是蛔虫")
        print("中了也没有奖励")
    else:
        if guess > secret:
            print("哥，大了大了")
        else:
            print("黑，小了！小了")
print("游戏结束")