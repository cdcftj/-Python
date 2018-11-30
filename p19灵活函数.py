#  离散数学题，在1-1000000中有多少个数字包括0或者1
#a = 0
c: int = 0
for i in range(1,1000000):
#while a < 1000000:
#    a += 1
#    b = str(a)
    b = str(i)
#    list(b)
#    print(list(b))
#    print('0' in b or '1' in b)
    if ('0' in b or '1' in b):
        c += 1
print(c)

# p20 函数与过程
# 函数(function):有返回值
# 过程(procedure)是简单、特殊并且没有返回值
# Python只有函数没有过程
def hello():
    print('Hello FishC!')
temp = hello()
print(temp)# 打印返回None对象
print(type(temp)) # 返回class 'NoneType"
# Pyhton没有变量，只有名字，可以返回多个值
def back():
    return [1,'小甲鱼',3.14]
print(back()) #list返回多个值

def back():
    return 1,'小甲鱼',3.14
print(back())#返回值是元组
# 重点函数变量的作用域问题：
# 局部变量和全局变量
# 局部变量（Local Variable） 全局变量（Globl Variable）
def discounts(price, rate):
    final_price = price * rate
   # print('这里试图打印全局变量old_price的值:',old_price)
    #打印全局变量是可以的
    old_price = 50 #不要改全局变量的值
    #在函数内修改全局变量Python将自动创建一个新的局部变量代替，名字跟全局变量一样
    print('修改后old_price的值是1：',old_price)
    return  final_price

old_price = float(input('请输入原价：'))
#old_price、rate、new_price是全局变量
rate = float(input('请输入折扣率:'))
new_price = discounts(old_price,rate)
print('打折后价格是：',new_price)
print('修改后old_price的值是2：',old_price)
#print('这里试图打印局部变量final_price的值',final_price)
#final_price 只在discounts函数内生效
