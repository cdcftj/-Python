# 递归求解汗诺塔
def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        hanoi(n-1, x, z, y)# 将前n-1个盘子从x移动到y上
        print(x, '-->', z) # 将最底下的最后一个盘子从x移动到z上
        hanoi(n-1, y, x, z)# 将y上的n-1个盘子移动到z上
n = int(input('请输入汗诺塔的层数：'))
hanoi(n, 'x', 'y', 'z')

# p26 字典：当索引不好用时
# 创建和访问字典
brand = ['李宁', '耐克', '鱼c工作室']
slogan =['一切皆有可能', 'Just do it ', '让编程改变世界']
print('鱼c工作室的口号是：', slogan[brand.index('鱼c工作室')])
# 建字典,字典是映射类型,李宁是key 冒号后面value
dict1 = {'李宁': '一切皆有可能', '耐克': 'Just do it', '鱼c工作室': '让编程改变世界'}
print('鱼c工作室的口号是：', dict1['鱼c工作室'])

dict2 = {1: 'one', 2: 'two', 3: 'three'}
print(dict2[2])
# 空字典
dict3 = {}
dict3 = dict((('F', 70), ('i', 105), ('s', 115)))
print(dict3)
# 关键字也可以
dict4 = dict(小甲鱼='让编程改变世界',李宁='一切皆有可能')
print(dict4)
# 改变值 ,替换了
dict4['李宁'] = '一切都完蛋了'
print(dict4)
# 增加项
dict4['成都天气'] = '现在2018年12月10日四度非常冷'
print(dict4)
# 字典不好用二 工厂函数
dict1 = {}
print(dict1.fromkeys((1, 2, 3)))
#结果是空的None,现在设置Number
print(dict1.fromkeys((1, 2, 3), 'Number'))
# 访问字典的几个方法：keys() values() items()
dict1 = dict1.fromkeys(range(32), '赞')
# 打印序号
for eachkey in dict1.keys():
    print(eachkey)
# 打印赞
for eachValue in dict1.values():
    print(eachValue)
# 打印整个项,元组形式
for eachItem in dict1.items():
    print(eachItem)
# get方法解决报错
print(dict1.get(32, '木有！'))
# 成员资格操作符 in ,not in
print(31 in dict1)
print(32 in dict1)
# 清空一个字典用clear()方法
dict1.clear()
print(dict1)
# a = {} 方式清空有危险
a = {'姓名': '小甲鱼'}
b = a
a = {}
a = b
print(a)
print(b)
a.clear()
print(a)
print(b)
# 全拷贝copy方法
a = {1: 'one', 2: 'two'}
b = a.copy()
c = a
print(c)
print(a)
print(b)
# 赋值地址一样，全拷贝地址不一样
print(id(a))
print(id(b))
print(id(c))
c[4] = 'three'
print(c)
print(a)
print(b)# 全拷贝b没有改变
# pop()给定键弹出给定的值
# popitem()弹出一个项
print(a.pop(2))
print(a.popitem())# 随机弹
# setdefault 跟get类似，找不到自己添加
a.setdefault('小白')
print(a)
a.setdefault(5, 'five')
print(a)
# update 用字典映射关系去更新一个字典
b = {'小白': '一只狗'}
a.update(b)
print(a)












