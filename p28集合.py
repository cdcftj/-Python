# python支持字典是对映射的反应，集合在我的世界里，你就是唯一！
num = {}
print(type(num))
num2 = {1, 2, 3, 4, 5}
print((type(num2))) # class 'set' 就是集合
num2 = {1, 2, 3, 4, 5, 4, 3, 2}
print(num2) # 重复都剔除
# 集合是无序的
# num2[2] #要报错
# 创建集合：1、直接把一堆元素用花括号括起来
# 2、使用set()工厂函数
set1 = set([1, 2, 3, 4, 5, 5])
print(set1)
# 要求：去掉列表在重复的元素
num1 = [1, 2, 3, 4, 5, 5, 3, 1, 0]
temp = []
for each in num1:
    if each not in temp:
        temp.append(each)
print(temp)
# 用集合写
num1 = list(set(num1)) # 先集合去除重复元素，在列表
print(num1)  # 如果关心元素前后关系要小心，列表是排了序的。

# 如何访问集合在的值
# 可以使用for把集合中的数据一个个读取出来
# 可以通过in和not in判断一个元素是否在集合中已经存在
print(1 in num2)
print('1' in num2)
num2.add(6)   # 把6加进去
print(num2)
num2.remove(5)  # 移除
print(num2)

# 不可变集合 frozen：冰冻的，冻结的
num3 = frozenset([1, 2, 3, 4, 5])
# num3.add(0)是错误的




