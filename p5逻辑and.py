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
print('type()函数')
print(type('520'))
print(type(True))
print(type(3e4))

#建议用isinstanc
print('建议用isinstanc')
print(isinstance(520,int))
print(isinstance('520',str))
print(isinstance(520.0,float))
print(isinstance(520.0,bool))

#算术操作符：+ - * / % ** //
print('算术操作符：+ - * / % ** //')
a = 5
a =a+3
print(a)
a += 3
print(a)
b = 3
b -=1
print(b)
a =b = c = d =10
a += 1
print(a)
b -= 3
print(b)
c *= 10
print(c)
d /= 8
print(d)
#python是float除法，地板除法//
print('python是float除法，地板除法//')
print(10//8)
print(3.0//2)
# %取余数
print('%取余数')
print(5%2)
print(11%2)
# 幂运算 **
print('幂运算 **')
print(3**2)
# 运算优先级，先乘法、除法、后加、减 ,
print('运算优先级，先乘法、除法、后加、减,比较运算符优先逻辑运算符')
print((3 < 4 )and (4 < 5))
print('幂运算高于左边，低于右边运算符')
print(-3**2)
print(3**-2)
print('and左右同时为真才是真，or是一边是真就是真，同时为假就是假，not去相反的bool类型值')
print(not True)
print(not False)
print(not 0,'0 python解释为False')
print(not 4,'非零的数字解释为True')
print(3<4<5,'等同' ,3<4 and 4<5)
print('幂运算**优先正负号+* -*优先算术操作符* / // + -优先比较操作符< <= > >= == !=优先逻辑运算符and or not')













