# lambda表达式
def ds(x):
    return 2 * x +1
print(ds(5))
print(lambda x : 2 * x+1)
# 冒号前边是原函数的参数，冒号后边是原函数的返回值
# 调用就是赋值
g = lambda x : 2 * x +1 #这个函数就是匿名的
print(g(5))
# 两个参数
def add(x,y):
    return x + y
print(add(3,4))
#转化为lambda表达式
lambda x ,y : x + y
g = lambda x ,y : x + y
print(g(3,4))
#Python写一些执行脚本时，用lambda就可以省下定义函数过程，
#比如说我们只需要写个简单的脚本来管理服务器时间，我们就不需
# 要专门定义一个函数然后再写调用，使用lambda就可以
#使得代码更加精简
#两个牛逼的BIF:filter()过滤器
filter(None,[1,0,False,True])
print(list(filter(None,[1,0,False,True])))
#过滤器就是把非True的过滤掉
#筛选不能被二整除的奇数的过滤器
def odd(x):
    return x % 2
temp = range(10) #分配0到9十个数字
show = filter(odd,temp)
print(list(show))
#一行实现
print(list(filter(lambda x: x % 2,range(10))))
# map()不是地图是映射来解释
print(list(map(lambda x : x * 2,range(10))))

#  递归是神马？树结构的定义
def recursion():
    return recursion()
# ctr+c 断了，设置递归深度
import sys
sys.setrecursionlimit(10000)
# 写一个递归求阶乘 1 *2*3*4*5
def factorial(n):
    result  = n
    for i in range(1,n):
        result *= i
    return result
number = int(input('请输入一个正整数'))
result = factorial(number)
print("%d 的阶乘是：%d" %(number,result))
# 递归实现,1、调用函数自身，2、设置自身正确的返回值
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
number = int(input('请输入一个正整数'))
result = factorial(number)
print("%d 的阶乘是：%d" %(number,result))

# 兔子问题：斐波那契数列 递归 和 迭代实现
# 迭代实现
def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 1:
        print('输入有误！')
        return -1
    while (n-2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    return n3
result = fab(20)
if result != -1:
    print('总共有%d对小兔崽子诞生!' % result)
# 递归实现，两个递归
def fab(n):
    if n < 1:
        return -1
    if n ==1 or n ==2:
        return 1
    else:
        return fab(n-1) + fab(n-2)
result = fab(20)
if result != -1:
    print('总共有%d对小兔崽子诞生' % result)
# 分制思想
