#列表：一个打了激素的数组：整数、浮点数、字符串、对象
#普通列表
member = ['tanjin','tanyuanhong','胡庆']
print(member)
#混合列表
mix = [1,'胡庆',[1,2,3,4],3.14]
print(mix)
#空列表
empty =  []
print(empty)
#向列表添加元素 .append()点就是member的方法
member.append('福禄娃娃')
print(member)
len(member)
#扩展列表 extend()扩展方式，参数是一个列表
member.extend(['竹林小溪','Crazy'])
print(member)
print(len(member))

#插入列表insert()排靠前
member.insert(0,'Frist')
print(member)
print(len(member))

# index 从list中获取单个元素，索引值从0开始
print(member[0])
print(member[1])
#变量调换，先给一个中间变量
temp = member[0]
member[0] = member[1]
member[1] = temp
print(member)
# 从列表删除元素三种方法：remove不需要知道位置
member.remove('Crazy')
print(member)
# del是一个语句不要括号,可以删除member整个列表
del member[1]
print(member)
# pop()
member.pop()
print(member)
#最后一个删除了
# 赋值
name = member.pop()
print(name)
# 指定
print(member.pop(1))

#列表分片,冒号隔开，原来列表拷贝
print(member)
member.insert(2,'Tanyuanhong')
print(member)
print(member[1:3])
print(member[:3]) #0到3
print(member[1:])#1到结束
print((member[:]))#原列表拷贝
member2 = member[:]#member的拷贝
print(member2)




