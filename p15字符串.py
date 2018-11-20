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


