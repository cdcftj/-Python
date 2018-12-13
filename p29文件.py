# 因为懂你，所以永恒，程序都是输入、处理、输出
print(help(open))
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#     Open file and return a stream.  Raise IOError upon failure.
# 打开模式 'r'只读（默认） 。'w'写入，会覆盖已存在文件。'x'如果文件存在会引发异常。
# 'a'写入模式，如果文件存在，则在末尾追加写入。'b'以二进制模式打开文件。
# 't'以文本模式打开（默认）。'+'可读写模式（可添加到其他模式在使用）。
# ‘U’通用换行符支持
f = open('/home/t/Documents/test.txt')
print(f.read())
# 文件对象方法
# f.clsoe() 写入后立即关闭习惯
print(f.read())
print(f.read(5))
print(f.tell())
print(f.seek(11, 0))
print(f.readline())
f = open('/home/t/Documents/test.txt')
print(list(f))  # list直接变成列表
print(f.seek(0, 0))
lines = list(f)
for each_line in lines:
    print(each_line)
# 这样效率不高，我们用for直接迭代出来
f.seek(0, 0)
for each_line in f:
    print(each_line)
# 写入字符
f = open('/home/t/Documents/test1.txt')
print(f.writable('我爱胡庆'))
f.close()











