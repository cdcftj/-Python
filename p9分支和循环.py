score = int(input('输入分数'))
if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
    print('B')
elif 80 > score >=60:
    print('C')
elif 60 > score >=0:
    print('D')
else:
    print('输入错误')
# 条件表达式（三元操作符）
x,y = 4,5
if x < y:
    small = x
else:
    small =y
# x < y 条件为True把x给small,条件为False把y给small
small = x if x < y else y

#断言 assert关键字后边的条件为Flase程序崩溃抛出AssertionError

assert  3 > 4
