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

assert  3 < 4

# while循环，条件为True就一直循环下去
# for循环 for 目标 in 表达式：
#   循环体

favourite = 'fishC'
for i in favourite:
    print(i,end=' ')

#[]是列表
member = ['今天','明天','小甲鱼','谭劲']
for each in member:
    print(each, len(each))

# range([strat,] stop [,step = 1])
test = range(5)
print(test)
print(list(range(5)))
for i in range(5):
    print(i,'下一步')

for i in range(2,9):
    print(i)

for i in range(1, 10,2):
    print(i,'三参数步进2')
# break语句
bingo = '胡庆是美女'
answer = input('请输入一句话：')

while True:
    if answer == bingo:
        break
    answer = input('抱歉，错了，请重新输入')

print('哎哟，你真行')
# continue终止本轮循环，开始下一轮循环，参数循环条件为True
for i in range(10):
    if i%2 != 0:
        print(i)
        continue
    i += 2
    print(i)

