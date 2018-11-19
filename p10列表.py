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
print(member[1:3])#3减1等于2
print(member[:3]) #0到3
print(member[1:])#1到结束
print((member[:]))#原列表拷贝
member2 = member[:]#member的拷贝
print(member2)

#列表的一些常有操作符，比较、逻辑、连接、重复、成员关系操作符
list1 = [123]
list2 = [234]
print(list1 > list2)

list1 = [123,456]
list2 = [234,123]
print(list1 >list2)#第0个元素比较假了整个都假
#逻辑and左右两边都是True结果为True
list3 =[123,456]
print((list1 <list2) and (list1 ==list3))
#连接,不能添加新元素
list4 = list1 + list2
print(list4)
#×重复操作符
print('#整个列表复制3次')
print(list3 *3)
print('#列表复制三次')
list3 *= 3
print(list3)
print('#列表在上面3次后又乘5次就是15次')
list3 *= 5
print(list3)
#成员关系操作符：in,not in
print(123 in list3)
print('小甲鱼' not in list3)
print(123 not in list3)
list5 = [123, ['小甲鱼', '牡丹'], 456]
print('小甲鱼' in list5)#结果为Flase只能影响一层，跟Break continue一样
print('小甲鱼' in list5[1])#引入元素1就是True了
#访问数组的值
print(list5[1][1])
#列表类型的内置函数，列表的小伙伴们
print(dir(list))
#count计算参数在列表中出现次数
print(list3.count(123))
#list 3起始位置，7结束位置
print(list3.index(123,3,7))
#reverse将整个列表原地翻转,没有参数
list3.reverse()
print(list3)
#sort()指定方式对列表成员进行排序，默认是从小到大
list6 = [4,2,5,1,9,23,32,0]
list6.sort()
print(list6)
#sort(reverse=F)
list6.sort(reverse=True)
print(list6)
#等号，分片拷贝区别。等号只是换名称内容没有变
list7 = list6[:]
list8 =list6
list6.sort()
print(list6)
print(list7)
print(list8)#等号过来跟list6一样变

#元组是不可改变的类型，元组和列表的不同，列表可以任意插入、删除元素
#元组大部分是用小括号,逗号是创建元组的关键
tuple1 = (1,2,3,4,5,6,7,8)
print(tuple1)
#访问元组
print(tuple1[1])
print(tuple1[5:])
print(tuple1[:5])
tuple2 = tuple1[:]
print(tuple2)
temp = (1)
print(type(temp))
temp =(),print('空元组')
print(type(temp))
temp = (1,),print('一个元素加逗号')
print(type(temp))
temp = 1,
print(type(temp))
temp = 8 * (8,)
print('*号是重复操作符')
print(temp)

#更新和删除一个元组
temp =('小甲鱼' ,'黑夜','迷途','小布丁')
temp = temp[:2] + ('怡静',) + temp[2:]
print(temp)
#del temp 是删除元组
#元组相关的操作符：+号拼接操作符，×重复操作符，大于小于< > 成员操作符in 逻辑and













