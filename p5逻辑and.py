print(3>2 and 1<2)
print((3>2) and (1<2))#两边都是True才是True
print((3>2) and (1>2))#一边是False结果是False
#Python数字类型：整形、浮点型、布尔型、科学计数法e记法
print(1.5e11)
#类型转换int() str() float()
a = 5.99
b = int(a)
print(b) #浮点数不会四舍五入
a = '520'
b = float(a)
print(b)
a = 520
b = float(a)
print(b)
a = 5.99
b = str(a)
print(b)
c = str(5e19)
print(c)
#type()函数
print(type('520'))
print(type(True))
print(type(3e4))






