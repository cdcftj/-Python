#列表、元祖、字符串的共同点
#都可以通过索引得到每一个元素
#默认索引值是从0开始
#可以通过分片的方法得到一个范围内元素的集合
#有很多共同的操作符（重复×、拼接+、成员关系操作符）
#list()把一个迭代对象转换为列表
print(help(list))
a = list()
print(a)
b = 'I love FishC.com'
b = list(b)#字符串迭代
print(b)
#元祖变成列表
c = (1,1,2,3,5,8,13,21,34)
c = list(c)
print(c)
#tuple([iterable])把一个可迭代对象转换为元祖
print(help(tuple))
#str(obj)把object对象转换为字符串
#len(sub)返回参数的长度
print(len(a))
print(len(b))
#max()返回序列或参数集合中的最大值
print(max(1,2,3,4,5))
print(max(b))
number = [1,18,13,0,-98,34,54,76,32]
print(max(number))
# min()返回序列或者参数集合中的最小值
print(min(number))
chars =  '1234567890'
print(min(chars))
# 元祖,要保证数据类型都一样
tuple1 = (1,2,3,4,5,6,7,8,9,0)
print(max(tuple1))
# sum(iterable[,start=0])返回序列iterable和可选参数start的总和
tuple2 = (3.1,2.3,3.4)
print(sum(tuple2))
print(number.pop())
print(sum(number))
print(sum(number,8))#加8
# sorted()排序列表
print(sorted(number))
# reversed返回迭代器对象
print(reversed(number))
# 用list可以转换成列表
print(list(reversed(number)))
# 枚举
print(enumerate(number))
print(list(enumerate(number)))#插入索引值,元组
# zip打包
a = [1,2,3,4,5,6,7,8]
b = [4,5,6,7,8]
print(list(zip(a,b)))#打包成元组，多余的省去
## p017 函数：python的乐高积木
# 函数、对象、模块
def MyFirstFunction():
    print('这是我创建的第一个函数!')
    print('我表示很激动')
    print('在此我要感谢大家.......')
# 调用函数
MyFirstFunction()
# 函数带参数
def MySecondFunction(name):
    print(name + '我爱你！')
MySecondFunction('Huqing')
MySecondFunction('小甲鱼')#参数就可变了

def add(num1,num2):
    result = num1 +num2
    print(result)
print(add(1,2))

print('# 函数的返回值 return')
def add(num1,num2):
    return (num1 + num2)
print(add(5,6))
