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


