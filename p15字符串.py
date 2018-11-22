str1 = 'I love huqing'
print(str1[:6])
#索引e
print(str1[5])
print(str1[:6] + '  插入的字符串' + str1[6:])
str2 = 'xiaoxie'
print(str2.capitalize())
print('第一个字母大写')
str2 = 'DAXIExiaoxie'
print(str2.casefold())#全部小写
print(str2.center(40))#居中
print(str2.count('xi'))#查找位置
print(str2.endswith('xi'))#检查xi结束
str3 = 'I\tlove\tFishc.com,'
print(str3.expandtabs())
print(str3.find('efc'))#找不到
str4 = '小甲鱼'
print(str4.islower())#可以认识中文
str5 = 'FishC'
print(str5.istitle())#不是标题
print(str5.join('12345'))#加入
str6 = '    I love you'
print(str6.lstrip())#去掉左边空格
str6 = 'I love huqing'
print(str6.partition('ov'))#ov隔成三个子串组成元组
print(str6.replace('huqing','Huqing'))
print(str6.split())#空格就切，变成列表
str7 = '      sssssaaaassss   '
print(str7.strip())#切前后空格
str7 = str7.strip()
print(str7.strip('s'))#切s
print(str5.swapcase())#大小写翻转
print(str7.translate(str.maketrans('s', 'b')))
#s转成b
##字符串：格式化，规范进制不同的问题
#关键字参数 replacement字段
#格式化位置参数
print("{0}love{1}.{2}".format("I","FishC","com"))
#关键字参数
print("{a}love{b}.{c}".format(a="I",b="FishC",c="com"))
#混合使用
print("{0}love{b}.{c}".format("I",b="FishC",c="com"))
print('\ta')#\t是tab键5个字符
print('\\')
print("{{0}}".format("不打印"))
print('#冒号是格式化符号的开始，.1就是四舍五入保留小数点1位，f打印定点数，')
print('{0:.1f}{1}'.format(27.658,'GB'))
##字符串操作符
print('%c' % 97)#97 ASCII就是a
print('%c %c %c' % (97,98,99))
#%s格式化字符串
print('%s' % 'I love FishC.com')
#%d 字符串整数
print('%d + %d = %d' %(4,5,4+5))
# %o格式化无符号八进制数
print('%o' % 10)
print('%x' % 10)#小写格式化无符号16进制
print('%X' % 10)#大写格式化无符号16进制
print('%f' % 27.658)#格式化定点数，指定精度
print('%e' % 27.658)#科学计数法格式化定点数
print('%E' % 27.658)
print('%g' % 27.658)#智能选择f E
#格式化操作符辅助指令
print('%5.1f' % 27.658)#总宽度是5
print('%.2e' % 27.658)#2位小数点
print('%10d'  % 5)#5前面9个空格
print('%-10d'  % 5)#负号左对齐
print('%+d'  % 5)#正数前面显示加号
print('%#o'  % 10)#o表示八进制
print('%#X'  % 108)
print('%#d'  % 10)
print('%#10d'  % 5)
print('%#-10d'  % 5)






