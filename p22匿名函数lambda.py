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




