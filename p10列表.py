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
#扩展列表 extend()
member.extend(['竹林小溪','Crazy'])
print(member)
print(len(member))

#插入列表insert()
member.insert(0,'Frist')
print(member)
print(len(member))
